#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
2026-09-11 早报行情数据卡片
数据来源：Yahoo Finance / Morningstar / Investing.com（权威收盘终值）
数据基准：美国市场 2026-09-10 收盘终值
"""

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.font_manager import FontProperties
import os

# ── 中文字体配置 ──────────────────────────────────────────────────────────────
font_paths = [
    '/System/Library/Fonts/STHeiti Medium.ttc',
    '/System/Library/Fonts/PingFang.ttc',
    '/System/Library/Fonts/Supplemental/Arial Unicode MS.ttf',
]
prop = None
for fp in font_paths:
    if os.path.exists(fp):
        prop = FontProperties(fname=fp)
        break
if prop is None:
    prop = FontProperties()

plt.rcParams['font.family'] = 'sans-serif'
plt.rcParams['axes.unicode_minus'] = False

# ── 数据定义（2026-09-10 收盘终值）────────────────────────────────────────────
data = [
    # (资产名称,    现价字符串,      涨跌幅%)
    ('道琼斯',    '52,064.10',   -0.610),
    ('标普500',   '7,591.70',    -0.580),
    ('纳斯达克',  '26,081.72',   -0.650),
    ('10Y 美债',  '4.943%',      +1.095),  # 收益率上行=债价下跌，标红
    ('美元指数',  '98.75',       +0.320),
    ('EUR/USD',   '1.1608',      -0.220),
    ('伦敦金现',  '$4,442.47',   +0.975),
    ('Brent 原油', '$107.63',    +5.820),
    ('比特币',    '$77,988',     -0.910),
]

labels  = [d[0] for d in data]
prices  = [d[1] for d in data]
changes = [d[2] for d in data]
colors  = ['#E8434B' if c > 0 else '#2DB87C' for c in changes]

# ── 绘图 ──────────────────────────────────────────────────────────────────────
fig, ax = plt.subplots(figsize=(13, 6))
fig.patch.set_facecolor('#0F1923')
ax.set_facecolor('#0F1923')
ax.axis('off')

ax.text(0.5, 0.97,
        '2026年09月11日（周五）国际市场早报 · 核心行情数据卡片',
        ha='center', va='top', transform=ax.transAxes,
        fontproperties=prop, fontsize=13, color='#F0F4F8', fontweight='bold')

ax.text(0.5, 0.91,
        '数据基准：美国市场 2026-09-10 收盘终值 | 来源：Yahoo Finance / Morningstar / Investing.com',
        ha='center', va='top', transform=ax.transAxes,
        fontproperties=prop, fontsize=8, color='#8899AA')

x_starts = [0.04, 0.37, 0.70]
y_starts  = [0.72, 0.42, 0.12]
card_w, card_h = 0.28, 0.25

for idx, (label, price, change, color) in enumerate(zip(labels, prices, changes, colors)):
    col = idx % 3
    row = idx // 3
    x0 = x_starts[col]
    y0 = y_starts[row]

    rect = mpatches.FancyBboxPatch(
        (x0, y0), card_w, card_h,
        boxstyle='round,pad=0.01',
        linewidth=1.5,
        edgecolor=color,
        facecolor='#1A2635',
        transform=ax.transAxes,
        clip_on=False
    )
    ax.add_patch(rect)

    ax.text(x0 + card_w/2, y0 + card_h - 0.04,
            label, ha='center', va='top', transform=ax.transAxes,
            fontproperties=prop, fontsize=10.5, color='#C8D8E8', fontweight='bold')

    ax.text(x0 + card_w/2, y0 + card_h/2 + 0.01,
            price, ha='center', va='center', transform=ax.transAxes,
            fontproperties=prop, fontsize=13.5, color='#F0F4F8', fontweight='bold')

    sign = '+' if change > 0 else ''
    icon = '▲' if change > 0 else '▼'
    ax.text(x0 + card_w/2, y0 + 0.04,
            f'{icon} {sign}{change:.3f}%',
            ha='center', va='bottom', transform=ax.transAxes,
            fontproperties=prop, fontsize=9.5, color=color, fontweight='bold')

ax.text(0.5, 0.01,
        '数据仅供参考，不构成投资建议。涨跌颜色：红色=上涨，绿色=下跌。',
        ha='center', va='bottom', transform=ax.transAxes,
        fontproperties=prop, fontsize=7, color='#556677')

output_dir = os.path.join(os.path.dirname(__file__), '..', 'images', 'charts')
os.makedirs(output_dir, exist_ok=True)
output_path = os.path.join(output_dir, '2026-09-11-morning-chart.png')
plt.tight_layout(pad=0.2)
plt.savefig(output_path, dpi=150, bbox_inches='tight', facecolor=fig.get_facecolor())
plt.close()
print(f'✅ 行情卡片已保存至: {output_path}')
