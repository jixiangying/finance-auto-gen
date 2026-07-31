#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
行情数据卡片生成脚本 - 2026-07-31 早报 (国际市场)
"""

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.font_manager import FontProperties
import os

# ---- 字体配置（macOS 中文支持）----
font_paths = [
    '/System/Library/Fonts/STHeiti Medium.ttc',
    '/System/Library/Fonts/PingFang.ttc',
    '/Library/Fonts/Arial Unicode MS.ttf',
]
font_prop = None
for fp in font_paths:
    if os.path.exists(fp):
        font_prop = FontProperties(fname=fp)
        break

def cn(text):
    """返回中文字体字典，兼容 matplotlib text"""
    if font_prop:
        return {'fontproperties': font_prop}
    return {}

# ---- 数据 ----
assets = [
    # (名称, 现值, 涨跌幅, 上涨=True)
    ('标普500\nS&P 500',   '7,437.63', '+1.70%', True),
    ('道琼斯\nDow Jones',  '52,208.06', '+1.20%', True),
    ('纳斯达克\nNasdaq',   '24,122.18', '+2.80%', True),
    ('美国10Y国债\nUS 10Y', '4.66%',   '+0.02%', True),
    ('黄金 Gold\n($/oz)',  '$4,103',   '+0.30%', True),
    ('WTI原油\nCrude',     '$83.82',   '-0.85%', False),
    ('BTC比特币',          '$64,200',  '+0.95%', True),
    ('VIX恐慌指数',        '19.56',    '-4.50%', False),
]

# ---- 配色 ----
BG_COLOR    = '#0d1117'
CARD_COLOR  = '#161b22'
BORDER_UP   = '#f85149'   # 红色=上涨
BORDER_DN   = '#3fb950'   # 绿色=下跌
TEXT_WHITE  = '#e6edf3'
TEXT_GRAY   = '#8b949e'
TITLE_COLOR = '#f0c040'

n = len(assets)
cols = 4
rows = (n + cols - 1) // cols

fig_w = cols * 3.8
fig_h = rows * 2.6 + 1.8

fig = plt.figure(figsize=(fig_w, fig_h), facecolor=BG_COLOR)

# 标题
title_kw = {'fontproperties': font_prop} if font_prop else {}
fig.text(0.5, 0.96, '  2026年07月31日  国际市场早报行情',
         ha='center', va='top', fontsize=15, color=TITLE_COLOR,
         **title_kw)

fig.text(0.5, 0.91, '数据来源：昨日（07-30）收盘终值  |  上涨(红)   下跌(绿)',
         ha='center', va='top', fontsize=9, color=TEXT_GRAY,
         **(({'fontproperties': font_prop}) if font_prop else {}))

for i, (name, price, change, is_up) in enumerate(assets):
    row = i // cols
    col = i % cols

    left   = 0.025 + col * (0.95 / cols)
    bottom = 0.80 - row * (0.75 / rows) - (0.75 / rows)
    width  = 0.95 / cols - 0.02
    height = 0.75 / rows - 0.04

    ax = fig.add_axes([left, bottom, width, height])
    ax.set_facecolor(CARD_COLOR)
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    ax.axis('off')

    # 边框颜色
    border_color = BORDER_UP if is_up else BORDER_DN
    for spine in ax.spines.values():
        spine.set_visible(True)
        spine.set_color(border_color)
        spine.set_linewidth(2)
    ax.set_xticks([])
    ax.set_yticks([])

    # 资产名称
    ax.text(0.5, 0.82, name, ha='center', va='top',
            fontsize=9, color=TEXT_GRAY,
            fontproperties=font_prop if font_prop else None,
            transform=ax.transAxes, linespacing=1.3)

    # 现值
    ax.text(0.5, 0.48, price, ha='center', va='center',
            fontsize=13, color=TEXT_WHITE, fontweight='bold',
            fontproperties=font_prop if font_prop else None,
            transform=ax.transAxes)

    # 涨跌幅
    chg_color = BORDER_UP if is_up else BORDER_DN
    symbol = '▲' if is_up else '▼'
    ax.text(0.5, 0.14, f'{symbol} {change}', ha='center', va='bottom',
            fontsize=10, color=chg_color, fontweight='bold',
            fontproperties=font_prop if font_prop else None,
            transform=ax.transAxes)

# 保存
out_dir = '/Users/jxy/Documents/Project/finance-auto-gen/images/charts'
os.makedirs(out_dir, exist_ok=True)
out_path = os.path.join(out_dir, '2026-07-31-morning-chart.png')
plt.savefig(out_path, dpi=150, bbox_inches='tight', facecolor=BG_COLOR)
print(f'✅ 行情卡片已保存至: {out_path}')
