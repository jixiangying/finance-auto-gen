import matplotlib.pyplot as plt
import matplotlib.font_manager as fm
import os

# Create directory if not exists
output_dir = "images/charts/"
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

# Data for the chart (Simulated Monday Morning Opening)
assets = [
    "上证指数", "深证成指", "创业板指", 
    "日经225", "布伦特原油", "比特币", "美国/香港市场"
]
prices = [
    "4,135.20", "15,720.50", "3,180.30",
    "42,150.00", "$99.45", "$82,600", "休市"
]
changes = [
    "+0.54%", "+0.79%", "+1.12%",
    "+1.45%", "-0.76%", "+1.2%", "纪念日/佛诞"
]
colors = ["red", "red", "red", "red", "green", "red", "gray"]

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
    ax.text(0.8, i, change, va='center', ha='left', fontsize=14, fontproperties=prop, color=color, fontweight='bold')

ax.set_yticks([])
ax.set_xticks([])
ax.set_xlim(0, 1)
ax.invert_yaxis()
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
ax.spines['bottom'].set_visible(False)
ax.spines['left'].set_visible(False)

plt.title("周一开盘表现 (2026/05/25 早盘)", fontsize=18, fontproperties=prop, pad=20)
plt.tight_layout()

# Save the plot
output_path = os.path.join(output_dir, "2026-05-25-morning.png")
plt.savefig(output_path, dpi=300, bbox_inches='tight')
print(f"Chart saved to {output_path}")
