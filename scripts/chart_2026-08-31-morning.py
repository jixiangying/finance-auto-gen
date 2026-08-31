#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
周度行情数据卡片 - 2026-08-31 (周日) 早报周末复盘
"""
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.font_manager import FontProperties
import os

# ── 字体配置（macOS 中文支持）────────────────────────────────────────
FONT_PATH = '/System/Library/Fonts/STHeiti Medium.ttc'
if not os.path.exists(FONT_PATH):
    FONT_PATH = '/System/Library/Fonts/PingFang.ttc'
prop = FontProperties(fname=FONT_PATH)

# ── 核心市场数据（周度涨跌） ─────────────────────────────────────────
assets = [
    # 美股
    {"name": "S&P 500",   "price": "7,711.76",  "weekly": "+0.50%", "daily": "-0.28%", "up": True},
    {"name": "纳斯达克",  "price": "26,402.42", "weekly": "+0.90%", "daily": "-0.41%", "up": True},
    {"name": "道琼斯",    "price": "53,559.99", "weekly": "+0.30%", "daily": "-0.19%", "up": True},
    # 中港
    {"name": "上证指数",  "price": "3,952.18",  "weekly": "+1.20%", "daily": "+0.67%", "up": True},
    {"name": "恒生指数",  "price": "25,584.79", "weekly": "-0.35%", "daily": "-0.52%", "up": False},
    # 大宗 / 加密
    {"name": "WTI 原油",  "price": "$83.40",    "weekly": "-4.10%", "daily": "-1.85%", "up": False},
    {"name": "黄金",      "price": "$4,594.99", "weekly": "-0.61%", "daily": "-0.61%", "up": False},
    {"name": "比特币",    "price": "$77,678",   "weekly": "-3.30%", "daily": "-3.30%", "up": False},
    # 债市
    {"name": "美债10Y",   "price": "4.72%",     "weekly": "+17bp",  "daily": "+12bp",  "up": False},
]

# ── 布局设置 ──────────────────────────────────────────────────────────
n = len(assets)
fig, axes = plt.subplots(1, n, figsize=(22, 5))
fig.patch.set_facecolor('#0d1117')

UP_COLOR   = '#e84118'   # 红 = 上涨
DOWN_COLOR = '#44bd32'   # 绿 = 下跌
BG_CARD    = '#161b22'
TITLE_BG   = '#21262d'

for ax, item in zip(axes, assets):
    color = UP_COLOR if item["up"] else DOWN_COLOR
    ax.set_facecolor(BG_CARD)

    # 卡片边框
    for spine in ax.spines.values():
        spine.set_edgecolor(color)
        spine.set_linewidth(2)

    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    ax.set_xticks([])
    ax.set_yticks([])

    # 资产名称
    ax.text(0.5, 0.88, item["name"], ha='center', va='center',
            fontsize=12, fontweight='bold', color='#e6edf3',
            fontproperties=prop)

    # 价格
    ax.text(0.5, 0.62, item["price"], ha='center', va='center',
            fontsize=11, color='#c9d1d9', fontproperties=prop)

    # 周涨跌
    ax.text(0.5, 0.40, f"周度  {item['weekly']}", ha='center', va='center',
            fontsize=11, fontweight='bold', color=color,
            fontproperties=prop)

    # 单日涨跌（周五）
    ax.text(0.5, 0.20, f"周五  {item['daily']}", ha='center', va='center',
            fontsize=9.5, color='#8b949e', fontproperties=prop)

    # 箭头装饰
    arrow = "▲" if item["up"] else "▼"
    ax.text(0.5, 0.06, arrow, ha='center', va='center',
            fontsize=10, color=color, fontproperties=prop)

# 总标题
fig.suptitle("本周全球核心资产表现  (Aug 25–28, 2026)",
             fontsize=14, fontweight='bold', color='#e6edf3',
             fontproperties=prop, y=1.02)

# 注释
fig.text(0.5, -0.04,
         "注：红色▲上涨  绿色▼下跌  ｜  数据来源：Morningstar / Investing.com",
         ha='center', fontsize=8, color='#8b949e', fontproperties=prop)

plt.tight_layout()

out_path = os.path.join(os.path.dirname(__file__),
                        '../images/charts/chart_2026-08-31-morning.png')
os.makedirs(os.path.dirname(out_path), exist_ok=True)
plt.savefig(out_path, dpi=160, bbox_inches='tight',
            facecolor=fig.get_facecolor())
print(f"图表已保存至: {out_path}")
