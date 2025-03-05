# RSV Evolution Neutralization Project

## Methods

Study done by Cassie Simonich and Teagan McMahon starting in 2024. This study validates a pseudovirus based neutralization assay developed by the authors and also looks at how well mAbs and human serum retain their neutralization as RSV evolves over time.  

## Directory Structure

- [./01_data/](01_data)
  - [./frac_infect/](01_data/frac_infect): Processed data used for analysis.
  - [./combined_frac_infect/](01_data/combined_frac_infect): combined files based on experiment_rep for use in plotting/summary tables
  - [./raw_plate_reader/](01_data/raw_plate_reader/): Raw data, not read into the notebooks.
  - [./maps/](01_data/maps): includes .csv files of the plate maps used to calculate fraction infectivity from .xlsx files
  - [./PlateLayouts/](01_data/PlateLayouts): includes .csv files of the plate layouts used to calculate fraction infectivity from .xlsx files
  - [./other/](01_data/other): includes .csv files for plotting of other (non fraction infectivity) data type, mainly titer data. Also includes fraction infectivities for the 293T vs 293T TIM1 test
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

- for titer plots see
  - [G CT deletion 1B](03_output/plots/Titer_CTdel_G_Only.html)
  - [F CT deletion 1C](03_output/plots/Titer_CTdel_filtered_F.html)
  - [Pseudovirus titer TU/mL 2A](03_output/plots/Titer_TU-mL.html)
  - [Pseudovirus titer RLU/uL 2B](03_output/plots/Titer_CTdel_filtered_F.html)
  - [Freezing conditions Supplemental 1](03_output/plots/Titer_Freeze1.html)
  - [293T vs 293T-TIM1 Supplemental 2B](03_output/plots/Titer_CTdel_supplement.html)
- for compaison of neutralization on 293T vs 293T-TIM1 cells see:
  - [Nirsevimab 2C](03_output/plots/CellLine_Rep1_nirsevimab.svg)
  - [Pooled sera 2C](03_output/plots/CellLine_Rep1_pooledsera.svg)
  - [Clinical serum 2C](03_output/plots/CellLine_Rep1_87_9.svg)
- for validation against full length A2 assay and refernce/standard sera see:
  - [Compaison to A2 assay 3A](03_output/plots/Neut_Assay_Comparison_Correlation.html)
  - [Compaison to A2 assay curves Supplemental 4A](03_output/plots/241031_greninger_draftfig.pdf)
  - [BEI sera curves 3B](03_output/plots/NeutCurves_BEI_FigSubset_V3FONT.svg)
  - [NIBSC & BEI sera additional curves Supplemental 5A](03_output/plots/BEI_NeutCurves_NIBSC_A2.svg)
  - [NIBSC & BEI sera additional curves Supplemental 5A](03_output/plots/NeutCurves_NIBSC_B1.svg)
  - [BEI comparison to published values 3C](03_output/plots/ReferenceSera_faceted_slope_graph_narrowV2.svg)
  - [Dilution of virus impacts neutralization RSV B N201S Supplemental 3](03_output/plots/250130_VirusDilution_NirsN201S-H.svg)
  - [Dilution of virus impacts neutralization RSV B 1982 Supplemental 3](03_output/plots/250130_VirusDilution_PoolB82_H.svg)
- for depleted sera neuts/ELISAs see:
  - [ELISA with RSV G, F, Pre-F 4B](03_output/plots/ELISACurves.pdf)
  - [Neutralization assay with depleted sera 4C](03_output/plots/241101_DepletedSera_NeutCurve_Fig.svg)
- for RSV F trees see:
  - [RSV-A-F tree used in 5A](https://nextstrain.org/community/jbloomlab/RSV-evolution-neut@main/RSV-A-F)
  - [RSV-B-F tree used in 5B and 7A](https://nextstrain.org/community/jbloomlab/RSV-evolution-neut@main/RSV-B-F)
- for historical sera NT50s and curves see:
  - [RSV A and B historical sera NT50s 6B](03_output/plots/RSVEvo_historicalsera_neutralization_plot.html)
  - [RSV A and B historical sera curves Supplemental 6](03_output/plots/Supplemental_Curves_Historic_Sera.svg)
  - [Influenza H3 historical sera NT50s](03_output/plots/H3Evo_historicalsera_neutralization_plot.html)
  - [Influenza H3 historical sera curves Supplemental 7 replicate 1](03_output/plots/Supplemental_Curves_Historic_Sera_H3_rep1.svg)
  - [Influenza H3 historical sera curves Supplemental 7 replicate 2](03_output/plots/Supplemental_Curves_Historic_Sera_H3_rep2.svg)
  - [RSV B N201S sera NT50s 7C](03_output/plots/RSVEvo_historicalsera_neutralization_plot_escape_strains.html)
  - [RSV B N201S sera curves Supplemental 9](03_output/plots/Supplemental_Curves_Escape_Sera_AllReps.svg)
- for mAb curves see:
  - [mAbs curves for non lab adapted strains 7B](03_output/plots/mAbs_Fig7.svg)
  - [mAbs curves for lab adapted strains replicate 1 Supplemental 8A](03_output/plots/mAbs_Supplemental_Fig8_rep1.svg)
  - [mAbs curves for lab adapted strains replicate 2 Supplemental 8B](03_output/plots/mAbs_Supplemental_Fig8_rep2.svg)
  - [mAbs curves for non lab adapted strains replicate 2 Supplemental 8C](03_output/plots/mAbs_Supplemental_Fig8_rep2_standard_strains.svg)