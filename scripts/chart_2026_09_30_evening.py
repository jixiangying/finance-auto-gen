#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
2026-09-30 晚报行情数据卡片生成脚本
国庆前最后交易日 — A股+港股
"""

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.font_manager import FontProperties
import os

# ── 字体设置（macOS 中文支持）──────────────────────────────
FONT_PATHS = [
    '/System/Library/Fonts/STHeiti Medium.ttc',
    '/System/Library/Fonts/Supplemental/Songti.ttc',
    '/System/Library/Fonts/PingFang.ttc',
]
font_prop = None
for fp in FONT_PATHS:
    if os.path.exists(fp):
        font_prop = FontProperties(fname=fp)
        plt.rcParams['font.family'] = font_prop.get_name()
        break

if font_prop is None:
    plt.rcParams['font.sans-serif'] = ['Arial Unicode MS', 'DejaVu Sans']

plt.rcParams['axes.unicode_minus'] = False

# ── 数据 ────────────────────────────────────────────────────
assets = [
    {"name": "上证指数",    "value": "3,842.19", "change": "+0.31%", "up": True},
    {"name": "深证成指",    "value": "12,887.62","change": "-0.11%", "up": False},
    {"name": "创业板指",    "value": "3,135.28", "change": "-0.23%", "up": False},
    {"name": "科创50",      "value": "—",         "change": "-2.51%", "up": False},
    {"name": "恒生指数",    "value": "24,613.27", "change": "+0.37%", "up": True},
    {"name": "国企指数",    "value": "8,220.08",  "change": "+0.50%", "up": True},
    {"name": "恒生科技",    "value": "4,253.89",  "change": "+0.10%", "up": True},
    {"name": "CNY/USD",    "value": "6.7065",    "change": "中间价 6.7351", "up": True},
]

COLS = 4
ROWS = 2
FIG_W = 14
FIG_H = 5.2

fig, axes = plt.subplots(ROWS, COLS, figsize=(FIG_W, FIG_H))
fig.patch.set_facecolor('#0D1117')

kw = dict(fontproperties=font_prop) if font_prop else {}

for idx, ax in enumerate(axes.flat):
    if idx >= len(assets):
        ax.set_visible(False)
        continue

    d = assets[idx]
    color = '#FF4C4C' if d['up'] else '#00C27A'
    bg    = '#1A1F2B'

    ax.set_facecolor(bg)
    for spine in ax.spines.values():
        spine.set_edgecolor('#2E3448')
        spine.set_linewidth(0.8)
    ax.set_xticks([])
    ax.set_yticks([])

    # 资产名称
    ax.text(0.5, 0.80, d['name'], transform=ax.transAxes,
            fontsize=12, color='#AABBD3', ha='center', va='center',
            **kw)
    # 点位/价格
    ax.text(0.5, 0.50, d['value'], transform=ax.transAxes,
            fontsize=16, color='#E8EDF5', ha='center', va='center',
            fontweight='bold', **kw)
    # 涨跌幅
    ax.text(0.5, 0.20, d['change'], transform=ax.transAxes,
            fontsize=13, color=color, ha='center', va='center',
            fontweight='bold', **kw)

    # 色块左侧竖线
    rect = mpatches.FancyBboxPatch((0.0, 0.0), 0.035, 1.0,
                                   boxstyle='square,pad=0',
                                   transform=ax.transAxes,
                                   facecolor=color, alpha=0.85,
                                   clip_on=False)
    ax.add_patch(rect)

# 标题 + 来源
fig.suptitle('2026年09月30日（国庆前最后交易日）· 收盘行情',
             fontsize=14, color='#C8D8E8', y=1.02, **kw)
fig.text(0.99, -0.03,
         '数据来源：东方财富 / 富途 / 中国外汇交易中心',
         ha='right', fontsize=8, color='#5A6A80', **kw)

plt.tight_layout(pad=1.2)

out_dir = '/Users/jxy/Documents/Project/finance-auto-gen/images/charts'
os.makedirs(out_dir, exist_ok=True)
out_path = os.path.join(out_dir, 'chart_2026_09_30_evening.png')
plt.savefig(out_path, dpi=150, bbox_inches='tight', facecolor=fig.get_facecolor())
plt.close()
print(f'✅ 图表已保存：{out_path}')
