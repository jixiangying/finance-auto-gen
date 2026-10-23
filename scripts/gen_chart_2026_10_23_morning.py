#!/usr/bin/env python3
"""
生成 2026-10-23 早报全球核心资产数据卡片（10月22日隔夜收盘 · 常规交易日 · 模式A）
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
plt.rcParams['font.sans-serif'] = ['PingFang SC', 'STHeiti', 'Arial Unicode MS']
plt.rcParams['axes.unicode_minus'] = False

# ── 核心资产数据（10月22日收盘） ────────────────────────────────
assets = [
    {"name": "道琼斯",       "val": "52,867.98", "day": "+0.02%", "sub": "+11.89点 尾盘转正",   "up": True},
    {"name": "标普500",      "val": "7,663.43",  "day": "-1.21%", "sub": "-93.74点 科技股拖累",  "up": False},
    {"name": "纳斯达克",     "val": "26,008.86", "day": "-2.60%", "sub": "6月以来最大单日跌幅",  "up": False},
    {"name": "美股芯片板块", "val": "≈-7.0%",    "day": "暴跌",   "sub": "CoreWeave约-10%",      "up": False},
    {"name": "恒生指数",     "val": "22,934.68", "day": "-3.03%", "sub": "-717.19点",            "up": False},
    {"name": "恒生科技",     "val": "3,793.93",  "day": "-5.03%", "sub": "失守4000点关口",       "up": False},
    {"name": "上证指数",     "val": "3,658.03",  "day": "-1.48%", "sub": "成交1.53万亿放量",     "up": False},
    {"name": "创业板指",     "val": "2,576.90",  "day": "-4.37%", "sub": "近5000只个股飘绿",     "up": False},
    {"name": "WTI原油(12月)", "val": "$99.41",   "day": "+1.91%", "sub": "美伊紧张+去库 逼近100", "up": True},
    {"name": "布伦特原油",   "val": "$113.24",   "day": "≈+4.0%", "sub": "中东供应风险溢价",     "up": True},
    {"name": "现货黄金",     "val": "$4,060.68", "day": "-1.93%", "sub": "油涨金跌 加息预期",    "up": False},
    {"name": "美债10年期",   "val": "≈4.96%",    "day": "-17bp",  "sub": "避险买盘涌入国债",     "up": None},
]

bar_labels = ["道指", "标普500", "纳指", "芯片股", "恒指", "恒生科技", "上证", "深成指", "创业板", "日经(盘中)"]
bar_values = [0.02, -1.21, -2.60, -7.0, -3.03, -5.03, -1.48, -2.96, -4.37, -1.78]

# ── 布局设计 ──────────────────────────────────────────────────
cols = 6
rows = (len(assets) + cols - 1) // cols
fig = plt.figure(figsize=(21, rows * 3.4 + 4.2))
fig.patch.set_facecolor('#0d1117')
gs = fig.add_gridspec(rows + 1, cols, height_ratios=[1] * rows + [1.25])

for i, a in enumerate(assets):
    ax = fig.add_subplot(gs[i // cols, i % cols])
    ax.set_facecolor('#0d1117')
    ax.axis('off')
    if a['up'] is None:
        color, bg, arrow = '#d4a017', '#1a1400', '■'
    elif a['up']:
        color, bg, arrow = '#ff4d4d', '#1a0000', '▲'
    else:
        color, bg, arrow = '#00cc66', '#001a0d', '▼'

    ax.add_patch(mpatches.FancyBboxPatch(
        (0.04, 0.04), 0.92, 0.92, boxstyle="round,pad=0.04", linewidth=1.5,
        edgecolor=color, facecolor=bg, transform=ax.transAxes, zorder=0))
    ax.text(0.5, 0.82, a['name'], transform=ax.transAxes, fontsize=13,
            color='#e6edf3', ha='center', va='center', fontproperties=prop_bold)
    ax.text(0.5, 0.58, a['val'], transform=ax.transAxes, fontsize=16,
            color='white', ha='center', va='center', fontproperties=prop_bold)
    ax.text(0.5, 0.35, f"变动: {arrow}{a['day']}", transform=ax.transAxes, fontsize=12,
            color=color, ha='center', va='center', fontproperties=prop)
    ax.text(0.5, 0.16, a['sub'], transform=ax.transAxes, fontsize=11,
            color='#8b949e', ha='center', va='center', fontproperties=prop)

# ── 底部：主要股指涨跌幅柱状图 ─────────────────────────────────
axb = fig.add_subplot(gs[rows, :])
axb.set_facecolor('#0d1117')
colors = ['#ff4d4d' if v > 0 else '#00cc66' for v in bar_values]
x = range(len(bar_labels))
bars = axb.bar(x, bar_values, color=colors, width=0.55)
axb.axhline(0, color='#8b949e', linewidth=0.8)
axb.set_xticks(list(x))
axb.set_xticklabels(bar_labels, fontproperties=prop, color='#e6edf3', fontsize=12)
yticks = [-7.0, -6.0, -5.0, -4.0, -3.0, -2.0, -1.0, 0, 0.5]
axb.set_yticks(yticks)
axb.set_yticklabels([f"{t:+.1f}%" for t in yticks], fontproperties=prop, color='#8b949e')
axb.set_ylim(-8.0, 1.2)
for spine in axb.spines.values():
    spine.set_visible(False)
for b, v in zip(bars, bar_values):
    axb.text(b.get_x() + b.get_width() / 2, v + (0.15 if v >= 0 else -0.15), f"{v:+.2f}%",
             ha='center', va='bottom' if v >= 0 else 'top', color='white',
             fontproperties=prop, fontsize=11)
axb.set_title('全球主要股指 10月22日 涨跌幅对比', fontproperties=prop_bold, color='white', fontsize=13)

plt.suptitle('2026-10-23 早报  ·  全球核心资产隔夜收盘（10月22日 · 常规交易日 · 模式A）',
             fontsize=15, color='white', y=1.01, fontproperties=prop_bold)
plt.tight_layout(pad=0.8)

out_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'images', 'charts')
os.makedirs(out_dir, exist_ok=True)
out_path = os.path.join(out_dir, 'chart_2026_10_23_morning.png')
plt.savefig(out_path, dpi=140, bbox_inches='tight', facecolor=fig.get_facecolor())
print(f"✅ 图表已保存：{out_path}")
