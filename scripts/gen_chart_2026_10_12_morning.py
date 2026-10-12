"""2026-10-12 新周展望 · 全球核心资产开局坐标卡片（基于10月9日收盘 + 周末加密市场）"""
import os
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib import font_manager
from matplotlib.patches import FancyBboxPatch

FONT_PATH = "/System/Library/Fonts/STHeiti Medium.ttc"
prop = font_manager.FontProperties(fname=FONT_PATH)
font_manager.fontManager.addfont(FONT_PATH)
plt.rcParams["font.family"] = prop.get_name()
plt.rcParams["axes.unicode_minus"] = False

# (名称, 现价, 涨跌幅%, 口径说明)
assets = [
    ("标普500", "7,811.54", 1.15, "全周累计"),
    ("道琼斯", "51,654.95", 0.93, "全周累计"),
    ("纳斯达克", "27,366.17", 0.64, "全周累计 · 四连周涨"),
    ("恒生指数", "24,211.35", 1.79, "周五单日"),
    ("日经225", "69,030.92", -0.02, "周五单日 · 周一休市"),
    ("WTI原油", "$91.85", 0.81, "全周累计"),
    ("现货黄金", "$4,193.87", 1.47, "周五单日 · 全周持平"),
    ("10年期美债", "5.24%", None, "全周 -3.3bp · 周一休市"),
    ("比特币", "≈$83,000", None, "周日盘中 · 横盘整理"),
]

UP, DOWN, FLAT = "#d62728", "#2ca02c", "#7f7f7f"

fig, ax = plt.subplots(figsize=(14, 9), dpi=150)
fig.patch.set_facecolor("#0f1624")
ax.set_facecolor("#0f1624")
ax.set_xlim(0, 3)
ax.set_ylim(0, 3)
ax.axis("off")

for i, (name, price, chg, note) in enumerate(assets):
    col, row = i % 3, 2 - i // 3
    if chg is None:
        color, chg_txt = FLAT, "—"
        if "bp" in note:
            color, chg_txt = DOWN, "-3.3bp"
    else:
        color = UP if chg > 0 else (DOWN if chg < 0 else FLAT)
        arrow = "▲" if chg > 0 else ("▼" if chg < 0 else "■")
        chg_txt = f"{arrow} {chg:+.2f}%"
    box = FancyBboxPatch((col + 0.05, row + 0.08), 0.9, 0.84,
                         boxstyle="round,pad=0.02,rounding_size=0.05",
                         linewidth=2, edgecolor=color, facecolor="#1b2436")
    ax.add_patch(box)
    ax.text(col + 0.5, row + 0.75, name, ha="center", va="center",
            fontproperties=prop, fontsize=18, color="white")
    ax.text(col + 0.5, row + 0.52, price, ha="center", va="center",
            fontproperties=prop, fontsize=24, color="white", weight="bold")
    ax.text(col + 0.5, row + 0.30, chg_txt, ha="center", va="center",
            fontproperties=prop, fontsize=20, color=color)
    ax.text(col + 0.5, row + 0.15, note, ha="center", va="center",
            fontproperties=prop, fontsize=12, color="#aab4c8")

fig.suptitle("新周开局坐标 · 全球核心资产（截至10月9日收盘 / BTC为10月11日）",
             fontproperties=prop, fontsize=20, color="white", y=0.97)
fig.text(0.5, 0.02, "红色=上涨  绿色=下跌  |  数据：AP / Investing.com / TradingEconomics",
         ha="center", fontproperties=prop, fontsize=11, color="#8892a6")

out = os.path.join(os.path.dirname(__file__), "..", "images", "charts", "chart_2026_10_12_morning.png")
os.makedirs(os.path.dirname(out), exist_ok=True)
plt.savefig(out, facecolor=fig.get_facecolor(), bbox_inches="tight")
print("saved", os.path.abspath(out))
