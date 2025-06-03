# RSV Evolution Neutralization Project

This repository has the data for [Simonich et al (2025)](https://www.biorxiv.org/content/10.1101/2025.03.11.642476v1), a study on RSV evolution from the [Bloom lab](https://jbloomlab.org/).

## Methods

Study done by Cassie Simonich and Teagan McMahon starting in 2024. This study validates a pseudovirus based neutralization assay developed by the authors and also looks at how well mAbs and human serum retain their neutralization as RSV evolves over time.  

## Directory Structure

- [./01_data/](01_data)
  - [./frac_infect/](01_data/frac_infect): Processed data used for analysis.
  - [./combined_frac_infect/](01_data/combined_frac_infect): combined files based on experiment_rep for use in plotting/summary tables
  - [./raw_plate_reader/](01_data/raw_plate_reader/): Raw data, not read into the notebooks.
  - [./maps/](01_data/maps): includes .csv files of the plate maps used to calculate fraction infectivity from .xlsx files
  - [./PlateLayouts/](01_data/PlateLayouts): includes .csv files of the plate layouts used to calculate fraction infectivity from .xlsx files
  - [./other/](01_data/other): includes .csv files for plotting of other data types (not fraction infectivity used in major summary plots), mainly titer data but also includes .tif files for western blot images. Also includes fraction infectivities for the 293T vs 293T TIM1 test. 
- [./02_notebooks/](02_notebooks): Jupyter notebooks for data processing and visualization.
- [./03_output/](03_output)
  - [./plots/](03_output/plots): Saved plots from the notebooks.
  - [./processed_data/](03_output/processed_data): Data files processed in the notebooks.
  - [./summary_tables/](03_output/summary_tables): manually reformated data useful in the paper (ex. summary IC50/NT50, antibody sequences)
- [./04_plasmid_maps/](04_plasmid_maps):
  - includes all plasmid maps (.gb) used in the study
- [./auspice/](auspice):
  - This directory includes JSON trees for RSV A and B F proteins, named so that they display via [Nextstrain Community Builds](https://docs.nextstrain.org/en/latest/guides/share/community-builds.html) at [https://nextstrain.org/community/jbloomlab/RSV-evolution-neut@main/RSV-A-F](https://nextstrain.org/community/jbloomlab/RSV-evolution-neut@main/RSV-A-F) and [https://nextstrain.org/community/jbloomlab/RSV-evolution-neut@main/RSV-B-F](https://nextstrain.org/community/jbloomlab/RSV-evolution-neut@main/RSV-B-F). These trees were created by running the NextStrain RSV build at [https://github.com/nextstrain/rsv](https://github.com/nextstrain/rsv) but removing the step to subsample sequences for the F gene builds, on May-9-2024.

## Relevant Tables

- [Strain naming table Supplemental Table 1](03_output/summary_tables/strains.xlsx)
- [Sera information Supplemental Table 2](03_output/summary_tables/Sera_ID_age.xlsx)
- [mAb sequences](03_output/summary_tables/RSV_mAb_AAseq.csv)

## Relevant Figures

- at github page with properly rendered figures can be found [here](https://jbloomlab.github.io/RSV-evolution-neut/)
