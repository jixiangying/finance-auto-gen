#!/usr/bin/env python3
"""
行情数据卡片 - 2026年10月1日早报（国庆节假日特辑）
"""
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm
import matplotlib.patches as mpatches
import os

# ─── 中文字体 ───────────────────────────────────────────────
font_candidates = [
    '/System/Library/Fonts/STHeiti Medium.ttc',
    '/System/Library/Fonts/Supplemental/Songti.ttc',
    '/System/Library/Fonts/PingFang.ttc',
]
prop = None
for fp in font_candidates:
    if os.path.exists(fp):
        prop = fm.FontProperties(fname=fp)
        plt.rcParams['font.family'] = prop.get_name()
        break
if prop is None:
    prop = fm.FontProperties()

# ─── 数据定义 ────────────────────────────────────────────────
assets = [
    # (资产名称,  当前值,  涨跌显示,  方向: 1=涨红/0=持平灰/-1=跌绿)
    ("富时A50期货\n(SGX)",    "13,931",  "+0.05%",  1),
    ("USD/CNH\n离岸人民币",   "6.7073",  "±0.00%",  0),
    ("BTC/USD\n比特币",       "$84,350", "震荡",    1),
    ("XAU/USD\n黄金",         "$4,157",  "承压↓",  -1),
    ("WTI原油",               "$90.64",  "+地缘",   1),
    ("Brent原油",             "$98.18",  "+逼近$100",1),
    ("S&P 500",               "7,651.54","-0.25%", -1),
    ("NASDAQ",                "26,861",  "+0.24%",  1),
    ("DJIA 道琼斯",           "50,906",  "-0.86%", -1),
    ("美债10Y收益率",         "5.29%",   "↑2002年新高", 1),
]

COLOR_UP   = "#E63946"   # 红 = 上涨
COLOR_DOWN = "#2DC653"   # 绿 = 下跌
COLOR_FLAT = "#888888"   # 灰 = 持平
BG_CARD    = "#1A1A2E"
BG_MAIN    = "#0F0F1A"
TEXT_WHITE = "#FFFFFF"
TEXT_GRAY  = "#AAAAAA"

n = len(assets)
cols = 5
rows = (n + cols - 1) // cols

fig_w = cols * 2.8
fig_h = rows * 2.0 + 1.4

fig = plt.figure(figsize=(fig_w, fig_h), facecolor=BG_MAIN)

# 全图透明底层 axes，用于放置 patches
ax_bg = fig.add_axes([0, 0, 1, 1], frameon=False)
ax_bg.set_xlim(0, 1)
ax_bg.set_ylim(0, 1)
ax_bg.axis('off')

# 标题
fig.text(0.5, 0.97, "🎊 国庆节假日特辑 · 全球市场关键指标",
         ha='center', va='top', fontsize=14, color=TEXT_WHITE,
         fontproperties=prop, fontweight='bold')
fig.text(0.5, 0.92, "2026年10月1日（星期四）早报  |  A股/港股休市  |  数据截至北京时间 08:00",
         ha='center', va='top', fontsize=8.5, color=TEXT_GRAY,
         fontproperties=prop)

pad_x = 0.03
pad_y = 0.06
card_w = (1.0 - 2*pad_x) / cols
card_h = (0.88 - pad_y) / rows

for i, (name, price, change, direction) in enumerate(assets):
    row = i // cols
    col = i % cols

    x = pad_x + col * card_w
    y = 0.88 - pad_y - (row + 1) * card_h

    color = COLOR_UP if direction == 1 else (COLOR_DOWN if direction == -1 else COLOR_FLAT)

    # 卡片背景
    rect = mpatches.FancyBboxPatch(
        (x + 0.005, y + 0.01), card_w - 0.01, card_h - 0.02,
        boxstyle="round,pad=0.01",
        linewidth=1.5, edgecolor=color,
        facecolor=BG_CARD, transform=fig.transFigure
    )
    ax_bg.add_patch(rect)

    cx = x + card_w / 2
    cy = y + card_h / 2

    # 资产名称
    fig.text(cx, cy + 0.038, name, ha='center', va='center',
             fontsize=8, color=TEXT_GRAY, fontproperties=prop,
             transform=fig.transFigure)

    # 价格
    fig.text(cx, cy + 0.003, price, ha='center', va='center',
             fontsize=12, color=TEXT_WHITE, fontproperties=prop,
             fontweight='bold', transform=fig.transFigure)

    # 涨跌幅
    fig.text(cx, cy - 0.030, change, ha='center', va='center',
             fontsize=9, color=color, fontproperties=prop,
             fontweight='bold', transform=fig.transFigure)

# 底部说明
fig.text(0.5, 0.02,
         "数据来源：TradingKey/SGX/Investing.com  |  ⚠️ 仅供参考，不构成投资建议",
         ha='center', va='bottom', fontsize=7, color=TEXT_GRAY,
         fontproperties=prop)

out_path = os.path.join(
    os.path.dirname(os.path.abspath(__file__)),
    '2026-10-01-morning-chart.png'
)
os.makedirs(os.path.dirname(out_path), exist_ok=True)
plt.savefig(out_path, dpi=150, bbox_inches='tight',
            facecolor=BG_MAIN, edgecolor='none')
plt.close()
print(f"✅ 图表已保存：{out_path}")
