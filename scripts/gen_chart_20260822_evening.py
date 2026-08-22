#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
周末复盘数据卡片：2026-08-22 (周六) 晚报
模式B：核心资产周度/单日表现
"""

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm
from matplotlib.patches import FancyBboxPatch
import numpy as np

# ── 中文字体 ────────────────────────────────────────────────────────────────
FONT_PATHS = [
    "/System/Library/Fonts/STHeiti Medium.ttc",
    "/System/Library/Fonts/Supplemental/PingFang.ttc",
    "/System/Library/Fonts/PingFang.ttc",
]
prop = None
for fp in FONT_PATHS:
    try:
        prop = fm.FontProperties(fname=fp)
        plt.rcParams["font.family"] = prop.get_name()
        break
    except Exception:
        continue
if prop is None:
    prop = fm.FontProperties()

# ── 数据 ─────────────────────────────────────────────────────────────────────
assets = [
    # (名称, 收盘点位/价格, 单日涨跌%, 周度涨跌%)
    ("上证指数",  "3,905.20",  "+0.04%",  "-0.56%"),
    ("深证成指",  "14,094.17", "+0.87%",  "-1.81%"),
    ("创业板指",  "3,545.58",  "+1.43%",  "-2.23%"),
    ("恒生指数",  "26,009.46", "+1.21%",  "+3.55%"),
    ("恒生科技",  "4,766.16",  "+0.73%",  "+1.24%"),
    ("标普500",   "7,674.37",  "+0.43%",  "-1.43%"),
    ("纳斯达克",  "26,180.45", "+0.43%",  "-2.05%"),
    ("现货黄金",  "$4,600+",   "周涨",    "+5.00%"),
    ("比特币",    "$77,000",   "周涨",    "+22.0%"),
    ("10Y美债",   "4.74%",     "收益率",  "↑本周"),
]

def get_color(pct_str: str):
    """红涨绿跌（中国惯例）"""
    s = pct_str.replace("%", "").replace(" ", "")
    if s.startswith("+") or (s.startswith("$") is False and "↑" in pct_str):
        return "#E8302A"  # 红
    if s.startswith("-") or "↓" in pct_str:
        return "#1CB050"  # 绿
    return "#888888"

# ── 画布 ─────────────────────────────────────────────────────────────────────
ncols, nrows = 5, 2
fig_w, fig_h = 18, 7.5
fig, axes = plt.subplots(nrows, ncols, figsize=(fig_w, fig_h),
                         facecolor="#0F1117")
fig.suptitle("2026年08月22日（周六）｜ 本周核心资产复盘", fontsize=17,
             color="white", fontproperties=prop, y=0.97)

for idx, ax in enumerate(axes.flat):
    ax.set_facecolor("#1A1D27")
    ax.set_xticks([])
    ax.set_yticks([])
    for spine in ax.spines.values():
        spine.set_visible(False)

    if idx >= len(assets):
        ax.set_visible(False)
        continue

    name, price, daily, weekly = assets[idx]
    week_color = get_color(weekly)
    day_color  = get_color(daily)

    # 资产名称
    ax.text(0.5, 0.82, name, transform=ax.transAxes,
            ha="center", va="center", fontsize=13, color="#C8CDD8",
            fontproperties=prop, fontweight="bold")
    # 收盘价/现价
    ax.text(0.5, 0.58, price, transform=ax.transAxes,
            ha="center", va="center", fontsize=15, color="white",
            fontproperties=prop, fontweight="bold")

    # 周度涨跌（大字）
    ax.text(0.5, 0.35, f"周度 {weekly}", transform=ax.transAxes,
            ha="center", va="center", fontsize=18, color=week_color,
            fontproperties=prop, fontweight="bold")

    # 单日涨跌（小字）
    ax.text(0.5, 0.12, f"周五单日 {daily}", transform=ax.transAxes,
            ha="center", va="center", fontsize=10, color=day_color,
            fontproperties=prop)

    # 圆角边框
    fancy = FancyBboxPatch((0.03, 0.05), 0.94, 0.90,
                           boxstyle="round,pad=0.02",
                           linewidth=1.5, edgecolor=week_color,
                           facecolor="none", transform=ax.transAxes,
                           clip_on=False)
    ax.add_patch(fancy)

plt.tight_layout(rect=[0, 0, 1, 0.94])
out = "/Users/jxy/Documents/Project/finance-auto-gen/images/charts/2026-08-22-evening.png"
plt.savefig(out, dpi=150, bbox_inches="tight", facecolor=fig.get_facecolor())
print(f"✅ 已保存：{out}")
