#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
2026-09-25 Morning Chart Generator
国际市场核心资产行情数据卡片（早报）
"""

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.patches import FancyBboxPatch
import numpy as np
import os

# ── 字体配置 ──────────────────────────────────────────────
import matplotlib.font_manager as fm
font_paths = [
    '/System/Library/Fonts/STHeiti Medium.ttc',
    '/System/Library/Fonts/PingFang.ttc',
    '/System/Library/Fonts/Supplemental/Arial Unicode MS.ttf',
]
chinese_font = None
for fp in font_paths:
    if os.path.exists(fp):
        chinese_font = fm.FontProperties(fname=fp)
        break

def get_font(size=12, bold=False):
    if chinese_font:
        prop = fm.FontProperties(fname=chinese_font.get_file(), size=size)
        if bold:
            prop.set_weight('bold')
        return prop
    return fm.FontProperties(size=size, weight='bold' if bold else 'normal')

# ── 数据定义 ───────────────────────────────────────────────
date_str = "2026-09-25  |  国际市场早报"
subtitle = "（截至 2026-09-24 美股收盘）"

assets = [
    # name, value, change_pct, unit
    ("S&P 500",          "7,704.13",   -0.02,  ""),
    ("纳斯达克综合",      "26,939.37",  +0.01,  ""),
    ("道琼斯工业",        "51,349.98",  -0.31,  ""),
    ("罗素2000",          "2,835.57",   -0.11,  ""),
    ("DAX（德国）",       "25,267.00",  -0.57,  ""),
    ("FTSE 100（英国）",  "10,679.99",  -0.20,  ""),
    ("CAC 40（法国）",    "8,123.41",   -0.39,  ""),
    ("10Y美债收益率",      "5.16%",     +0.05,  ""),
    ("美元指数 DXY",      "101.26",     +0.30,  ""),
    ("VIX 恐慌指数",      "15.74",      +3.70,  ""),
    ("现货黄金",          "$4,270",     -0.55,  "/盎司"),
    ("WTI 原油",          "$95.00",     +2.10,  "/桶"),
    ("布伦特原油",        "$104.70",    +1.80,  "/桶"),
    ("比特币 BTC",        "$84,815",    +0.43,  ""),
    ("以太坊 ETH",        "$2,695",     +0.40,  ""),
]

# ── 颜色方案 ───────────────────────────────────────────────
BG_COLOR     = "#0d1117"
CARD_BG      = "#161b22"
TITLE_COLOR  = "#e6edf3"
SUBTITLE_CLR = "#8b949e"
UP_COLOR     = "#f85149"   # 红涨
DOWN_COLOR   = "#3fb950"   # 绿跌
FLAT_COLOR   = "#8b949e"
BORDER_COLOR = "#30363d"

def get_change_color(pct):
    if pct > 0:
        return UP_COLOR
    elif pct < 0:
        return DOWN_COLOR
    return FLAT_COLOR

def format_change(pct):
    sign = "+" if pct >= 0 else ""
    return f"{sign}{pct:.2f}%"

# ── 绘图 ──────────────────────────────────────────────────
ncols = 3
nrows = 5
fig_w, fig_h = 18, 14
fig = plt.figure(figsize=(fig_w, fig_h), facecolor=BG_COLOR)

# 标题区
title_ax = fig.add_axes([0, 0.90, 1, 0.10])
title_ax.set_facecolor(BG_COLOR)
title_ax.axis('off')
title_ax.text(0.5, 0.70, "🌐  国际市场核心行情卡片", ha='center', va='center',
              fontproperties=get_font(28, bold=True), color=TITLE_COLOR)
title_ax.text(0.5, 0.20, f"{date_str}  {subtitle}", ha='center', va='center',
              fontproperties=get_font(14), color=SUBTITLE_CLR)

# 数据卡片网格
left_margin   = 0.02
right_margin  = 0.02
top_margin    = 0.89
bottom_margin = 0.03
h_gap = 0.012
v_gap = 0.015

total_w = 1 - left_margin - right_margin - h_gap * (ncols - 1)
total_h = top_margin - bottom_margin - v_gap * (nrows - 1)
card_w = total_w / ncols
card_h = total_h / nrows

for i, (name, value, chg, unit) in enumerate(assets):
    row = i // ncols
    col = i % ncols
    x = left_margin + col * (card_w + h_gap)
    y = top_margin - (row + 1) * card_h - row * v_gap

    ax = fig.add_axes([x, y, card_w, card_h])
    ax.set_facecolor(CARD_BG)
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    ax.axis('off')

    # 卡片边框
    for spine in ax.spines.values():
        spine.set_visible(False)
    rect = FancyBboxPatch((0.01, 0.01), 0.98, 0.98,
                           boxstyle="round,pad=0.01",
                           linewidth=1.2, edgecolor=BORDER_COLOR,
                           facecolor=CARD_BG, transform=ax.transAxes, zorder=0)
    ax.add_patch(rect)

    color = get_change_color(chg)
    chg_str = format_change(chg)

    # 品种名称
    ax.text(0.08, 0.72, name, ha='left', va='center',
            fontproperties=get_font(13, bold=True), color=SUBTITLE_CLR,
            transform=ax.transAxes)
    # 数值
    ax.text(0.08, 0.38, f"{value}{unit}", ha='left', va='center',
            fontproperties=get_font(20, bold=True), color=TITLE_COLOR,
            transform=ax.transAxes)
    # 涨跌幅
    ax.text(0.92, 0.38, chg_str, ha='right', va='center',
            fontproperties=get_font(16, bold=True), color=color,
            transform=ax.transAxes)
    # 底部色条
    bar_h = 0.06
    ax.add_patch(FancyBboxPatch((0.05, 0.08), 0.90, bar_h,
                                boxstyle="round,pad=0.005",
                                linewidth=0, facecolor=color, alpha=0.35,
                                transform=ax.transAxes, zorder=1))

# 水印
watermark_ax = fig.add_axes([0, 0, 1, 0.03])
watermark_ax.set_facecolor(BG_COLOR)
watermark_ax.axis('off')
watermark_ax.text(0.5, 0.5, "Finance Auto-Gen  |  数据来源：Barchart / TradingEconomics / Morningstar  |  仅供参考，不构成投资建议",
                  ha='center', va='center', fontproperties=get_font(10), color=SUBTITLE_CLR)

# ── 保存 ──────────────────────────────────────────────────
out_dir = "/Users/jxy/Documents/Project/finance-auto-gen/images/charts"
os.makedirs(out_dir, exist_ok=True)
out_path = os.path.join(out_dir, "chart_20260925_morning.png")
plt.savefig(out_path, dpi=150, bbox_inches='tight', facecolor=BG_COLOR)
print(f"✅ 图表已保存至：{out_path}")
plt.close()
