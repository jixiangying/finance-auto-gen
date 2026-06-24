import matplotlib.pyplot as plt
import matplotlib.font_manager as fm
import os

# Create directory if not exists
output_dir = "/Users/jxy/Documents/Project/finance-auto-gen/images/charts/"
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

# Data for the chart (Wednesday Morning Overview - Market Status after Close of June 23)
assets = [
    "S&P 500", "Dow Jones", "Nasdaq", "SpaceX (SPCX)",
    "Brent Crude", "Spot Gold", "Bitcoin (BTC)", "US 10-Yr Yield",
    "SSE Composite", "Chinext", "Hang Seng"
]
prices = [
    "7,365.46", "51,666.84", "25,587.04", "156.11",
    "$77.08", "$4,101.04", "$62,418.00", "4.465%",
    "4,106.25", "4,192.19", "23,336.28"
]
changes = [
    "隔夜 -1.44%", "隔夜 -0.09%", "隔夜 -2.21%", "隔夜 +0.98%",
    "隔夜 -2.07%", "隔夜 -2.30%", "隔夜 -3.01%", "隔夜 -4.2bp",
    "昨日 -1.37%", "昨日 -3.84%", "昨日 -1.82%"
]
# Color coding: red for up, green for down
colors = ["green", "green", "green", "red", "green", "green", "green", "green", "green", "green", "green"]

# Font setting for macOS
font_path = "/System/Library/Fonts/STHeiti Medium.ttc"
if not os.path.exists(font_path):
    font_path = "/System/Library/Fonts/PingFang.ttc"
prop = fm.FontProperties(fname=font_path)

# Plotting
fig, ax = plt.subplots(figsize=(10, 8.5))
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

plt.title("全球核心资产表现及早盘波动 (2026/06/24 周三早盘)", fontsize=16, fontproperties=prop, pad=20)
plt.tight_layout()

# Save the plot
output_path = os.path.join(output_dir, "2026-06-24-morning.png")
plt.savefig(output_path, dpi=300, bbox_inches='tight')
plt.close()
print(f"Chart saved to {output_path}")
