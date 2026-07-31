#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
行情数据卡片生成脚本 - 2026-07-31 晚报 (国内市场)
"""

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
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

# ---- 数据 ----
assets = [
    # (名称, 现值, 涨跌幅, 上涨=True)
    ('上证指数\nSSEC',   '3,832.26', '+0.72%', True),
    ('深证成指\nSZCOMP', '13,578.93', '+2.21%', True),
    ('创业板指\nCHINEXT', '3,343.96', '+3.06%', True),
    ('科创50\nSTAR50',   '1,635.96', '+2.99%', True),
    ('恒生指数\nHSI',     '25,884.43', '+0.10%', True),
    ('恒生科技\nHSTECH',  '4,829.22', '+0.53%', True),
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
cols = 3
rows = (n + cols - 1) // cols

fig_w = cols * 4.5
fig_h = rows * 2.8 + 1.8

fig = plt.figure(figsize=(fig_w, fig_h), facecolor=BG_COLOR)

# 标题
title_kw = {'fontproperties': font_prop} if font_prop else {}
fig.text(0.5, 0.94, '  2026年07月31日  国内市场晚报行情',
         ha='center', va='top', fontsize=16, color=TITLE_COLOR,
         **title_kw)

fig.text(0.5, 0.88, '数据来源：今日（07-31）收盘终值  |  上涨(红)   下跌(绿)',
         ha='center', va='top', fontsize=10, color=TEXT_GRAY,
         **(({'fontproperties': font_prop}) if font_prop else {}))

for i, (name, price, change, is_up) in enumerate(assets):
    row = i // cols
    col = i % cols

    left   = 0.04 + col * (0.92 / cols)
    bottom = 0.76 - row * (0.70 / rows) - (0.70 / rows)
    width  = 0.92 / cols - 0.03
    height = 0.70 / rows - 0.05

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
    ax.text(0.5, 0.80, name, ha='center', va='top',
            fontsize=10, color=TEXT_GRAY,
            fontproperties=font_prop if font_prop else None,
            transform=ax.transAxes, linespacing=1.3)

    # 现值
    ax.text(0.5, 0.46, price, ha='center', va='center',
            fontsize=15, color=TEXT_WHITE, fontweight='bold',
            fontproperties=font_prop if font_prop else None,
            transform=ax.transAxes)

    # 涨跌幅
    chg_color = BORDER_UP if is_up else BORDER_DN
    symbol = '▲' if is_up else '▼'
    ax.text(0.5, 0.16, f'{symbol} {change}', ha='center', va='bottom',
            fontsize=12, color=chg_color, fontweight='bold',
            fontproperties=font_prop if font_prop else None,
            transform=ax.transAxes)

# 保存
out_dir = 'images/charts'
os.makedirs(out_dir, exist_ok=True)
out_path = os.path.join(out_dir, '2026-07-31-evening.png')
plt.savefig(out_path, dpi=150, bbox_inches='tight', facecolor=BG_COLOR)
print(f'✅ 行情卡片已保存至: {out_path}')
