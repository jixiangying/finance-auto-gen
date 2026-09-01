#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""国际市场行情卡片生成脚本 - 2026-09-01 早报"""

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.font_manager import FontProperties
import os

font_paths = [
    '/System/Library/Fonts/STHeiti Medium.ttc',
    '/System/Library/Fonts/PingFang.ttc',
    '/System/Library/Fonts/Supplemental/Arial Unicode.ttf',
]
prop = None
for fp in font_paths:
    if os.path.exists(fp):
        prop = FontProperties(fname=fp)
        break
if prop is None:
    prop = FontProperties(family='sans-serif')

plt.rcParams['axes.unicode_minus'] = False

assets = [
    ('S&P 500',    '7,711.76', -0.25),
    ('纳斯达克',    '26,402',   -0.52),
    ('道琼斯',      '53,560',   -0.02),
    ('美债10Y',     '4.76%',    +4.0),
    ('黄金',        '$4,435',   -0.30),
    ('WTI原油',     '$86.10',   +4.50),
    ('布伦特',      '$90.20',   +3.80),
    ('BTC',         '$78,740',  -1.20),
]

def get_color(chg): return '#E53935' if chg >= 0 else '#43A047'
def get_arrow(chg): return '▲' if chg >= 0 else '▼'

fig, ax = plt.subplots(figsize=(14, 7))
fig.patch.set_facecolor('#0D1117')
ax.set_facecolor('#0D1117')
ax.axis('off')

ax.text(0.5, 0.97, '全球市场行情卡片  2026年09月01日 早报',
        transform=ax.transAxes, fontproperties=prop,
        fontsize=16, color='#E0E0E0', ha='center', va='top', fontweight='bold')
ax.text(0.5, 0.91, '以8月31日（周一）美国收盘数据为基准',
        transform=ax.transAxes, fontproperties=prop,
        fontsize=10, color='#888888', ha='center', va='top')

cols, rows = 4, 2
card_w = 1.0 / cols
card_h = 0.38

for i, (name, price, chg) in enumerate(assets):
    row = i // cols
    col = i % cols
    x = col * card_w + 0.01
    y = 0.83 - row * (card_h + 0.04) - card_h
    bg_color = '#1A1F2E' if i % 2 == 0 else '#161B2A'
    rect = mpatches.FancyBboxPatch(
        (x, y), card_w - 0.02, card_h,
        boxstyle="round,pad=0.01", linewidth=1.5,
        edgecolor=get_color(chg), facecolor=bg_color,
        transform=ax.transAxes)
    ax.add_patch(rect)
    cx = x + (card_w - 0.02) / 2
    cy_top = y + card_h - 0.04
    ax.text(cx, cy_top, name, transform=ax.transAxes,
            fontproperties=prop, fontsize=12, color='#B0BEC5',
            ha='center', va='top', fontweight='bold')
    ax.text(cx, cy_top - 0.12, price, transform=ax.transAxes,
            fontproperties=prop, fontsize=13, color='#ECEFF1',
            ha='center', va='top', fontweight='bold')
    chg_str = f'{get_arrow(chg)} {abs(chg):.2f}%'
    ax.text(cx, cy_top - 0.26, chg_str, transform=ax.transAxes,
            fontproperties=prop, fontsize=12, color=get_color(chg),
            ha='center', va='top', fontweight='bold')

ax.text(0.01, 0.03,
        'A Red=Up  V Green=Down  |  Sources: Schwab / TradingEconomics / GoldPrice.org / TwelveData',
        transform=ax.transAxes, fontproperties=prop,
        fontsize=8, color='#555555', ha='left', va='bottom')

output_path = '/Users/jxy/Documents/Project/finance-auto-gen/images/charts/chart_2026-09-01-morning.png'
plt.tight_layout()
plt.savefig(output_path, dpi=150, bbox_inches='tight',
            facecolor='#0D1117', edgecolor='none')
plt.close()
print(f"Chart saved: {output_path}")
