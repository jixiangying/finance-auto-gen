#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
数据信息卡片生成脚本 - 2026-09-04 早报（国际市场）
复盘日期：2026-09-03（周四）美股收盘
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
    ("道琼斯",      "53,685.52",  "+1.18%",   True),
    ("标普500",     "7,747.71",   "+1.06%",   True),
    ("纳斯达克",    "26,584.06",  "+1.40%",   True),
    ("10Y美债",     "4.761%",     "-0.04 pct",False),
    ("黄金(oz)",    "$4,488",     "+3.86%",   True),
    ("WTI原油",     "$91.64",     "+2.10%",   True),
    ("比特币",      "$81,000",    "+5.19%",   True),
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
        "2026-09-04 早报  |  国际市场收盘行情",
        transform=ax.transAxes,
        ha='center', va='top',
        fontsize=14, color='white',
        fontproperties=prop,
        fontweight='bold')

ax.text(0.5, 0.91,
        "复盘日期：2026-09-03（周四）NYSE/NASDAQ 收盘",
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
    emoji = "+" if is_up else "-"

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
out_path = os.path.join(out_dir, '2026-09-04-morning-chart.png')

plt.tight_layout(pad=0)
plt.savefig(out_path, dpi=150, bbox_inches='tight',
            facecolor=BG_COLOR, edgecolor='none')
plt.close()
print(f"Chart saved: {out_path}")
