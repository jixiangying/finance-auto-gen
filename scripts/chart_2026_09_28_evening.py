#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
2026-09-28 晚报 — 核心行情数据卡片
生成多资产行情信息图，保存至 images/charts/
"""

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib import font_manager
import numpy as np
import os

# ── 中文字体 ─────────────────────────────────────────────
font_paths = [
    '/System/Library/Fonts/STHeiti Medium.ttc',
    '/System/Library/Fonts/Supplemental/Songti.ttc',
    '/System/Library/Fonts/PingFang.ttc',
]
prop = None
for fp in font_paths:
    if os.path.exists(fp):
        prop = font_manager.FontProperties(fname=fp)
        plt.rcParams['font.family'] = prop.get_name()
        break
if prop is None:
    plt.rcParams['font.family'] = 'sans-serif'

# ── 数据 ──────────────────────────────────────────────────
assets = [
    # (名称, 现价/点位, 涨跌幅%, 单位)
    ('上证指数',  '3,823.62',  -1.67,  'pts'),
    ('深证成指',  '12,858.75', -3.44,  'pts'),
    ('创业板指',  '3,139.82',  -4.53,  'pts'),
    ('恒生指数',  '24,642.51', +0.54,  'pts'),
    ('恒生科技',  '4,296.00',  -0.37,  'pts'),
    ('布伦特原油', '~100.0',   +2.00,  'USD/桶'),
    ('现货黄金',  '~4,175',    -2.50,  'USD/盎司'),
    ('BTC',       '~83,500',   -1.20,  'USD'),
    ('人民币汇率', '6.7399',   +0.13,  'CNY/USD中间价'),
]

UP_COLOR   = '#E84040'   # 红色 = 上涨
DOWN_COLOR = '#27AE60'   # 绿色 = 下跌
BG_COLOR   = '#0D1117'
CARD_BG    = '#161B22'
TEXT_WHITE = '#E6EDF3'
TEXT_GRAY  = '#8B949E'

COLS = 3
ROWS = 3
fig, axes = plt.subplots(ROWS, COLS, figsize=(16, 10))
fig.patch.set_facecolor(BG_COLOR)

# 标题
fig.text(0.5, 0.97, '2026年9月28日（周一） 收盘行情速览',
         ha='center', va='top', fontsize=18, color=TEXT_WHITE,
         fontproperties=prop, fontweight='bold')
fig.text(0.5, 0.93, '国庆节前最后交易日 · 沪深全线回调 · 港股逆势小涨',
         ha='center', va='top', fontsize=11, color=TEXT_GRAY,
         fontproperties=prop)

for idx, ax in enumerate(axes.flat):
    ax.set_facecolor(CARD_BG)
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    ax.axis('off')

    if idx >= len(assets):
        continue

    name, price, chg, unit = assets[idx]
    color = UP_COLOR if chg >= 0 else DOWN_COLOR
    arrow = '▲' if chg >= 0 else '▼'
    chg_str = f'{arrow} {abs(chg):.2f}%'

    # 圆角背景（用 FancyBboxPatch）
    fancy = mpatches.FancyBboxPatch(
        (0.05, 0.08), 0.90, 0.84,
        boxstyle="round,pad=0.02",
        linewidth=2, edgecolor=color,
        facecolor=CARD_BG, zorder=1
    )
    ax.add_patch(fancy)

    # 资产名称
    ax.text(0.5, 0.82, name, ha='center', va='center',
            fontsize=13, color=TEXT_GRAY, fontproperties=prop, zorder=2)
    # 价格
    ax.text(0.5, 0.57, price, ha='center', va='center',
            fontsize=19, color=TEXT_WHITE, fontweight='bold', zorder=2)
    # 涨跌幅
    ax.text(0.5, 0.34, chg_str, ha='center', va='center',
            fontsize=16, color=color, fontweight='bold', zorder=2)
    # 单位
    ax.text(0.5, 0.15, unit, ha='center', va='center',
            fontsize=9, color=TEXT_GRAY, fontproperties=prop, zorder=2)

plt.subplots_adjust(left=0.03, right=0.97, top=0.90, bottom=0.04,
                    hspace=0.20, wspace=0.15)

# 输出路径
out_dir = os.path.join(os.path.dirname(__file__), '..', 'images', 'charts')
os.makedirs(out_dir, exist_ok=True)
out_path = os.path.join(out_dir, 'chart_2026_09_28_evening.png')
plt.savefig(out_path, dpi=150, bbox_inches='tight', facecolor=BG_COLOR)
plt.close()
print(f'✅ 图表已保存：{out_path}')
