from pathlib import Path

import matplotlib.pyplot as plt
from matplotlib.font_manager import FontProperties
from matplotlib.patches import FancyBboxPatch

plt.rcParams["font.family"] = "STHeiti"
plt.rcParams["axes.unicode_minus"] = False
font = FontProperties(family="STHeiti")

assets = [
    ("道琼斯工业指数", "50,182.95", "+0.33%", 1, "11/25 收盘"),
    ("标普 500", "7,182.78", "-0.25%", -1, "11/25 收盘"),
    ("纳斯达克综合指数", "23,585.80", "-0.62%", -1, "11/25 收盘"),
    ("欧洲 STOXX 600", "636.98", "+1.75%", 1, "11/26 收盘"),
    ("德国 DAX", "25,215.52", "+2.08%", 1, "11/26 收盘"),
    ("法国 CAC 40", "8,108.74", "+1.61%", 1, "11/26 收盘"),
    ("英国富时 100", "10,609.30", "+1.75%", 1, "11/26 收盘"),
    ("美国 10 年期国债", "4.848%", "-5.6 BP", -1, "11/25 收盘"),
    ("COMEX 黄金", "$3,654.40", "+3.35%", 1, "11/27 盘中"),
    ("NYMEX WTI 原油", "$85.69", "+2.40%", 1, "11/27 盘中"),
    ("富时中国 A50 期货", "12,564.50", "+0.41%", 1, "11/27 盘中"),
    ("离岸人民币 USD/CNH", "6.6653", "人民币 +0.03%", 1, "11/27 盘中"),
    ("比特币 BTC", "$61,497.48", "+1.84%", 1, "11/27 盘中"),
    ("以太坊 ETH", "$1,728.06", "+2.23%", 1, "11/27 盘中"),
    ("美元指数 DXY", "103.693", "+0.02%", 1, "11/27 盘中"),
]

fig, axes = plt.subplots(4, 4, figsize=(20, 14), dpi=160)
fig.patch.set_facecolor("#07111f")
fig.suptitle(
    "全球核心资产行情看板｜2026 年 11 月 27 日早报",
    fontsize=28,
    fontweight="bold",
    color="#f5f7fa",
    fontproperties=font,
    y=0.985,
)
fig.text(
    0.5,
    0.952,
    "美股与美债为 11 月 25 日收盘终值；欧股为 11 月 26 日收盘终值；其余为 11 月 27 日盘中快照",
    ha="center",
    fontsize=13,
    color="#a9b7c9",
    fontproperties=font,
)

red = "#ef5350"
green = "#20b486"
for index, ax in enumerate(axes.flat):
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    ax.axis("off")
    if index >= len(assets):
        card = FancyBboxPatch(
            (0.035, 0.06), 0.93, 0.86,
            boxstyle="round,pad=0.025,rounding_size=0.045",
            facecolor="#101f31", edgecolor="#31445b", linewidth=1.4,
        )
        ax.add_patch(card)
        ax.text(0.5, 0.66, "交易提示", ha="center", color="#f5f7fa", fontsize=19,
                fontweight="bold", fontproperties=font)
        ax.text(0.5, 0.43, "11/26 美股、美债感恩节休市", ha="center", color="#a9b7c9",
                fontsize=13, fontproperties=font)
        ax.text(0.5, 0.29, "11/27 美股提前至 13:00 ET 收市", ha="center", color="#a9b7c9",
                fontsize=13, fontproperties=font)
        continue

    name, value, change, direction, stamp = assets[index]
    color = red if direction > 0 else green
    card = FancyBboxPatch(
        (0.035, 0.06), 0.93, 0.86,
        boxstyle="round,pad=0.025,rounding_size=0.045",
        facecolor="#101f31", edgecolor=color, linewidth=1.8,
    )
    ax.add_patch(card)
    ax.text(0.09, 0.79, name, color="#dce5ef", fontsize=16, fontweight="bold",
            fontproperties=font, va="center")
    ax.text(0.09, 0.52, value, color="#ffffff", fontsize=23, fontweight="bold",
            fontproperties=font, va="center")
    ax.text(0.09, 0.29, change, color=color, fontsize=19, fontweight="bold",
            fontproperties=font, va="center")
    ax.text(0.91, 0.16, stamp, color="#8fa3b8", fontsize=10.5,
            fontproperties=font, ha="right", va="center")
    ax.set_xticks([])
    ax.set_yticks([])

plt.subplots_adjust(left=0.025, right=0.975, top=0.925, bottom=0.025, wspace=0.09, hspace=0.13)
output = Path(__file__).resolve().parents[1] / "images" / "charts" / "chart_2026_11_27_morning.png"
output.parent.mkdir(parents=True, exist_ok=True)
fig.savefig(output, facecolor=fig.get_facecolor(), bbox_inches="tight")
plt.close(fig)
print(output)
