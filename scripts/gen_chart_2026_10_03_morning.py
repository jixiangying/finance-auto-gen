#!/usr/bin/env python3
"""
生成 2026-10-03 早报行情数据卡片
"""
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.font_manager import FontProperties
import numpy as np
import os

# ── 中文字体 ──────────────────────────────────────────────────
FONT_PATH = "/System/Library/Fonts/STHeiti Medium.ttc"
prop = FontProperties(fname=FONT_PATH)
prop_bold = FontProperties(fname=FONT_PATH, weight='bold')
plt.rcParams['axes.unicode_minus'] = False

# ── 数据 ────────────────────────────────────────────────────
assets = [
    {"name": "道琼斯",      "val": "51,176.96", "chg": "+0.49%", "up": True},
    {"name": "标普500",     "val": "7,722.72",  "chg": "+0.73%", "up": True},
    {"name": "纳斯达克",    "val": "27,190.86", "chg": "+1.19%", "up": True},
    {"name": "德国DAX",     "val": "25,231.20", "chg": "+1.17%", "up": True},
    {"name": "WTI原油",     "val": "$91.26",    "chg": "-1.73%", "up": False},
    {"name": "黄金",        "val": "$4,192",    "chg": "+0.42%", "up": True},
    {"name": "美债10Y",     "val": "5.217%",    "chg": "-5.0bp", "up": False},
    {"name": "BTC",         "val": "$85,357",   "chg": "-1.31%", "up": False},
    {"name": "A50期货",     "val": "13,796",    "chg": "-0.72%", "up": False},
    {"name": "离岸人民币",  "val": "6.7043",    "chg": "偏弱",   "up": False},
]

# ── 布局 ─────────────────────────────────────────────────────
n = len(assets)
cols = 5
rows = (n + cols - 1) // cols

fig, axes = plt.subplots(rows, cols, figsize=(18, rows * 3.2))
fig.patch.set_facecolor('#0d1117')

for i, ax in enumerate(axes.flat):
    ax.set_facecolor('#0d1117')
    ax.axis('off')
    if i >= n:
        continue
    a = assets[i]
    color = '#ff4d4d' if a['up'] else '#00cc66'
    bg    = '#1a0000' if a['up'] else '#001a0d'

    # 卡片背景
    fancy = mpatches.FancyBboxPatch((0.05, 0.05), 0.90, 0.90,
        boxstyle="round,pad=0.04", linewidth=1.5,
        edgecolor=color, facecolor=bg, transform=ax.transAxes, zorder=0)
    ax.add_patch(fancy)

    # 资产名称
    ax.text(0.5, 0.78, a['name'], transform=ax.transAxes,
            fontsize=13, color='#cccccc', ha='center', va='center',
            fontproperties=prop)
    # 价格
    ax.text(0.5, 0.52, a['val'], transform=ax.transAxes,
            fontsize=16, color='white', ha='center', va='center',
            fontproperties=prop_bold)
    # 涨跌幅
    arrow = '▲' if a['up'] else '▼'
    ax.text(0.5, 0.26, f"{arrow} {a['chg']}", transform=ax.transAxes,
            fontsize=14, color=color, ha='center', va='center',
            fontproperties=prop_bold)

plt.suptitle('2026-10-03 早报  ·  全球核心资产行情（美股周五收盘）',
             fontsize=15, color='white', y=1.01, fontproperties=prop_bold)
plt.tight_layout(pad=0.6)

out_dir = os.path.join(os.path.dirname(__file__), '..', 'images', 'charts')
os.makedirs(out_dir, exist_ok=True)
out_path = os.path.join(out_dir, 'chart_2026_10_03_morning.png')
plt.savefig(out_path, dpi=140, bbox_inches='tight',
            facecolor=fig.get_facecolor())
print(f"✅ 图表已保存：{out_path}")
