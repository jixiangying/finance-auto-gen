#!/usr/bin/env python3
"""
生成 2026-10-08 早报全球核心资产数据卡片（隔夜收盘与A股复市前瞻）
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

# ── 核心资产数据（隔夜收盘与A股复市前瞻） ────────────────────────
assets = [
    {"name": "道琼斯",    "val": "51,179.87", "day": "-0.66%", "sub": "收盘: -341.41点", "up": False},
    {"name": "标普500",   "val": "7,801.77",  "day": "-0.22%", "sub": "收盘: -17.16点",  "up": False},
    {"name": "纳斯达克",  "val": "27,538.69", "day": "-0.22%", "sub": "收盘: -61.20点",  "up": False},
    {"name": "德国DAX",   "val": "25,104.36", "day": "-1.36%", "sub": "欧债抛售拖累回落", "up": False},
    {"name": "法国CAC40", "val": "7,769.21",  "day": "-1.22%", "sub": "财政赤字担忧承压", "up": False},
    {"name": "恒生指数",  "val": "24,130.50", "day": "-0.62%", "sub": "恒科成份扩至50只", "up": False},
    {"name": "WTI原油",   "val": "$88.28",    "day": "-1.30%", "sub": "日跌$1.16通胀降温", "up": False},
    {"name": "现货黄金",  "val": "$4,163.71", "day": "+0.67%", "sub": "避险反弹涨$27.7", "up": True},
    {"name": "美债10Y",   "val": "5.277%",    "day": "+0.7bp", "sub": "纪要前夕长端韧性", "up": True},
    {"name": "A50期指",   "val": "13,985.0",  "day": "-0.28%", "sub": "蓄势节后开门红",   "up": False},
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

plt.suptitle('2026-10-08 早报  ·  全球核心资产隔夜收盘与A股复市前瞻（常规交易日 · 模式A）',
             fontsize=15, color='white', y=1.02, fontproperties=prop_bold)
plt.tight_layout(pad=0.8)

out_dir = os.path.join(os.path.dirname(__file__), '..', 'images', 'charts')
os.makedirs(out_dir, exist_ok=True)
out_path = os.path.join(out_dir, 'chart_2026_10_08_morning.png')
plt.savefig(out_path, dpi=140, bbox_inches='tight', facecolor=fig.get_facecolor())
print(f"✅ 图表已保存：{out_path}")
