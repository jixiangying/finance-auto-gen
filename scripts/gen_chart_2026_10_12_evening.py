import os
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib import font_manager as fm
from matplotlib.patches import FancyBboxPatch

FONT_PATH = "/System/Library/Fonts/STHeiti Medium.ttc"
prop = fm.FontProperties(fname=FONT_PATH)
plt.rcParams["font.sans-serif"] = ["Heiti TC", "PingFang SC", "STHeiti"]
plt.rcParams["axes.unicode_minus"] = False

RED, GREEN = "#d62728", "#2ca02c"

assets = [
    ("上证指数", "3797.24", -0.43),
    ("深证成指", "12384.87", -2.03),
    ("创业板指", "2963.82", -2.61),
    ("恒生指数", "24271.20", 0.25),
    ("恒生科技", "4169.57", -0.67),
    ("WTI原油", "$89.98", -2.0),
]

fig, axes = plt.subplots(2, 3, figsize=(12, 6), facecolor="#0f1720")
for ax, (name, price, chg) in zip(axes.flat, assets):
    color = RED if chg >= 0 else GREEN
    ax.set_facecolor("#0f1720")
    ax.add_patch(FancyBboxPatch((0.04, 0.06), 0.92, 0.88, boxstyle="round,pad=0.02",
                                fc="#1b2633", ec=color, lw=2.5, transform=ax.transAxes))
    ax.text(0.5, 0.75, name, ha="center", va="center", fontproperties=prop,
            fontsize=18, color="white", transform=ax.transAxes)
    ax.text(0.5, 0.48, price, ha="center", va="center", fontproperties=prop,
            fontsize=24, color="white", fontweight="bold", transform=ax.transAxes)
    arrow = "▲" if chg >= 0 else "▼"
    ax.text(0.5, 0.22, f"{arrow} {chg:+.2f}%", ha="center", va="center", fontproperties=prop,
            fontsize=18, color=color, transform=ax.transAxes)
    ax.set_xticks([])
    ax.set_yticks([])
    ax.set_xticklabels([], fontproperties=prop)
    ax.set_yticklabels([], fontproperties=prop)
    for s in ax.spines.values():
        s.set_visible(False)

fig.suptitle("2026年10月12日 国内核心资产收盘（沪深北成交 1.55万亿，缩量约3700亿）",
             fontproperties=prop, fontsize=16, color="white")
plt.tight_layout(rect=[0, 0, 1, 0.93])
out = os.path.join(os.path.dirname(__file__), "..", "images", "charts", "chart_2026_10_12_evening.png")
os.makedirs(os.path.dirname(out), exist_ok=True)
plt.savefig(out, dpi=150, facecolor=fig.get_facecolor())
print("saved", os.path.abspath(out))
