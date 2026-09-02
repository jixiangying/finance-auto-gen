#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
2026-09-02 晚间收盘·A股与港股核心市场数据卡片生成脚本
"""

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.font_manager import FontProperties
import os

# ── 字体配置 ──────────────────────────────────────────────────────────────
FONT_PATHS = [
    "/System/Library/Fonts/STHeiti Medium.ttc",
    "/System/Library/Fonts/Supplemental/Songti.ttc",
    "/System/Library/Fonts/PingFang.ttc",
]
prop = None
for fp in FONT_PATHS:
    if os.path.exists(fp):
        prop = FontProperties(fname=fp)
        plt.rcParams['font.family'] = prop.get_name()
        break

if prop is None:
    print("⚠️  未找到中文字体，使用系统默认字体")
    prop = FontProperties()

plt.rcParams['axes.unicode_minus'] = False

# ── 核心收盘资产数据 ──────────────────────────────────────────────────
assets = [
    {"name": "上证指数",     "value": "3,941.39",  "change": "-0.97%", "up": False},
    {"name": "深证成指",     "value": "13,611.55", "change": "-1.88%", "up": False},
    {"name": "创业板指",     "value": "3,312.24",  "change": "-2.39%", "up": False},
    {"name": "沪深300",      "value": "4,547.96",  "change": "-1.38%", "up": False},
    {"name": "科创50",       "value": "1,617.60",  "change": "-1.82%", "up": False},
    {"name": "恒生指数",     "value": "25,311.21", "change": "-0.07%", "up": False},
]

# ── 布局 ──────────────────────────────────────────────────────────────────
fig, ax = plt.subplots(figsize=(12, 5))
ax.set_facecolor("#1a1a2e")
fig.patch.set_facecolor("#1a1a2e")
ax.axis('off')

n = len(assets)
cols = 3
rows = (n + cols - 1) // cols
card_w, card_h = 3.5, 1.8
gap_x, gap_y = 0.4, 0.5
start_x, start_y = 0.3, 3.6

for i, asset in enumerate(assets):
    row, col = divmod(i, cols)
    x = start_x + col * (card_w + gap_x)
    y = start_y - row * (card_h + gap_y)

    color = "#e74c3c" if asset["up"] else "#2ecc71"       # 红涨绿跌 (A股习惯)
    bg    = "#2c1a1a" if asset["up"] else "#1a2c1a"

    rect = mpatches.FancyBboxPatch(
        (x, y), card_w, card_h,
        boxstyle="round,pad=0.1",
        linewidth=1.5, edgecolor=color,
        facecolor=bg,
        transform=ax.transData, clip_on=False
    )
    ax.add_patch(rect)

    # 资产名称
    ax.text(x + card_w/2, y + card_h - 0.35, asset["name"],
            ha='center', va='center', fontsize=13, color="#ecf0f1",
            fontproperties=prop, fontweight='bold')
    # 点位
    ax.text(x + card_w/2, y + card_h/2 - 0.05, asset["value"],
            ha='center', va='center', fontsize=14, color="#f0f0f0",
            fontproperties=prop)
    # 涨跌幅
    tag = "▲" if asset["up"] else "▼"
    ax.text(x + card_w/2, y + 0.32, f"{tag} {asset['change']}",
            ha='center', va='center', fontsize=13, color=color,
            fontproperties=prop, fontweight='bold')

# 标题
ax.text(6.1, 4.65, "2026-09-02 晚间收盘 · A股与港股主要指数盘点",
        ha='center', va='center', fontsize=15, color="#f39c12",
        fontproperties=prop, fontweight='bold')
# 副标题
ax.text(6.1, 4.3, "全市场缩量震荡整固  |  军工逆势领涨，半导体与农业承压回调",
        ha='center', va='center', fontsize=9.5, color="#95a5a6",
        fontproperties=prop)

ax.set_xlim(0, 12.2)
ax.set_ylim(0, 5)

output_path = "images/charts/chart_2026-09-02-evening.png"
os.makedirs(os.path.dirname(output_path), exist_ok=True)
plt.tight_layout()
plt.savefig(output_path, dpi=150, bbox_inches='tight',
            facecolor=fig.get_facecolor())
plt.close()
print(f"✅ 图表已保存至：{output_path}")
