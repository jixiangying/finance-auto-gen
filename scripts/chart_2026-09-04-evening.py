#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""行情数据卡片 - 2026-09-04 晚报"""

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.font_manager import FontProperties
import os

font_paths = [
    '/System/Library/Fonts/STHeiti Medium.ttc',
    '/System/Library/Fonts/PingFang.ttc',
]
font_prop = None
for fp in font_paths:
    if os.path.exists(fp):
        font_prop = FontProperties(fname=fp)
        plt.rcParams['font.family'] = font_prop.get_name()
        break
plt.rcParams['axes.unicode_minus'] = False

assets = [
    ('上证指数',      '3,930.12',  -0.30),
    ('深证成指',      '13,516.97', -0.79),
    ('创业板指',      '3,286.55',  -0.78),
    ('恒生指数',      '25,650.87', +1.74),
    ('恒生科技',      '4,569.80',  +2.27),
    ('现货黄金',      '$4,474',    +0.20),
    ('WTI原油',       '$91.5',     +0.50),
    ('美元/离岸人民币', '6.716',   -0.12),
]

UP_COLOR   = '#E8392D'
DOWN_COLOR = '#1DB954'
BG_COLOR   = '#1a1a2e'
CARD_BG    = '#16213e'
TEXT_COLOR = '#E8E8E8'

fig, ax = plt.subplots(figsize=(12, 6))
fig.patch.set_facecolor(BG_COLOR)
ax.set_facecolor(BG_COLOR)
ax.set_xlim(0, 4)
ax.set_ylim(-0.5, len(assets) + 0.6)
ax.axis('off')

ax.text(2, len(assets) + 0.3, '📊 2026年9月4日  A股/港股/商品  收盘数据',
        ha='center', va='center', fontsize=13, color='#FFD700',
        fontweight='bold', fontproperties=font_prop)

headers = ['资产', '收盘价/点位', '涨跌幅', '趋势']
col_x = [0.1, 1.45, 2.65, 3.6]
for hx, hd in zip(col_x, headers):
    ax.text(hx, len(assets) - 0.1, hd, ha='left', va='center',
            fontsize=9.5, color='#AAAAAA', fontproperties=font_prop)
ax.axhline(y=len(assets) - 0.3, color='#444466', linewidth=0.8)

for i, (name, val, chg) in enumerate(assets):
    y = len(assets) - 1 - i
    color = UP_COLOR if chg >= 0 else DOWN_COLOR
    arrow = '▲' if chg >= 0 else '▼'
    rect = mpatches.FancyBboxPatch((0.05, y - 0.38), 3.9, 0.76,
                                    boxstyle="round,pad=0.03",
                                    linewidth=0.5, edgecolor='#333355',
                                    facecolor=CARD_BG)
    ax.add_patch(rect)
    ax.text(col_x[0], y, name, ha='left', va='center', fontsize=10,
            color=TEXT_COLOR, fontproperties=font_prop)
    ax.text(col_x[1], y, val, ha='left', va='center', fontsize=10,
            color=TEXT_COLOR, fontweight='bold', fontproperties=font_prop)
    ax.text(col_x[2], y, f'{chg:+.2f}%', ha='left', va='center',
            fontsize=11, color=color, fontweight='bold', fontproperties=font_prop)
    ax.text(col_x[3], y, arrow, ha='left', va='center', fontsize=14, color=color)

ax.text(3.95, -0.42, '数据源：东方财富 | 富途 | 市场综合',
        ha='right', va='center', fontsize=7, color='#666688', fontproperties=font_prop)

out_dir = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'images', 'charts')
os.makedirs(out_dir, exist_ok=True)
out_path = os.path.join(out_dir, 'chart_2026-09-04-evening.png')
plt.tight_layout(pad=0.3)
plt.savefig(out_path, dpi=150, bbox_inches='tight', facecolor=BG_COLOR)
plt.close()
print(f'✅ 图表已保存：{out_path}')
