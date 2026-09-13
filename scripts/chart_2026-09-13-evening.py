#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
数据信息卡片生成脚本 - 2026-09-13 晚报（新周展望）
生成新一周核心资产全景对比与关键前瞻指标卡片
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
    "/System/Library/Fonts/PingFang.ttc",
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

# ── 核心资产数据 ──────────────────────────────────────────────
data = [
    # (资产名,       收盘/最新点位,     日变动,      全周累计,    涨跌True/False)
    ("上证指数",    "3,888.11",     "-1.18%",   "-1.07%",   False),
    ("创业板指",    "3,322.04",     "-0.49%",   "+1.08%",   True),
    ("恒生科技",    "4,320.57",     "-0.23%",   "-5.45%",   False),
    ("纳斯达克",    "26,333.04",    "+0.96%",   "-0.66%",   False),
    ("标普500",     "7,656.98",     "+0.86%",   "-0.80%",   False),
    ("10Y美债",     "4.890%",       "-5.3 bps", "+11.0 bps",True),
    ("Brent原油",   "$104.25",      "-3.14%",   "+14.18%",  True),
    ("现货黄金",    "$4,394.67",    "-1.08%",   "-0.68%",   False),
]

UP_COLOR   = "#E74C3C"   # 红色 (上涨/利率上行)
DOWN_COLOR = "#27AE60"   # 绿色 (下跌/回落)
BG_COLOR   = "#0D1117"   # 深色背景
CARD_COLOR = "#161B22"   # 卡片底色

fig_w, fig_h = 10, 6.5
fig, ax = plt.subplots(figsize=(fig_w, fig_h))
fig.patch.set_facecolor(BG_COLOR)
ax.set_facecolor(BG_COLOR)
ax.axis('off')

# 标题与副标题
ax.text(0.5, 0.96,
        "2026-09-13 新周展望 | 全球与国内核心资产周度收官对比",
        transform=ax.transAxes,
        ha='center', va='top',
        fontsize=14, color='white',
        fontproperties=prop,
        fontweight='bold')

ax.text(0.5, 0.90,
        "超级央行周决战前夕 · 核心资产收盘基准 (截至2026-09-11周五收盘)",
        transform=ax.transAxes,
        ha='center', va='top',
        fontsize=9.5, color='#8B949E',
        fontproperties=prop)

cols = 4
card_w = 0.215
card_h = 0.28
x_start = 0.03
y_start = 0.80
x_gap = 0.245
y_gap = 0.33

for i, (label, price, daily_pct, weekly_pct, is_up) in enumerate(data):
    col = i % cols
    row = i // cols
    x = x_start + col * x_gap
    y = y_start - row * y_gap

    color = UP_COLOR if is_up else DOWN_COLOR

    rect = mpatches.FancyBboxPatch(
        (x, y - card_h), card_w, card_h,
        boxstyle="round,pad=0.012",
        linewidth=1.5,
        edgecolor=color,
        facecolor=CARD_COLOR,
        transform=ax.transAxes,
        clip_on=False
    )
    ax.add_patch(rect)

    # 标签
    ax.text(x + card_w / 2, y - 0.025,
            label,
            transform=ax.transAxes,
            ha='center', va='top',
            fontsize=11, color='#C9D1D9',
            fontproperties=prop,
            fontweight='bold')

    # 点位
    ax.text(x + card_w / 2, y - 0.10,
            price,
            transform=ax.transAxes,
            ha='center', va='top',
            fontsize=12, color='white',
            fontproperties=prop,
            fontweight='bold')

    # 周五表现
    ax.text(x + card_w / 2, y - 0.17,
            f"周五: {daily_pct}",
            transform=ax.transAxes,
            ha='center', va='top',
            fontsize=9.5, color='#8B949E',
            fontproperties=prop)

    # 全周累计
    ax.text(x + card_w / 2, y - 0.235,
            f"全周: {weekly_pct}",
            transform=ax.transAxes,
            ha='center', va='top',
            fontsize=10.5, color=color,
            fontproperties=prop,
            fontweight='bold')

# 底部备注
ax.text(0.5, 0.04,
        "Source: SSE, SZSE, HKEX, NYSE, CME, ICE | Finance Auto Gen Pipeline",
        transform=ax.transAxes,
        ha='center', va='bottom',
        fontsize=8, color='#484F58',
        fontproperties=prop)

out_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'images', 'charts')
out_dir = os.path.normpath(out_dir)
os.makedirs(out_dir, exist_ok=True)
out_path = os.path.join(out_dir, '2026-09-13-evening.png')

plt.tight_layout(pad=0)
plt.savefig(out_path, dpi=150, bbox_inches='tight',
            facecolor=BG_COLOR, edgecolor='none')
plt.close()
print(f"Chart saved successfully: {out_path}")
