# RSV Evolution Neutralization Project

## Methods

Study done by Cassie Simonich and Teagan McMahon starting in 2024. This study validates a pseudovirus based neutralization assay developed by the authors and also looks at how well mAbs and human serum retain their neutralization as RSV evolves over time.  

## Directory Structure

- **01_data/**
  - `frac_infect/`: Processed data used for analysis.
  - `combined_frac_infect/`: combined files based on experiment_rep for use in plotting/summary tables
  - `raw_plate_reader/`: Raw data, not read into the notebooks.
  - `maps/`: includes .csv files of the plate maps used to calculate fraction infectivity from .xlsx files
  - `PlateLayouts\`: includes .csv files of the plate layouts used to calculate fraction infectivity from .xlsx files
  - `other\`: includes .csv files for plotting of other (non fraction infectivity) data type, mainly titer data. Also includes fraction infectivities for the 293T vs 293T TIM1 test
- **02_notebooks/**: Jupyter notebooks for data processing and visualization.
- **03_output/**
  - `plots/`: Saved plots from the notebooks.
  - `processed_data/`: Data files processed in the notebooks.
  - `summary_tables/`: manually reformated data useful in the paper (ex. summary IC50/NT50, antibody sequences)
- **04_plasmid_maps/**
  - includes all plasmid maps (.gb) used in the study
- **05_trees/**
  - includes RSV-A and RSV-B F .json phylogenetic trees (Jesse will update)

## Setup Instructions

1. Clone the repo.
2. Set up the environment:
   ```bash
   conda env create -f environment.yml
