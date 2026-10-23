#!/usr/bin/env python3
"""
生成 2026-10-23 晚报核心资产数据卡片（10月23日A股/港股收盘 + 10月22日隔夜美股 · 常规交易日 · 模式A）
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

# ── 核心资产数据（10月23日A股/港股收盘 + 10月22日美股收盘） ──────
assets = [
    {"name": "上证指数",     "val": "3,690.48",  "day": "+0.89%", "sub": "午后绝地反攻",         "up": True},
    {"name": "深证成指",     "val": "11,673.83", "day": "+2.79%", "sub": "放量4276亿",           "up": True},
    {"name": "创业板指",     "val": "2,684.10",  "day": "+4.16%", "sub": "盘中一度跌超3%",       "up": True},
    {"name": "恒生指数",     "val": "23,093.37", "day": "+0.69%", "sub": "+158.69点",            "up": True},
    {"name": "恒生科技",     "val": "3,871.66",  "day": "+2.05%", "sub": "科网股反弹",           "up": True},
    {"name": "北证50",       "val": "—",         "day": "+1.88%", "sub": "同步收涨",             "up": True},
    {"name": "道琼斯",       "val": "52,867.98", "day": "+0.02%", "sub": "隔夜微涨持平",         "up": True},
    {"name": "标普500",      "val": "7,663.43",  "day": "-1.21%", "sub": "7月末以来最大跌幅",    "up": False},
    {"name": "纳斯达克",     "val": "26,008.86", "day": "-2.60%", "sub": "6月以来最大跌幅",      "up": False},
    {"name": "金龙中国指数", "val": "5,518.53",  "day": "-1.19%", "sub": "中概股整体回调",       "up": False},
    {"name": "布伦特原油",   "val": "≈$113",     "day": "+4%以上", "sub": "中东局势升温",        "up": True},
    {"name": "现货黄金",     "val": "<$4,030",   "day": "回落",   "sub": "跌破4030美元关口",     "up": False},
]

bar_labels = ["上证", "深成指", "创业板", "恒指", "恒生科技", "道指", "标普500", "纳指", "金龙指数"]
bar_values = [0.89, 2.79, 4.16, 0.69, 2.05, 0.02, -1.21, -2.60, -1.19]

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
yticks = [-3.0, -2.0, -1.0, 0, 1.0, 2.0, 3.0, 4.0]
axb.set_yticks(yticks)
axb.set_yticklabels([f"{t:+.1f}%" for t in yticks], fontproperties=prop, color='#8b949e')
axb.set_ylim(-3.4, 5.0)
for spine in axb.spines.values():
    spine.set_visible(False)
for b, v in zip(bars, bar_values):
    axb.text(b.get_x() + b.get_width() / 2, v + (0.12 if v >= 0 else -0.12), f"{v:+.2f}%",
             ha='center', va='bottom' if v >= 0 else 'top', color='white',
             fontproperties=prop, fontsize=11)
axb.set_title('全球主要股指 10月23日（A股/港股）与 10月22日（美股隔夜）涨跌幅对比',
              fontproperties=prop_bold, color='white', fontsize=13)

plt.suptitle('2026-10-23 晚报  ·  A股港股收盘 + 隔夜美股（常规交易日 · 模式A）',
             fontsize=15, color='white', y=1.01, fontproperties=prop_bold)
plt.tight_layout(pad=0.8)

out_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'images', 'charts')
os.makedirs(out_dir, exist_ok=True)
out_path = os.path.join(out_dir, 'chart_2026_10_23_evening.png')
plt.savefig(out_path, dpi=140, bbox_inches='tight', facecolor=fig.get_facecolor())
print(f"✅ 图表已保存：{out_path}")
