#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Generate market data chart for 2026-09-29 morning report.
US International Market closing data from Sep 28, 2026.
"""

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.font_manager import FontProperties
import os

# ── Font configuration for macOS Chinese support ──────────────────────────────
FONT_PATHS = [
    '/System/Library/Fonts/STHeiti Medium.ttc',
    '/System/Library/Fonts/Supplemental/Songti.ttc',
    '/Library/Fonts/Arial Unicode MS.ttf',
]
prop = None
for fp in FONT_PATHS:
    if os.path.exists(fp):
        prop = FontProperties(fname=fp)
        break
if prop is None:
    prop = FontProperties()  # fallback

plt.rcParams['axes.unicode_minus'] = False

# ── Data ──────────────────────────────────────────────────────────────────────
assets = [
    ('道指\nDJIA', 51481.51, -0.67),
    ('标普500\nS&P 500', 7683.69, -0.77),
    ('纳斯达克\nNasdaq', 26820.38, -0.92),
    ('10Y美债\n收益率%', 5.24, +7),      # change in bps not pct; special handling below
    ('布伦特油\n$/桶', 105.29, +1.8),
    ('WTI油\n$/桶', 95.73, +1.5),
    ('黄金\n$/盎司', 4114.98, -3.5),
    ('美元指数\nDXY', 101.16, +0.3),
    ('BTC\n$', 83408, -0.6),
]

# separate bond yield for display
LABELS     = [a[0] for a in assets]
VALUES     = [a[1] for a in assets]
CHANGES    = [a[2] for a in assets]

# color: red = up (Chinese convention: red=up), green = down
# but skill says: red=up 🔴 green=down 🟢
COLORS = []
for i, (_, _, chg) in enumerate(assets):
    if i == 3:  # bond yield: yield UP is bad for equities → treat as "red" only for coloring
        COLORS.append('#e74c3c' if chg > 0 else '#27ae60')
    else:
        COLORS.append('#e74c3c' if chg > 0 else '#27ae60')

# ── Figure ────────────────────────────────────────────────────────────────────
fig, axes = plt.subplots(1, len(assets), figsize=(20, 5.5))
fig.patch.set_facecolor('#1a1a2e')

for ax, label, value, chg, color in zip(axes, LABELS, VALUES, CHANGES, COLORS):
    ax.set_facecolor('#16213e')
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    ax.axis('off')

    # asset name
    ax.text(0.5, 0.85, label, ha='center', va='center',
            fontsize=9, color='#aeb6bf', fontproperties=prop,
            transform=ax.transAxes)

    # value
    if value >= 1000:
        val_str = f'{value:,.2f}' if value < 100000 else f'{value:,.0f}'
    elif value < 10:
        val_str = f'{value:.2f}'
    else:
        val_str = f'{value:,.2f}'
    ax.text(0.5, 0.50, val_str, ha='center', va='center',
            fontsize=13, fontweight='bold', color='white',
            transform=ax.transAxes)

    # change
    arrow = '▲' if chg > 0 else '▼'
    if abs(chg) < 5:
        chg_str = f'{arrow} {abs(chg):.2f}%'
    else:
        # bond: bps
        chg_str = f'{arrow} {abs(chg):.0f}bps' if label.startswith('10Y') else f'{arrow} {abs(chg):.2f}%'

    # fix bond yield change
    if '10Y' in label:
        chg_str = f'▲ +7bps' if chg > 0 else f'▼ {abs(chg):.0f}bps'

    ax.text(0.5, 0.20, chg_str, ha='center', va='center',
            fontsize=11, color=color, fontproperties=prop,
            transform=ax.transAxes)

    # border
    for spine in ['top', 'bottom', 'left', 'right']:
        ax.spines[spine].set_visible(True)
        ax.spines[spine].set_color(color)
        ax.spines[spine].set_linewidth(1.5)

# ── Title ─────────────────────────────────────────────────────────────────────
fig.text(0.5, 0.97,
         '🌐 国际市场行情复盘 | 2026年9月28日（周一）美国收盘',
         ha='center', va='top', fontsize=13, color='white',
         fontproperties=prop, fontweight='bold')
fig.text(0.5, 0.01,
         '数据来源：TradingEconomics / Investing.com / XinhuaNet',
         ha='center', va='bottom', fontsize=7, color='#566573',
         fontproperties=prop)

# ── Save ──────────────────────────────────────────────────────────────────────
out_path = os.path.join(
    os.path.dirname(os.path.dirname(os.path.abspath(__file__))),
    'images', 'charts', 'chart_2026_09_29_morning.png'
)
os.makedirs(os.path.dirname(out_path), exist_ok=True)
plt.tight_layout(rect=[0, 0.04, 1, 0.94])
plt.savefig(out_path, dpi=150, bbox_inches='tight',
            facecolor=fig.get_facecolor())
print(f'Chart saved to: {out_path}')
plt.close()
