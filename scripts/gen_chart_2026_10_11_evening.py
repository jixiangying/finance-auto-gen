#!/usr/bin/env python3
"""
生成 2026-10-11 晚报（新周展望 · 模式C）国内核心资产数据卡片：最近交易日(10/9) + 节后首周累计
"""
import os
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.font_manager import FontProperties

# ── 中文字体设置 (macOS) ───────────────────────────────────────
FONT_PATH = "/System/Library/Fonts/STHeiti Medium.ttc"
prop = FontProperties(fname=FONT_PATH)
plt.rcParams['axes.unicode_minus'] = False

# ── 核心资产数据（10月9日收盘；week 为相对9月30日节前收盘的累计） ──
assets = [
    {"name": "上证指数",   "val": "3,813.79",  "day": "+0.05%",   "week": "-0.74%",  "up": False},
    {"name": "深证成指",   "val": "12,641.86", "day": "+0.17%",   "week": "—",       "up": True},
    {"name": "创业板指",   "val": "3,043.33",  "day": "+0.22%",   "week": "—",       "up": True},
    {"name": "恒生指数",   "val": "24,211.35", "day": "+1.79%",   "week": "—",       "up": True},
    {"name": "恒生科技",   "val": "4,197.84",  "day": "+3.06%",   "week": "—",       "up": True},
    {"name": "沪深北成交额", "val": "1.92万亿", "day": "+2224亿",  "week": "—",       "up": True},
    {"name": "南向资金",   "val": "+2.90亿港元", "day": "净买入",  "week": "—",       "up": True},
    {"name": "现货黄金",   "val": "$4,193.87", "day": "+1.47%",   "week": "≈持平",   "up": True},
    {"name": "WTI原油",    "val": "$91.85",    "day": "+0.39%",   "week": "+0.81%",  "up": True},
    {"name": "比特币",     "val": "≈$82,780",  "day": "—",        "week": "自8.7万回落", "up": False},
]

n = len(assets)
cols = 5
rows = (n + cols - 1) // cols

fig, axes = plt.subplots(rows, cols, figsize=(18, rows * 3.6))
fig.patch.set_facecolor('#0d1117')

for i, ax in enumerate(axes.flat):
    ax.set_facecolor('#0d1117')
    ax.axis('off')
    if i >= n:
        continue
    a = assets[i]
    color = '#ff4d4d' if a['up'] else '#00cc66'
    bg = '#1a0000' if a['up'] else '#001a0d'

    card = mpatches.FancyBboxPatch(
        (0.04, 0.04), 0.92, 0.92,
        boxstyle="round,pad=0.02,rounding_size=0.06",
        transform=ax.transAxes, facecolor=bg, edgecolor=color, linewidth=2)
    ax.add_patch(card)

    ax.text(0.5, 0.82, a['name'], ha='center', va='center', color='#e6edf3',
            fontsize=17, fontproperties=prop, transform=ax.transAxes)
    ax.text(0.5, 0.58, a['val'], ha='center', va='center', color='white',
            fontsize=24, fontweight='bold', fontproperties=prop, transform=ax.transAxes)
    ax.text(0.5, 0.34, f"10/9 单日  {a['day']}", ha='center', va='center',
            color='#c9d1d9', fontsize=13, fontproperties=prop, transform=ax.transAxes)
    ax.text(0.5, 0.16, f"节后首周  {a['week']}", ha='center', va='center',
            color=color, fontsize=16, fontweight='bold', fontproperties=prop,
            transform=ax.transAxes)

fig.suptitle("2026-10-11 新周展望 · 国内核心资产（截至10月9日收盘）",
             color='white', fontsize=22, fontproperties=prop, y=0.99)
fig.text(0.5, 0.01, "红色=上涨  绿色=下跌（上证按周度方向） | 数据来源：交易所公开数据、东方财富、财联社、Investing.com",
         ha='center', color='#8b949e', fontsize=11, fontproperties=prop)

plt.tight_layout(rect=[0, 0.03, 1, 0.95])
root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
out = os.path.join(root, "images", "charts", "chart_2026_10_11_evening.png")
os.makedirs(os.path.dirname(out), exist_ok=True)
plt.savefig(out, dpi=150, facecolor=fig.get_facecolor())
print(f"Saved: {out}")
