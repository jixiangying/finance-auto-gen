#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
数据卡片生成脚本 - 2026-08-23 新周展望（核心资产周末快照）
"""

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.font_manager import FontProperties
import os

# ── 中文字体 ──────────────────────────────────────────────
font_paths = [
    "/System/Library/Fonts/STHeiti Medium.ttc",
    "/System/Library/Fonts/PingFang.ttc",
    "/System/Library/Fonts/Supplemental/Arial Unicode MS.ttf",
]
prop = None
for fp in font_paths:
    if os.path.exists(fp):
        prop = FontProperties(fname=fp)
        break
if prop is None:
    prop = FontProperties()

plt.rcParams['axes.unicode_minus'] = False

# ── 数据定义 ──────────────────────────────────────────────
assets = [
    {"name": "黄金",       "value": "4,603",  "unit": "美元/盎司", "change": "+本周强劲",  "up": True},
    {"name": "WTI原油",    "value": "87.06",  "unit": "美元/桶",   "change": "+地缘支撑",  "up": True},
    {"name": "BTC",        "value": "77,081", "unit": "美元",      "change": "+周内>+20%", "up": True},
    {"name": "10Y美债",    "value": "4.74%",  "unit": "收益率",    "change": "↑高位震荡",  "up": False},
    {"name": "美元指数",   "value": "98.81",  "unit": "DXY",       "change": "↓近三月低",  "up": False},
    {"name": "布伦特油",   "value": "~94",    "unit": "美元/桶",   "change": "+突破94",    "up": True},
]

# ── 画布 ──────────────────────────────────────────────────
fig, axes = plt.subplots(2, 3, figsize=(13, 7))
fig.patch.set_facecolor("#0f1117")

for ax, asset in zip(axes.flatten(), assets):
    ax.set_facecolor("#1a1d2e")
    for spine in ax.spines.values():
        spine.set_visible(False)
    ax.set_xticks([])
    ax.set_yticks([])

    color = "#FF4C4C" if asset["up"] else "#26a65b"
    badge_color = "#3b0000" if asset["up"] else "#003b1a"

    # 资产名称
    ax.text(0.5, 0.78, asset["name"], transform=ax.transAxes,
            ha="center", va="center", fontsize=16, fontweight="bold",
            color="#ffffff", fontproperties=prop)
    # 价格
    ax.text(0.5, 0.52, asset["value"], transform=ax.transAxes,
            ha="center", va="center", fontsize=22, fontweight="bold",
            color=color)
    # 单位
    ax.text(0.5, 0.35, asset["unit"], transform=ax.transAxes,
            ha="center", va="center", fontsize=10, color="#aaaaaa",
            fontproperties=prop)
    # 涨跌徽章
    fancy = mpatches.FancyBboxPatch((0.18, 0.08), 0.64, 0.18,
                                    boxstyle="round,pad=0.02",
                                    transform=ax.transAxes,
                                    facecolor=badge_color,
                                    edgecolor=color, linewidth=1.2,
                                    clip_on=False)
    ax.add_patch(fancy)
    ax.text(0.5, 0.17, asset["change"], transform=ax.transAxes,
            ha="center", va="center", fontsize=10, color=color,
            fontproperties=prop)

# ── 标题 ──────────────────────────────────────────────────
fig.suptitle("核心资产 · 周末快照  |  2026-08-23",
             fontsize=15, color="#ccccdd", y=1.01,
             fontproperties=prop)

plt.tight_layout(pad=1.2)

output_dir = "images/charts"
os.makedirs(output_dir, exist_ok=True)
output_path = os.path.join(output_dir, "20260823_evening_assets.png")
plt.savefig(output_path, dpi=150, bbox_inches="tight",
            facecolor=fig.get_facecolor())
plt.close()
print(f"✅ 图表已保存至: {output_path}")
