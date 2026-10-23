#!/usr/bin/env python3
"""
生成 2026-10-21 早报全球核心资产数据卡片（10月20日隔夜收盘 · 常规交易日 · 模式A）
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

# ── 核心资产数据（10月20日收盘） ────────────────────────────────
assets = [
    {"name": "道琼斯",       "val": "52,495.88", "day": "+1.02%", "sub": "+529.85点 3M大涨领涨", "up": True},
    {"name": "标普500",      "val": "7,712.57",  "day": "+0.28%", "sub": "+21.84点",            "up": True},
    {"name": "纳斯达克",     "val": "26,424.82", "day": "-0.02%", "sub": "-6.07点 科技巨头分化",  "up": False},
    {"name": "费城半导体",   "val": "11,283.80", "day": "-0.29%", "sub": "泛林-3.21% ARM-3.07%", "up": False},
    {"name": "欧洲STOXX600", "val": "638.64",    "day": "-0.14%", "sub": "法国政局扰动",          "up": False},
    {"name": "恒生指数",     "val": "23,867.74", "day": "-1.32%", "sub": "节后复牌失守24000",     "up": False},
    {"name": "上证指数",     "val": "3,735.37",  "day": "+0.12%", "sub": "两市成交1.47万亿",      "up": True},
    {"name": "WTI原油(11月)", "val": "$101.79",  "day": "-1.80%", "sub": "美伊折中方案传闻",      "up": False},
    {"name": "布伦特原油",   "val": "$108.79",   "day": "-0.69%", "sub": "盘中曾近$112",          "up": False},
    {"name": "现货黄金",     "val": "$4,124.48", "day": "-0.39%", "sub": "美元偏强压制",          "up": False},
    {"name": "美债10年期",   "val": "≈5.12%",    "day": "持平",    "sub": "日内5.08%-5.15%",       "up": None},
    {"name": "比特币",       "val": "≈$82,790",  "day": "+0.78%", "sub": "$82.7K-$83K区间",       "up": True},
]

bar_labels = ["道指", "标普500", "纳指", "费半", "STOXX600", "恒指", "恒生科技", "上证", "深成指", "创业板"]
bar_values = [1.02, 0.28, -0.02, -0.29, -0.14, -1.32, -1.52, 0.12, -0.14, -0.26]

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
yticks = [-1.5, -1.0, -0.5, 0, 0.5, 1.0]
axb.set_yticks(yticks)
axb.set_yticklabels([f"{t:+.1f}%" for t in yticks], fontproperties=prop, color='#8b949e')
axb.set_ylim(-1.9, 1.4)
for spine in axb.spines.values():
    spine.set_visible(False)
for b, v in zip(bars, bar_values):
    axb.text(b.get_x() + b.get_width() / 2, v + (0.08 if v >= 0 else -0.08), f"{v:+.2f}%",
             ha='center', va='bottom' if v >= 0 else 'top', color='white',
             fontproperties=prop, fontsize=11)
axb.set_title('全球主要股指 10月20日 涨跌幅对比', fontproperties=prop_bold, color='white', fontsize=13)

plt.suptitle('2026-10-21 早报  ·  全球核心资产隔夜收盘（10月20日 · 常规交易日 · 模式A）',
             fontsize=15, color='white', y=1.01, fontproperties=prop_bold)
plt.tight_layout(pad=0.8)

out_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'images', 'charts')
os.makedirs(out_dir, exist_ok=True)
out_path = os.path.join(out_dir, 'chart_2026_10_21_morning.png')
plt.savefig(out_path, dpi=140, bbox_inches='tight', facecolor=fig.get_facecolor())
print(f"✅ 图表已保存：{out_path}")
