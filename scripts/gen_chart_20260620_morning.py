import matplotlib.pyplot as plt
import matplotlib.font_manager as fm
import os

# Create directory if not exists
output_dir = "/Users/jxy/Documents/Project/finance-auto-gen/images/charts/"
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

# Data for the chart (Saturday Morning Overview - Friday Market Close / Holiday)
assets = [
    "S&P 500", "Dow Jones", "Nasdaq", 
    "SpaceX (SPCX)", "US 10Y Yield", "Brent Crude", 
    "Spot Gold", "Bitcoin (BTC)"
]
prices = [
    "7,500.58", "51,564.70", "26,517.93",
    "178.60", "4.46%", "$80.04", 
    "$4,126.50", "$63,018.00"
]
changes = [
    "休市 (0.00%)", "休市 (0.00%)", "休市 (0.00%)",
    "休市 (0.00%)", "休市 (0.00%)", "上涨 (+2.73%)",
    "下跌 (-1.84%)", "下跌 (-2.18%)"
]
colors = ["gray", "gray", "gray", "gray", "gray", "red", "green", "green"]

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

plt.title("隔夜核心数据与宏观指标 (2026/06/20 早盘 - 美股休市特辑)", fontsize=16, fontproperties=prop, pad=20)
plt.tight_layout()

# Save the plot
output_path = os.path.join(output_dir, "2026-06-20-morning.png")
plt.savefig(output_path, dpi=300, bbox_inches='tight')
plt.close()
print(f"Chart saved to {output_path}")
