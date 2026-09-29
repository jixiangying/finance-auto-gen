#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
2026-09-29 晚报行情数据卡片生成脚本
"""
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.font_manager import FontProperties
import numpy as np

# ── 字体设置 (macOS 中文支持) ──────────────────────────────────────────────
import os
FONT_PATHS = [
    "/System/Library/Fonts/STHeiti Medium.ttc",
    "/System/Library/Fonts/PingFang.ttc",
    "/System/Library/Fonts/Supplemental/Arial Unicode MS.ttf",
]
font_path = next((p for p in FONT_PATHS if os.path.exists(p)), None)
prop = FontProperties(fname=font_path) if font_path else FontProperties()
prop_bold = FontProperties(fname=font_path, weight='bold') if font_path else FontProperties(weight='bold')

# ── 行情数据 ──────────────────────────────────────────────────────────────
assets = [
    # (名称,               数值字符串,         涨跌幅,   涨跌方向)
    ("上证指数",           "3,830.45",         "+0.18%", "up"),
    ("深证成指",           "12,901.95",        "+0.34%", "up"),
    ("创业板指",           "3,142.56",         "+0.09%", "up"),
    ("恒生指数",           "24,444.15",        "-0.48%", "down"),
    ("恒生科技",           "4,249.62",         "-1.08%", "down"),
    ("在岸人民币",         "6.7037",           "+91pts", "up"),
]

UP_COLOR   = "#D93025"   # 红 = 上涨
DOWN_COLOR = "#1E8C43"   # 绿 = 下跌
BG_COLOR   = "#0D1117"
CARD_BG    = "#161B22"
BORDER_UP  = "#FF4D4F"
BORDER_DN  = "#52C41A"
TEXT_LIGHT = "#F0F6FC"
TEXT_GRAY  = "#8B949E"
ACCENT     = "#58A6FF"

n = len(assets)
fig_w, fig_h = 10, 7.2
fig, ax = plt.subplots(figsize=(fig_w, fig_h))
ax.set_facecolor(BG_COLOR)
fig.patch.set_facecolor(BG_COLOR)
ax.axis('off')

# ── 顶部标题条 ────────────────────────────────────────────────────────────
title_rect = mpatches.FancyBboxPatch((0.01, 0.88), 0.98, 0.10,
    boxstyle="round,pad=0.01", linewidth=0,
    facecolor="#1F2937", transform=ax.transAxes, clip_on=False)
ax.add_patch(title_rect)
ax.text(0.5, 0.935, "📊  2026年9月29日  |  国内市场收盘晚报  |  行情速览",
        ha='center', va='center', fontsize=13, color=TEXT_LIGHT,
        fontproperties=prop_bold, transform=ax.transAxes)

# 副标题
ax.text(0.5, 0.858, "▌ 成交额 1.42万亿元  ·  较前日缩量2,951亿元  ·  3,400+个股上涨",
        ha='center', va='center', fontsize=9.5, color=TEXT_GRAY,
        fontproperties=prop, transform=ax.transAxes)

# ── 卡片布局：3列 × 2行 ───────────────────────────────────────────────────
cols, rows = 3, 2
card_w, card_h = 0.30, 0.32
x_starts = [0.02, 0.35, 0.68]
y_starts = [0.50, 0.14]

for idx, (name, val, chg, direction) in enumerate(assets):
    col = idx % cols
    row = idx // cols
    x0 = x_starts[col]
    y0 = y_starts[row]
    bcolor = BORDER_UP if direction == "up" else BORDER_DN
    fcolor = "#1A0505" if direction == "up" else "#051A0C"

    # 卡片背景
    card = mpatches.FancyBboxPatch((x0, y0), card_w, card_h,
        boxstyle="round,pad=0.015", linewidth=1.5,
        edgecolor=bcolor, facecolor=fcolor,
        transform=ax.transAxes, clip_on=False)
    ax.add_patch(card)

    # 左侧彩条
    bar = mpatches.FancyBboxPatch((x0 + 0.005, y0 + 0.03), 0.008, card_h - 0.06,
        boxstyle="round,pad=0.003", linewidth=0,
        facecolor=bcolor, alpha=0.85,
        transform=ax.transAxes, clip_on=False)
    ax.add_patch(bar)

    cx = x0 + card_w / 2
    # 资产名称
    ax.text(cx, y0 + card_h - 0.055, name,
            ha='center', va='center', fontsize=11.5, color=TEXT_LIGHT,
            fontproperties=prop_bold, transform=ax.transAxes)
    # 数值
    ax.text(cx, y0 + card_h / 2 - 0.01, val,
            ha='center', va='center', fontsize=14, color=TEXT_LIGHT,
            fontproperties=prop_bold, transform=ax.transAxes)
    # 涨跌幅
    chg_color = UP_COLOR if direction == "up" else DOWN_COLOR
    emoji = "🔴" if direction == "up" else "🟢"
    ax.text(cx, y0 + 0.055, f"{emoji}  {chg}",
            ha='center', va='center', fontsize=11, color=chg_color,
            fontproperties=prop, transform=ax.transAxes)

# ── 底部注释 ──────────────────────────────────────────────────────────────
ax.text(0.5, 0.04,
        "数据来源：东方财富 / 富途证券 / 港交所  |  收盘终值  |  仅供参考，不构成投资建议",
        ha='center', va='center', fontsize=7.5, color=TEXT_GRAY,
        fontproperties=prop, transform=ax.transAxes)

out_path = "images/charts/chart_2026_09_29_evening.png"
plt.tight_layout(pad=0)
plt.savefig(out_path, dpi=150, bbox_inches='tight',
            facecolor=BG_COLOR, edgecolor='none')
plt.close()
print(f"✅ 数据卡片已保存: {out_path}")
