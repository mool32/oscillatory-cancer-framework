[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![License: CC-BY 4.0](https://img.shields.io/badge/Data%20%26%20Manuscript-CC--BY%204.0-lightgrey.svg)](https://creativecommons.org/licenses/by/4.0/)
[![Preprint](https://img.shields.io/badge/Preprint-PDF-red)](paper/Spiro_2026_preprint.pdf)

# Temporal architecture of signaling oscillations predicts cancer gene function across pathways

**157 genes across 14 oscillatory signaling pathways classified by temporal role only — rise-phase genes map to oncogenes, recovery-phase genes to tumor suppressors (OR = 27.5, p = 3.6 × 10⁻⁹), with predicted inversions in growth-inhibitory pathways**

Theodor Spiro | [ORCID 0009-0004-5382-9346](https://orcid.org/0009-0004-5382-9346) | tspiro@vaika.org

📄 **Preprint:** [`paper/Spiro_2026_preprint.pdf`](paper/Spiro_2026_preprint.pdf) · [`paper/manuscript.md`](paper/manuscript.md) (Markdown source)
🧮 **Main analysis script:** [`scripts/paper1_figures.py`](scripts/paper1_figures.py) (generates all 6 main figures)
🧬 **Companion paper:** [Negative feedback loop architecture as a modular predictor of cancer vulnerability](https://github.com/mool32/oscillatory-nfl-cancer) (Spiro 2026) — algorithmic complement that recovers the same organizational principle directly from KEGG topology

---

## Brief Summary

Cancer driver genes are conventionally classified pathway by pathway. We test whether a single organizational principle — the gene's temporal position within signaling oscillation cycles — can unify these classifications. Across **157 genes in 14 oscillatory signaling pathways** classified independently of cancer phenotype, the analysis demonstrates that:

1. **Rise-phase genes (signal activation, *n* = 80) map to oncogenes; recovery-phase genes (signal termination, *n* = 77) map to tumor suppressors.** Odds ratio = **27.5** (95% CI [7.9, 96.2]; Fisher exact *p* = **3.6 × 10⁻⁹**). The pattern holds for **12/12 pathways with testable cancer genes**.
2. **Predicted inversions in growth-inhibitory pathways are confirmed.** In p53 and TGF-β, where sustained signaling suppresses growth, the rise/recovery → onco/TSG mapping inverts as predicted. Of 75 gene-cancer associations among CGC members in the 14 pathways, 63 are coupled and 12 are anti-coupled as predicted; **zero are inconsistent with the framework**.
3. **The temporal framework outperforms naive biochemical classification on divergent cases.** In 22 cases where temporal classification diverges from naive categorization (e.g., phosphatases classified as oncogenes, kinases as tumor suppressors), the oscillatory framework is correct in **19/22 (86%)** vs **3/22 (14%)** for naive classification.
4. **Specificity to oscillatory pathways.** Genes in oscillatory signaling pathways show **24.1-fold enrichment** in the Cancer Gene Census relative to genome background (95% CI [17.5, 33.3], *p* = 2.1 × 10⁻⁶²), while 41 genes from non-oscillatory metabolic pathways show **zero CGC membership** — establishing a clear control distinction.
5. **Algorithmic validation: KEGG NFL extraction recovers the same enrichment.** Independent algorithmic NFL extraction (companion paper) yields a 59-fold CGC enrichment in NFL genes — the principle is recoverable from topology alone, not just from manual classification.
6. **Drug-target asymmetry corroborates the mechanism.** GoF (gain-of-function) drug targets are concentrated in the rise arm: **28/33 = 85%** (*p* = 3.3 × 10⁻⁵). The asymmetry in approved oncology targets matches the predicted asymmetry in the framework.

These results establish the temporal position of a gene within a signaling oscillation cycle as a specific, pathway-independent predictor of cancer function.

## Key results

| Statistic | Value |
|---|---|
| Pathways analyzed | 14 |
| Total genes classified | 157 (80 rise, 77 recovery) |
| CGC enrichment (oscillatory pathways) | 24.1-fold (*p* = 2.1 × 10⁻⁶²) |
| Rise-oncogene / Recovery-TSG OR | **27.5** [95% CI: 7.9, 96.2] |
| Pathways matching prediction | 12/12 |
| Predicted inversions confirmed | 2/2 (p53, TGF-β) |
| Divergent cases — oscillatory framework correct | **19/22 (86%)** |
| Divergent cases — naive classification correct | 3/22 (14%) |
| GoF drug targets in rise arm | 28/33 (85%, *p* = 3.3 × 10⁻⁵) |
| KEGG NFL extraction OR (companion paper) | **59.0** [37.0, 94.1] |
| Non-oscillatory metabolic control in CGC | 0/41 |

## Data sources

| Source | Use | Access |
|---|---|---|
| **COSMIC Cancer Gene Census** v103 | Cancer gene annotations (740 genes) | [cancer.sanger.ac.uk/census](https://cancer.sanger.ac.uk/census) (registration required) |
| **KEGG Pathway Database** | 14 oscillatory signaling pathways for the temporal classification | [genome.jp/kegg](https://www.genome.jp/kegg/) |
| **DrugBank / Pharmacology literature** | GoF/LoF mode-of-action labels for drug targets | Compiled in `data/gof_lof_analysis.csv` |

## Repository structure

```
├── paper/
│   ├── manuscript.md            # Manuscript source (Markdown)
│   └── Spiro_2026_preprint.pdf  # Compiled preprint
├── scripts/
│   └── paper1_figures.py        # Generates all 6 main figures from data/
├── data/
│   ├── gof_lof_analysis.csv     # 72 genes with rise/recovery, CGC status, GoF/LoF
│   ├── pathway_summary.csv      # Per-pathway summary (14 pathways)
│   ├── loop_components.csv      # 22 core feedback loop pairs
│   └── cgc_enrichment.json      # KEGG NFL extraction enrichment statistics
├── figures/                     # 6 publication figures (PDF + PNG)
├── supplementary/               # 4 supplementary tables
├── README.md
└── LICENSE
```

### Figures

| File | Topic |
|---|---|
| `figures/fig1_schematic.pdf/png` | Oscillation schematic + waveform classes |
| `figures/fig2_enrichment.pdf/png` | **Main result:** cancer gene enrichment by rise/recovery |
| `figures/fig3_divergent.pdf/png` | Divergent predictions vs naive classification (86% vs 14%) |
| `figures/fig4_gof_drugs.pdf/png` | GoF/LoF consistency + drug-target asymmetry |
| `figures/fig5_kegg_validation.pdf/png` | KEGG algorithmic NFL extraction validation |
| `figures/fig6_waveform.pdf/png` | Waveform asymmetry across 14 systems |

### Supplementary tables

| File | Contents |
|---|---|
| `supplementary/table_s1_gene_classification.csv` | Full 157-gene classification (rise / recovery / pathway / CGC status) |
| `supplementary/table_s2_divergent_predictions.csv` | 22 divergent cases (temporal vs biochemical) |
| `supplementary/table_s3_nfl_extraction.csv` | Algorithmic NFL extraction results |
| `supplementary/table_s4_waveform_parameters.csv` | Waveform parameters across 14 oscillatory systems |

## Reproducing the analysis

```bash
git clone https://github.com/mool32/oscillatory-cancer-framework.git
cd oscillatory-cancer-framework
pip install numpy scipy matplotlib
python scripts/paper1_figures.py
```

The repository commits the curated `data/` and `supplementary/` files; the figure-generation script reads from those directly. Re-running from primary sources (CGC, KEGG, DrugBank) is documented inline in the manuscript Methods.

## Citation

```bibtex
@article{spiro2026oscillatorycancer,
  author  = {Spiro, Theodor},
  title   = {Temporal architecture of signaling oscillations predicts cancer gene function across pathways},
  journal = {Preprint},
  year    = {2026},
  note    = {Preprint forthcoming. https://github.com/mool32/oscillatory-cancer-framework}
}
```

## Contact

Theodor Spiro — tspiro@vaika.org

## License

- **Code** (`scripts/`): MIT (see [LICENSE](LICENSE))
- **Data** (`data/`, `supplementary/`): CC-BY 4.0, with COSMIC CGC and KEGG attribution requirements honored per their respective licences
- **Figures** (`figures/`): CC-BY 4.0
- **Manuscript** (`paper/manuscript.md`, `paper/Spiro_2026_preprint.pdf`): CC-BY 4.0
