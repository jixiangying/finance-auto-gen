import matplotlib.pyplot as plt
import matplotlib.font_manager as fm
import os

# Create directory if not exists
output_dir = "/Users/jxy/Documents/Project/finance-auto-gen/images/charts/"
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

# Data for the chart (Monday Evening Overview - Monday Market Close)
assets = [
    "上证指数", "深证成指", "创业板指", 
    "恒生指数", "恒生科技指数", "沪深两市成交额"
]
prices = [
    "4,096.47", "15,531.11", "4,033.53",
    "24,842.67", "4,765.46", "3.05万亿元"
]
changes = [
    "大涨 (+1.61%)", "狂飙 (+3.79%)", "暴涨 (+5.30%)",
    "上涨 (+0.50%)", "上涨 (+1.28%)", "微幅回落 (-5.86%)"
]
colors = ["red", "red", "red", "red", "red", "grey"]

# Font setting for macOS
font_path = "/System/Library/Fonts/STHeiti Medium.ttc"
if not os.path.exists(font_path):
    font_path = "/System/Library/Fonts/PingFang.ttc"
prop = fm.FontProperties(fname=font_path)

# Plotting
fig, ax = plt.subplots(figsize=(10, 5))
fig.patch.set_facecolor('#f4f4f4')
ax.set_facecolor('#ffffff')

y_pos = range(len(assets))
bars = ax.barh(y_pos, [1]*len(assets), color='white', edgecolor='#dddddd')

# Add text labels
for i, (asset, price, change, color) in enumerate(zip(assets, prices, changes, colors)):
    ax.text(0.05, i, asset, va='center', ha='left', fontsize=14, fontproperties=prop, fontweight='bold')
    ax.text(0.4, i, price, va='center', ha='left', fontsize=14, fontproperties=prop)
    if color == "red":
        c = "#ff4d4f"
    elif color == "green":
        c = "#52c41a"
    else:
        c = "#8c8c8c"
    ax.text(0.7, i, change, va='center', ha='left', fontsize=14, fontproperties=prop, color=c, fontweight='bold')

ax.set_yticks([])
ax.set_xticks([])
ax.set_xlim(0, 1)
ax.invert_yaxis()
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
ax.spines['bottom'].set_visible(False)
ax.spines['left'].set_visible(False)

plt.title("今日A股/港股核心数据与两市成交额 (2026/06/15 收盘)", fontsize=18, fontproperties=prop, pad=20)
plt.tight_layout()

# Save the plot
output_path = os.path.join(output_dir, "2026-06-15-evening.png")
plt.savefig(output_path, dpi=300, bbox_inches='tight')
print(f"Chart saved to {output_path}")
