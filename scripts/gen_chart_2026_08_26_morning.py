#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib import font_manager
import os

font_paths = [
    '/System/Library/Fonts/STHeiti Medium.ttc',
    '/System/Library/Fonts/Supplemental/Arial Unicode MS.ttf',
]
prop = None
for fp in font_paths:
    if os.path.exists(fp):
        prop = font_manager.FontProperties(fname=fp)
        plt.rcParams['font.family'] = prop.get_name()
        break

if prop is None:
    plt.rcParams['font.sans-serif'] = ['PingFang SC', 'Heiti SC', 'Arial Unicode MS']
    plt.rcParams['axes.unicode_minus'] = False

assets = [
    ('标普500',   '7,677.28',  +0.32),
    ('纳斯达克',  '26,151.30', +0.66),
    ('道琼斯',    '53,577.40', +0.30),
    ('美10Y收益', '4.638%',    None),
    ('现货黄金',  '$4,640',    None),
    ('WTI原油',   '$81.53',   -1.80),
    ('BTC',       '$78,900',  +2.10),
]

RISE_COLOR = '#E84040'
FALL_COLOR = '#2BAA66'
FLAT_COLOR = '#888888'

fig, ax = plt.subplots(figsize=(12, 5.2))
fig.patch.set_facecolor('#0D1117')
ax.set_facecolor('#0D1117')
ax.axis('off')

kw_base = dict(transform=ax.transAxes, ha='center', clip_on=False,
               fontproperties=prop if prop else None)

ax.text(0.5, 0.97, '2026-08-26 早报  ·  全球核心行情一览',
        fontsize=15, fontweight='bold', color='#F0E6C8', va='top', **kw_base)
ax.text(0.5, 0.89, '数据来源：NYSE / Yahoo Finance / Tradeweb  ·  截至 8月25日收盘',
        fontsize=8.5, color='#888888', va='top', **kw_base)
ax.axhline(y=0.84, color="#333", linewidth=0.8)

cols = 4
card_w = 1.0 / cols
card_h = 0.36
start_y = 0.76
rows_data = [assets[:4], assets[4:]]

for row_idx, row_assets in enumerate(rows_data):
    n = len(row_assets)
    total_w = n * card_w
    start_x = (1.0 - total_w) / 2
    for col_idx, (name, price, pct) in enumerate(row_assets):
        cx = start_x + col_idx * card_w + card_w / 2
        cy = start_y - row_idx * (card_h + 0.02)
        if pct is None:
            color = FLAT_COLOR; pct_str = '—'
        elif pct >= 0:
            color = RISE_COLOR; pct_str = f'+{pct:.2f}%'
        else:
            color = FALL_COLOR; pct_str = f'{pct:.2f}%'
        rect = mpatches.FancyBboxPatch(
            (cx - card_w*0.44, cy - card_h*0.5),
            card_w*0.88, card_h*0.9,
            boxstyle='round,pad=0.01', linewidth=1.2,
            edgecolor=color, facecolor='#161B22',
            transform=ax.transAxes, clip_on=False)
        ax.add_patch(rect)
        ax.text(cx, cy+0.10, name, fontsize=11, color='#CCCCCC', fontweight='bold', va='center', **kw_base)
        ax.text(cx, cy-0.03, price, fontsize=13, color='#FFFFFF', fontweight='bold', va='center', **kw_base)
        ax.text(cx, cy-0.15, pct_str, fontsize=12, color=color, fontweight='bold', va='center', **kw_base)

ax.text(0.5, 0.03, '🔴 红色=上涨   🟢 绿色=下跌   — = 收益率/价格（无单日幅）',
        fontsize=8, color='#666666', va='bottom', **kw_base)

out_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'images', 'charts')
os.makedirs(out_dir, exist_ok=True)
out_path = os.path.join(out_dir, '2026-08-26-morning-chart.png')
plt.savefig(out_path, dpi=150, bbox_inches='tight', facecolor=fig.get_facecolor())
plt.close()
print(f'Chart saved → {out_path}')
