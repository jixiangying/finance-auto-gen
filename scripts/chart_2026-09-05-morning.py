#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
数据信息卡片生成脚本 - 2026-09-05 早报（国际市场）
复盘日期：2026-09-04（周五）美股收盘
"""

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.font_manager import FontProperties
import os

# ── 中文字体 (macOS) ──────────────────────────────────────────
FONT_PATHS = [
    "/System/Library/Fonts/STHeiti Medium.ttc",
    "/System/Library/Fonts/Supplemental/Songti.ttc",
    "/Library/Fonts/Arial Unicode MS.ttf",
]
prop = None
for fp in FONT_PATHS:
    if os.path.exists(fp):
        prop = FontProperties(fname=fp)
        break
if prop is None:
    prop = FontProperties()

plt.rcParams['axes.unicode_minus'] = False

# ── 市场数据 ──────────────────────────────────────────────────
data = [
    # (标签,         现值字符串,    涨跌%,     涨跌方向 True=涨)
    ("道琼斯",      "53,414.25",  "-0.51%",   False),
    ("标普500",     "7,718.60",   "-0.38%",   False),
    ("纳斯达克",    "26,506.99",  "-0.29%",   False),
    ("10Y美债",     "4.780%",     "+0.02 pct",True),
    ("黄金(oz)",    "$4,420",     "-1.51%",   False),
    ("WTI原油",     "$91.30",     "-0.37%",   False),
    ("比特币",      "$79,220",    "-2.20%",   False),
]

UP_COLOR   = "#E74C3C"
DOWN_COLOR = "#27AE60"
BG_COLOR   = "#0D1117"
CARD_COLOR = "#161B22"

n = len(data)
fig_w, fig_h = 10, 7
fig, ax = plt.subplots(figsize=(fig_w, fig_h))
ax.set_facecolor(BG_COLOR)
fig.patch.set_facecolor(BG_COLOR)
ax.axis('off')

ax.text(0.5, 0.97,
        "2026-09-05 早报  |  国际市场收盘行情",
        transform=ax.transAxes,
        ha='center', va='top',
        fontsize=14, color='white',
        fontproperties=prop,
        fontweight='bold')

ax.text(0.5, 0.91,
        "复盘日期：2026-09-04（周五）NYSE/NASDAQ 收盘",
        transform=ax.transAxes,
        ha='center', va='top',
        fontsize=9, color='#8B949E',
        fontproperties=prop)

cols = 4
card_w = 0.21
card_h = 0.25
x_start = 0.03
y_start = 0.82
x_gap = 0.24
y_gap = 0.30

for i, (label, price, pct, is_up) in enumerate(data):
    col = i % cols
    row = i // cols
    x = x_start + col * x_gap
    y = y_start - row * y_gap

    color = UP_COLOR if is_up else DOWN_COLOR

    rect = mpatches.FancyBboxPatch(
        (x, y - card_h), card_w, card_h,
        boxstyle="round,pad=0.01",
        linewidth=1.5,
        edgecolor=color,
        facecolor=CARD_COLOR,
        transform=ax.transAxes,
        clip_on=False
    )
    ax.add_patch(rect)

    ax.text(x + card_w / 2, y - 0.03,
            label,
            transform=ax.transAxes,
            ha='center', va='top',
            fontsize=10, color='#8B949E',
            fontproperties=prop)

    ax.text(x + card_w / 2, y - 0.11,
            price,
            transform=ax.transAxes,
            ha='center', va='top',
            fontsize=12, color='white',
            fontproperties=prop,
            fontweight='bold')

    ax.text(x + card_w / 2, y - 0.19,
            pct,
            transform=ax.transAxes,
            ha='center', va='top',
            fontsize=10, color=color,
            fontproperties=prop)

ax.text(0.5, 0.03,
        "Data: NYSE/NASDAQ Official Close | For reference only",
        transform=ax.transAxes,
        ha='center', va='bottom',
        fontsize=7, color='#484F58',
        fontproperties=prop)

out_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'images', 'charts')
out_dir = os.path.normpath(out_dir)
os.makedirs(out_dir, exist_ok=True)
out_path = os.path.join(out_dir, '2026-09-05-morning-chart.png')

plt.tight_layout(pad=0)
plt.savefig(out_path, dpi=150, bbox_inches='tight',
            facecolor=BG_COLOR, edgecolor='none')
plt.close()
print(f"Chart saved: {out_path}")
