#!/usr/bin/env python3
"""
2026-09-07 早报 行情数据卡片
假日模式（美国劳工节）+ 模式 C（新周展望）
替代指标：A50期货、BTC、离岸人民币 + 上周美股收盘参考
"""

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.font_manager import FontProperties
import os

# 中文字体设置
FONT_PATH = '/System/Library/Fonts/STHeiti Medium.ttc'
if not os.path.exists(FONT_PATH):
    FONT_PATH = '/System/Library/Fonts/Supplemental/Songti.ttc'
prop = FontProperties(fname=FONT_PATH)
plt.rcParams['font.family'] = prop.get_name()

# 数据定义
# 格式: (资产名, 数值, 变化幅度, 单位, 上涨=True/下跌=False)
ASSETS = [
    # --- 节假日替代指标 ---
    ("🟡 BTC/比特币",      "~$79,800",  "周末盘整",   "",      None),
    ("🌏 A50期货 (SGX)",   "14,703",    "日区间±81",  "点",    None),
    ("💱 美元/离岸人民币", "6.7083",    "区间 6.707-6.708", "", None),
    # --- 上周收盘参考（截至09/04）---
    ("🇺🇸 标普500",        "7,718.60",  "周涨 +0.10%", "点",   True),
    ("🇺🇸 纳斯达克",       "26,506.99", "周涨 +0.15%", "点",   True),
    ("🇺🇸 道琼斯",         "53,414.25", "周跌 -0.20%", "点",   False),
    ("📈 10Y美债收益率",   "4.780%",    "周升 +0.05pct","",     False),
    ("🥇 现货黄金",        "$4,429.83", "周跌 -0.85%", "/oz",  False),
    ("🛢 WTI原油",         "$91.30",    "周涨 +2.60%", "/桶",  True),
]

FIG_W, FIG_H = 14, 10
fig, ax = plt.subplots(figsize=(FIG_W, FIG_H))
ax.set_facecolor('#0d1117')
fig.patch.set_facecolor('#0d1117')
ax.set_xlim(0, FIG_W)
ax.set_ylim(0, FIG_H)
ax.axis('off')

# 标题
ax.text(FIG_W/2, FIG_H - 0.55, "🗓 2026年09月07日 · 早报（劳工节假日 · 新周展望）",
        color='white', fontsize=15, fontweight='bold', ha='center', va='center',
        fontproperties=prop)
ax.text(FIG_W/2, FIG_H - 1.1,
        "⚠ 今日美股(NYSE/NASDAQ)休市 · 以下为假期可交易替代指标 + 上周收盘参考",
        color='#f0a500', fontsize=10, ha='center', va='center', fontproperties=prop)

# 分隔线
ax.axhline(y=FIG_H - 1.4, color='#333', linewidth=1, xmin=0.03, xmax=0.97)

# 绘制卡片
COLS = 3
ROWS = 3
pad_x, pad_y = 0.5, 0.4
card_w = (FIG_W - 2 * pad_x) / COLS
card_h = (FIG_H - 1.8 - pad_y) / ROWS

colors_up   = '#00c851'
colors_down = '#ff4444'
colors_none = '#888888'

for idx, (name, price, change, unit, is_up) in enumerate(ASSETS):
    row = idx // COLS
    col = idx % COLS
    x0 = pad_x + col * card_w
    y0 = FIG_H - 1.8 - (row + 1) * card_h

    # 卡片背景
    border_color = (colors_up if is_up is True else
                    colors_down if is_up is False else colors_none)
    rect = mpatches.FancyBboxPatch(
        (x0 + 0.1, y0 + 0.1), card_w - 0.2, card_h - 0.2,
        boxstyle="round,pad=0.1", linewidth=2,
        edgecolor=border_color, facecolor='#161b22')
    ax.add_patch(rect)

    cx = x0 + card_w / 2
    cy_name   = y0 + card_h * 0.72
    cy_price  = y0 + card_h * 0.42
    cy_change = y0 + card_h * 0.15

    ax.text(cx, cy_name, name, color='#c9d1d9', fontsize=9.5,
            ha='center', va='center', fontproperties=prop)
    ax.text(cx, cy_price, f"{price}{unit}", color='white', fontsize=13,
            fontweight='bold', ha='center', va='center', fontproperties=prop)

    chg_color = (colors_up if is_up is True else
                 colors_down if is_up is False else '#aaaaaa')
    ax.text(cx, cy_change, change, color=chg_color, fontsize=9,
            ha='center', va='center', fontproperties=prop)

# 底部注释
ax.text(FIG_W/2, 0.22,
        "数据来源：TradingView / xe.com / bitcoin.com  ·  上周美股数据截至 2026-09-04",
        color='#555', fontsize=8, ha='center', va='center', fontproperties=prop)

OUTPUT = os.path.join(os.path.dirname(__file__),
                      '..', 'images', 'charts', '2026-09-07-morning-chart.png')
OUTPUT = os.path.normpath(OUTPUT)
plt.tight_layout()
plt.savefig(OUTPUT, dpi=150, bbox_inches='tight',
            facecolor=fig.get_facecolor())
plt.close()
print(f"✅ 图表已保存：{OUTPUT}")
