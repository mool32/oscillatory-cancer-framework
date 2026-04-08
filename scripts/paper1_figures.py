"""
Generate all main figures for Paper 1: Temporal architecture of signaling oscillations
predicts cancer gene function across pathways.

Produces 6 figures as PDF + PNG at publication quality (300 DPI).
"""

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.patches import FancyBboxPatch
from matplotlib.gridspec import GridSpec
import matplotlib
matplotlib.rcParams.update({
    'font.family': 'sans-serif',
    'font.sans-serif': ['Arial', 'Helvetica', 'DejaVu Sans'],
    'font.size': 9,
    'axes.labelsize': 10,
    'axes.titlesize': 11,
    'xtick.labelsize': 8,
    'ytick.labelsize': 8,
    'legend.fontsize': 8,
    'figure.dpi': 300,
    'savefig.dpi': 300,
    'savefig.bbox': 'tight',
    'pdf.fonttype': 42,  # TrueType for editability
    'ps.fonttype': 42,
})

RISE_COLOR = '#E74C3C'
RECOVERY_COLOR = '#3498DB'
NEUTRAL_COLOR = '#95A5A6'
PROMOTE_COLOR = '#E8D5B7'
INHIBIT_COLOR = '#D5E8D4'
CGC_COLOR = '#E74C3C'
NONCGC_COLOR = '#BDC3C7'
METABOLIC_COLOR = '#ECF0F1'

import os
OUTDIR = '/Users/teo/Desktop/research/paper1_main_figures'
os.makedirs(OUTDIR, exist_ok=True)


def save(fig, name):
    fig.savefig(f'{OUTDIR}/{name}.pdf', bbox_inches='tight')
    fig.savefig(f'{OUTDIR}/{name}.png', bbox_inches='tight', dpi=300)
    plt.close(fig)
    print(f'  Saved {name}')


# ======================================================================
# FIGURE 1: Schematic + waveform classes
# ======================================================================
def fig1():
    fig = plt.figure(figsize=(7.5, 8))
    gs = GridSpec(2, 2, figure=fig, hspace=0.35, wspace=0.3,
                  height_ratios=[1, 1])

    # Panel A: Oscillation schematic
    ax_a = fig.add_subplot(gs[0, 0])
    t = np.linspace(0, 3, 500)
    # Asymmetric waveform (Class I style)
    from scipy.signal import sawtooth
    # Build custom waveform: fast rise, slow recovery
    def asym_wave(t, period=1.0, A=0.3):
        phase = (t % period) / period
        y = np.where(phase < A,
                     np.sin(np.pi * phase / A / 2),
                     np.cos(np.pi * (phase - A) / (1 - A) / 2))
        return y

    y = asym_wave(t, period=1.0, A=0.28)
    ax_a.plot(t, y, 'k-', lw=1.5)
    # Shade rise and recovery for first cycle
    mask_rise = (t >= 0) & (t <= 0.28)
    mask_recov = (t >= 0.28) & (t <= 1.0)
    ax_a.fill_between(t[mask_rise], 0, y[mask_rise], alpha=0.3, color=RISE_COLOR,
                       label='Rise phase')
    ax_a.fill_between(t[mask_recov], 0, y[mask_recov], alpha=0.3, color=RECOVERY_COLOR,
                       label='Recovery phase')
    ax_a.annotate('Rise\n(fast)', xy=(0.14, 0.5), fontsize=8, ha='center',
                  color=RISE_COLOR, fontweight='bold')
    ax_a.annotate('Recovery\n(slow)', xy=(0.64, 0.3), fontsize=8, ha='center',
                  color=RECOVERY_COLOR, fontweight='bold')
    ax_a.set_xlabel('Time')
    ax_a.set_ylabel('Signal activity')
    ax_a.set_title('A', fontsize=13, fontweight='bold', loc='left')
    ax_a.set_xlim(0, 3)
    ax_a.set_ylim(-0.15, 1.15)
    ax_a.spines['top'].set_visible(False)
    ax_a.spines['right'].set_visible(False)
    ax_a.set_xticks([])
    ax_a.set_yticks([])
    ax_a.legend(loc='upper right', frameon=False, fontsize=7)

    # Panel B: Cancer prediction schematic
    ax_b = fig.add_subplot(gs[0, 1])
    ax_b.set_xlim(0, 10)
    ax_b.set_ylim(0, 10)
    ax_b.axis('off')
    ax_b.set_title('B', fontsize=13, fontweight='bold', loc='left')

    # Growth-promoting
    ax_b.add_patch(FancyBboxPatch((0.5, 5.5), 4, 4, boxstyle="round,pad=0.2",
                                   fc=PROMOTE_COLOR, ec='gray', lw=0.8))
    ax_b.text(2.5, 9.0, 'Growth-promoting', ha='center', fontsize=8, fontweight='bold')
    ax_b.text(2.5, 8.2, '(NF-kB, ERK, Wnt...)', ha='center', fontsize=6.5, color='gray')
    ax_b.text(1.3, 7.2, 'Rise GoF', ha='center', fontsize=7.5, color=RISE_COLOR, fontweight='bold')
    ax_b.text(1.3, 6.7, '= Oncogene', ha='center', fontsize=7, color=RISE_COLOR)
    ax_b.text(3.7, 7.2, 'Recovery LoF', ha='center', fontsize=7.5, color=RECOVERY_COLOR, fontweight='bold')
    ax_b.text(3.7, 6.7, '= TSG', ha='center', fontsize=7, color=RECOVERY_COLOR)
    ax_b.annotate('', xy=(1.3, 6.3), xytext=(1.3, 5.8),
                  arrowprops=dict(arrowstyle='->', color=RISE_COLOR, lw=1.5))
    ax_b.text(1.3, 5.5, 'Sustained\nactivation', ha='center', fontsize=6, color='#555')
    ax_b.annotate('', xy=(3.7, 6.3), xytext=(3.7, 5.8),
                  arrowprops=dict(arrowstyle='->', color=RECOVERY_COLOR, lw=1.5))
    ax_b.text(3.7, 5.5, 'No signal\ntermination', ha='center', fontsize=6, color='#555')

    # Growth-inhibitory
    ax_b.add_patch(FancyBboxPatch((5.5, 5.5), 4, 4, boxstyle="round,pad=0.2",
                                   fc=INHIBIT_COLOR, ec='gray', lw=0.8))
    ax_b.text(7.5, 9.0, 'Growth-inhibitory', ha='center', fontsize=8, fontweight='bold')
    ax_b.text(7.5, 8.2, '(p53, TGF-beta)', ha='center', fontsize=6.5, color='gray')
    ax_b.text(6.3, 7.2, 'Rise LoF', ha='center', fontsize=7.5, color=RECOVERY_COLOR, fontweight='bold')
    ax_b.text(6.3, 6.7, '= TSG', ha='center', fontsize=7, color=RECOVERY_COLOR)
    ax_b.text(8.7, 7.2, 'Recovery GoF', ha='center', fontsize=7.5, color=RISE_COLOR, fontweight='bold')
    ax_b.text(8.7, 6.7, '= Oncogene', ha='center', fontsize=7, color=RISE_COLOR)
    ax_b.text(7.5, 5.9, 'INVERTED', ha='center', fontsize=8, fontweight='bold',
              color='#666', style='italic')

    # Common outcome
    ax_b.add_patch(FancyBboxPatch((2, 0.5), 6, 2.5, boxstyle="round,pad=0.2",
                                   fc='#FADBD8', ec='gray', lw=0.8))
    ax_b.text(5, 2.3, 'CANCER', ha='center', fontsize=10, fontweight='bold', color=RISE_COLOR)
    ax_b.text(5, 1.5, 'Oscillation → Sustained signal', ha='center', fontsize=7.5, color='#555')
    ax_b.text(5, 1.0, '(pulsatile → constitutive)', ha='center', fontsize=6.5, color='#888')

    # Arrows to cancer box
    ax_b.annotate('', xy=(3.5, 3.0), xytext=(2.5, 5.5),
                  arrowprops=dict(arrowstyle='->', color='gray', lw=1))
    ax_b.annotate('', xy=(6.5, 3.0), xytext=(7.5, 5.5),
                  arrowprops=dict(arrowstyle='->', color='gray', lw=1))

    # Panel C: Three waveform classes
    ax_c = fig.add_subplot(gs[1, :])
    ax_c.set_title('C', fontsize=13, fontweight='bold', loc='left')

    classes = [
        ('Class I: A < 0.5', 0.28, ['NF-kB (0.28)', 'p53 (0.33)', 'ERK (0.30)', 'Circadian (0.33)'],
         'Fast destruction\nSlow synthesis'),
        ('Class II: A ≈ 0.5', 0.48, ['Hes1 (0.47)', 'STAT3 (0.50)', 'cAMP (0.45)'],
         'Balanced\nkinetics'),
        ('Class III: A > 0.5', 0.65, ['NFAT (0.63)', 'YAP (0.67)', 'Smad1 (0.75)'],
         'Slow activation\nFast inactivation'),
    ]

    colors = [RISE_COLOR, '#F39C12', RECOVERY_COLOR]
    t_wave = np.linspace(0, 2, 300)

    for i, (title, A, examples, mech) in enumerate(classes):
        x_offset = i * 3.5
        y_wave = asym_wave(t_wave, period=1.0, A=A)
        ax_c.plot(t_wave + x_offset, y_wave + 0.3, '-', color=colors[i], lw=2)

        # Shade
        mask_r = (t_wave <= A)
        mask_f = (t_wave >= A) & (t_wave <= 1.0)
        ax_c.fill_between(t_wave[mask_r] + x_offset, 0.3, y_wave[mask_r] + 0.3,
                           alpha=0.15, color=RISE_COLOR)
        ax_c.fill_between(t_wave[mask_f] + x_offset, 0.3, y_wave[mask_f] + 0.3,
                           alpha=0.15, color=RECOVERY_COLOR)

        ax_c.text(x_offset + 1, 1.65, title, ha='center', fontsize=9, fontweight='bold',
                  color=colors[i])
        ax_c.text(x_offset + 1, -0.1, mech, ha='center', fontsize=7, color='#555',
                  style='italic')
        for j, ex in enumerate(examples):
            ax_c.text(x_offset + 1, -0.45 - j * 0.18, ex, ha='center', fontsize=6.5,
                      color='#666')

    ax_c.set_xlim(-0.3, 10.5)
    ax_c.set_ylim(-1.2, 1.85)
    ax_c.axis('off')

    save(fig, 'fig1_schematic')


# ======================================================================
# FIGURE 2: Cancer gene enrichment
# ======================================================================
def fig2():
    fig, axes = plt.subplots(1, 3, figsize=(10, 4), gridspec_kw={'width_ratios': [1, 1.3, 2]})

    # Panel A: CGC fraction barplot
    ax = axes[0]
    categories = ['Oscillatory\npathways', 'Genome\nbackground', 'Metabolic\ncontrol']
    values = [47.8, 3.7, 0]
    colors_bar = [CGC_COLOR, NEUTRAL_COLOR, METABOLIC_COLOR]
    edgecolors = [CGC_COLOR, 'gray', 'gray']
    bars = ax.bar(categories, values, color=colors_bar, edgecolor=edgecolors, linewidth=0.8, width=0.6)
    ax.set_ylabel('Genes in CGC (%)')
    ax.set_title('A', fontsize=13, fontweight='bold', loc='left')
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.set_ylim(0, 60)
    # Annotations
    ax.text(0, 50, '75/157', ha='center', fontsize=8, fontweight='bold')
    ax.text(1, 6.5, '~740/20k', ha='center', fontsize=7, color='gray')
    ax.text(2, 3, '0/41', ha='center', fontsize=8, fontweight='bold')
    ax.text(0.5, 55, '24.1x', ha='center', fontsize=10, fontweight='bold', color=CGC_COLOR)

    # Panel B: 2x2 heatmap
    ax = axes[1]
    table_data = np.array([[37, 7], [5, 26]])
    im = ax.imshow(table_data, cmap='Reds', aspect='auto', vmin=0, vmax=40)
    ax.set_xticks([0, 1])
    ax.set_xticklabels(['Oncogene', 'TSG'], fontsize=9)
    ax.set_yticks([0, 1])
    ax.set_yticklabels(['Rise', 'Recovery'], fontsize=9)
    for i in range(2):
        for j in range(2):
            color = 'white' if table_data[i, j] > 20 else 'black'
            ax.text(j, i, str(table_data[i, j]), ha='center', va='center',
                    fontsize=14, fontweight='bold', color=color)
    ax.set_title('B', fontsize=13, fontweight='bold', loc='left')
    ax.text(0.5, -0.6, 'OR = 27.5 [7.9, 96.2]\np = 3.6e-9',
            ha='center', transform=ax.transAxes, fontsize=8, color='#333')

    # Panel C: Per-pathway patterns
    ax = axes[2]
    pathways = ['NF-kB', 'ERK', 'Wnt', 'Notch', 'Hippo', 'mTOR', 'JAK/STAT',
                'NRF2', 'Hedgehog', 'Calcium', 'p53*', 'TGF-β*', 'Circadian†', 'UPR†']
    coupled = [6, 9, 5, 4, 5, 14, 9, 4, 5, 2, 0, 0, 0, 0]
    anticoupled = [0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 6, 5, 0, 0]

    y_pos = np.arange(len(pathways))
    bars1 = ax.barh(y_pos, coupled, height=0.6, color=RISE_COLOR, alpha=0.8, label='Coupled (standard)')
    bars2 = ax.barh(y_pos, [-a for a in anticoupled], height=0.6, color=RECOVERY_COLOR, alpha=0.8,
                    label='Anti-coupled (inverted)')
    ax.set_yticks(y_pos)
    ax.set_yticklabels(pathways, fontsize=8)
    ax.set_xlabel('Gene-cancer associations')
    ax.axvline(0, color='gray', lw=0.5)
    ax.set_title('C', fontsize=13, fontweight='bold', loc='left')
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.legend(loc='lower right', fontsize=7, frameon=False)
    ax.text(0.95, 0.02, '*Predicted inversion\n†No CGC genes',
            transform=ax.transAxes, fontsize=6.5, ha='right', va='bottom', color='#666')
    ax.invert_yaxis()

    plt.tight_layout()
    save(fig, 'fig2_enrichment')


# ======================================================================
# FIGURE 3: Divergent predictions
# ======================================================================
def fig3():
    fig, axes = plt.subplots(1, 2, figsize=(8, 4.5))

    # Panel A: Accuracy comparison
    ax = axes[0]
    frameworks = ['Oscillatory\ntemporal', 'Naive\nbiochemical']
    correct = [19, 3]
    incorrect = [1, 17]
    partial = [2, 2]
    x = np.arange(2)
    w = 0.5
    ax.bar(x, correct, w, label='Correct', color='#27AE60', edgecolor='white')
    ax.bar(x, partial, w, bottom=correct, label='Partial', color='#F39C12', edgecolor='white')
    ax.bar(x, incorrect, w, bottom=[c+p for c, p in zip(correct, partial)],
           label='Incorrect', color='#E74C3C', edgecolor='white')
    ax.set_xticks(x)
    ax.set_xticklabels(frameworks, fontsize=10)
    ax.set_ylabel('Number of divergent genes (n=22)')
    ax.set_title('A', fontsize=13, fontweight='bold', loc='left')
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.legend(frameon=False, fontsize=8)
    # Percentage labels
    ax.text(0, 20.5, '86%', ha='center', fontsize=11, fontweight='bold', color='#27AE60')
    ax.text(1, 4.5, '14%', ha='center', fontsize=11, fontweight='bold', color='#27AE60')

    # Panel B: Category breakdown
    ax = axes[1]
    categories = ['Kinases\nas TSGs', 'E3 ligases\nas TSGs', 'Phosphatases\nas oncogenes',
                  'DUBs\nas TSGs', 'Scaffolds\n(surprising)', 'Other']
    counts = [7, 5, 2, 2, 4, 2]
    colors_cat = ['#3498DB', '#2ECC71', '#E74C3C', '#9B59B6', '#F39C12', '#95A5A6']
    bars = ax.barh(range(len(categories)), counts, color=colors_cat, edgecolor='white', height=0.6)
    ax.set_yticks(range(len(categories)))
    ax.set_yticklabels(categories, fontsize=8)
    ax.set_xlabel('Number of divergent genes')
    ax.set_title('B', fontsize=13, fontweight='bold', loc='left')
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.invert_yaxis()
    for i, c in enumerate(counts):
        ax.text(c + 0.2, i, str(c), va='center', fontsize=9, fontweight='bold')

    plt.tight_layout()
    save(fig, 'fig3_divergent')


# ======================================================================
# FIGURE 4: GoF/LoF + Drug targets
# ======================================================================
def fig4():
    fig, axes = plt.subplots(1, 2, figsize=(8, 4))

    # Panel A: GoF/LoF consistency
    ax = axes[0]
    labels = ['GoF +\nRise', 'LoF +\nRecovery', 'GoF +\nRecovery*', 'LoF +\nRise*']
    values = [28, 22, 5, 7]
    colors_gof = [RISE_COLOR, RECOVERY_COLOR, '#F39C12', '#F39C12']
    bars = ax.bar(labels, values, color=colors_gof, edgecolor='white', width=0.6)
    ax.set_ylabel('Number of CGC genes')
    ax.set_title('A', fontsize=13, fontweight='bold', loc='left')
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    # Brace for standard vs inverted
    ax.annotate('Standard (51)', xy=(0.5, 30), fontsize=8, ha='center', color='#333')
    ax.annotate('Inverted (12)', xy=(2.5, 10), fontsize=8, ha='center', color='#F39C12')
    ax.text(0.5, -5, '*p53 + TGF-β pathways', ha='center', fontsize=7, color='#888',
            transform=ax.transData)
    for i, v in enumerate(values):
        ax.text(i, v + 0.5, str(v), ha='center', fontsize=9, fontweight='bold')
    ax.set_ylim(0, 35)

    # Panel B: Drug target pie
    ax = axes[1]
    sizes = [28, 5]
    labels_pie = [f'Rise arm\n({28}/33)', f'Recovery arm\n({5}/33)']
    colors_pie = [RISE_COLOR, RECOVERY_COLOR]
    explode = (0.05, 0.05)
    wedges, texts, autotexts = ax.pie(sizes, explode=explode, labels=labels_pie,
                                       autopct='%1.0f%%', colors=colors_pie,
                                       startangle=90, textprops={'fontsize': 9})
    for t in autotexts:
        t.set_fontsize(10)
        t.set_fontweight('bold')
    ax.set_title('B', fontsize=13, fontweight='bold', loc='left', x=-0.1)
    ax.text(0, -1.35, 'GoF drug targets by temporal role\n(p = 3.3e-5)',
            ha='center', fontsize=8, color='#333')

    plt.tight_layout()
    save(fig, 'fig4_gof_drugs')


# ======================================================================
# FIGURE 5: KEGG validation
# ======================================================================
def fig5():
    fig, axes = plt.subplots(1, 3, figsize=(10, 4))

    # Panel A: Pipeline schematic (text-based)
    ax = axes[0]
    ax.axis('off')
    ax.set_title('A', fontsize=13, fontweight='bold', loc='left')
    steps = [
        ('KEGG KGML\npathways', '#D5E8D4'),
        ('Signed\nDiGraph', '#DAE8FC'),
        ('Cycle\nenumeration', '#DAE8FC'),
        ('NFL\nfiltering', '#DAE8FC'),
        ('76 unique\nNFL genes', '#E8D5B7'),
    ]
    for i, (txt, color) in enumerate(steps):
        y = 0.85 - i * 0.18
        ax.add_patch(FancyBboxPatch((0.1, y - 0.05), 0.8, 0.12,
                                     boxstyle="round,pad=0.02", fc=color, ec='gray', lw=0.5,
                                     transform=ax.transAxes))
        ax.text(0.5, y + 0.01, txt, ha='center', va='center', fontsize=8,
                transform=ax.transAxes)
        if i < 4:
            ax.annotate('', xy=(0.5, y - 0.05), xytext=(0.5, y - 0.06),
                        xycoords='axes fraction', textcoords='axes fraction',
                        arrowprops=dict(arrowstyle='->', color='gray', lw=1))

    # Panel B: Three-tier enrichment
    ax = axes[1]
    tests = ['NFL vs\nGenome', 'NFL vs\nKEGG signaling', 'NFL vs\nnon-NFL\n(same pathways)']
    folds = [12.8, 28.1, 59.0]
    colors_b = ['#E8D5B7', '#F5CBA7', CGC_COLOR]
    bars = ax.bar(tests, folds, color=colors_b, edgecolor='gray', linewidth=0.5, width=0.55)
    ax.set_ylabel('Enrichment (fold or OR)')
    ax.set_title('B', fontsize=13, fontweight='bold', loc='left')
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    for i, (v, c) in enumerate(zip(folds, colors_b)):
        ax.text(i, v + 1.5, f'{v:.1f}×', ha='center', fontsize=9, fontweight='bold')
    ax.set_ylim(0, 72)

    # Panel C: Venn overlap
    ax = axes[2]
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 10)
    ax.axis('off')
    ax.set_title('C', fontsize=13, fontweight='bold', loc='left')

    # Manual circles
    from matplotlib.patches import Circle
    c1 = Circle((3.8, 5), 2.5, fill=True, fc=RISE_COLOR, alpha=0.2, ec=RISE_COLOR, lw=1.5)
    c2 = Circle((6.2, 5), 2.5, fill=True, fc=RECOVERY_COLOR, alpha=0.2, ec=RECOVERY_COLOR, lw=1.5)
    ax.add_patch(c1)
    ax.add_patch(c2)
    ax.text(2.5, 5, '46', fontsize=16, fontweight='bold', ha='center', va='center', color=RISE_COLOR)
    ax.text(5, 5, '24', fontsize=16, fontweight='bold', ha='center', va='center', color='#333')
    ax.text(7.5, 5, '12', fontsize=16, fontweight='bold', ha='center', va='center', color=RECOVERY_COLOR)
    ax.text(2.5, 8.3, 'Manual\noscillatory\n(70 CGC)', ha='center', fontsize=8, color=RISE_COLOR)
    ax.text(7.5, 8.3, 'Algorithmic\nNFL extraction\n(36 CGC)', ha='center', fontsize=8, color=RECOVERY_COLOR)

    plt.tight_layout()
    save(fig, 'fig5_kegg_validation')


# ======================================================================
# FIGURE 6: Waveform asymmetry
# ======================================================================
def fig6():
    fig, axes = plt.subplots(1, 2, figsize=(9, 4.5))

    # Data: (name, A, T_minutes, class)
    systems = [
        ('Ca²⁺ (vasopressin)', 0.20, 0.33, 1),
        ('NF-κB', 0.28, 100, 1),
        ('ERK', 0.30, 30, 1),
        ('p53', 0.33, 330, 1),
        ('Circadian', 0.33, 1440, 1),
        ('Insulin/pAKT', 0.20, 5, 1),
        ('Hes7', 0.43, 150, 2),
        ('cAMP', 0.45, 6, 2),
        ('Hes1', 0.47, 120, 2),
        ('STAT3', 0.50, 120, 2),
        ('NFAT', 0.63, 23, 3),
        ('YAP', 0.67, 75, 3),
        ('Smad1', 0.75, 120, 3),
    ]

    class_colors = {1: RISE_COLOR, 2: '#F39C12', 3: RECOVERY_COLOR}
    class_labels = {1: 'Class I (A<0.5)', 2: 'Class II (A≈0.5)', 3: 'Class III (A>0.5)'}

    # Panel A: A values strip chart
    ax = axes[0]
    for i, (name, A, T, cls) in enumerate(systems):
        ax.scatter(A, i, c=class_colors[cls], s=80, zorder=3, edgecolors='white', linewidth=0.5)
        ax.text(A + 0.02, i, name, fontsize=7, va='center')

    # Shade regions
    ax.axvspan(0.15, 0.40, alpha=0.08, color=RISE_COLOR)
    ax.axvspan(0.40, 0.55, alpha=0.08, color='#F39C12')
    ax.axvspan(0.55, 0.80, alpha=0.08, color=RECOVERY_COLOR)
    ax.axvline(0.5, color='gray', ls='--', lw=0.5, alpha=0.5)

    ax.set_xlabel('Asymmetry ratio A = τ_rise / T')
    ax.set_yticks([])
    ax.set_title('A', fontsize=13, fontweight='bold', loc='left')
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.spines['left'].set_visible(False)
    ax.set_xlim(0.1, 0.95)
    # Class labels at top
    ax.text(0.275, len(systems) + 0.5, 'Class I', ha='center', fontsize=8,
            color=RISE_COLOR, fontweight='bold')
    ax.text(0.475, len(systems) + 0.5, 'Class II', ha='center', fontsize=8,
            color='#F39C12', fontweight='bold')
    ax.text(0.675, len(systems) + 0.5, 'Class III', ha='center', fontsize=8,
            color=RECOVERY_COLOR, fontweight='bold')

    # Panel B: Period vs A (log scale for T)
    ax = axes[1]
    for name, A, T, cls in systems:
        ax.scatter(T, A, c=class_colors[cls], s=80, zorder=3, edgecolors='white', linewidth=0.5)
        offset_x = 1.15
        ha = 'left'
        ax.text(T * offset_x, A, name, fontsize=6.5, va='center', ha=ha, color='#555')

    ax.set_xscale('log')
    ax.axhline(0.5, color='gray', ls='--', lw=0.5, alpha=0.5)
    ax.axhspan(0.15, 0.40, alpha=0.05, color=RISE_COLOR)
    ax.axhspan(0.40, 0.55, alpha=0.05, color='#F39C12')
    ax.axhspan(0.55, 0.80, alpha=0.05, color=RECOVERY_COLOR)
    ax.set_xlabel('Period T (minutes)')
    ax.set_ylabel('Asymmetry ratio A')
    ax.set_title('B', fontsize=13, fontweight='bold', loc='left')
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.set_xlim(0.1, 5000)
    ax.set_ylim(0.1, 0.85)

    # Annotation: NF-kB and Circadian share A despite 15x T difference
    ax.annotate('', xy=(1440, 0.34), xytext=(100, 0.34),
                arrowprops=dict(arrowstyle='<->', color='gray', lw=1, ls='--'))
    ax.text(380, 0.36, '15× period\nsame A', fontsize=6.5, ha='center', color='gray', style='italic')

    handles = [plt.scatter([], [], c=class_colors[c], s=50, label=class_labels[c]) for c in [1, 2, 3]]
    ax.legend(handles=handles, loc='upper left', fontsize=7, frameon=False)

    plt.tight_layout()
    save(fig, 'fig6_waveform')


# ======================================================================
# Run all
# ======================================================================
if __name__ == '__main__':
    print('Generating Paper 1 figures...')
    fig1()
    fig2()
    fig3()
    fig4()
    fig5()
    fig6()
    print('Done! Figures saved to', OUTDIR)
