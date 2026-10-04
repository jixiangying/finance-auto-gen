#!/usr/bin/env python3
"""
生成 2026-10-04 早报周末复盘行情数据卡片
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
prop_bold = FontProperties(fname=FONT_PATH, weight='bold')
plt.rcParams['axes.unicode_minus'] = False

# ── 核心资产数据（包含周五单日与全周表现） ────────────────────
assets = [
    {"name": "道琼斯",    "val": "51,176.96", "day": "+0.49%", "week": "+0.82%", "up": True},
    {"name": "标普500",   "val": "7,722.72",  "day": "+0.73%", "week": "+1.15%", "up": True},
    {"name": "纳斯达克",  "val": "27,190.86", "day": "+1.19%", "week": "+1.88%", "up": True},
    {"name": "德国DAX",   "val": "25,231.20", "day": "+1.17%", "week": "+0.95%", "up": True},
    {"name": "恒生指数",  "val": "23,972.29", "day": "-2.60%", "week": "-3.15%", "up": False},
    {"name": "WTI原油",   "val": "$91.26",    "day": "-1.73%", "week": "-2.85%", "up": False},
    {"name": "现货黄金",  "val": "$4,192.30", "day": "+0.42%", "week": "+1.05%", "up": True},
    {"name": "美债10Y",   "val": "5.217%",    "day": "-5.0bp", "week": "较周高松动", "up": False},
    {"name": "A50期指",   "val": "13,796.0",  "day": "-0.72%", "week": "区间防守", "up": False},
    {"name": "比特币BTC", "val": "$87,420",   "day": "+2.10%", "week": "+3.80%", "up": True},
]

# ── 布局设计 ──────────────────────────────────────────────────
n = len(assets)
cols = 5
rows = (n + cols - 1) // cols

fig, axes = plt.subplots(rows, cols, figsize=(18, rows * 3.4))
fig.patch.set_facecolor('#0d1117')

for i, ax in enumerate(axes.flat):
    ax.set_facecolor('#0d1117')
    ax.axis('off')
    if i >= n:
        continue
    a = assets[i]
    color = '#ff4d4d' if a['up'] else '#00cc66'
    bg    = '#1a0000' if a['up'] else '#001a0d'

    # 卡片背景框
    fancy = mpatches.FancyBboxPatch(
        (0.04, 0.04), 0.92, 0.92,
        boxstyle="round,pad=0.04", linewidth=1.5,
        edgecolor=color, facecolor=bg, transform=ax.transAxes, zorder=0
    )
    ax.add_patch(fancy)

    # 资产名称
    ax.text(0.5, 0.82, a['name'], transform=ax.transAxes,
            fontsize=13, color='#e6edf3', ha='center', va='center',
            fontproperties=prop_bold)
    # 点位/现价
    ax.text(0.5, 0.58, a['val'], transform=ax.transAxes,
            fontsize=16, color='white', ha='center', va='center',
            fontproperties=prop_bold)
    # 单日与周度涨跌
    day_arrow = '▲' if a['day'].startswith('+') else ('▼' if a['day'].startswith('-') else '')
    ax.text(0.5, 0.35, f"周五: {day_arrow}{a['day']}", transform=ax.transAxes,
            fontsize=12, color=color, ha='center', va='center',
            fontproperties=prop)
    ax.text(0.5, 0.16, f"全周: {a['week']}", transform=ax.transAxes,
            fontsize=11, color='#8b949e', ha='center', va='center',
            fontproperties=prop)

plt.suptitle('2026-10-04 早报  ·  全球核心资产周末总复盘（周五收盘与全周累计）',
             fontsize=15, color='white', y=1.02, fontproperties=prop_bold)
plt.tight_layout(pad=0.8)

out_dir = os.path.join(os.path.dirname(__file__), '..', 'images', 'charts')
os.makedirs(out_dir, exist_ok=True)
out_path = os.path.join(out_dir, 'chart_2026_10_04_morning.png')
plt.savefig(out_path, dpi=140, bbox_inches='tight', facecolor=fig.get_facecolor())
print(f"✅ 图表已保存：{out_path}")
