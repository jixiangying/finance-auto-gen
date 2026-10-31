#!/usr/bin/env python3
"""
生成 2026-10-31 晚报（周六下午 · 模式B：周末复盘）核心资产周度与日度表现数据看板
包含：收盘点位、周五单日涨跌幅、全周累计涨跌幅（10月26日-10月30日）及行业/跨市场横向对比
"""
import os
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import numpy as np
from matplotlib.font_manager import FontProperties

# ── 中文字体设置 (macOS) ───────────────────────────────────────
FONT_PATH = "/System/Library/Fonts/STHeiti Medium.ttc"
prop = FontProperties(fname=FONT_PATH)
prop_bold = FontProperties(fname=FONT_PATH, weight='bold')
plt.rcParams['font.sans-serif'] = ['PingFang SC', 'STHeiti', 'Arial Unicode MS']
plt.rcParams['axes.unicode_minus'] = False

# ── 核心资产周度/日度数据（模式B：同时展示周五单日与全周累计） ────────
assets = [
    {"name": "上证指数",     "val": "3,599.02",  "day": "-1.44%", "week": "-2.48%",  "note": "险失3600 / 银行红利护盘", "up_w": False},
    {"name": "深证成指",     "val": "10,833.78", "day": "-2.73%", "week": "-7.20%",  "note": "三季报收官前成长换手",   "up_w": False},
    {"name": "创业板指",     "val": "2,413.63",  "day": "-4.13%", "week": "-10.08%", "note": "算力链调整创阶段新低",   "up_w": False},
    {"name": "沪深300",      "val": "3,985.50",  "day": "-1.39%", "week": "-2.92%",  "note": "白酒涨停潮+大金融稳盘",  "up_w": False},
    {"name": "科创50指数",   "val": "1,160.84",  "day": "-5.48%", "week": "-13.72%", "note": "硬科技估值集中消化",     "up_w": False},
    {"name": "北证50指数",   "val": "885.74",    "day": "-2.67%", "week": "-10.07%", "note": "高弹性微盘筹码出清",     "up_w": False},
    {"name": "恒生指数",     "val": "23,294.42", "day": "+1.46%", "week": "+0.87%",  "note": "终结周线两连跌逆势收红", "up_w": True},
    {"name": "恒生科技指数", "val": "3,754.90",  "day": "+0.29%", "week": "-3.02%",  "note": "周五翻红 / 科网权重回暖", "up_w": False},
    {"name": "申万银行指数", "val": "领涨全场",  "day": "逆势护盘","week": "+4.97%",  "note": "工行建行盘中频创新高",   "up_w": True},
    {"name": "申万食品饮料", "val": "消费反攻",  "day": "批量涨停","week": "+3.29%",  "note": "老窖古井涨停/青食5连板", "up_w": True},
    {"name": "纳斯达克综合", "val": "25,437.00", "day": "-2.86%", "week": "-2.00%",  "note": "芯片重挫 / INTC跌28.6%", "up_w": False},
    {"name": "WTI原油期货",  "val": "$104.12",   "day": "+2.08%", "week": "周线收涨", "note": "中东航运溢价破百元关",  "up_w": True},
]

# ── 底部对比柱状图数据（核心指数与代表板块：周五单日 vs 全周累计） ──
bar_labels = [
    "申万银行", "石油石化", "食品饮料", "恒生指数",
    "道琼斯", "标普500", "纳斯达克", "上证指数",
    "沪深300", "恒生科技", "深证成指", "北证50",
    "创业板指", "科创50"
]
week_vals = [
    4.97, 3.50, 3.29, 0.87,
    -0.85, -0.57, -2.00, -2.48,
    -2.92, -3.02, -7.20, -10.07,
    -10.08, -13.72
]

# ── 画布与网格布局 ────────────────────────────────────────────
cols = 6
rows = 2
fig = plt.figure(figsize=(22, 11.8))
fig.patch.set_facecolor('#0d1117')
gs = fig.add_gridspec(rows + 1, cols, height_ratios=[1.0, 1.0, 1.45])

for i, a in enumerate(assets):
    ax = fig.add_subplot(gs[i // cols, i % cols])
    ax.set_facecolor('#0d1117')
    ax.axis('off')

    if a['up_w']:
        color, bg, arrow = '#ff4d4d', '#1f0808', '▲'
    else:
        color, bg, arrow = '#00cc66', '#041c11', '▼'

    day_color = '#ff4d4d' if ('+' in a['day'] or '涨' in a['day'] or '护盘' in a['day']) else '#00cc66'

    ax.add_patch(mpatches.FancyBboxPatch(
        (0.03, 0.04), 0.94, 0.92, boxstyle="round,pad=0.04", linewidth=1.6,
        edgecolor=color, facecolor=bg, transform=ax.transAxes, zorder=0))

    ax.text(0.5, 0.84, a['name'], transform=ax.transAxes, fontsize=13.5,
            color='#e6edf3', ha='center', va='center', fontproperties=prop_bold)
    ax.text(0.5, 0.62, a['val'], transform=ax.transAxes, fontsize=16,
            color='white', ha='center', va='center', fontproperties=prop_bold)
    ax.text(0.5, 0.42, f"全周: {arrow} {a['week']}", transform=ax.transAxes, fontsize=12,
            color=color, ha='center', va='center', fontproperties=prop_bold)
    ax.text(0.5, 0.26, f"周五单日: {a['day']}", transform=ax.transAxes, fontsize=10.8,
            color=day_color, ha='center', va='center', fontproperties=prop)
    ax.text(0.5, 0.11, a['note'], transform=ax.transAxes, fontsize=9.8,
            color='#8b949e', ha='center', va='center', fontproperties=prop)

# ── 底部柱状图：全周累计涨跌幅横向排序（红涨绿跌） ────────────────
axb = fig.add_subplot(gs[rows, :])
axb.set_facecolor('#0d1117')
x = np.arange(len(bar_labels))
colors = ['#ff4d4d' if v > 0 else '#00cc66' for v in week_vals]
bars = axb.bar(x, week_vals, color=colors, width=0.56)

axb.axhline(0, color='#8b949e', linewidth=1.0)
axb.set_xticks(x)
axb.set_xticklabels(bar_labels, fontproperties=prop, color='#e6edf3', fontsize=11.5, rotation=10)

yticks = [-15.0, -12.0, -9.0, -6.0, -3.0, 0.0, 3.0, 6.0]
axb.set_yticks(yticks)
axb.set_yticklabels([f"{t:+.1f}%" for t in yticks], fontproperties=prop, color='#8b949e', fontsize=10.5)
axb.set_ylim(-15.6, 6.8)
axb.grid(axis='y', linestyle='--', alpha=0.18, color='#8b949e')
for spine in axb.spines.values():
    spine.set_visible(False)

for b, v in zip(bars, week_vals):
    offset = 0.28 if v >= 0 else -0.35
    va = 'bottom' if v >= 0 else 'top'
    axb.text(b.get_x() + b.get_width() / 2, v + offset, f"{v:+.2f}%",
             ha='center', va=va, color='white', fontproperties=prop_bold, fontsize=10.2)

axb.set_title('本周（10月26日—10月30日）核心宽基指数与领涨防御板块全周累计涨跌幅对比（红涨绿跌）',
              fontproperties=prop_bold, color='white', fontsize=13, pad=10)

plt.suptitle('2026-10-31 周末复盘  ·  中国与全球核心资产周度/日度表现看板（三季报收官 · 央行隔夜利率1.25%换锚 · 10月PMI出炉）',
             fontsize=15.5, color='white', y=1.01, fontproperties=prop_bold)
plt.tight_layout(pad=0.85)

out_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'images', 'charts')
os.makedirs(out_dir, exist_ok=True)
out_path = os.path.join(out_dir, 'chart_2026_10_31_evening.png')
plt.savefig(out_path, dpi=140, bbox_inches='tight', facecolor=fig.get_facecolor())
print(f"Chart successfully saved to {out_path}")
