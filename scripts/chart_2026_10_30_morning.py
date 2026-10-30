# -*- coding: utf-8 -*-
"""2026-10-30 早报数据卡片：隔夜美股收盘（10月29日）核心行情看板"""
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib import font_manager

FONT_PATH = "/System/Library/Fonts/STHeiti Medium.ttc"
prop = font_manager.FontProperties(fname=FONT_PATH)
plt.rcParams["font.family"] = prop.get_name()
plt.rcParams["axes.unicode_minus"] = False

UP = "#d32f2f"    # 红涨
DOWN = "#2e7d32"  # 绿跌
BG = "#fafafa"

# (名称, 现价, 涨跌幅%)
assets = [
    ("道琼斯工业指数", "52,342.55", -0.25),
    ("标普500指数", "7,720.39", -0.30),
    ("纳斯达克综合指数", "26,184.72", -1.38),
    ("Alphabet (GOOGL)", "财报后暴跌", -12.64),
    ("微软 (MSFT)", "Azure +48%", 2.61),
    ("10年期美债收益率", "5.003%", 0.01),
    ("现货黄金 XAU/USD", "$4,021.52", -1.15),
    ("WTI原油", "$102.85", 0.88),
    ("布伦特原油", "$111.59", 0.76),
    ("比特币 BTC/USD", "≈$77,000", -1.20),
    ("离岸人民币 CNH", "升破6.66", 0.35),
    ("美元指数 DXY", "102.14", -0.23),
]

fig, axes = plt.subplots(3, 4, figsize=(16, 9))
fig.patch.set_facecolor(BG)
fig.suptitle("2026-10-30 周五早报 · 隔夜全球金融市场核心行情看板（美东10月29日收盘）",
             fontproperties=prop, fontsize=20, fontweight="bold", y=0.98)

for ax, (name, price, chg) in zip(axes.flat, assets):
    ax.set_facecolor("#ffffff")
    color = UP if chg > 0 else DOWN
    arrow = "▲" if chg > 0 else "▼"
    ax.text(0.5, 0.72, name, ha="center", va="center",
            fontproperties=prop, fontsize=15, color="#333333")
    ax.text(0.5, 0.42, price, ha="center", va="center",
            fontproperties=prop, fontsize=18, fontweight="bold", color="#111111")
    ax.text(0.5, 0.14, f"{arrow} {chg:+.2f}%", ha="center", va="center",
            fontproperties=prop, fontsize=16, fontweight="bold", color=color)
    for spine in ax.spines.values():
        spine.set_edgecolor(color)
        spine.set_linewidth(2.5)
    ax.set_xticks([])
    ax.set_yticks([])
    ax.set_xticklabels([], fontproperties=prop)
    ax.set_yticklabels([], fontproperties=prop)

plt.tight_layout(rect=[0, 0.02, 1, 0.95])
out = "images/charts/chart_2026_10_30_morning.png"
plt.savefig(out, dpi=150, facecolor=BG, bbox_inches="tight")
print("saved:", out)
