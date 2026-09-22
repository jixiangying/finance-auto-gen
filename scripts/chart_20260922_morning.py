#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
2026-09-22 早报 — 国际市场核心行情卡片
"""
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.font_manager import FontProperties
import os

# ── 字体设置（macOS 中文）──────────────────────────────────────────────
FONT_PATHS = [
    '/System/Library/Fonts/STHeiti Medium.ttc',
    '/System/Library/Fonts/PingFang.ttc',
    '/Library/Fonts/Arial Unicode MS.ttf',
]
prop = None
for fp in FONT_PATHS:
    if os.path.exists(fp):
        prop = FontProperties(fname=fp)
        break
if prop is None:
    prop = FontProperties()

plt.rcParams['axes.unicode_minus'] = False

# ── 数据定义 ───────────────────────────────────────────────────────────
assets = [
    # 名称,             数值字符串,     涨跌幅,    类型
    ("S&P 500",         "7,764.70",    +1.50,  "美股"),
    ("纳斯达克",         "27,122.09",   +2.30,  "美股"),
    ("道琼斯",          "52,048.83",   +0.70,  "美股"),
    ("10Y美债收益率",    "4.955%",      -0.041, "债券"),  # 收益率下行
    ("布伦特原油",       "$100.29",     -3.40,  "商品"),
    ("WTI原油",         "$95.42",      -3.10,  "商品"),
    ("黄金",            "$4,347",      -0.45,  "商品"),
    ("比特币 BTC",       "$84,590",     +5.00,  "加密"),
    ("美元指数 DXY",     "100.12",      +0.13,  "外汇"),
    ("VIX 恐慌指数",     "14.86",       +0.34,  "波动"),
]

# ── 颜色规则：上涨红，下跌绿（A股习惯）──────────────────────────────────
def get_color(pct, asset_type):
    """债券收益率下行对应利好，用红色；其余正涨红、下跌绿"""
    if asset_type == "债券":
        return "#E63946" if pct < 0 else "#2DC653"  # 收益率跌 = 债券涨
    return "#E63946" if pct >= 0 else "#2DC653"

# ── 绘图 ──────────────────────────────────────────────────────────────
fig, axes = plt.subplots(2, 5, figsize=(18, 7))
fig.patch.set_facecolor('#0D1117')

for idx, (name, val, pct, atype) in enumerate(assets):
    row, col = divmod(idx, 5)
    ax = axes[row][col]
    color = get_color(pct, atype)
    ax.set_facecolor('#161B22')

    # 类型标签
    ax.text(0.5, 0.88, atype, transform=ax.transAxes,
            ha='center', va='center', fontsize=8,
            color='#8B949E', fontproperties=prop)
    # 资产名称
    ax.text(0.5, 0.70, name, transform=ax.transAxes,
            ha='center', va='center', fontsize=11, fontweight='bold',
            color='#C9D1D9', fontproperties=prop)
    # 数值
    ax.text(0.5, 0.48, val, transform=ax.transAxes,
            ha='center', va='center', fontsize=14, fontweight='bold',
            color='#FFFFFF', fontproperties=prop)
    # 涨跌幅
    sign = "▲" if pct >= 0 else "▼"
    ax.text(0.5, 0.24, f"{sign} {abs(pct):.2f}%", transform=ax.transAxes,
            ha='center', va='center', fontsize=12, fontweight='bold',
            color=color, fontproperties=prop)

    # 底部色条
    rect = mpatches.FancyBboxPatch(
        (0.1, 0.06), 0.8, 0.07,
        boxstyle="round,pad=0.01",
        linewidth=0, facecolor=color, alpha=0.7,
        transform=ax.transAxes, clip_on=False
    )
    ax.add_patch(rect)
    ax.axis('off')

    # 边框
    for spine in ax.spines.values():
        spine.set_edgecolor('#30363D')
        spine.set_linewidth(0.8)

# 标题
fig.text(0.5, 0.97,
         '🌐  2026年09月22日（周二）国际市场早报  —  核心资产行情',
         ha='center', va='center', fontsize=15, fontweight='bold',
         color='#E6EDF3', fontproperties=prop)
fig.text(0.5, 0.92,
         '数据基准：美东时间 2026-09-21 收盘 | 来源：NYSE / NASDAQ / CME / Binance',
         ha='center', va='center', fontsize=8,
         color='#8B949E', fontproperties=prop)

plt.tight_layout(rect=[0, 0, 1, 0.90])

# ── 保存 ──────────────────────────────────────────────────────────────
out_dir = os.path.join(os.path.dirname(__file__), '..', 'images', 'charts')
os.makedirs(out_dir, exist_ok=True)
out_path = os.path.join(out_dir, 'chart_20260922_morning.png')
plt.savefig(out_path, dpi=150, bbox_inches='tight',
            facecolor=fig.get_facecolor())
print(f"[OK] 图表已保存：{out_path}")
