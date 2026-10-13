#!/usr/bin/env python3
"""
生成 2026-10-13 早报全球核心资产数据卡片（10月12日隔夜收盘 · 常规交易日 · 模式A）
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

# ── 核心资产数据（10月12日收盘） ────────────────────────────────
assets = [
    {"name": "道琼斯",    "val": "51,850.55", "day": "+0.38%", "sub": "收盘: +195.60点",   "up": True},
    {"name": "标普500",   "val": "7,807.24",  "day": "-0.06%", "sub": "收盘: -4.30点",     "up": False},
    {"name": "纳斯达克",  "val": "27,245.90", "day": "-0.44%", "sub": "收盘: -120.27点",   "up": False},
    {"name": "德国DAX",   "val": "25,277.68", "day": "+0.76%", "sub": "欧股连续两日收涨",   "up": True},
    {"name": "英国富时100", "val": "10,656.28", "day": "+0.99%", "sub": "能源/银行股领涨",  "up": True},
    {"name": "恒生指数",  "val": "24,271.20", "day": "+0.25%", "sub": "恒科 -0.67% 分化",  "up": True},
    {"name": "上证指数",  "val": "3,797.24",  "day": "-0.43%", "sub": "创业板 -2.61%",     "up": False},
    {"name": "WTI原油",   "val": "$93.74",    "day": "+2.06%", "sub": "日涨$1.89 地缘溢价", "up": True},
    {"name": "布伦特原油", "val": "$106.65",  "day": "+1.84%", "sub": "近两周高位",         "up": True},
    {"name": "现货黄金",  "val": "$4,171",    "day": "-0.55%", "sub": "强美元压制金价",     "up": False},
    {"name": "美元指数",  "val": "102.58",    "day": "+0.34%", "sub": "18个月新高",         "up": True},
    {"name": "比特币",    "val": "$82,400",   "day": "约-1.8%", "sub": "CPI前风险偏好降温", "up": False},
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

plt.suptitle('2026-10-13 早报  ·  全球核心资产隔夜收盘（10月12日 · 常规交易日 · 模式A）',
             fontsize=15, color='white', y=1.02, fontproperties=prop_bold)
plt.tight_layout(pad=0.8)

out_dir = os.path.join(os.path.dirname(__file__), '..', 'images', 'charts')
os.makedirs(out_dir, exist_ok=True)
out_path = os.path.join(out_dir, 'chart_2026_10_13_morning.png')
plt.savefig(out_path, dpi=140, bbox_inches='tight', facecolor=fig.get_facecolor())
print(f"✅ 图表已保存：{out_path}")
