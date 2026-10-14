#!/usr/bin/env python3
"""
生成 2026-10-14 早报全球核心资产数据卡片（10月13日隔夜收盘 · 常规交易日 · 模式A）
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

# ── 核心资产数据（10月13日收盘） ────────────────────────────────
assets = [
    {"name": "道琼斯",     "val": "51,670.10", "day": "-0.33%", "sub": "收盘: -180.45点",    "up": False},
    {"name": "标普500",    "val": "7,805.45",  "day": "-0.02%", "sub": "收盘: -1.79点",      "up": False},
    {"name": "纳斯达克",   "val": "27,204.38", "day": "-0.15%", "sub": "收盘: -41.52点",     "up": False},
    {"name": "韩国KOSPI",  "val": "6,035.35",  "day": "-5.46%", "sub": "SK海力士跌超10%",    "up": False},
    {"name": "日经225",    "val": "67,777.52", "day": "-1.82%", "sub": "东京电子跌超7%",     "up": False},
    {"name": "恒生指数",   "val": "24,345.22", "day": "+0.30%", "sub": "V型反转 三连涨",     "up": True},
    {"name": "上证指数",   "val": "3,800.86",  "day": "+0.10%", "sub": "收复3800点",         "up": True},
    {"name": "WTI原油",    "val": "$94.14",    "day": "+0.43%", "sub": "日涨$0.40",          "up": True},
    {"name": "布伦特原油", "val": "$105.69",   "day": "-0.90%", "sub": "俄柴油供给预期",     "up": False},
    {"name": "现货黄金",   "val": "$4,187",    "day": "+0.39%", "sub": "美元回落提振",       "up": True},
    {"name": "美债10年",   "val": "~5.20%",    "day": "小幅回落", "sub": "距24年高位不远",   "up": False},
    {"name": "比特币",     "val": "$83,500",   "day": "约+0.8%", "sub": "CPI前窄幅整理",     "up": True},
]

# ── 布局设计 ──────────────────────────────────────────────────
n = len(assets)
cols = 6
rows = (n + cols - 1) // cols

fig, axes = plt.subplots(rows, cols, figsize=(21, rows * 3.4))
fig.patch.set_facecolor('#0d1117')

for i, ax in enumerate(axes.flat):
    ax.set_facecolor('#0d1117')
    ax.axis('off')
    if i >= n:
        continue
    a = assets[i]
    color = '#ff4d4d' if a['up'] else '#00cc66'
    bg    = '#1a0000' if a['up'] else '#001a0d'

    fancy = mpatches.FancyBboxPatch(
        (0.04, 0.04), 0.92, 0.92,
        boxstyle="round,pad=0.04", linewidth=1.5,
        edgecolor=color, facecolor=bg, transform=ax.transAxes, zorder=0
    )
    ax.add_patch(fancy)

    ax.text(0.5, 0.82, a['name'], transform=ax.transAxes,
            fontsize=13, color='#e6edf3', ha='center', va='center',
            fontproperties=prop_bold)
    ax.text(0.5, 0.58, a['val'], transform=ax.transAxes,
            fontsize=16, color='white', ha='center', va='center',
            fontproperties=prop_bold)
    day_arrow = '▲' if a['up'] else '▼'
    ax.text(0.5, 0.35, f"变动: {day_arrow}{a['day']}", transform=ax.transAxes,
            fontsize=12, color=color, ha='center', va='center',
            fontproperties=prop)
    ax.text(0.5, 0.16, f"{a['sub']}", transform=ax.transAxes,
            fontsize=11, color='#8b949e', ha='center', va='center',
            fontproperties=prop)

plt.suptitle('2026-10-14 早报  ·  全球核心资产隔夜收盘（10月13日 · 常规交易日 · 模式A）',
             fontsize=15, color='white', y=1.02, fontproperties=prop_bold)
plt.tight_layout(pad=0.8)

out_dir = os.path.join(os.path.dirname(__file__), '..', 'images', 'charts')
os.makedirs(out_dir, exist_ok=True)
out_path = os.path.join(out_dir, 'chart_2026_10_14_morning.png')
plt.savefig(out_path, dpi=140, bbox_inches='tight', facecolor=fig.get_facecolor())
print(f"✅ 图表已保存：{out_path}")
