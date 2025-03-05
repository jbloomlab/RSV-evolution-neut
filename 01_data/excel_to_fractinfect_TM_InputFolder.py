import argparse
import os
import numpy as np
import pandas as pd

def parse_args():
    """Parse command line arguments."""
    parser = argparse.ArgumentParser(description='Convert plate reader Excel files to fraction infectivity csv.')
    parser.add_argument('input_dir', type=str, help='Directory containing the Excel files to convert to fraction infectivity.')
    parser.add_argument('outfile', type=str, help="Path for output fraction infectivity csvs.")
    parser.add_argument('sheet_map', type=str, help="File to map plate number and samples. Must have columns: 'Plate', 'Sample', 'Virus', 'SampleNum', 'PlateLayout', 'StartDil', 'DilFactor', 'Orientation', 'background', 'experiment_rep'")
    parser.add_argument('plate_layouts_dir', type=str, help='Directory containing csv files specifying plate layouts.')
    parser.add_argument('--start_row', type=int, help="Row of excel file where the plate column headers are, in 0-indexing.", default=22)
    return parser.parse_args()

def extract_plates(excelfile):
    """Extract plates from a single sheet with adjusted data area."""
    df = pd.read_excel(excelfile, sheet_name='Luminescence 1_01', header=None)
    df = df.astype(str)
    starts = df[df.apply(lambda row: row.str.contains('Wavelength: 0 nm', na=False)).any(axis=1)].index
    
    plates = {}
    for start in starts:
        plate_name = df.iloc[start + 2, 0]  # Plate name is 2 rows below 'Wavelength: 0 nm'
        end = start + 12  # Plate ends 12 rows below 'Wavelength: 0 nm'
        plate_df = df.iloc[start + 5:end + 1, 1:13]  # Data: starts 5 rows below, columns 1-12
        plate_df = plate_df.reset_index(drop=True)
        plates[plate_name] = plate_df
    return plates

def get_locs(layout, value):
    """Get (index, column) tuples for location of value in layout df."""
    locs_list = []
    locs = layout.isin([value])
    series = locs.any()
    columns = list(series[series].index)
    for col in columns:
        rows = list(locs[col][locs[col]].index)
        for row in rows:
            locs_list.append((row, col))
    return locs_list

def verify_replicate_and_concentration(plate_df, plate_map, layout_df, orientation):
    """Assign replicates and concentrations to each sample based on orientation."""
    sample_data = {'serum': [], 'virus': [], 'replicate': [], 'concentration': [], 'well_id': []}
    for sample in plate_map['SampleNum'].tolist():
        sample_locs = get_locs(layout_df, str(sample))
        start_dil = plate_map[plate_map['SampleNum'] == sample]['StartDil'].values[0]
        dil_factor = plate_map[plate_map['SampleNum'] == sample]['DilFactor'].values[0]
        
        if orientation.upper() == 'V':
            rows = sorted({loc[0] for loc in sample_locs})
            for i, row in enumerate(rows):
                replicate = i + 1
                replicate_locs = [loc for loc in sample_locs if loc[0] == row]
                for j, loc in enumerate(replicate_locs):
                    concentration = start_dil / (dil_factor ** j)
                    well_id = f"{chr(loc[0] + 65)}{int(loc[1])}"
                    sample_data['serum'].append(plate_map[plate_map['SampleNum'] == sample]['Sample'].iloc[0])
                    sample_data['virus'].append(plate_map[plate_map['SampleNum'] == sample]['Virus'].iloc[0])
                    sample_data['replicate'].append(replicate)
                    sample_data['concentration'].append(concentration)
                    sample_data['well_id'].append(well_id)
        elif orientation.upper() == 'H':
            cols = sorted({loc[1] for loc in sample_locs})
            for i, col in enumerate(cols):
                replicate = i + 1
                replicate_locs = [loc for loc in sample_locs if loc[1] == col]
                for j, loc in enumerate(replicate_locs):
                    concentration = start_dil / (dil_factor ** j)
                    well_id = f"{chr(loc[0] + 65)}{int(loc[1])}"
                    sample_data['serum'].append(plate_map[plate_map['SampleNum'] == sample]['Sample'].iloc[0])
                    sample_data['virus'].append(plate_map[plate_map['SampleNum'] == sample]['Virus'].iloc[0])
                    sample_data['replicate'].append(replicate)
                    sample_data['concentration'].append(concentration)
                    sample_data['well_id'].append(well_id)
        else:
            raise ValueError(f"Invalid orientation: {orientation}")
    return sample_data

def calculate_fraction_infectivity(plate_df, plate_map, layout_df, orientation, background_option):
    """Calculate fraction infectivity for the given plate."""
    if background_option == 'remove':
        bg_locs = get_locs(layout_df, 'neg_ctrl')
        bg_values = [pd.to_numeric(plate_df.at[loc[0], int(loc[1])], errors='coerce') for loc in bg_locs]
        bg_average = np.nanmean(bg_values)
        plate_data = plate_df - bg_average
    else:
        plate_data = plate_df

    pos_locs = get_locs(layout_df, 'pos_ctrl')
    pos_values = [pd.to_numeric(plate_data.at[loc[0], int(loc[1])], errors='coerce') for loc in pos_locs]
    pos_average = np.nanmean(pos_values)
    fraction_infectivity = []
    well_ids = []

    for sample in plate_map['SampleNum'].tolist():
        sample_locs = get_locs(layout_df, str(sample))
        for loc in sample_locs:
            well_value = pd.to_numeric(plate_data.at[loc[0], int(loc[1])], errors='coerce')
            fi_value = well_value / pos_average if pos_average > 0 else np.nan
            fraction_infectivity.append(fi_value)
            well_ids.append(f"{chr(loc[0] + 65)}{int(loc[1])}")

    fraction_infectivity_df = pd.DataFrame({
        'well_id': well_ids,
        'fraction infectivity': fraction_infectivity
    })
    return fraction_infectivity_df

def main():
    args = vars(parse_args())
    input_dir = args['input_dir']
    outfile = args['outfile']
    sheet_map_file = args['sheet_map']
    layouts_dir = args['plate_layouts_dir']

    # Extract the name of the input directory
    input_folder_name = os.path.basename(os.path.normpath(input_dir))

    sheet_map_df = pd.read_csv(sheet_map_file)
    required_cols = ['Plate', 'Sample', 'SampleNum', 'Virus', 'PlateLayout', 'StartDil', 'DilFactor', 'Orientation', 'background', 'experiment_rep']
    for col in required_cols:
        if col not in sheet_map_df.columns:
            raise ValueError(f"Required column {col} not in sample map.")

    # Loop over Excel files
    final_df = pd.DataFrame()
    
    for filename in os.listdir(input_dir):
        if filename.endswith('.xlsx'):
            file_path = os.path.join(input_dir, filename)
            print(f"Processing file: {file_path}")
            
            plates = extract_plates(file_path)
            sheet_map_df['Plate'] = sheet_map_df['Plate'].str.lower()

            for plate_name, plate_df in plates.items():
                plate_name_lower = plate_name.lower()
                plate_map = sheet_map_df[sheet_map_df['Plate'] == plate_name_lower]
                if plate_map.empty:
                    raise ValueError(f"No matching plate found in the sheet map for plate: {plate_name}")

                layout_file = f"{layouts_dir}/{plate_map['PlateLayout'].iloc[0]}"
                layout_df = pd.read_csv(layout_file).astype(str)
                background_option = plate_map['background'].iloc[0]
                orientation = plate_map['Orientation'].iloc[0]

                print(f"Processing plate: {plate_name}")

                # Verify replicates and concentrations (create metadata)
                sample_data = verify_replicate_and_concentration(plate_df, plate_map, layout_df, orientation)
                metadata_df = pd.DataFrame(sample_data)
                metadata_df['plate_name'] = plate_name  # Add plate_name column
                metadata_df['experiment_rep'] = plate_map['experiment_rep'].iloc[0]  # Add experiment_rep column

                # Calculate fraction infectivity (create a separate dataframe)
                fraction_infectivity_df = calculate_fraction_infectivity(plate_df, plate_map, layout_df, orientation, background_option)
                fraction_infectivity_df['plate_name'] = plate_name  # Add plate_name column

                # Merge the two dataframes
                merged_df = pd.merge(metadata_df, fraction_infectivity_df, on=['well_id', 'plate_name'], how='inner')
                merged_df['input_folder'] = input_folder_name  # Add input folder column
                final_df = pd.concat([final_df, merged_df], ignore_index=True)

    # Write the final DataFrame to CSV
    final_df.to_csv(outfile, float_format='%.4g', index=False)

if __name__ == '__main__':
    main()
