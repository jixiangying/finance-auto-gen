import matplotlib.pyplot as plt
import matplotlib.font_manager as fm
import os

# Create directory if not exists
output_dir = "/Users/jxy/Documents/Project/finance-auto-gen/images/charts/"
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

# Data for the chart (Friday Evening Overview - Holiday Mode)
assets = [
    "富时中国A50期指", "离岸人民币 (USD/CNH)", "伦敦现货金", 
    "比特币 (BTC)", "布伦特原油", "德国DAX指数"
]
prices = [
    "15,695.91", "6.7784", "$4,126.50",
    "$63,018.00", "$80.04", "25,196.72"
]
changes = [
    "下跌 (-0.32%)", "微贬 (-0.09%)", "大跌 (-1.84%)",
    "下跌 (-2.18%)", "大涨 (+2.73%)", "上涨 (+0.37%)"
]
colors = ["green", "green", "green", "green", "red", "red"]

# Font setting for macOS
font_path = "/System/Library/Fonts/STHeiti Medium.ttc"
if not os.path.exists(font_path):
    font_path = "/System/Library/Fonts/PingFang.ttc"
prop = fm.FontProperties(fname=font_path)

# Plotting
fig, ax = plt.subplots(figsize=(10, 6))
fig.patch.set_facecolor('#f4f4f4')
ax.set_facecolor('#ffffff')

y_pos = range(len(assets))
bars = ax.barh(y_pos, [1]*len(assets), color='white', edgecolor='#dddddd')

# Add text labels
for i, (asset, price, change, color) in enumerate(zip(assets, prices, changes, colors)):
    ax.text(0.05, i, asset, va='center', ha='left', fontsize=13, fontproperties=prop, fontweight='bold')
    ax.text(0.4, i, price, va='center', ha='left', fontsize=13, fontproperties=prop)
    if color == "red":
        c = "#ff4d4f"
    elif color == "green":
        c = "#52c41a"
    else:
        c = "#8c8c8c"
    ax.text(0.7, i, change, va='center', ha='left', fontsize=13, fontproperties=prop, color=c, fontweight='bold')

ax.set_yticks([])
ax.set_xticks([])
ax.set_xlim(0, 1)
ax.invert_yaxis()
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
ax.spines['bottom'].set_visible(False)
ax.spines['left'].set_visible(False)

plt.title("离岸资产与全球商品表现 (2026/06/19 端午假期复盘)", fontsize=16, fontproperties=prop, pad=20)
plt.tight_layout()

# Save the plot
output_path = os.path.join(output_dir, "2026-06-19-evening.png")
plt.savefig(output_path, dpi=300, bbox_inches='tight')
plt.close()
print(f"Chart saved to {output_path}")
