# Temporal architecture of signaling oscillations predicts cancer gene function across pathways

**Preprint:** [bioRxiv link forthcoming]

**Author:** Theodor Spiro (theospirin@gmail.com)

---

## Overview

This repository contains code, data, and figures for the paper:

> **Temporal architecture of signaling oscillations predicts cancer gene function across pathways**
>
> Spiro, T. (2026)

We classify 157 genes across 14 oscillatory signaling pathways into rise-phase (signal activation) and recovery-phase (signal termination) components, and show that this temporal classification predicts cancer gene function (OR = 27.5, p = 3.6e-9) with higher accuracy than naive biochemical classification (86% vs 14% on divergent cases).

## Repository structure

```
data/
  gof_lof_analysis.csv       # 72 genes with rise/recovery, CGC status, GoF/LoF
  pathway_summary.csv         # Per-pathway summary (14 pathways)
  loop_components.csv         # 22 core feedback loop pairs
  cgc_enrichment.json         # KEGG NFL extraction enrichment stats

scripts/
  paper1_figures.py           # Generate all 6 main figures

figures/
  fig1_schematic.pdf/png      # Oscillation schematic + waveform classes
  fig2_enrichment.pdf/png     # Cancer gene enrichment
  fig3_divergent.pdf/png      # Divergent predictions (86% vs 14%)
  fig4_gof_drugs.pdf/png      # GoF/LoF consistency + drug targets
  fig5_kegg_validation.pdf/png# KEGG algorithmic validation
  fig6_waveform.pdf/png       # Waveform asymmetry across 14 systems

supplementary/
  table_s1_gene_classification.csv  # Full 157 genes with classifications
  table_s2_divergent_predictions.csv# 22 divergent prediction genes
  table_s3_nfl_extraction.csv       # Algorithmic NFL extraction results
  table_s4_waveform_parameters.csv  # Waveform compilation (14 systems)
```

## Key results

| Statistic | Value |
|-----------|-------|
| Pathways analyzed | 14 |
| Total genes classified | 157 (80 rise, 77 recovery) |
| CGC enrichment | 24.1-fold (p = 2.1e-62) |
| Rise-oncogene / Recovery-TSG OR | 27.5 [95% CI: 7.9, 96.2] |
| Pathways matching prediction | 12/12 |
| Predicted inversions confirmed | 2/2 (p53, TGF-beta) |
| Divergent cases: oscillatory correct | 19/22 (86%) |
| Divergent cases: naive correct | 3/22 (14%) |
| GoF drug targets in rise arm | 28/33 (85%, p = 3.3e-5) |
| KEGG NFL extraction OR | 59.0 [37.0, 94.1] |
| Non-oscillatory control in CGC | 0/41 |

## Data sources

- **COSMIC Cancer Gene Census v103**: https://cancer.sanger.ac.uk/census
- **KEGG Pathway Database**: https://www.genome.jp/kegg/

## Requirements

```
python >= 3.8
numpy
scipy
matplotlib
```

## License

MIT
