#!/usr/bin/env python3
"""
生成 2026-08-23 周末复盘行情数据卡片
"""
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.font_manager import FontProperties
import numpy as np

# 中文字体设置
try:
    prop = FontProperties(fname='/System/Library/Fonts/STHeiti Medium.ttc')
    prop_bold = FontProperties(fname='/System/Library/Fonts/STHeiti Medium.ttc', weight='bold')
except:
    prop = FontProperties(family='PingFang SC')
    prop_bold = FontProperties(family='PingFang SC', weight='bold')

# 数据（周五收盘 + 本周累计）
assets = [
    # (名称, 现价/数值, 单日涨跌%, 全周涨跌%, 颜色分类)
    ("标普500",   "7,674.37",  "+0.43%", "-1.40%", "down"),
    ("纳斯达克",  "26,171.44", "+0.40%", "-2.10%", "down"),
    ("道琼斯",    "53,276.21", "+0.98%", "-0.80%", "down"),
    ("美债10Y",   "4.74%",     "+0bp",   "+4bp",   "down"),
    ("黄金(COMEX)", "$4,621",  "+0.67%", "+5.2%",  "up"),
    ("WTI原油",   "$86.07",   "+1.22%", "+5.4%",  "up"),
    ("比特币BTC", "$77,464",  "+1.85%", "+20.6%", "up"),
    ("美元指数",  "98.82",    "-0.15%", "-0.6%",  "down"),
]

# 颜色
COLOR_RED    = "#E84040"   # 上涨 红
COLOR_GREEN  = "#2BC46A"   # 下跌 绿
COLOR_GOLD   = "#F4C430"
COLOR_BG     = "#0D1117"
COLOR_CARD   = "#161B22"
COLOR_BORDER_UP   = "#E84040"
COLOR_BORDER_DOWN = "#2BC46A"
COLOR_TEXT   = "#E6EDF3"
COLOR_SUBTEXT = "#8B949E"
COLOR_TITLE  = "#F0F6FC"

fig, ax = plt.subplots(figsize=(14, 9))
fig.patch.set_facecolor(COLOR_BG)
ax.set_facecolor(COLOR_BG)
ax.axis('off')

# 标题
ax.text(0.5, 0.97, "🌐  全球市场周报 · 本周核心资产收盘总览", fontproperties=prop_bold,
        transform=ax.transAxes, ha='center', va='top',
        fontsize=17, color=COLOR_GOLD)
ax.text(0.5, 0.92, "2026年08月18日（周一）— 08月22日（周五）", fontproperties=prop,
        transform=ax.transAxes, ha='center', va='top',
        fontsize=11, color=COLOR_SUBTEXT)

# 网格布局：4列 × 2行
cols = 4
rows = 2
card_w = 0.22
card_h = 0.30
x_starts = [0.02, 0.26, 0.50, 0.74]
y_starts  = [0.53, 0.13]

for i, (name, price, daily_chg, week_chg, direction) in enumerate(assets):
    col_i = i % cols
    row_i = i // cols
    x0 = x_starts[col_i]
    y0 = y_starts[row_i]

    is_up = (direction == "up")
    arrow = "▲" if is_up else "▼"
    bar_color = COLOR_RED if is_up else COLOR_GREEN
    border_color = COLOR_BORDER_UP if is_up else COLOR_BORDER_DOWN
    week_color  = COLOR_RED if week_chg.startswith("+") else COLOR_GREEN

    # 卡片背景
    fancy = mpatches.FancyBboxPatch((x0, y0), card_w, card_h,
                                     boxstyle="round,pad=0.005",
                                     facecolor=COLOR_CARD, edgecolor=border_color,
                                     linewidth=1.5, transform=ax.transAxes, zorder=2)
    ax.add_patch(fancy)

    cx = x0 + card_w / 2

    # 资产名称
    ax.text(cx, y0 + card_h - 0.035, name, fontproperties=prop_bold,
            transform=ax.transAxes, ha='center', va='top',
            fontsize=12, color=COLOR_TEXT, zorder=3)
    # 现价
    ax.text(cx, y0 + card_h - 0.095, price, fontproperties=prop_bold,
            transform=ax.transAxes, ha='center', va='top',
            fontsize=14, color=COLOR_TITLE, zorder=3)
    # 单日涨跌
    ax.text(cx, y0 + card_h - 0.155, f"{arrow} 昨日 {daily_chg}", fontproperties=prop,
            transform=ax.transAxes, ha='center', va='top',
            fontsize=10, color=bar_color, zorder=3)
    # 分隔线
    line_y = y0 + card_h - 0.205
    ax.plot([x0 + 0.01, x0 + card_w - 0.01], [line_y, line_y],
            transform=ax.transAxes, color=COLOR_SUBTEXT, lw=0.5, zorder=3, alpha=0.4)
    # 周度涨跌
    ax.text(cx - 0.015, y0 + 0.065, "本周:", fontproperties=prop,
            transform=ax.transAxes, ha='right', va='center',
            fontsize=9, color=COLOR_SUBTEXT, zorder=3)
    ax.text(cx + 0.015, y0 + 0.065, week_chg, fontproperties=prop_bold,
            transform=ax.transAxes, ha='left', va='center',
            fontsize=11, color=week_color, zorder=3)

# 底部免责
ax.text(0.5, 0.04, "红色▲上涨  绿色▼下跌  |  数据来源：NYSE/COMEX/CME  |  仅供参考，不构成投资建议",
        fontproperties=prop, transform=ax.transAxes, ha='center', va='center',
        fontsize=8, color=COLOR_SUBTEXT, alpha=0.7)

output_path = "images/charts/2026-08-23-morning.png"
plt.tight_layout()
plt.savefig(output_path, dpi=150, bbox_inches='tight', facecolor=COLOR_BG)
plt.close()
print(f"✅ 行情卡片已保存至 {output_path}")
