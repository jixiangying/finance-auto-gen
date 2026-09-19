#!/usr/bin/env python3
# chart_2026_09_19_evening.py — 2026-09-19 周末复盘行情卡片

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib import font_manager
import os

# ── 中文字体 ────────────────────────────────────────────────────────────────
FONT_PATHS = [
    '/System/Library/Fonts/STHeiti Medium.ttc',
    '/System/Library/Fonts/Supplemental/Songti.ttc',
    '/System/Library/Fonts/PingFang.ttc',
]
prop = None
for fp in FONT_PATHS:
    if os.path.exists(fp):
        prop = font_manager.FontProperties(fname=fp)
        plt.rcParams['font.family'] = prop.get_name()
        break
if prop is None:
    prop = font_manager.FontProperties()

# ── 数据（周五收盘 + 本周累计涨跌幅）─────────────────────────────────────
assets = [
    # A股
    {"name": "上证指数",    "close": "3911.87",  "week_pct": +0.61,  "day_pct": +0.94},
    {"name": "深证成指",    "close": "13640.87", "week_pct": +1.26,  "day_pct": +1.72},
    {"name": "创业板指",    "close": "3372.68",  "week_pct": +1.52,  "day_pct": +2.25},
    # 港股
    {"name": "恒生指数",    "close": "24750.78", "week_pct": -0.22,  "day_pct": +0.60},
    # 美股
    {"name": "标普500",     "close": "7650.50",  "week_pct": -0.08,  "day_pct": None},
    {"name": "纳斯达克",    "close": "26522.55", "week_pct": +0.72,  "day_pct": None},
    {"name": "道琼斯",      "close": "51682.64", "week_pct": -1.69,  "day_pct": None},
    # 商品 & 外汇
    {"name": "黄金($/oz)",  "close": "4377.52",  "week_pct": None,   "day_pct": None},
    {"name": "WTI原油($/桶)","close": "100.21",  "week_pct": None,   "day_pct": None},
    {"name": "人民币/美元", "close": "6.6977",   "week_pct": None,   "day_pct": None},
]

# ── 布局 ─────────────────────────────────────────────────────────────────────
n = len(assets)
cols = 5
rows = (n + cols - 1) // cols
fig, axes = plt.subplots(rows, cols, figsize=(18, rows * 3.2))
fig.patch.set_facecolor('#0d1117')
axes = axes.flatten()

for i, a in enumerate(assets):
    ax = axes[i]
    ax.set_facecolor('#161b22')
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    ax.axis('off')

    # 边框色
    week = a["week_pct"]
    if week is None:
        border_color = '#58a6ff'
    elif week >= 0:
        border_color = '#f85149'   # 红=涨
    else:
        border_color = '#3fb950'   # 绿=跌

    rect = mpatches.FancyBboxPatch(
        (0.04, 0.04), 0.92, 0.92,
        boxstyle="round,pad=0.02",
        linewidth=2, edgecolor=border_color,
        facecolor='#21262d'
    )
    ax.add_patch(rect)

    # 资产名称
    ax.text(0.5, 0.82, a["name"], ha='center', va='center',
            fontsize=11, color='#c9d1d9', fontweight='bold',
            fontproperties=prop)

    # 收盘价
    ax.text(0.5, 0.60, a["close"], ha='center', va='center',
            fontsize=13, color='#e6edf3', fontweight='bold',
            fontproperties=prop)

    # 周度涨跌
    if week is not None:
        sign = "▲" if week >= 0 else "▼"
        color = '#f85149' if week >= 0 else '#3fb950'
        week_str = f"周累计 {sign} {abs(week):.2f}%"
        ax.text(0.5, 0.38, week_str, ha='center', va='center',
                fontsize=10, color=color, fontproperties=prop)
    else:
        # 对商品/汇率显示标签
        ax.text(0.5, 0.38, "本周行情", ha='center', va='center',
                fontsize=9, color='#8b949e', fontproperties=prop)

    # 周五单日涨跌
    if a["day_pct"] is not None:
        sign2 = "▲" if a["day_pct"] >= 0 else "▼"
        color2 = '#f85149' if a["day_pct"] >= 0 else '#3fb950'
        day_str = f"周五单日 {sign2} {abs(a['day_pct']):.2f}%"
        ax.text(0.5, 0.20, day_str, ha='center', va='center',
                fontsize=9, color=color2, fontproperties=prop)

# 关闭多余子图
for j in range(n, len(axes)):
    axes[j].set_visible(False)

# ── 标题 ─────────────────────────────────────────────────────────────────────
fig.suptitle("2026-09-19  |  本周核心资产表现（9/14–9/18）",
             fontsize=14, color='#e6edf3', y=1.01, fontproperties=prop)

# ── 保存 ─────────────────────────────────────────────────────────────────────
out_dir = '/Users/jxy/Documents/Project/finance-auto-gen/images/charts'
os.makedirs(out_dir, exist_ok=True)
out_path = os.path.join(out_dir, 'chart_2026_09_19_evening.png')
plt.tight_layout()
plt.savefig(out_path, dpi=150, bbox_inches='tight',
            facecolor=fig.get_facecolor())
plt.close()
print(f"✅ 图表已保存：{out_path}")
