#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
2026-09-26 早报 国际市场行情数据卡片
数据来源：9月25日（周五）收盘终值
"""

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.font_manager import FontProperties
import numpy as np
import os

# ── 中文字体 ──────────────────────────────────────────────
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
    prop = FontProperties()

plt.rcParams['font.family'] = 'sans-serif'
plt.rcParams['axes.unicode_minus'] = False

# ── 市场数据 ──────────────────────────────────────────────
data = [
    # (资产名称,  现价/点位,  涨跌幅%)
    ("标普500\nS&P 500",     "7,743.41",  +0.51),
    ("纳斯达克\nNASDAQ",     "27,068.72", +0.48),
    ("道琼斯\nDJIA",         "51,828.62", +0.93),
    ("德国DAX\nDAX",         "28,964",    +0.75),
    ("英国FTSE\nFTSE 100",   "14,149",    +0.24),
    ("布伦特原油\nBrent Oil","$104.49",   -0.50),
    ("黄金\nGold",           "$4,283.66", +0.32),
    ("比特币\nBitcoin",      "$84,378",   -0.09),
    ("美元指数\nDXY",        "101.16",    -0.10),
    ("10Y美债\nUST 10Y",     "5.17%",     +0.01),
]

n = len(data)
ncols = 5
nrows = 2

fig, axes = plt.subplots(nrows, ncols,
                         figsize=(ncols * 3.4, nrows * 2.8),
                         facecolor='#0d1117')
fig.patch.set_facecolor('#0d1117')

for idx, ax in enumerate(axes.flat):
    ax.set_facecolor('#161b22')
    ax.set_xticks([])
    ax.set_yticks([])
    for spine in ax.spines.values():
        spine.set_edgecolor('#30363d')

    if idx >= n:
        ax.set_visible(False)
        continue

    name, price, chg = data[idx]
    color = '#f85149' if chg >= 0 else '#3fb950'   # 红涨绿跌
    arrow = '▲' if chg >= 0 else '▼'
    chg_str = f"{arrow} {abs(chg):.2f}%"

    # 资产名称
    ax.text(0.5, 0.78, name,
            transform=ax.transAxes,
            ha='center', va='center',
            fontproperties=prop,
            fontsize=10.5, color='#8b949e',
            linespacing=1.4)

    # 现价
    ax.text(0.5, 0.46, price,
            transform=ax.transAxes,
            ha='center', va='center',
            fontproperties=prop,
            fontsize=14, fontweight='bold', color='#e6edf3')

    # 涨跌幅
    ax.text(0.5, 0.18, chg_str,
            transform=ax.transAxes,
            ha='center', va='center',
            fontproperties=prop,
            fontsize=12, fontweight='bold', color=color)

# 标题
fig.suptitle('2026年09月26日  国际市场早报  |  9月25日（周五）收盘',
             fontproperties=prop,
             fontsize=13, color='#c9d1d9',
             y=1.02)

plt.tight_layout(rect=[0, 0, 1, 1], pad=0.6)

out_path = os.path.join(os.path.dirname(__file__),
                        '../images/charts/chart_20260926_morning.png')
out_path = os.path.normpath(out_path)
plt.savefig(out_path, dpi=150, bbox_inches='tight',
            facecolor='#0d1117')
plt.close()
print(f"✅ 行情卡片已保存：{out_path}")
