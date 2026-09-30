#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Generate market data chart for 2026-09-30 morning report.
US International Market closing data from Sep 29, 2026.
"""

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
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

# ── Data (2026-09-29 US close) ────────────────────────────────────────────────
assets = [
    ('道指\nDJIA', 51349.92, -0.26),
    ('标普500\nS&P 500', 7670.84, -0.17),
    ('纳斯达克\nNasdaq', 26797.54, -0.08),
    ('10Y美债\n收益率%', 5.25, +1),       # change in bps; special handling below
    ('黄金\n$/盎司', 4181.75, +1.6),
    ('WTI油\n$/桶', 89.25, -3.6),
    ('布伦特油\n$/桶', 102.90, -2.3),
    ('美元指数\nDXY', 101.39, +0.19),
    ('BTC\n$', 83385, +0.2),
]

LABELS  = [a[0] for a in assets]
VALUES  = [a[1] for a in assets]
CHANGES = [a[2] for a in assets]

# Chinese convention: red = up, green = down
COLORS = ['#e74c3c' if chg > 0 else '#27ae60' for (_, _, chg) in assets]

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
    if '10Y' in label:
        chg_str = f'{arrow} {abs(chg):.0f}bps'
    else:
        chg_str = f'{arrow} {abs(chg):.2f}%'

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
         '🌐 国际市场行情复盘 | 2026年9月29日（周二）美国收盘',
         ha='center', va='top', fontsize=13, color='white',
         fontproperties=prop, fontweight='bold')
fig.text(0.5, 0.01,
         '数据来源：Reuters / MarketWatch / Markets Insider / Trading Economics',
         ha='center', va='bottom', fontsize=7, color='#566573',
         fontproperties=prop)

# ── Save ──────────────────────────────────────────────────────────────────────
out_path = os.path.join(
    os.path.dirname(os.path.dirname(os.path.abspath(__file__))),
    'images', 'charts', 'chart_2026_09_30_morning.png'
)
os.makedirs(os.path.dirname(out_path), exist_ok=True)
plt.tight_layout(rect=[0, 0.04, 1, 0.94])
plt.savefig(out_path, dpi=150, bbox_inches='tight',
            facecolor=fig.get_facecolor())
print(f'Chart saved to: {out_path}')
plt.close()
