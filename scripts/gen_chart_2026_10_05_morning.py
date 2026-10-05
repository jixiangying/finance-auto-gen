#!/usr/bin/env python3
"""
生成 2026-10-05 早报新周展望与全球核心资产数据卡片
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

# ── 核心资产数据（包含最新报价与走势表现） ────────────────────
assets = [
    {"name": "道琼斯",    "val": "51,176.96", "day": "+0.49%", "sub": "周线: +0.82%", "up": True},
    {"name": "标普500",   "val": "7,722.72",  "day": "+0.73%", "sub": "周线: +1.15%", "up": True},
    {"name": "纳斯达克",  "val": "27,190.86", "day": "+1.19%", "sub": "周线: +1.88%", "up": True},
    {"name": "德国DAX",   "val": "25,231.20", "day": "+1.17%", "sub": "周线: +0.95%", "up": True},
    {"name": "恒生指数",  "val": "23,972.29", "day": "-2.60%", "sub": "今日周一开市", "up": False},
    {"name": "WTI原油",   "val": "$91.45",    "day": "-1.53%", "sub": "G7压制溢价",   "up": False},
    {"name": "现货黄金",  "val": "$4,198.50", "day": "+0.56%", "sub": "降息预期提振", "up": True},
    {"name": "美债10Y",   "val": "5.205%",    "day": "-1.2bp", "sub": "利率拐头下行", "up": False},
    {"name": "A50期指",   "val": "13,825.0",  "day": "+0.21%", "sub": "站稳1.38万关口", "up": True},
    {"name": "比特币BTC", "val": "$87,850",   "day": "+2.60%", "sub": "周末延续反弹", "up": True},
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
    # 涨跌表现
    day_arrow = '▲' if a['day'].startswith('+') else ('▼' if a['day'].startswith('-') else '')
    ax.text(0.5, 0.35, f"变动: {day_arrow}{a['day']}", transform=ax.transAxes,
            fontsize=12, color=color, ha='center', va='center',
            fontproperties=prop)
    ax.text(0.5, 0.16, f"{a['sub']}", transform=ax.transAxes,
            fontsize=11, color='#8b949e', ha='center', va='center',
            fontproperties=prop)

plt.suptitle('2026-10-05 早报  ·  全球核心资产周初展望与收盘总览（新周展望特辑）',
             fontsize=15, color='white', y=1.02, fontproperties=prop_bold)
plt.tight_layout(pad=0.8)

out_dir = os.path.join(os.path.dirname(__file__), '..', 'images', 'charts')
os.makedirs(out_dir, exist_ok=True)
out_path = os.path.join(out_dir, 'chart_2026_10_05_morning.png')
plt.savefig(out_path, dpi=140, bbox_inches='tight', facecolor=fig.get_facecolor())
print(f"✅ 图表已保存：{out_path}")
