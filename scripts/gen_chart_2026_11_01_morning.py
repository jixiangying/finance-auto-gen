#!/usr/bin/env python3
"""
生成 2026-11-01 周日早报全球核心资产周度/日度复盘数据卡片（模式B：周末复盘）
红色代表上涨，绿色代表下跌；同时展示“周五单日”与“全周累计”涨跌幅。
"""
import os
import numpy as np
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

# ── 核心资产数据（截至美东10月30日收盘 & 周末10月31日-11月1日动态） ──
assets = [
    {"name": "道琼斯指数",    "val": "51,770.31", "day": "-1.09%", "week": "-0.85%",  "sub": "全周跌444.85点 能源护盘",   "up": False},
    {"name": "标普500指数",   "val": "7,580.07",  "day": "-1.82%", "week": "-0.57%",  "sub": "全周跌43.61点 周线三连阴",  "up": False},
    {"name": "纳斯达克综合",  "val": "25,437.00", "day": "-2.86%", "week": "-2.00%",  "sub": "10月累跌5.30% 蒸发2万亿",   "up": False},
    {"name": "费城半导体",    "val": "10,688.80", "day": "-7.20%", "week": "-1.00%",  "sub": "英特尔单日崩28.58%引踩踏", "up": False},
    {"name": "中概金龙指数",  "val": "5,396.75",  "day": "-0.27%", "week": "-1.38%",  "sub": "离岸人民币强势守稳6.6533",  "up": False},
    {"name": "香港恒生指数",  "val": "23,294.42", "day": "+1.46%", "week": "+0.87%",  "sub": "逆势收红终结周线两连跌",   "up": True},
    {"name": "上证指数",      "val": "3,599.02",  "day": "-1.44%", "week": "-2.48%",  "sub": "央行11月2日隔夜1.25%换锚", "up": False},
    {"name": "创业板指",      "val": "2,413.63",  "day": "-4.13%", "week": "-10.08%", "sub": "高位算力出清 红利消费避险", "up": False},
    {"name": "WTI原油期货",   "val": "$104.21",   "day": "+1.32%", "week": "+0.91%",  "sub": "霍尔木兹遇袭+OPEC+稳配额", "up": True},
    {"name": "COMEX黄金",     "val": "$3,937.00", "day": "-2.10%", "week": "-2.14%",  "sub": "现货探3884 失守$4000关口",  "up": False},
    {"name": "10年期美债",    "val": "4.92%",     "day": "-8.3bp", "week": "-8.0bp",  "sub": "避险买盘+ECI降温创7周新低", "up": None},
    {"name": "比特币(周末)",  "val": "$77,300",   "day": "-0.02%", "week": "-4.30%",  "sub": "币安SAFU兜底 分批恢复提现", "up": False},
]

bar_labels = [
    "恒生指数", "WTI原油", "标普500", "道琼斯", "费城半导体",
    "中概金龙", "纳斯达克", "COMEX黄金", "上证指数", "比特币(7D)", "创业板指"
]
day_vals  = [1.46, 1.32, -1.82, -1.09, -7.20, -0.27, -2.86, -2.10, -1.44, -4.60, -4.13]
week_vals = [0.87, 0.91, -0.57, -0.85, -1.00, -1.38, -2.00, -2.14, -2.48, -4.30, -10.08]

# ── 布局设计 ──────────────────────────────────────────────────
cols = 6
rows = (len(assets) + cols - 1) // cols
fig = plt.figure(figsize=(22, rows * 3.5 + 4.8))
fig.patch.set_facecolor('#0d1117')
gs = fig.add_gridspec(rows + 1, cols, height_ratios=[1] * rows + [1.45])

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
    ax.text(0.5, 0.84, a['name'], transform=ax.transAxes, fontsize=13,
            color='#e6edf3', ha='center', va='center', fontproperties=prop_bold)
    ax.text(0.5, 0.61, a['val'], transform=ax.transAxes, fontsize=16,
            color='white', ha='center', va='center', fontproperties=prop_bold)
    ax.text(0.5, 0.41, f"全周: {arrow}{a['week']}  |  周五: {a['day']}",
            transform=ax.transAxes, fontsize=11,
            color=color, ha='center', va='center', fontproperties=prop_bold)
    ax.text(0.5, 0.16, a['sub'], transform=ax.transAxes, fontsize=10.2,
            color='#8b949e', ha='center', va='center', fontproperties=prop)

# ── 底部：核心资产“全周累计 vs 周五单日”双柱对比图 ──────────────────
axb = fig.add_subplot(gs[rows, :])
axb.set_facecolor('#0d1117')

x = np.arange(len(bar_labels))
w = 0.36
week_colors = ['#ff4d4d' if v > 0 else '#00cc66' for v in week_vals]
day_colors  = ['#ff8080' if v > 0 else '#4dff99' for v in day_vals]

bars_w = axb.bar(x - w / 2, week_vals, width=w, color=week_colors, label='全周累计涨跌幅 (%)')
bars_d = axb.bar(x + w / 2, day_vals,  width=w, color=day_colors, alpha=0.68, label='周五单日涨跌幅 (%，BTC为周五冲击日)')

axb.axhline(0, color='#8b949e', linewidth=0.9)
axb.set_xticks(x)
axb.set_xticklabels(bar_labels, fontproperties=prop, color='#e6edf3', fontsize=11.5, rotation=8)

yticks = [-12.0, -10.0, -8.0, -6.0, -4.0, -2.0, 0.0, 2.0, 4.0]
axb.set_yticks(yticks)
axb.set_yticklabels([f"{t:+.1f}%" for t in yticks], fontproperties=prop, color='#8b949e', fontsize=10.5)
axb.set_ylim(-11.8, 3.6)
axb.grid(axis='y', linestyle='--', alpha=0.18, color='#8b949e')
for spine in axb.spines.values():
    spine.set_visible(False)

for b, v in zip(bars_w, week_vals):
    offset = 0.22 if v >= 0 else -0.26
    va = 'bottom' if v >= 0 else 'top'
    axb.text(b.get_x() + b.get_width() / 2, v + offset, f"{v:+.2f}%",
             ha='center', va=va, color='white', fontproperties=prop_bold, fontsize=9.5)

for b, v in zip(bars_d, day_vals):
    offset = 0.22 if v >= 0 else -0.26
    va = 'bottom' if v >= 0 else 'top'
    axb.text(b.get_x() + b.get_width() / 2, v + offset, f"{v:+.2f}%",
             ha='center', va=va, color='#c9d1d9', fontproperties=prop, fontsize=8.8)

legend_patches = [
    mpatches.Patch(color='#ff4d4d', label='全周累计上涨 (深红)'),
    mpatches.Patch(color='#00cc66', label='全周累计下跌 (深绿)'),
    mpatches.Patch(color='#4dff99', alpha=0.68, label='周五单日涨跌幅对比 (浅红/浅绿)'),
]
leg = axb.legend(handles=legend_patches, loc='lower left', facecolor='#161b22', edgecolor='#30363d')
for text in leg.get_texts():
    text.set_fontproperties(prop)
    text.set_color('#e6edf3')

axb.set_title('全球核心股指与跨资产“全周累计 vs 周五单日”涨跌幅全景对比（中国10月制造业PMI报49.3%，高技术制造业51.3%逆势扩张）',
              fontproperties=prop_bold, color='white', fontsize=12.5, pad=10)

plt.suptitle('2026-11-01 周日早报  ·  全球金融市场周末深度复盘看板（10月26日–11月1日 · 模式B）',
             fontsize=15.5, color='white', y=1.01, fontproperties=prop_bold)
plt.tight_layout(pad=0.85)

out_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'images', 'charts')
os.makedirs(out_dir, exist_ok=True)
out_path = os.path.join(out_dir, 'chart_2026_11_01_morning.png')
plt.savefig(out_path, dpi=140, bbox_inches='tight', facecolor=fig.get_facecolor())
print(f"Chart successfully saved to {out_path}")
