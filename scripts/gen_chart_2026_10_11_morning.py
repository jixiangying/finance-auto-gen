#!/usr/bin/env python3
"""
生成 2026-10-11 早报（周末复盘 · 模式B）全球核心资产数据卡片：周五单日 + 全周累计
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

# ── 核心资产数据（10月9日收盘；week 为相对10月2日收盘的周度累计） ──
# up: 决定颜色（红涨绿跌）；以周度方向为主
assets = [
    {"name": "道琼斯",    "val": "51,654.95", "day": "+0.83%", "week": "+0.93%", "up": True},
    {"name": "标普500",   "val": "7,811.54",  "day": "+0.59%", "week": "+1.15%", "up": True},
    {"name": "纳斯达克",  "val": "27,366.17", "day": "+0.64%", "week": "+0.64%", "up": True},
    {"name": "STOXX 600", "val": "631.55",    "day": "+1.03%", "week": "+0.2%",  "up": True},
    {"name": "恒生指数",  "val": "24,211.35", "day": "+1.79%", "week": "—",      "up": True},
    {"name": "日经225",   "val": "69,030.92", "day": "-0.02%", "week": "—",      "up": False},
    {"name": "WTI原油",   "val": "$91.85",    "day": "+0.39%", "week": "+0.81%", "up": True},
    {"name": "现货黄金",  "val": "$4,193.87", "day": "+1.47%", "week": "≈持平",  "up": True},
    {"name": "美债10Y",   "val": "5.24%",     "day": "—",      "week": "-3.3bp", "up": False},
    {"name": "美元指数",  "val": "102.23",    "day": "—",      "week": "+0.48%", "up": True},
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
    ax.text(0.5, 0.34, f"周五单日  {a['day']}", ha='center', va='center',
            color='#c9d1d9', fontsize=13, fontproperties=prop, transform=ax.transAxes)
    ax.text(0.5, 0.16, f"全周累计  {a['week']}", ha='center', va='center',
            color=color, fontsize=16, fontweight='bold', fontproperties=prop,
            transform=ax.transAxes)

fig.suptitle("2026-10-11 周末复盘 · 全球核心资产（截至10月9日收盘）",
             color='white', fontsize=22, fontproperties=prop, y=0.99)
fig.text(0.5, 0.01, "红色=上涨  绿色=下跌（周度方向） | 数据来源：AP、Investing.com、Reuters/EnergyNow、TradingEconomics",
         ha='center', color='#8b949e', fontsize=11, fontproperties=prop)

plt.tight_layout(rect=[0, 0.03, 1, 0.95])
root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
out = os.path.join(root, "images", "charts", "chart_2026_10_11_morning.png")
os.makedirs(os.path.dirname(out), exist_ok=True)
plt.savefig(out, dpi=150, facecolor=fig.get_facecolor())
print(f"Saved: {out}")
