import matplotlib.pyplot as plt
import matplotlib.font_manager as fm
import os

output_dir = "/Users/jxy/Documents/Project/finance-auto-gen/images/charts/"
os.makedirs(output_dir, exist_ok=True)

font_path = "/System/Library/Fonts/STHeiti Medium.ttc"
if not os.path.exists(font_path):
    font_path = "/System/Library/Fonts/PingFang.ttc"
prop = fm.FontProperties(fname=font_path)

sections = [
    ("美股", [
        ("标普500", "7,354.02", "🟢 -0.05%"),
        ("纳斯达克", "25,297.62", "🟢 -0.24%"),
        ("道琼斯", "51,876.11", "🟢 -0.09%"),
        ("费城半导体", "-", "🟢 -5.0%+"),
    ]),
    ("商品 & 宏观", [
        ("黄金 (盎司)", "$4,032", "🔴 +0.3%"),
        ("WTI原油 (桶)", "$69.23", "🟢 -3.74%"),
        ("10Y美债收益率", "4.369%", "🟢 -2.5bp"),
        ("美元指数", "101.36", "🟢 -0.12%"),
    ]),
    ("加密货币", [
        ("BTC", "$59,893", "🟢 -0.8%"),
    ]),
]

fig, ax = plt.subplots(figsize=(11, 7))
fig.patch.set_facecolor('#f8f9fa')
ax.set_facecolor('#ffffff')
ax.set_xlim(0, 1)
ax.set_ylim(0, 1)
ax.axis('off')

y = 0.96
for section_title, items in sections:
    ax.text(0.03, y, f"▌ {section_title}", fontproperties=prop, fontsize=12, fontweight='bold', color='#1a1a2e')
    y -= 0.055
    for name, price, change in items:
        ax.text(0.06, y, name, fontproperties=prop, fontsize=11, color='#333')
        ax.text(0.42, y, price, fontproperties=prop, fontsize=11, color='#333')
        color = "#27ae60" if "🟢" in change else "#e74c3c"
        ax.text(0.68, y, change, fontproperties=prop, fontsize=11, color=color, fontweight='bold')
        y -= 0.07
    y -= 0.01

ax.axhline(y=0.97, xmin=0.02, xmax=0.98, color='#cccccc', linewidth=0.8)
plt.title("国际市场核心资产收盘数据 (2026/06/26 周五 美股)", fontsize=14, fontproperties=prop, pad=14)
plt.tight_layout()

output_path = os.path.join(output_dir, "2026-06-27-morning.png")
plt.savefig(output_path, dpi=300, bbox_inches='tight')
plt.close()
print(f"Chart saved to {output_path}")
