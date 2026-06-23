import matplotlib.pyplot as plt
import matplotlib.font_manager as fm
import os

# Create directory if not exists
output_dir = "/Users/jxy/Documents/Project/finance-auto-gen/images/charts/"
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

# Data for the chart (Tuesday Morning Overview - Market Status after Close of June 22)
assets = [
    "S&P 500", "Dow Jones", "Nasdaq", "SpaceX (SPCX)",
    "SSE Composite", "Chinext", "Hang Seng",
    "Brent Crude", "Spot Gold", "Bitcoin (BTC)"
]
prices = [
    "7,472.79", "51,712.71", "26,166.60", "154.60",
    "4,163.10", "4,359.39", "23,768.52",
    "$78.71", "$4,197.41", "$64,352.00"
]
changes = [
    "隔夜 -0.37%", "隔夜 +0.29%", "隔夜 -1.32%", "隔夜 -13.44%",
    "昨日 +1.78%", "昨日 +2.52%", "昨日 -0.65%",
    "隔夜 -3.61%", "隔夜 +0.97%", "隔夜 +1.16%"
]
# Color coding: red for up, green for down
colors = ["green", "red", "green", "green", "red", "red", "green", "green", "red", "red"]

# Font setting for macOS
font_path = "/System/Library/Fonts/STHeiti Medium.ttc"
if not os.path.exists(font_path):
    font_path = "/System/Library/Fonts/PingFang.ttc"
prop = fm.FontProperties(fname=font_path)

# Plotting
fig, ax = plt.subplots(figsize=(10, 8))
fig.patch.set_facecolor('#f4f4f4')
ax.set_facecolor('#ffffff')

y_pos = range(len(assets))
bars = ax.barh(y_pos, [1]*len(assets), color='white', edgecolor='#dddddd')

# Add text labels
for i, (asset, price, change, color) in enumerate(zip(assets, prices, changes, colors)):
    ax.text(0.05, i, asset, va='center', ha='left', fontsize=13, fontproperties=prop, fontweight='bold')
    ax.text(0.4, i, price, va='center', ha='left', fontsize=13, fontproperties=prop)
    c = "#ff4d4f" if color == "red" else "#52c41a"
    ax.text(0.7, i, change, va='center', ha='left', fontsize=13, fontproperties=prop, color=c, fontweight='bold')

ax.set_yticks([])
ax.set_xticks([])
ax.set_xlim(0, 1)
ax.invert_yaxis()
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
ax.spines['bottom'].set_visible(False)
ax.spines['left'].set_visible(False)

plt.title("全球核心资产表现及早盘波动 (2026/06/23 周二早盘)", fontsize=16, fontproperties=prop, pad=20)
plt.tight_layout()

# Save the plot
output_path = os.path.join(output_dir, "2026-06-23-morning.png")
plt.savefig(output_path, dpi=300, bbox_inches='tight')
plt.close()
print(f"Chart saved to {output_path}")
