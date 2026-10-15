#!/usr/bin/env python3
"""
生成 2026-10-15 早报全球核心资产数据卡片（10月14日隔夜收盘 · 常规交易日 · 模式A）
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

# ── 核心资产数据（10月14日收盘） ────────────────────────────────
assets = [
    {"name": "道琼斯",       "val": "51,621.48", "day": "-0.09%", "sub": "收盘: -48.62点",    "up": False},
    {"name": "标普500",      "val": "7,718.94",  "day": "-1.11%", "sub": "收盘: -86.51点",    "up": False},
    {"name": "纳斯达克",     "val": "26,692.87", "day": "-1.88%", "sub": "收盘: -511.51点",   "up": False},
    {"name": "欧洲STOXX600", "val": "637.85",    "day": "+0.40%", "sub": "ASML财报强劲带动", "up": True},
    {"name": "日经225",      "val": "67,744.29", "day": "-0.05%", "sub": "收盘: -33.23点",    "up": False},
    {"name": "韩国KOSPI",    "val": "6,008.81",  "day": "-0.40%", "sub": "暴跌后窄幅企稳",   "up": False},
    {"name": "恒生指数",     "val": "24,314.17", "day": "-0.13%", "sub": "收盘: -31.05点",    "up": False},
    {"name": "上证指数",     "val": "3,767.23",  "day": "-0.88%", "sub": "内需担忧小幅调整", "up": False},
    {"name": "WTI原油",      "val": "$94.50",    "day": "+0.38%", "sub": "中东地缘溢价支撑", "up": True},
    {"name": "现货黄金",     "val": "$4,145",    "day": "-1.00%", "sub": "强通胀提振美指承压", "up": False},
    {"name": "美元指数",     "val": "102.85",    "day": "+0.54%", "sub": "创15个月新高",     "up": True},
    {"name": "比特币",       "val": "$82,200",   "day": "-1.56%", "sub": "流动性预期压制",   "up": False},
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

plt.suptitle('2026-10-15 早报  ·  全球核心资产隔夜收盘（10月14日 · 常规交易日 · 模式A）',
             fontsize=15, color='white', y=1.02, fontproperties=prop_bold)
plt.tight_layout(pad=0.8)

out_dir = os.path.join(os.path.dirname(__file__), '..', 'images', 'charts')
os.makedirs(out_dir, exist_ok=True)
out_path = os.path.join(out_dir, 'chart_2026_10_15_morning.png')
plt.savefig(out_path, dpi=140, bbox_inches='tight', facecolor=fig.get_facecolor())
print(f"✅ 图表已保存：{out_path}")
