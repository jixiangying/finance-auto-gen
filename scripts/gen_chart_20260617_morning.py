import matplotlib.pyplot as plt
import matplotlib.font_manager as fm
import os

# Create directory if not exists
output_dir = "/Users/jxy/Documents/Project/finance-auto-gen/images/charts/"
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

# Data for the chart (Wednesday Morning Overview - Tuesday Market Close)
assets = [
    "S&P 500", "Dow Jones", "Nasdaq", 
    "SpaceX (SPCX)", "US 10Y Yield", "WTI Crude", 
    "Spot Gold", "Bitcoin (BTC)"
]
prices = [
    "7,511.35", "51,999.67", "26,376.34",
    "201.68", "4.43%", "$76.05", 
    "$4,315.87", "$65,850.00"
]
changes = [
    "下跌 (-0.57%)", "大涨 (+0.64%)", "大跌 (-1.15%)",
    "暴涨 (+17.32%)", "下行 (-4 bp)", "暴跌 (-5.17%)",
    "微涨 (+0.28%)", "下跌 (-0.75%)"
]
colors = ["green", "red", "green", "red", "green", "green", "red", "green"]

# Font setting for macOS
font_path = "/System/Library/Fonts/STHeiti Medium.ttc"
if not os.path.exists(font_path):
    font_path = "/System/Library/Fonts/PingFang.ttc"
prop = fm.FontProperties(fname=font_path)

# Plotting
fig, ax = plt.subplots(figsize=(10, 7))
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

plt.title("隔夜核心数据与宏观指标 (2026/06/17 早盘)", fontsize=16, fontproperties=prop, pad=20)
plt.tight_layout()

# Save the plot
output_path = os.path.join(output_dir, "2026-06-17-morning.png")
plt.savefig(output_path, dpi=300, bbox_inches='tight')
plt.close()
print(f"Chart saved to {output_path}")
