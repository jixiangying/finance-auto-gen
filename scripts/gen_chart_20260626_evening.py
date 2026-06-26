import matplotlib.pyplot as plt
import matplotlib.font_manager as fm
import os

output_dir = "/Users/jxy/Documents/Project/finance-auto-gen/images/charts/"
os.makedirs(output_dir, exist_ok=True)

font_path = "/System/Library/Fonts/STHeiti Medium.ttc"
if not os.path.exists(font_path):
    font_path = "/System/Library/Fonts/PingFang.ttc"
prop = fm.FontProperties(fname=font_path)

assets = ["上证指数", "深证成指", "创业板指", "科创50", "恒生指数", "恒生科技"]
prices = ["4,027.26", "15,782.22", "4,194.21", "2,032.28", "22,671.86", "N/A"]
changes = ["大跌 (-2.26%)", "大跌 (-3.44%)", "暴跌 (-4.07%)", "下跌 (-1.65%)", "下跌 (-1.76%)", "下跌"]
colors  = ["green", "green", "green", "green", "green", "green"]

fig, ax = plt.subplots(figsize=(10, 6))
fig.patch.set_facecolor('#f4f4f4')
ax.set_facecolor('#ffffff')

ax.barh(range(len(assets)), [1]*len(assets), color='white', edgecolor='#dddddd')

for i, (asset, price, change, color) in enumerate(zip(assets, prices, changes, colors)):
    ax.text(0.05, i, asset, va='center', ha='left', fontsize=13, fontproperties=prop, fontweight='bold')
    ax.text(0.42, i, price, va='center', ha='left', fontsize=13, fontproperties=prop)
    c = "#52c41a" if color == "green" else "#ff4d4f"
    ax.text(0.70, i, change, va='center', ha='left', fontsize=13, fontproperties=prop, color=c, fontweight='bold')

ax.set_yticks([])
ax.set_xticks([])
ax.set_xlim(0, 1)
ax.invert_yaxis()
for spine in ax.spines.values():
    spine.set_visible(False)

plt.title("今日A股/港股核心指数收盘数据 (2026/06/26 晚报)", fontsize=15, fontproperties=prop, pad=18)
plt.tight_layout()

output_path = os.path.join(output_dir, "2026-06-26-evening.png")
plt.savefig(output_path, dpi=300, bbox_inches='tight')
plt.close()
print(f"Chart saved to {output_path}")
