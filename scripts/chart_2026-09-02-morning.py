#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
2026-09-02 早报 核心行情数据卡片
数据来源：NYSE/NASDAQ/CME 昨日（2026-09-01）收盘数据
"""

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.font_manager import FontProperties
import os

# ── 中文字体设置 ────────────────────────────────────────────────
font_paths = [
    '/System/Library/Fonts/STHeiti Medium.ttc',
    '/System/Library/Fonts/Supplemental/Arial Unicode MS.ttf',
    '/System/Library/Fonts/PingFang.ttc',
]
prop = None
for fp in font_paths:
    if os.path.exists(fp):
        prop = FontProperties(fname=fp)
        break
if prop is None:
    prop = FontProperties()

plt.rcParams['axes.unicode_minus'] = False

# ── 行情数据（2026-09-01 收盘） ────────────────────────────────
assets = [
    # (资产名称, 数值显示, 涨跌幅%, 是否上涨)
    ('道琼斯\nDJIA',       '52,766',    -0.79, False),
    ('标普500\nS&P 500',   '7,631',     -0.70, False),
    ('纳斯达克\nNasdaq',   '26,100',    -1.03, False),
    ('德国DAX',            '25,960',    -1.22, False),
    ('英国富时\nFTSE 100', '10,790',    -0.32, False),
    ('美债10Y\n收益率',    '4.778%',    +0.06, True),  # 以收益率涨幅为正
    ('布伦特原油\n($/bbl)', '$91.5',    +3.20, True),
    ('黄金现货\n($/oz)',   '$4,375',    -2.70, False),
    ('比特币\nBTC ($)',    '$78,553',   -1.10, False),
    ('美元指数\nDXY',      '99.57',     +0.30, True),
]

# ── 配色 ──────────────────────────────────────────────────────
UP_BG    = '#1a3a1a'   # 深绿背景（上涨）
DOWN_BG  = '#3a1a1a'   # 深红背景（下跌）
UP_TXT   = '#00e676'   # 亮绿文字
DOWN_TXT = '#ff5252'   # 亮红文字
SUBTITLE = '#aaaaaa'

# ── 画布 ──────────────────────────────────────────────────────
COLS = 5
ROWS = 2
fig, axes = plt.subplots(ROWS, COLS, figsize=(18, 7))
fig.patch.set_facecolor('#0d0d0d')
axes_flat = axes.flatten()

for i, (name, val, pct, up) in enumerate(assets):
    ax = axes_flat[i]
    ax.set_facecolor(UP_BG if up else DOWN_BG)
    for spine in ax.spines.values():
        spine.set_edgecolor('#333333')

    # 资产名称
    ax.text(0.5, 0.75, name, transform=ax.transAxes,
            ha='center', va='center', fontproperties=prop,
            fontsize=11, color='#dddddd', fontweight='bold', linespacing=1.4)

    # 数值
    ax.text(0.5, 0.45, val, transform=ax.transAxes,
            ha='center', va='center', fontproperties=prop,
            fontsize=15, color='white', fontweight='bold')

    # 涨跌幅
    arrow = '▲' if up else '▼'
    color = UP_TXT if up else DOWN_TXT
    pct_txt = f'{arrow} {abs(pct):.2f}%'
    ax.text(0.5, 0.20, pct_txt, transform=ax.transAxes,
            ha='center', va='center', fontproperties=prop,
            fontsize=13, color=color, fontweight='bold')

    ax.set_xticks([])
    ax.set_yticks([])

# 标题
fig.text(0.5, 0.97,
         '2026-09-02 早报｜国际市场昨日收盘行情（2026-09-01）',
         ha='center', va='top', fontproperties=prop,
         fontsize=14, color='white', fontweight='bold')
fig.text(0.5, 0.02,
         '数据来源：NYSE / NASDAQ / Investing.com  ｜  🔴 上涨  🟢 下跌',
         ha='center', va='bottom', fontproperties=prop,
         fontsize=9, color=SUBTITLE)

plt.tight_layout(rect=[0, 0.04, 1, 0.95])

# ── 输出 ──────────────────────────────────────────────────────
out_dir = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))),
                       'images', 'charts')
os.makedirs(out_dir, exist_ok=True)
out_path = os.path.join(out_dir, '2026-09-02-morning-chart.png')
plt.savefig(out_path, dpi=150, bbox_inches='tight', facecolor=fig.get_facecolor())
plt.close()
print(f'[OK] 行情卡片已保存至：{out_path}')
