import matplotlib.pyplot as plt
import matplotlib.font_manager as fm
import os

# Create directory if not exists
output_dir = "/Users/jxy/Documents/Project/finance-auto-gen/images/charts/"
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

# Data for the chart (Monday Morning Overview - Weekly Cumulative Change / Closes)
assets = [
    "S&P 500", "Dow Jones", "Nasdaq", 
    "SSE Composite", "Chinext", "Hang Seng",
    "WTI Crude", "Spot Gold", "Bitcoin (BTC)"
]
prices = [
    "7,431.46", "51,202.26", "25,888.84",
    "4,031.51", "3,830.35", "24,718.10",
    "$84.29", "$4,216.00", "$63,552.30"
]
changes = [
    "周涨 +0.65%", "周涨 +0.66%", "周涨 +0.70%",
    "周涨 +0.09%", "周跌 -3.22%", "周跌 -0.98%",
    "周跌 -6.90%", "周跌 -2.66%", "周涨 +6.27%"
]
# Color coding: red for up, green for down
colors = ["red", "red", "red", "red", "green", "green", "green", "green", "red"]

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

plt.title("本周全球核心资产收盘表现回顾 (2026/06/15 周一早盘)", fontsize=16, fontproperties=prop, pad=20)
plt.tight_layout()

# Save the plot
output_path = os.path.join(output_dir, "2026-06-15-morning.png")
plt.savefig(output_path, dpi=300, bbox_inches='tight')
print(f"Chart saved to {output_path}")
