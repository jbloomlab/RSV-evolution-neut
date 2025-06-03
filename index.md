# RSV Evolution Neutralization Project

Plots for for [Simonich et al (2025)](https://www.biorxiv.org/content/10.1101/2025.03.11.642476v1), a study on RSV evolution from the [Bloom lab](https://jbloomlab.org/).

## Methods

Study done by Cassie Simonich and Teagan McMahon starting in 2024. This study validates a pseudovirus based neutralization assay developed by the authors and also looks at how well mAbs and human serum retain their neutralization as RSV evolves over time. See [repo for full analysis](https://github.com/jbloomlab/RSV-evolution-neut).

## Relevant Figures

- for compaison of neutralization on 293T vs 293T-TIM1 cells see:
  - [Nirsevimab 2C](03_output/plots/CellLine_Rep1_nirsevimab.svg)
  - [Pooled sera 2C](03_output/plots/CellLine_Rep1_pooledsera.svg)
  - [Clinical serum 2C](03_output/plots/CellLine_Rep1_87_9.svg)
  - [Control serum 2C](03_output/plots/CellLine_Rep1_ctrl_IgGDepleteSera.svg)
- for validation against full length A2 assay and refernce/standard sera see:
  - [Compaison to A2 assay 3A](03_output/plots/Neut_Assay_Comparison_Correlation.html)
  - [Compaison to A2 assay curves Supplemental 7A](03_output/plots/241031_greninger_draftfig.pdf)
  - [BEI sera curves 3B](03_output/plots/NeutCurves_BEI_FigSubset_V3FONT.svg)
  - [NIBSC & BEI sera additional curves Supplemental 8A](03_output/plots/BEI_NeutCurves_NIBSC_A2.svg)
  - [NIBSC & BEI sera additional curves Supplemental 8A](03_output/plots/NeutCurves_NIBSC_B1.svg)
  - [BEI comparison to published values 3C](03_output/plots/ReferenceSera_faceted_slope_graph_narrowV2.svg)
  - [Dilution of virus impacts neutralization RSV B N201S Supplemental 6A](03_output/plots/250130_VirusDilution_NirsN201S-H.svg)
  - [Dilution of virus impacts neutralization RSV B 1982 Supplemental 6A](03_output/plots/250130_VirusDilution_PoolB82_H.svg)
  - [Increasing virus input after four fold dilution does not impact neutralization RSV Long Supplemental 6B](03_output/plots/250130_VirusDilution_PoolB82_H.svg)
- for depleted sera neuts/ELISAs see:
  - [ELISA with RSV G, F, Pre-F 4B](03_output/plots/ELISACurves.pdf)
  - [Neutralization assay with depleted sera 4C](03_output/plots/241101_DepletedSera_NeutCurve_Fig.svg)
- for RSV F trees see:
  - [RSV-A-F tree used in 5A](https://nextstrain.org/community/jbloomlab/RSV-evolution-neut@main/RSV-A-F)
  - [RSV-B-F tree used in 5B and 7A](https://nextstrain.org/community/jbloomlab/RSV-evolution-neut@main/RSV-B-F)
- for historical sera NT50s and curves see:
  - [RSV A and B historical sera NT50s 6B](03_output/plots/RSVEvo_historicalsera_neutralization_plot.html)
  - [RSV A and B historical sera NT50s 6B, colored by sera](03_output/plots/RSVEvo_historicalsera_neutralization_plot_colored_interactive_subset.html)
  - [RSV A and B historical sera curves Supplemental 9](03_output/plots/Supplemental_Curves_Historic_Sera.svg)
  - [Influenza H3 historical sera NT50s](03_output/plots/H3Evo_historicalsera_neutralization_plot.html)
  - [Influenza H3 historical sera curves Supplemental 10 replicate 1](03_output/plots/Supplemental_Curves_Historic_Sera_H3_rep1.svg)
  - [Influenza H3 historical sera curves Supplemental 10 replicate 2](03_output/plots/Supplemental_Curves_Historic_Sera_H3_rep2.svg)
  - [RSV B N201S sera NT50s 7C](03_output/plots/RSVEvo_historicalsera_neutralization_plot_escape_strains.html)
  - [RSV B N201S sera curves Supplemental 12](03_output/plots/Supplemental_Curves_Escape_Sera_AllReps.svg)
- for mAb curves see:
  - [mAbs curves for non lab adapted strains 7B](03_output/plots/mAbs_Fig7.svg)
  - [mAbs curves for lab adapted strains replicate 1 Supplemental 11A](03_output/plots/mAbs_Supplemental_Fig8_rep1.svg)
  - [mAbs curves for lab adapted strains replicate 2 Supplemental 11B](03_output/plots/mAbs_Supplemental_Fig8_rep2.svg)
  - [mAbs curves for non lab adapted strains replicate 2 Supplemental 11C](03_output/plots/mAbs_Supplemental_Fig8_rep2_standard_strains.svg)
- for titer plots (and some other miscellaneous plots) see:
  - [G CT deletion 1B](03_output/plots/Titer_CTdel_G_Only.html)
  - [F CT deletion 1C](03_output/plots/Titer_CTdel_filtered_F.html)
  - [Pseudovirus titer TU/mL 2A](03_output/plots/Titer_TU-mL.html)
  - [Pseudovirus titer RLU/uL 2B](03_output/plots/Titer_CTdel_filtered_F.html)
  - [Pseudovirus titer RLU/uL from previous methods Supplemental 1](03_output/plots/Titer_Cui-Hu-Haid_filtered.html)
  - [p24 titer RLU/uL Supplement 2C](03_output/plots/p24_Titer.html)
  - [Western blot band quanitification Supplement 2B](03_output/plots/Western_NormalizedAUC.html)
  - [Freezing conditions Supplemental 3](03_output/plots/Titer_Freeze1.html)
  - [Long G vs A2020 G nirsevimab Supplemental 4B](03_output/plots/Neut_Nirsev_GCompare_forrevision.svg)
  - [Long G vs A2020 G sera Supplemental 4B](03_output/plots/2025.05.08_sera_GCompare.svg)
  - [293T vs 293T-TIM1 Supplemental 5B](03_output/plots/Titer_CTdel_supplement.html)
  - [293T-TIM1 vs other common cell types Supplemental 5C](03_output/plots/Titer_ours-Long_bycell_colored.html)
  - [293T-TIM1 vs A549 mAb Supplemental 5E](03_output/plots/Neut_Long_mabs_A549TIM1.svg)
  - [293T-TIM1 vs A549 sera Supplemental 5E](03_output/plots/Neut_Long_CellLine_sera.svg)