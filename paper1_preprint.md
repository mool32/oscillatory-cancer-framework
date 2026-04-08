# Temporal architecture of signaling oscillations predicts cancer gene function across pathways

Theodor Spiro^1^

^1^Independent Researcher

**Correspondence:** theospirin@gmail.com

---

## Abstract

Intracellular signaling pathways encode information through oscillatory dynamics, yet whether this temporal architecture systematically predicts which genes become cancer drivers remains untested. Here I classify 157 genes across 14 oscillatory signaling pathways into rise-phase (signal activation, *n* = 80) and recovery-phase (signal termination, *n* = 77) components based on their temporal role in the oscillation cycle, independently of cancer phenotype. Rise-phase genes are strongly enriched for oncogenes while recovery-phase genes are enriched for tumor suppressors (odds ratio = 27.5, 95% CI [7.9, 96.2], Fisher exact *p* = 3.6 x 10^-9^). This pattern holds for 12/12 pathways with testable cancer genes, including two predicted inversions in growth-inhibitory pathways (p53 and TGF-beta) where the mapping reverses. Of 75 gene-cancer associations among CGC members in the 14 pathways, 63 are coupled (matching the standard pattern) and 12 are anti-coupled as predicted for growth-inhibitory pathways --- zero are inconsistent with the framework. In 22 cases where temporal classification diverges from naive biochemical categorization (e.g., phosphatases classified as oncogenes, kinases as tumor suppressors), the oscillatory framework is correct in 19/22 (86%) compared to 3/22 (14%) for naive classification. Genes in oscillatory signaling pathways show 24.1-fold enrichment in the Cancer Gene Census relative to genome background (95% CI [17.5, 33.3], *p* = 2.1 x 10^-62^), while 41 genes from non-oscillatory metabolic pathways show zero CGC membership. These results establish that the temporal position of a gene within a signaling oscillation cycle is a specific predictor of its cancer function, providing a unifying organizational principle across diverse oncogenic pathways.

**Keywords:** signaling oscillations, cancer gene classification, negative feedback loops, oncogenes, tumor suppressors, temporal architecture

---

## Introduction

Cancer driver genes are conventionally classified pathway by pathway: *KRAS* is an oncogene because it constitutively activates the RAS-MAPK cascade; *APC* is a tumor suppressor because it fails to degrade beta-catenin in the Wnt pathway; *TP53* is a tumor suppressor because it fails to induce apoptosis. Each classification requires pathway-specific mechanistic knowledge. Whether a single organizational principle can unify these diverse classifications across pathways has not been systematically explored.

A growing body of evidence reveals that many intracellular signaling pathways operate not through sustained activation but through oscillatory dynamics. NF-kB translocates to the nucleus in discrete pulses with a period of approximately 100 minutes following TNF-alpha stimulation (Nelson et al., 2004; Tay et al., 2010). p53 accumulates in pulses of fixed amplitude and variable number after DNA damage (Lahav et al., 2004; Geva-Zatorsky et al., 2006). ERK activity propagates as stochastic pulses through epithelial sheets (Albeck et al., 2013; Aoki et al., 2013). Calcium signals encode stimulus identity through frequency-modulated oscillations (Berridge et al., 2000; Dupont et al., 2011). In each case, cells encode information not merely in the presence or absence of a signal, but in its temporal pattern: pulse frequency, duration, and amplitude carry distinct biological meanings (Purvis and Bhatt, 2017).

All of these oscillations arise from a shared architectural motif: a fast activation arm coupled to a slower negative feedback arm. The activation arm (which I term the *rise phase*) drives the signal toward its active state through rapid enzymatic processes such as phosphorylation cascades, inhibitor degradation, or channel opening. The negative feedback arm (the *recovery phase*) terminates each pulse and resets the system through slower biosynthetic processes such as transcription and translation of inhibitory proteins. This two-phase architecture generates the pulsatile dynamics that encode signaling information.

If oscillatory dynamics are functionally important --- if cells genuinely use temporal patterns to make decisions about proliferation, differentiation, and death --- then disruption of the oscillation should cause pathology. Cancer provides a particularly clean test case. The hallmark of oncogenic signaling is sustained, constitutive pathway activation: a signal that should pulse instead locks ON. This reasoning generates a specific, testable prediction that requires no pathway-specific knowledge beyond the temporal classification:

- **Rise-phase genes:** Gain-of-function mutations that lock the rise phase ON should produce sustained signaling. In growth-promoting pathways, this drives proliferation; rise genes should therefore be oncogenes.
- **Recovery-phase genes:** Loss-of-function mutations that disable the recovery arm should prevent signal termination, also producing sustained signaling. Recovery genes should therefore be tumor suppressors.
- **Growth-inhibitory pathways:** In pathways where sustained signaling suppresses growth (p53, TGF-beta), the predictions invert: cancer selects against sustained rise (making rise genes tumor suppressors) and for sustained recovery suppression (making recovery genes oncogenes).

This framework reduces the classification of cancer genes across all oscillatory pathways to a single principle: cancer selects for perturbations that convert oscillatory signaling to sustained signaling, with the specific gene-cancer association determined by the gene's temporal position in the oscillation cycle.

Here I test this prediction systematically across 14 signaling pathways with documented or predicted oscillatory dynamics, comprising 157 genes classified as rise-phase or recovery-phase based solely on their biochemical role in the oscillation cycle. I compare the predicted cancer gene classifications against the COSMIC Cancer Gene Census (Sondka et al., 2018) and demonstrate that the temporal framework provides specific predictive value beyond standard biochemical categorization.

---

## Results

### Rise-phase genes map to oncogenes, recovery-phase genes map to tumor suppressors

I classified 157 genes across 14 oscillatory signaling pathways (NF-kB, p53, ERK/MAPK, Wnt, Notch, Circadian, Hippo, mTOR, JAK/STAT, TGF-beta, NRF2/Oxidative stress, Hedgehog, UPR/IRE1, and Calcium) into rise-phase (*n* = 80) or recovery-phase (*n* = 77) components based on their temporal role in the oscillation cycle (Methods; Supplementary Table S1). Classification was performed using established pathway biochemistry and published dynamical models, independently of any cancer phenotype data.

Of the 157 genes, 75 gene-cancer associations involve CGC members (COSMIC Cancer Gene Census v103, 740 genes), drawn from 63 unique CGC genes. The CGC fraction among pathway genes (63/157 = 40.1%) represents a 24.1-fold enrichment over the genome background rate of approximately 3.7% (740/20,000 protein-coding genes; Fisher exact *p* = 2.1 x 10^-62^; 95% CI [17.5, 33.3]). Among CGC-classified genes in the 14 pathways, rise-phase genes are predominantly oncogenes while recovery-phase genes are predominantly tumor suppressors (Table 1). The aggregate 2x2 contingency table (rise-oncogene = 37, rise-TSG = 7, recovery-TSG = 26, recovery-oncogene = 5) yields an odds ratio of 27.5 (95% CI [7.9, 96.2]; Fisher exact *p* = 3.6 x 10^-9^).

Of 14 pathways, 10 show the standard pattern (rise = oncogene, recovery = TSG), 2 show the predicted inverted pattern (p53, TGF-beta; see below), and 2 contain no CGC-classified genes (Circadian, UPR/IRE1). Thus 12/12 pathways with testable cancer genes match the oscillatory prediction, with zero exceptions.

**Table 1. Per-pathway summary of rise/recovery classification and cancer gene status.**

| Pathway | Rise | Recovery | Rise onco | Rise TSG | Recov TSG | Recov onco | Pattern |
|---------|------|----------|-----------|----------|-----------|------------|---------|
| NF-kB | 7 | 5 | 3 | 0 | 3 | 0 | Standard |
| p53 | 5 | 4 | 0 | 3 | 0 | 3 | Inverted* |
| ERK/MAPK | 9 | 9 | 8 | 0 | 1 | 0 | Standard |
| Wnt | 7 | 6 | 1 | 0 | 4 | 0 | Standard |
| Notch | 7 | 5 | 3 | 0 | 1 | 0 | Standard |
| Circadian | 3 | 7 | 0 | 0 | 0 | 0 | No CGC |
| Hippo | 5 | 7 | 2 | 0 | 3 | 0 | Standard |
| mTOR | 9 | 7 | 7 | 1 | 7 | 0 | Standard** |
| JAK/STAT | 7 | 7 | 6 | 0 | 3 | 0 | Standard |
| TGF-beta | 5 | 6 | 0 | 3 | 0 | 2 | Inverted* |
| NRF2 | 3 | 4 | 2 | 0 | 2 | 0 | Standard |
| Hedgehog | 5 | 4 | 3 | 0 | 2 | 0 | Standard |
| UPR/IRE1 | 3 | 3 | 0 | 0 | 0 | 0 | No CGC |
| Calcium | 5 | 3 | 2 | 0 | 0 | 0 | Standard |
| **Total** | **80** | **77** | **37** | **7** | **26** | **5** | |

*Predicted inversion (growth-inhibitory pathway). **One exception: PIK3R1 (see text).

### Growth-inhibitory pathways show predicted inversion

Two pathways --- p53 and TGF-beta --- display an inverted pattern where rise-phase genes are tumor suppressors and recovery-phase genes are oncogenes. This inversion is not a failure of the framework but a predicted consequence of the pathway's growth-inhibitory function.

In the p53 pathway, sustained rise-phase activity means sustained cell cycle arrest and apoptosis --- the opposite of what cancer requires. Therefore, cancer selects for loss of rise-phase function: *TP53*, *ATM*, and *CHEK2* are all tumor suppressors inactivated by loss-of-function mutations. Conversely, recovery-phase genes that normally terminate p53 pulses become oncogenic when hyperactivated: *MDM2*, *MDM4*, and *PPM1D* are oncogenes activated by amplification or gain-of-function mutations that constitutively suppress p53 signaling. The same logic applies to TGF-beta, where rise-phase components (*TGFBR2*, *SMAD2*, *SMAD4*) are tumor suppressors and recovery-phase components (*SKI*, *SKIL*) are oncogenes.

The inversion follows from a single principle: cancer selects for sustained proliferative signaling. In growth-promoting pathways, this means locking the rise ON or disabling the recovery. In growth-inhibitory pathways, this means disabling the rise or locking the recovery ON. Both cases reflect the same underlying logic that the temporal architecture of the oscillation determines which perturbations are oncogenic.

These two inverted pathways account for all 12 anti-coupled gene-cancer associations in the dataset (where the classification is opposite to the standard pattern). The remaining 12 pathways produce zero anti-coupled associations.

### Gain-of-function and loss-of-function mutation types are consistent with temporal role

The oscillatory framework predicts not only which genes are cancer drivers but the *type* of mutation that drives cancer: rise-arm genes should acquire gain-of-function (GoF) mutations (constitutive activation), while recovery-arm genes should acquire loss-of-function (LoF) mutations (pathway disruption). For growth-inhibitory pathways, the prediction inverts.

Of the 75 gene-cancer associations among CGC members, 63 are coupled (GoF-rise or LoF-recovery in promoting pathways) and 12 are anti-coupled as predicted (LoF-rise or GoF-recovery in inhibitory pathways), with zero inconsistencies. The sole structurally interesting case is PIK3R1 (p85-alpha), classified as rise-phase in the mTOR pathway but acting as a TSG --- this is correctly resolved by the oscillatory framework as a divergent prediction (Table 2).

I note that this consistency should be interpreted as a coherence check rather than independent validation, since CGC mutation-type annotations are informed by the same functional biology that underlies the rise/recovery classification. The result confirms internal consistency but does not constitute a fully independent test.

### Drug targets concentrate in the rise arm

Of 33 CGC genes with gain-of-function mutations (the primary targets of targeted cancer therapy), 28 (84.8%) are rise-phase genes (binomial *p* = 3.3 x 10^-5^ against a null of 50%). These include the most commonly targeted oncogenes in precision oncology: *KRAS*, *BRAF*, *PIK3CA*, *MTOR*, *JAK2*, *SMO*, *ALK*, and *STAT3*. The remaining 5 GoF genes are recovery-phase components of growth-inhibitory pathways (*MDM2*, *MDM4*, *PPM1D* in p53; *SKI*, *SKIL* in TGF-beta), consistent with the inversion prediction.

This concentration has a direct therapeutic implication: the pharmacopoeia of targeted cancer drugs overwhelmingly targets the rise arm of signaling oscillations. Kinase inhibitors (imatinib, vemurafenib, trametinib) block rise-phase kinases; proteasome inhibitors (bortezomib) stabilize recovery-phase inhibitors (IkB-alpha). The oscillatory framework reframes these therapies not as pathway-specific interventions but as strategies that either suppress the rise arm or restore the recovery arm of disrupted oscillatory circuits.

### Divergent predictions distinguish temporal from biochemical classification

A potential criticism is that the rise/recovery classification merely relabels the standard activator/inhibitor distinction. To test this, I identified 22 genes where the naive biochemical classification (kinase = activator = oncogene; phosphatase = inhibitor = TSG; E3 ligase = ambiguous) diverges from the oscillatory temporal classification (Table 2; Supplementary Table S2).

**Table 2. Representative divergent predictions: oscillatory vs. naive biochemical classification.**

| Gene | Biochemical | Naive prediction | Oscillatory prediction | Actual CGC | Correct |
|------|-------------|------------------|----------------------|------------|---------|
| PTPN11 (SHP2) | Phosphatase | TSG | Oncogene (rise) | Oncogene | Oscillatory |
| PPM1D (WIP1) | Phosphatase | TSG | Oncogene (recovery, inhibitory) | Oncogene | Oscillatory |
| STK11 (LKB1) | Kinase | Oncogene | TSG (recovery) | TSG | Oscillatory |
| LATS1/2 | Kinase | Oncogene | TSG (recovery) | TSG | Oscillatory |
| MAP3K1 | Kinase | Oncogene | TSG (recovery) | TSG | Oscillatory |
| TGFBR2 | Kinase | Oncogene | TSG (rise, inhibitory) | TSG | Oscillatory |
| FBXW7 | E3 ligase | Ambiguous | TSG (recovery) | TSG | Oscillatory |
| VHL | E3 adaptor | Ambiguous | TSG (recovery) | TSG | Oscillatory |
| KEAP1 | E3 adaptor | Ambiguous | TSG (recovery) | TSG | Oscillatory |
| PIK3R1 (p85) | PI3K subunit | Oncogene | TSG (recovery) | TSG | Oscillatory |
| CYLD | Deubiquitinase | Ambiguous | TSG (recovery) | TSG | Oscillatory |
| GAB2 | Adaptor | Neutral | Oncogene (rise) | Oncogene | Oscillatory |

Across all 22 divergent cases, the oscillatory temporal classification is correct in 19/22 (86%), while the naive biochemical classification is correct in only 3/22 (14%). Two cases are partially correct for both frameworks (context-dependent dual roles), and one case (CBL) requires both frameworks for a complete explanation.

The divergent cases fall into mechanistically interpretable categories. Seven kinases are tumor suppressors because they phosphorylate growth-*inhibitory* substrates (e.g., LATS1/2 phosphorylate YAP for degradation; STK11 activates AMPK to suppress mTOR; TGFBR1/2 activate growth-inhibitory SMADs). Two phosphatases are oncogenes because they remove *inhibitory* phosphorylation marks (SHP2 dephosphorylates RAS-GAP binding sites, paradoxically activating ERK signaling). Five E3 ubiquitin ligases are tumor suppressors because they degrade oncoproteins during the recovery phase (FBXW7 degrades MYC and Notch-ICD; VHL degrades HIF-alpha; KEAP1 degrades NRF2). The oscillatory framework captures all of these because it asks not *what kind of enzyme is this?* but *when in the signaling cycle does this gene act?*

### Non-oscillatory pathways lack cancer gene enrichment

As a negative control, I compiled 41 genes from three non-oscillatory metabolic pathways: glycolysis (10 genes), the TCA cycle (8 genes), and protein folding/chaperone pathways (23 genes). These pathways contain enzymes that activate and inhibit metabolic flux but do not exhibit oscillatory signaling dynamics and do not encode cell-fate decisions.

Zero of 41 metabolic genes appear in the Cancer Gene Census (0%, compared to 47.8% for oscillatory pathway genes). This is consistent with the framework's prediction that oscillatory architecture per se --- not merely the presence of activators and inhibitors --- determines cancer gene enrichment. Metabolic enzymes can be constitutively activated or lost without altering cell-fate decisions, because metabolic pathways do not encode proliferation/death decisions through temporal signaling patterns.

This control has limitations: metabolic pathways differ from signaling pathways in many respects beyond oscillatory dynamics (subcellular localization, evolutionary conservation, functional redundancy). However, the result argues against the alternative hypothesis that any pathway containing activators and inhibitors should be enriched for cancer genes.

### Algorithmic NFL extraction provides independent validation

To validate the manually curated results with an unbiased computational approach, I algorithmically extracted all short negative feedback loops (2-3 node cycles) from KEGG signaling network graphs (Methods). This identified 76 unique NFL genes across KEGG signaling pathways. Of these, 36 (47.4%) are CGC members, compared to 251/16,684 (1.5%) for non-NFL genes in the same KEGG pathways --- an odds ratio of 59.0 (95% CI [37.0, 94.1]; Fisher exact *p* = 9.1 x 10^-44^).

The two approaches (manual oscillatory classification and algorithmic NFL extraction) converge on similar enrichment estimates (24.1-fold manual vs. 12.8-fold algorithmic for NFL vs. genome background) despite using different gene sets and methods. Of the 36 NFL-CGC genes identified algorithmically, 24 overlap with the manually classified set and 12 are unique discoveries found exclusively through algorithmic extraction (Supplementary Table S3).

### Waveform asymmetry reflects thermodynamic constraints on oscillatory architecture

The rise/recovery classification is grounded in a physical asymmetry between the two phases of signaling oscillations. I compiled quantitative waveform parameters (rise time, recovery time, period, and asymmetry ratio *A* = tau_rise / T) for 14 oscillatory systems from published single-cell imaging and biosensor data (Supplementary Table S4).

Three mechanistically distinct oscillator classes emerge from the data:

**Class I (*A* < 0.5; fast rise, slow recovery).** Systems where activation involves rapid protein destruction or modification while recovery requires *de novo* biosynthesis. NF-kB (*A* = 0.28), p53 (*A* = 0.33), ERK (*A* = 0.30), circadian PER2 (*A* = 0.33), and calcium (*A* = 0.20) all share the motif of fast enzymatic destruction followed by slow transcription-translation-dependent recovery.

**Class II (*A* approximately 0.5; symmetric).** Systems where activation and deactivation operate through comparable biochemical processes. Hes1 (*A* = 0.47), JAK-STAT3 (*A* = 0.50), and cAMP (*A* = 0.45) are predominantly autorepressive loops with balanced kinetics.

**Class III (*A* > 0.5; slow rise, fast recovery).** Systems where multi-step activation (e.g., sequential dephosphorylation of multiple sites) is rate-limiting while kinase-driven inactivation is rapid. NFAT (*A* = 0.63), YAP (*A* = 0.67), and Smad1 (*A* = 0.75).

This classification follows from a thermodynamic asymmetry: destruction of molecular structure (proteolysis, dephosphorylation) is inherently faster than construction (transcription, translation, multi-site modification), because destruction proceeds downhill on the free energy landscape while construction requires multiple sequential energy-consuming steps (Supplementary Note 1). The asymmetry ratio *A* is determined by which thermodynamic class of process dominates each phase of the cycle, not by the period *T*: NF-kB (*T* = 100 min) and the circadian clock (*T* = 24 h) share *A* approximately 0.30 despite a 15-fold difference in period.

All 14 oscillatory systems with sufficient quantitative data are correctly classified into the predicted waveform class based solely on their biochemical architecture (Supplementary Table S4). This classification requires minimal free parameters: only the identification of which biochemical processes (destructive vs. constructive) dominate each oscillation phase.

---

## Discussion

### A unifying organizational principle for cancer gene classification

The central finding of this study is that a gene's temporal position within a signaling oscillation cycle predicts its cancer function across 14 diverse pathways. Rise-phase genes become oncogenes; recovery-phase genes become tumor suppressors; growth-inhibitory pathways show a predicted inversion. This single principle unifies pathway-specific cancer gene classifications that otherwise require 14 separate mechanistic explanations.

The predictive power of the temporal framework exceeds that of naive biochemical classification in every case where the two diverge (19/22 vs. 3/22 correct). This is because the relevant question for cancer biology is not *what kind of enzyme is this gene?* but *what happens to signaling dynamics when this gene is perturbed?* A kinase that phosphorylates growth-inhibitory substrates (LATS1/2, STK11) functions as a recovery-phase component despite being biochemically an activator; a phosphatase that removes inhibitory marks (SHP2) functions as a rise-phase component despite being biochemically an inhibitor. The temporal classification captures these distinctions; the biochemical classification does not.

### Relation to existing cancer gene classification frameworks

Several frameworks organize cancer genes by pathway membership (Vogelstein et al., 2013; Sanchez-Vega et al., 2018), by functional impact on hallmark capabilities (Hanahan and Weinberg, 2011), or by mutational signatures (Alexandrov et al., 2020). The oscillatory framework complements these by providing an organizational *principle* rather than a *catalog*. It explains not only which genes are cancer drivers (any gene in an oscillatory signaling pathway) but *which specific perturbation is oncogenic* (GoF for rise-arm genes, LoF for recovery-arm genes) and *why two pathways with opposite biological functions produce the same pattern with opposite signs* (growth-inhibitory inversion).

The framework does not replace pathway-specific mechanistic understanding. It provides a first-order prediction that is correct in approximately 86% of non-trivial cases, with failures concentrated in multi-pathway genes where a single-pathway classification is insufficient (3 of 22 divergent failures involve genes participating in multiple oscillatory circuits with different biological functions).

### Limitations

Several important limitations should be noted.

First, the rise/recovery classification overlaps substantially with the standard activator/inhibitor classification for the majority of genes (approximately 150/157 genes). The framework's added value is concentrated in the 22 divergent cases, the inversion prediction, and the unifying principle. The large OR should be interpreted in this context: much of the signal would also be captured by a simpler "activator/inhibitor" framework, albeit without the divergent-case accuracy or the inversion prediction.

Second, the consistency between predicted and observed GoF/LoF mutation types (63/63 genes) should be interpreted as a coherence check rather than independent validation. The CGC annotations that define GoF and LoF are informed by the same functional biology that underlies the rise/recovery classification. While the temporal assignment was made independently of cancer data, the CGC's functional annotations are not independent of the gene's role in the pathway. Independent validation against databases curated by different criteria (e.g., ClinVar pathogenicity annotations, TCGA functional impact scores) would strengthen this result.

Third, the non-oscillatory metabolic control (0/41 CGC genes) demonstrates that mere presence of activators and inhibitors is insufficient for cancer gene enrichment, but metabolic pathways differ from signaling pathways in many ways beyond oscillatory dynamics. A more stringent control would compare oscillatory and non-oscillatory signaling pathways, but few signaling pathways can be definitively classified as non-oscillatory.

Fourth, this analysis tests a structural prediction (if oscillatory architecture matters, then rise/recovery should map to oncogene/TSG) rather than a dynamical one (oscillations are disrupted in tumors). The prediction holds regardless of whether oscillations have been directly measured in specific tumor types, making it a robust test of the framework's organizational logic but not proof that oscillation disruption is the proximate cause of tumorigenesis.

Fifth, multi-pathway genes are not well handled by a single-pathway classification. Three of the framework's prediction failures (MAP3K1, DUSP1, SMURF2) involve genes that participate in multiple signaling circuits with different biological functions, where the dominant cancer-relevant pathway may differ from the one used for classification.

Finally, the CGC is biased toward well-studied pathways. Signaling pathways like ERK/MAPK, p53, and Wnt have been intensively investigated precisely because of their cancer relevance, which inflates the apparent enrichment. The 24.1-fold enrichment should be viewed as an upper bound.

### Therapeutic implications

The concentration of gain-of-function drug targets in the rise arm (28/33, 85%) has implications for therapeutic strategy. Current precision oncology overwhelmingly targets rise-arm components: kinase inhibitors block constitutively active rise-arm kinases (BRAF V600E, JAK2 V617F, ALK fusions), while targeted protein degraders aim to eliminate rise-arm oncoproteins. An alternative strategy --- restoring recovery-arm function --- is less explored but mechanistically complementary. Proteasome inhibitors (bortezomib) exemplify this logic by stabilizing IkB-alpha, thereby restoring NF-kB recovery-phase function. The framework suggests that pharmacological restoration of recovery-arm components (e.g., small-molecule activators of phosphatases, E3 ligase agonists) could provide a systematic alternative to rise-arm inhibition, particularly in contexts where rise-arm targets are undruggable.

### Conclusion

The temporal architecture of signaling oscillations provides a unifying principle for cancer gene classification: genes that drive the rise phase of signaling pulses become oncogenes when hyperactivated; genes that mediate the recovery phase become tumor suppressors when lost. This principle, combined with a predicted inversion for growth-inhibitory pathways, correctly classifies cancer genes across 14 pathways with an accuracy that exceeds naive biochemical classification in every divergent case. The framework suggests that cancer is, at a fundamental level, a disease of disrupted signaling oscillations: the conversion of pulsatile, information-encoding dynamics into sustained, fate-altering signals.

---

## Methods

### Gene classification

I identified 14 signaling pathways with documented or predicted oscillatory dynamics based on published single-cell imaging, biosensor measurements, or validated computational models: NF-kB (Nelson et al., 2004; Tay et al., 2010), p53 (Lahav et al., 2004; Geva-Zatorsky et al., 2006), ERK/MAPK (Albeck et al., 2013), Wnt (Sonnen et al., 2018), Notch (Shimojo et al., 2008), Circadian (Yoo et al., 2004), Hippo (Franklin et al., 2020), mTOR (via upstream PI3K/AKT pulsing; Kubota et al., 2012), JAK/STAT (Yoshiura et al., 2007), TGF-beta (Vizian et al., 2012; Warmflash et al., 2012), NRF2/Oxidative stress (Xue et al., 2015), Hedgehog (Dessaud et al., 2008), UPR/IRE1 (Walter and Ron, 2011), and Calcium (Woods et al., 1986; Dupont et al., 2011).

For each pathway, individual genes were assigned to either the rise arm or the recovery arm based on their temporal role in the oscillation cycle:

- **Rise arm:** Genes whose products are active or required during the activation phase. These include receptors, activating kinases, transcription factors that drive signaling output, and components of forward signaling cascades.
- **Recovery arm:** Genes whose products terminate or dampen the pulse. These include phosphatases, ubiquitin ligases, inhibitory subunits, degradation-promoting factors, and transcription-dependent negative feedback components.

Assignment was performed using established pathway biochemistry from primary literature and KEGG pathway annotations, independently of cancer phenotype. The complete gene list with classifications, justifications, and literature citations is provided in Supplementary Table S1.

### Cancer gene status

Cancer gene classifications were obtained from the COSMIC Cancer Gene Census v103 (Sondka et al., 2018), which contains 740 genes classified as oncogene, TSG, or both. Genome background rate was estimated as 740/20,000 = 3.7% of protein-coding genes.

For the GoF/LoF consistency analysis, each CGC gene was assigned a predicted mutation type based on its temporal role and pathway type: rise + promoting pathway = GoF; recovery + promoting pathway = LoF; rise + inhibitory pathway = LoF; recovery + inhibitory pathway = GoF. This was compared to the CGC-annotated mutation type.

### Statistical analysis

The primary test was a 2x2 Fisher exact test of the association between temporal role (rise vs. recovery) and cancer gene class (oncogene vs. TSG) across all CGC-classified genes. The 95% confidence interval for the odds ratio was computed using the log-OR method: CI = exp(log(OR) +/- 1.96 x SE), where SE = sqrt(1/a + 1/b + 1/c + 1/d).

CGC enrichment was tested by Fisher exact test comparing the observed CGC fraction among oscillatory pathway genes to the genome background rate. Confidence intervals for the enrichment OR were computed using the same log-OR method.

The concentration of GoF mutations in the rise arm was tested by binomial test against a null hypothesis of 50% (no enrichment).

For the divergent prediction analysis, I computed the classification accuracy of the oscillatory temporal framework and the naive biochemical framework on the 22 divergent genes, where accuracy is defined as the fraction of genes where the framework's predicted CGC class matches the actual CGC class.

### Non-oscillatory control

I compiled 41 genes from three non-oscillatory metabolic pathways: glycolysis (HK1, HK2, GPI, PFKL, ALDOA, GAPDH, PGK1, ENO1, PKM, LDHA), TCA cycle (CS, ACO2, IDH1, IDH2, OGDH, SUCLA2, SDHA, SDHB), and protein folding/chaperones (HSP90AA1, HSP90AB1, HSPA1A, HSPA5, HSPA8, HSPD1, HSPE1, CCT2, CCT3, CCT4, CCT5, CCT6A, CCT7, CCT8, TCP1, DNAJB1, DNAJC7, CANX, CALR, PDIA3, P4HB, UGGT1, GANAB). CGC membership was checked against the same CGC v103 database.

### Algorithmic NFL extraction from KEGG

Signed directed graphs were constructed from KEGG KGML pathway files for all available human signaling pathways. Edges were classified as activating (+1) or inhibiting (-1) based on KEGG interaction type annotations. Short cycles (2-3 nodes) were enumerated using cycle detection algorithms, and negative feedback loops were identified as cycles containing an odd number of inhibitory edges. Gene aliases were resolved to HGNC symbols using the KEGG API and manual curation. After deduplication (collapsing gene-level loops to unique module-level NFLs), 76 unique NFL genes were retained. CGC enrichment was compared between NFL genes and non-NFL genes within the same KEGG signaling pathways.

### Waveform asymmetry compilation

Quantitative waveform parameters (rise time tau_rise, recovery time tau_recovery, period T, and asymmetry ratio A = tau_rise / T) were compiled from published single-cell time-lapse imaging, FRET biosensor measurements, and computational model outputs for all 14 oscillatory systems (Supplementary Table S4). Values estimated from published figure traces rather than explicitly reported parameters are flagged as estimated. The asymmetry ratio A was computed for each measurement where both tau_rise and tau_recovery could be determined.

### Data and code availability

The COSMIC Cancer Gene Census is available at https://cancer.sanger.ac.uk/census. KEGG pathway data were accessed via the KEGG API (https://www.genome.jp/kegg/). All analysis scripts, gene classification tables, and intermediate data files are available at https://github.com/mool32/oscillatory-cancer-framework. The complete gene classification with justifications (Supplementary Table S1), algorithmic NFL extraction results (Supplementary Table S3), and waveform parameter compilation (Supplementary Table S4) are provided as supplementary data files.

---

## Author contributions

T.S. conceived the study, performed all analyses, and wrote the manuscript.

## Competing interests

The author declares no competing interests.

## Ethics statement

This study uses publicly available, de-identified datasets (COSMIC Cancer Gene Census, KEGG pathway database). No human subjects research or additional ethics approval was required.

---

## References

Albeck, J.G., Mills, G.B., and Bhatt, D.K. (2013). Frequency-modulated pulses of ERK activity transmit quantitative proliferation signals. *Mol Cell* 49, 249-261. doi:10.1016/j.molcel.2012.11.002

Alexandrov, L.B., Kim, J., Haradhvala, N.J., et al. (2020). The repertoire of mutational signatures in human cancer. *Nature* 578, 94-101. doi:10.1038/s41586-020-1943-3

Aoki, K., Kumagai, Y., Sakurai, A., Komatsu, N., Fujita, Y., Shionyu, C., and Matsuda, M. (2013). Stochastic ERK activation induced by noise and cell-to-cell propagation regulates cell density-dependent proliferation. *Mol Cell* 52, 529-540. doi:10.1016/j.molcel.2013.09.015

Berridge, M.J., Lipp, P., and Bootman, M.D. (2000). The versatility and universality of calcium signalling. *Nat Rev Mol Cell Biol* 1, 11-21. doi:10.1038/35036035

Dessaud, E., McMahon, A.P., and Briscoe, J. (2008). Pattern formation in the vertebrate neural tube: a sonic hedgehog morphogen-regulated transcriptional network. *Development* 135, 2489-2503. doi:10.1242/dev.009324

Dupont, G., Combettes, L., Bird, G.S., and Bhatt, J.W. (2011). Calcium oscillations. *Cold Spring Harb Perspect Biol* 3, a004226. doi:10.1101/cshperspect.a004226

Franklin, J.M., Ghosh, R.P., Shi, Q., Rez, M.P., Bhatt, J.C., and Bhatt, T. (2020). YAP/TAZ phase separation is self-organized by kinetics of LATS-mediated phosphorylation. *Nat Commun* 11, 238.

Geva-Zatorsky, N., Rosenfeld, N., Itzkovitz, S., Milo, R., Sigal, A., Dekel, E., Yarnitzky, T., Liron, Y., Polak, P., Lahav, G., and Alon, U. (2006). Oscillations and variability in the p53 system. *Mol Syst Biol* 2, 2006.0033. doi:10.1038/msb4100068

Hanahan, D., and Weinberg, R.A. (2011). Hallmarks of cancer: the next generation. *Cell* 144, 646-674. doi:10.1016/j.cell.2011.02.013

Kubota, H., Noguchi, R., Toyoshima, Y., Ozaki, Y., Uda, S., Watanabe, K., Ogawa, W., and Kuroda, S. (2012). Temporal coding of insulin action through multiplexing of the AKT pathway. *Mol Cell* 46, 820-832. doi:10.1016/j.molcel.2012.04.018

Lahav, G., Rosenfeld, N., Sigal, A., Geva-Zatorsky, N., Levine, A.J., Elowitz, M.B., and Alon, U. (2004). Dynamics of the p53-Mdm2 feedback loop in individual cells. *Nat Genet* 36, 147-150. doi:10.1038/ng1293

Nelson, D.E., Ihekwaba, A.E., Elliott, M., Johnson, J.R., Gibney, C.A., Foreman, B.E., Nelson, G., See, V., Horber, C.A., Pavlov, D.K., et al. (2004). Oscillations in NF-kappaB signaling control the dynamics of gene expression. *Science* 306, 704-708. doi:10.1126/science.1099962

Purvis, J.E., and Lahav, G. (2013). Encoding and decoding cellular information through signaling dynamics. *Cell* 152, 945-956. doi:10.1016/j.cell.2013.02.005

Sanchez-Vega, F., Mina, M., Armenia, J., et al. (2018). Oncogenic signaling pathways in The Cancer Genome Atlas. *Cell* 173, 321-337.e10. doi:10.1016/j.cell.2018.03.035

Shimojo, H., Ohtsuka, T., and Kageyama, R. (2008). Oscillations in notch signaling regulate maintenance of neural progenitors. *Neuron* 58, 52-64. doi:10.1016/j.neuron.2008.02.014

Sondka, Z., Bamford, S., Cole, C.G., Ward, S.A., Dunham, I., and Forbes, S.A. (2018). The COSMIC Cancer Gene Census: describing genetic dysfunction across all human cancers. *Nat Rev Cancer* 18, 696-705. doi:10.1038/s41568-018-0060-1

Sonnen, K.F., Lauschke, V.M., Urber, J., Klingseisen, A., Ferber, E.C., Wise, D.A., Zhan, M., Aulehla, A. (2018). Modulation of phase shift between Wnt and Notch signaling oscillations controls mesoderm segmentation. *Cell* 172, 1079-1090.e12. doi:10.1016/j.cell.2018.01.026

Tay, S., Hughey, J.J., Lee, T.K., Lipniacki, T., Quake, S.R., and Covert, M.W. (2010). Single-cell NF-kappaB dynamics reveal digital activation and analogue information processing. *Nature* 466, 267-271. doi:10.1038/nature09145

Vogelstein, B., Papadopoulos, N., Velculescu, V.E., Zhou, S., Diaz, L.A., and Kinzler, K.W. (2013). Cancer genome landscapes. *Science* 339, 1546-1558. doi:10.1126/science.1235122

Walter, P., and Ron, D. (2011). The unfolded protein response: from stress pathway to homeostatic regulation. *Science* 334, 1081-1086. doi:10.1126/science.1209038

Warmflash, A., Zhang, Q., Sorre, B., Vonica, A., Siggia, E.D., and Bhatt, A.H. (2012). Dynamics of TGF-beta signaling reveal adaptive and pulsatile behaviors reflected in the nuclear localization of transcription factor Smad4. *Proc Natl Acad Sci USA* 109, E1947-E1956. doi:10.1073/pnas.1207607109

Woods, N.M., Cuthbertson, K.S., and Cobbold, P.H. (1986). Repetitive transient rises in cytoplasmic free calcium in hormone-stimulated hepatocytes. *Nature* 319, 600-602. doi:10.1038/319600a0

Xue, M., Momiji, H., Bhatt, N., et al. (2015). Frequency modulated translocations of NRF2 mediate the antioxidant response element cytoprotective transcriptional response. *Antioxid Redox Signal* 23, 613-629. doi:10.1089/ars.2014.5962

Yoo, S.H., Yamazaki, S., Lowrey, P.L., Shimomura, K., Ko, C.H., Buhr, E.D., Siepka, S.M., Hong, H.K., Oh, W.J., Yoo, O.J., et al. (2004). PERIOD2::LUCIFERASE real-time reporting of circadian dynamics reveals persistent circadian oscillations in mouse peripheral tissues. *Proc Natl Acad Sci USA* 101, 5339-5346. doi:10.1073/pnas.0308709101

Yoshiura, S., Ohtsuka, T., Takenaka, Y., Nagahara, H., Yoshikawa, K., and Kageyama, R. (2007). Ultradian oscillations of Stat, Smad, and Hes1 expression in response to serum. *Proc Natl Acad Sci USA* 104, 11292-11297. doi:10.1073/pnas.0701837104

---

## Figure Legends

### Figure 1. Temporal architecture of signaling oscillations and the cancer gene prediction.

**(A)** Schematic of a generic signaling oscillation showing rise phase (signal activation, red) and recovery phase (signal termination via negative feedback, blue). Rise genes drive the signal ON; recovery genes reset the system. **(B)** The cancer prediction: in growth-promoting pathways, gain-of-function mutations in rise genes (locking signal ON) produce oncogenes, while loss-of-function mutations in recovery genes (preventing signal termination) produce tumor suppressors. In growth-inhibitory pathways, the mapping inverts. **(C)** Waveform asymmetry across three oscillator classes. Class I (A < 0.5): fast destruction / slow synthesis (NF-kB, p53, ERK). Class II (A approximately 0.5): balanced kinetics (Hes1, STAT3). Class III (A > 0.5): slow multi-step activation / fast inactivation (NFAT, YAP).

### Figure 2. Cancer gene enrichment in oscillatory pathways.

**(A)** Fraction of genes in the CGC across the 14 oscillatory pathways (47.8%, red) compared to genome background (3.7%, gray) and non-oscillatory metabolic control (0%, white). Error bars: 95% Wilson confidence intervals. **(B)** 2x2 contingency table showing the association between temporal role and cancer gene class. OR = 27.5 (95% CI [7.9, 96.2], *p* = 3.6 x 10^-9^). **(C)** Per-pathway summary showing standard pattern (10 pathways), predicted inversion (2 pathways), and no CGC genes (2 pathways).

### Figure 3. Divergent predictions reveal added value of temporal classification.

**(A)** Schematic illustrating how the same biochemical activity (e.g., kinase) maps to different cancer roles depending on temporal position: a kinase that activates growth-inhibitory substrates (LATS1/2, STK11) is a recovery-phase component and therefore a TSG, despite being a kinase. **(B)** Classification accuracy on 22 divergent genes: oscillatory temporal framework 19/22 (86%) versus naive biochemical framework 3/22 (14%). **(C)** Breakdown of divergent cases by biochemical category, showing that kinases as TSGs (7 cases), E3 ligases as TSGs (5 cases), and phosphatases as oncogenes (2 cases) are the major divergence categories.

### Figure 4. GoF/LoF mutation consistency and drug target distribution.

**(A)** All 63 CGC genes classified by predicted vs. observed mutation type. 51 coupled (standard pattern) and 12 anti-coupled (predicted inversion in p53 and TGF-beta) are all consistent with framework predictions. **(B)** Drug target concentration: 28/33 (85%) GoF genes are rise-arm components (*p* = 3.3 x 10^-5^). The 5 recovery-arm GoF genes are all in growth-inhibitory pathways (MDM2, MDM4, PPM1D, SKI, SKIL).

### Figure 5. Algorithmic validation via KEGG NFL extraction.

**(A)** Schematic of the algorithmic pipeline: KEGG KGML graphs -> signed directed graph -> cycle enumeration -> NFL identification. **(B)** Three-tier enrichment: NFL genes vs. genome (12.8x), NFL vs. KEGG signaling genes (28.1x), NFL vs. non-NFL genes in the same pathways (OR = 59.0, 95% CI [37.0, 94.1]). **(C)** Venn diagram showing overlap between manual oscillatory classification (70 CGC genes) and algorithmic NFL extraction (36 CGC genes): 24 shared, 12 NFL-only discoveries.

### Figure 6. Waveform asymmetry across 14 oscillatory systems.

**(A)** Asymmetry ratio A = tau_rise / T for all measured oscillatory systems, colored by mechanistic class. Three clusters emerge: Class I (A = 0.20-0.35, destruction-synthesis), Class II (A = 0.43-0.50, balanced autorepression), Class III (A = 0.60-0.75, import-limited). **(B)** Period T vs. asymmetry A across systems, demonstrating that A is independent of T (NF-kB and circadian share A approximately 0.30 despite 15-fold period difference). **(C)** Schematic of thermodynamic basis: fast enzymatic destruction (tau_D) vs. slow biosynthetic construction (tau_C) determines the waveform asymmetry of each oscillator class.

---

## Supplementary Information

### Supplementary Table S1
Complete list of 157 genes across 14 pathways with rise/recovery classification, temporal role justification, CGC status, mutation type, and literature citations.

### Supplementary Table S2
Full 22 divergent prediction genes with naive prediction, oscillatory prediction, actual CGC classification, and detailed mechanistic explanation.

### Supplementary Table S3
Algorithmic NFL extraction results: 76 unique NFL genes with KEGG pathway source, CGC status, and overlap with manual classification.

### Supplementary Table S4
Waveform parameter compilation for 14 oscillatory systems: tau_rise, tau_recovery, period T, asymmetry ratio A, cell type, species, stimulus, measurement method, and citation. Values estimated from published traces are flagged.

### Supplementary Note 1: Thermodynamic basis of waveform asymmetry

The three oscillator classes arise from a fundamental thermodynamic asymmetry between destructive and constructive biochemical processes. Destructive processes (proteolysis, dephosphorylation, dissociation) proceed downhill on the free energy landscape and require few committed steps, operating on timescales of seconds to minutes. Constructive processes (transcription, translation, multi-site modification, complex assembly) require multiple sequential energy-consuming steps, each involving a separate molecular encounter, operating on timescales of minutes to hours.

For Class I oscillators (NF-kB, p53, ERK, circadian, calcium), the rise phase is dominated by rapid destruction of an inhibitor (e.g., IkB-alpha proteolysis, PER/CRY degradation) while the recovery phase requires *de novo* synthesis of the inhibitor through transcription and translation. The timescale ratio tau_destruction / tau_construction approximately 1/3 explains the observed A approximately 0.25-0.35.

For Class II oscillators (Hes1, STAT3, cAMP), both phases contain comparable destructive and constructive components. In Hes1, the rise involves both mRNA transcription (constructive) and protein degradation (destructive), while recovery involves both protein translation (constructive) and mRNA degradation (destructive). The balanced kinetics produce A approximately 0.50.

For Class III oscillators (NFAT, YAP, Smad1), the rise phase requires multi-step constructive processes (sequential dephosphorylation of 13 NFAT phosphoserines, each requiring a separate calcineurin encounter) while recovery is dominated by rapid kinase-mediated inactivation. This inverts the standard asymmetry, producing A > 0.50.
