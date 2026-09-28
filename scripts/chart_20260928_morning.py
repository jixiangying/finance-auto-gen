#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
2026-09-28 周一早报 - 新周展望行情数据卡片
模式 C：新周展望（含上周五收盘数据 + 资产价格参考）
"""

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.font_manager import FontProperties
import os

# ── 字体设置（macOS 中文支持）──────────────────────────────
font_paths = [
    '/System/Library/Fonts/STHeiti Medium.ttc',
    '/System/Library/Fonts/Supplemental/Arial Unicode MS.ttf',
    '/System/Library/Fonts/PingFang.ttc',
]
font_prop = None
for fp in font_paths:
    if os.path.exists(fp):
        font_prop = FontProperties(fname=fp)
        break

plt.rcParams['axes.unicode_minus'] = False

# ── 数据定义 ──────────────────────────────────────────────
# 格式：(名称, 数值/区间, 涨跌幅, 单位注释, is_up)
assets = [
    # 美股（上周五 9/25 收盘）
    ("标普500\nS&P 500",  "7,743.51",  "+0.51%",  "上周五收盘", True),
    ("纳斯达克\nNasdaq",  "27,068.72", "+0.48%",  "上周五收盘", True),
    # 美债
    ("10年美债\n收益率",  "5.17%",     "↑ 高位",  "创2007年来新高", False),
    # 商品
    ("黄金现货\nXAU/USD", "4,285.12",  "+0.27%",  "美元/盎司", True),
    ("WTI原油",           "93.51",     "+1.19%",  "美元/桶", True),
    # 加密
    ("比特币\nBTC/USD",   "84,000",    "≈震荡",   "近期高位~87,000", True),
]

# ── 颜色主题 ──────────────────────────────────────────────
BG_COLOR    = "#0D1117"
CARD_UP     = "#1A2F1A"   # 深绿底（上涨）
CARD_DOWN   = "#2F1A1A"   # 深红底（下跌）
TITLE_COLOR = "#E6EDF3"
VAL_COLOR   = "#F0F6FC"
UP_COLOR    = "#3FB950"   # 绿色 = 上涨
DOWN_COLOR  = "#F85149"   # 红色 = 下跌
NEUTRAL     = "#8B949E"
ACCENT      = "#58A6FF"

# ── 画布布局 ──────────────────────────────────────────────
n = len(assets)
cols = 3
rows = (n + cols - 1) // cols
fig_w = cols * 3.8 + 0.6
fig_h = rows * 2.6 + 1.8

fig, axes = plt.subplots(rows, cols, figsize=(fig_w, fig_h))
fig.patch.set_facecolor(BG_COLOR)
axes_flat = axes.flatten() if rows > 1 else [axes] if cols == 1 else list(axes)

def draw_card(ax, name, value, change, note, is_up):
    bg = CARD_UP if is_up else CARD_DOWN
    change_color = UP_COLOR if is_up else DOWN_COLOR
    ax.set_facecolor(bg)
    for spine in ax.spines.values():
        spine.set_visible(False)
    ax.set_xticks([])
    ax.set_yticks([])

    # 资产名称
    kw = dict(fontproperties=font_prop) if font_prop else {}
    ax.text(0.5, 0.82, name, transform=ax.transAxes,
            ha='center', va='center', fontsize=11, color=TITLE_COLOR,
            fontweight='bold', linespacing=1.4, **kw)
    # 数值
    ax.text(0.5, 0.52, value, transform=ax.transAxes,
            ha='center', va='center', fontsize=15.5, color=VAL_COLOR,
            fontweight='bold', **kw)
    # 涨跌幅
    ax.text(0.5, 0.28, change, transform=ax.transAxes,
            ha='center', va='center', fontsize=12, color=change_color,
            fontweight='bold', **kw)
    # 注释
    ax.text(0.5, 0.09, note, transform=ax.transAxes,
            ha='center', va='center', fontsize=8.5, color=NEUTRAL,
            style='italic', **kw)
    # 边框线
    border_color = UP_COLOR if is_up else DOWN_COLOR
    for spine_name in ['top', 'bottom', 'left', 'right']:
        ax.spines[spine_name].set_visible(True)
        ax.spines[spine_name].set_color(border_color)
        ax.spines[spine_name].set_linewidth(1.2)

for i, (name, value, change, note, is_up) in enumerate(assets):
    draw_card(axes_flat[i], name, value, change, note, is_up)

# 隐藏多余格子
for j in range(n, len(axes_flat)):
    axes_flat[j].set_visible(False)

# ── 总标题 & 副标题 ─────────────────────────────────────────
kw = dict(fontproperties=font_prop) if font_prop else {}
fig.text(0.5, 0.97, "🌐 新周展望：核心资产价格总览", ha='center', va='top',
         fontsize=15, color=ACCENT, fontweight='bold', **kw)
fig.text(0.5, 0.93, "2026年9月28日（周一）| 模式C：新周展望", ha='center', va='top',
         fontsize=10, color=NEUTRAL, **kw)

plt.tight_layout(rect=[0, 0, 1, 0.91])

# ── 输出 ────────────────────────────────────────────────────
out_dir = "/Users/jxy/Documents/Project/finance-auto-gen/images/charts"
os.makedirs(out_dir, exist_ok=True)
out_path = os.path.join(out_dir, "chart_20260928_morning.png")
plt.savefig(out_path, dpi=150, bbox_inches='tight', facecolor=BG_COLOR)
plt.close()
print(f"✅ 图表已保存：{out_path}")
