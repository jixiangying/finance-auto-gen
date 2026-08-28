#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
2026-08-28 晚报核心行情数据卡片生成脚本
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
    print("⚠️  未找到中文字体，使用系统默认字体，可能出现乱码")
    prop = FontProperties()

plt.rcParams['axes.unicode_minus'] = False

# ── 数据 ──────────────────────────────────────────────────────────────────
assets = [
    {"name": "上证指数",   "value": "3,952.18", "change": "-0.11%", "up": False},
    {"name": "深证成指",   "value": "13,953.07","change": "-0.68%", "up": False},
    {"name": "创业板指",   "value": "3,424.40", "change": "-1.41%", "up": False},
    {"name": "科创50",    "value": "1,662.15", "change": "-1.85%", "up": False},
    {"name": "恒生指数",   "value": "25,684.00","change": "+0.47%", "up": True},
    {"name": "恒生科技",   "value": "4,648.00", "change": "+0.60%", "up": True},
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

    color = "#c0392b" if asset["up"] else "#27ae60"       # 红涨绿跌
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
    indicator = "🔴" if asset["up"] else "🟢"
    ax.text(x + card_w/2, y + 0.32, f"{indicator} {asset['change']}",
            ha='center', va='center', fontsize=13, color=color,
            fontproperties=prop, fontweight='bold')

# 标题
ax.text(6.1, 4.65, "📈 2026-08-28 A股 & 港股收盘行情",
        ha='center', va='center', fontsize=15, color="#f39c12",
        fontproperties=prop, fontweight='bold')
# 副标题
ax.text(6.1, 4.3, "成交额：沪深京合计约 2.12 万亿元  |  全市场超3000只个股上涨",
        ha='center', va='center', fontsize=9.5, color="#95a5a6",
        fontproperties=prop)

ax.set_xlim(0, 12.2)
ax.set_ylim(0, 5)

output_path = "images/charts/2026-08-28-evening-chart.png"
os.makedirs(os.path.dirname(output_path), exist_ok=True)
plt.tight_layout()
plt.savefig(output_path, dpi=150, bbox_inches='tight',
            facecolor=fig.get_facecolor())
plt.close()
print(f"✅ 图表已保存至：{output_path}")
