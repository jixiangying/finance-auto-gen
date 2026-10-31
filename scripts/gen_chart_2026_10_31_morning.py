#!/usr/bin/env python3
"""
生成 2026-10-31 早报全球核心资产数据卡片（10月30日隔夜收盘暨10月收官 · 常规交易日 · 模式A）
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

# ── 核心资产数据（美东10月30日收盘 / 跨市场对标） ──────────────────
assets = [
    {"name": "道琼斯指数",   "val": "51,770.31", "day": "-1.09%",  "sub": "-572.25点 10月月线收涨", "up": False},
    {"name": "标普500指数",  "val": "7,580.07",  "day": "-1.82%",  "day_pts": "-140.32", "sub": "-140.32点 抹平10月涨幅", "up": False},
    {"name": "纳斯达克综合", "val": "25,437.00", "day": "-2.86%",  "sub": "-747.72点 10月累跌5.30%", "up": False},
    {"name": "费城半导体",   "val": "重挫领跌",  "day": "-7.20%",  "sub": "AMD -10.88% / NVDA -4.22%", "up": False},
    {"name": "英特尔(INTC)", "val": "$65.76",    "day": "-28.58%", "sub": "-$26.31 Q4指引与毛利暴雷", "up": False},
    {"name": "亚马逊(AMZN)", "val": "$239.19",   "day": "-1.89%",  "sub": "单季CapEx达$773亿承压",   "up": False},
    {"name": "WTI原油",      "val": "$104.21",   "day": "+1.32%",  "sub": "霍尔木兹油轮遇袭破$104",  "up": True},
    {"name": "现货黄金",     "val": "$3,937.00", "day": "-2.10%",  "sub": "流动性挤兑失守$4000关口", "up": False},
    {"name": "10年期美债",   "val": "4.92%",     "day": "-8.3bp",  "sub": "避险涌入+ECI降温下破5%",  "up": None},
    {"name": "比特币(BTC)",  "val": "$77,315",   "day": "-4.60%",  "sub": "币安遭$63亿黑客攻击冲击", "up": False},
    {"name": "中概金龙指数", "val": "5,396.75",  "day": "-0.27%",  "sub": "离岸人民币走强至6.6533",  "up": False},
    {"name": "上证指数(周五)","val": "3,599.02", "day": "-1.44%",  "sub": "央行官宣隔夜利率1.25%换锚","up": False},
]

bar_labels = [
    "埃克森美孚", "WTI原油", "中概金龙", "道琼斯", "苹果",
    "上证指数", "微软", "标普500", "亚马逊", "现货黄金",
    "纳斯达克", "创业板指", "英伟达", "比特币", "费城半导体", "AMD"
]
bar_values = [
    1.40, 1.32, -0.27, -1.09, -1.23,
    -1.44, -1.55, -1.82, -1.89, -2.10,
    -2.86, -4.13, -4.22, -4.60, -7.20, -10.88
]

# ── 布局设计 ──────────────────────────────────────────────────
cols = 6
rows = (len(assets) + cols - 1) // cols
fig = plt.figure(figsize=(22, rows * 3.4 + 4.5))
fig.patch.set_facecolor('#0d1117')
gs = fig.add_gridspec(rows + 1, cols, height_ratios=[1] * rows + [1.35])

for i, a in enumerate(assets):
    ax = fig.add_subplot(gs[i // cols, i % cols])
    ax.set_facecolor('#0d1117')
    ax.axis('off')
    if a['up'] is None:
        color, bg, arrow = '#d4a017', '#1a1400', '■ '
    elif a['up']:
        color, bg, arrow = '#ff4d4d', '#1f0808', '▲ '
    else:
        color, bg, arrow = '#00cc66', '#041c11', '▼ '

    ax.add_patch(mpatches.FancyBboxPatch(
        (0.04, 0.04), 0.92, 0.92, boxstyle="round,pad=0.04", linewidth=1.6,
        edgecolor=color, facecolor=bg, transform=ax.transAxes, zorder=0))
    ax.text(0.5, 0.82, a['name'], transform=ax.transAxes, fontsize=13,
            color='#e6edf3', ha='center', va='center', fontproperties=prop_bold)
    ax.text(0.5, 0.57, a['val'], transform=ax.transAxes, fontsize=16,
            color='white', ha='center', va='center', fontproperties=prop_bold)
    ax.text(0.5, 0.34, f"单日变动: {arrow}{a['day']}", transform=ax.transAxes, fontsize=12,
            color=color, ha='center', va='center', fontproperties=prop_bold)
    ax.text(0.5, 0.15, a['sub'], transform=ax.transAxes, fontsize=10.5,
            color='#8b949e', ha='center', va='center', fontproperties=prop)

# ── 底部：核心资产与焦点个股涨跌幅横截面柱状图 ────────────────────
axb = fig.add_subplot(gs[rows, :])
axb.set_facecolor('#0d1117')
colors = ['#ff4d4d' if v > 0 else '#00cc66' for v in bar_values]
x = list(range(len(bar_labels)))
bars = axb.bar(x, bar_values, color=colors, width=0.58)
axb.axhline(0, color='#8b949e', linewidth=0.9)
axb.set_xticks(x)
axb.set_xticklabels(bar_labels, fontproperties=prop, color='#e6edf3', fontsize=11, rotation=12)
yticks = [-12.0, -10.0, -8.0, -6.0, -4.0, -2.0, 0.0, 2.0]
axb.set_yticks(yticks)
axb.set_yticklabels([f"{t:+.1f}%" for t in yticks], fontproperties=prop, color='#8b949e', fontsize=10.5)
axb.set_ylim(-12.6, 3.0)
axb.grid(axis='y', linestyle='--', alpha=0.18, color='#8b949e')
for spine in axb.spines.values():
    spine.set_visible(False)

for b, v in zip(bars, bar_values):
    offset = 0.25 if v >= 0 else -0.28
    va = 'bottom' if v >= 0 else 'top'
    axb.text(b.get_x() + b.get_width() / 2, v + offset, f"{v:+.2f}%",
             ha='center', va=va, color='white', fontproperties=prop, fontsize=10)

axb.set_title('全球核心指数、商品与焦点科技股单日涨跌幅对比（注：英特尔单日暴跌 -28.58% 已单独列示于上方卡片）',
              fontproperties=prop_bold, color='white', fontsize=12.5, pad=10)

plt.suptitle('2026-10-31 早报  ·  全球金融市场隔夜收盘暨10月收官看板（美东10月30日收盘 · 模式A）',
             fontsize=15.5, color='white', y=1.01, fontproperties=prop_bold)
plt.tight_layout(pad=0.85)

out_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'images', 'charts')
os.makedirs(out_dir, exist_ok=True)
out_path = os.path.join(out_dir, 'chart_2026_10_31_morning.png')
plt.savefig(out_path, dpi=140, bbox_inches='tight', facecolor=fig.get_facecolor())
print(f"Chart successfully saved to {out_path}")
