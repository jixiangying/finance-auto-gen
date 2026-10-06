#!/usr/bin/env python3
"""
生成 2026-10-06 早报全球核心资产数据卡片（隔夜收盘与假期追踪）
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

# ── 核心资产数据（隔夜收盘与长假追踪） ────────────────────────
assets = [
    {"name": "道琼斯",    "val": "51,268.03", "day": "+0.18%", "sub": "收盘: +91.07点", "up": True},
    {"name": "标普500",   "val": "7,773.95",  "day": "+0.66%", "sub": "逼近历史峰值",   "up": True},
    {"name": "纳斯达克",  "val": "27,477.31", "day": "+1.05%", "sub": "创历史新纪录",   "up": True},
    {"name": "德国DAX",   "val": "25,254.00", "day": "+0.09%", "sub": "欧洲高位窄幅震荡", "up": True},
    {"name": "法国CAC40", "val": "7,834.10",  "day": "-0.80%", "sub": "财政扰动承压回踩", "up": False},
    {"name": "恒生指数",  "val": "24,040.34", "day": "+0.28%", "sub": "周一开市企稳回升", "up": True},
    {"name": "WTI原油",   "val": "$91.57",    "day": "+0.13%", "sub": "地缘溢价保持高企", "up": True},
    {"name": "现货黄金",  "val": "$4,143.87", "day": "-1.30%", "sub": "高位获利蓄势整理", "up": False},
    {"name": "美债10Y",   "val": "5.310%",    "day": "+3.0bp", "sub": "发债供给高峰推升", "up": True},
    {"name": "A50期指",   "val": "13,860.0",  "day": "+0.25%", "sub": "离岸净多头超97%", "up": True},
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

plt.suptitle('2026-10-06 早报  ·  全球核心资产隔夜收盘与假期追踪（常规交易日 · 模式A）',
             fontsize=15, color='white', y=1.02, fontproperties=prop_bold)
plt.tight_layout(pad=0.8)

out_dir = os.path.join(os.path.dirname(__file__), '..', 'images', 'charts')
os.makedirs(out_dir, exist_ok=True)
out_path = os.path.join(out_dir, 'chart_2026_10_06_morning.png')
plt.savefig(out_path, dpi=140, bbox_inches='tight', facecolor=fig.get_facecolor())
print(f"✅ 图表已保存：{out_path}")
