import matplotlib.pyplot as plt
import matplotlib.font_manager as fm
import os

# Create directory if not exists
output_dir = "images/charts/"
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

# Data for the chart (Friday Morning Overview)
assets = [
    "S&P 500", "Dow Jones", "Nasdaq", 
    "US 10Y Yield", "WTI Crude", "Spot Gold", 
    "Bitcoin (BTC)"
]
prices = [
    "7,584.31", "51,561.93", "26,830.96",
    "4.46%", "$92.82", "$4,478.71", 
    "$62,580.00"
]
changes = [
    "Thursday Close (+0.41%)", "Record High (+1.73%)", "Broadcom Drag (-0.09%)",
    "Yield Decline (Prev 4.50%)", "Ceasefire Drop (-2.58%)", "Gold Rebound (+0.31%)",
    "ETF Outflow (-3.31%)"
]
# Color coding: red for up, green for down
colors = ["red", "red", "green", "green", "green", "red", "green"]

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
    ax.text(0.05, i, asset, va='center', ha='left', fontsize=14, fontproperties=prop, fontweight='bold')
    ax.text(0.4, i, price, va='center', ha='left', fontsize=14, fontproperties=prop)
    c = "#ff4d4f" if color == "red" else "#52c41a"
    ax.text(0.7, i, change, va='center', ha='left', fontsize=14, fontproperties=prop, color=c, fontweight='bold')

ax.set_yticks([])
ax.set_xticks([])
ax.set_xlim(0, 1)
ax.invert_yaxis()
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
ax.spines['bottom'].set_visible(False)
ax.spines['left'].set_visible(False)

plt.title("隔夜核心数据与宏观指标 (2026/06/05 早盘)", fontsize=18, fontproperties=prop, pad=20)
plt.tight_layout()

# Save the plot
output_path = os.path.join(output_dir, "2026-06-05-morning.png")
plt.savefig(output_path, dpi=300, bbox_inches='tight')
print(f"Chart saved to {output_path}")
