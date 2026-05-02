import matplotlib.pyplot as plt
import matplotlib.font_manager as fm
import os

# Set font for Chinese characters (macOS)
font_path = '/System/Library/Fonts/STHeiti Medium.ttc'
if not os.path.exists(font_path):
    font_path = '/System/Library/Fonts/PingFang.ttc'
prop = fm.FontProperties(fname=font_path)

plt.rcParams['font.family'] = prop.get_name()
plt.rcParams['axes.unicode_minus'] = False

# Data for 2026-05-02 Morning (Friday Close / Saturday Morning)
assets = [
    'S&P 500', 'Nasdaq', 'Dow Jones', 
    'Bitcoin (BTC)', 'WTI Crude', 'A50 Futures', 'Gold'
]
prices = [
    '7,230.12', '25,114.44', '49,499.27', 
    '$78,391', '$103.00', '15,654.0', '$4,612.50'
]
changes = [
    0.29, 0.89, -0.31, 
    1.46, -2.83, -0.75, -0.15
]

# Define colors: Red for Up (positive change), Green for Down (negative change)
# In Chinese market convention, red is usually up, green is down.
colors = ['#FF3131' if c > 0 else '#00D100' for c in changes]

fig, ax = plt.subplots(figsize=(10, 6))
fig.patch.set_facecolor('#ffffff')
ax.set_facecolor('#ffffff')

y_pos = range(len(assets))
# Use absolute values for bar lengths, colors will indicate direction
bars = ax.barh(y_pos, [abs(c) for c in changes], color=colors, height=0.6)

# Add asset names and prices on the left
for i, (asset, price, change) in enumerate(zip(assets, prices, changes)):
    sign = '+' if change > 0 else ''
    text = f"{asset}\n{price} ({sign}{change}%)"
    # Position text to the left of the y-axis
    ax.text(-0.1, i, text, va='center', ha='right', fontproperties=prop, fontsize=11, fontweight='bold')

# Adjust limits and hide axes
ax.set_xlim(0, max([abs(c) for c in changes]) + 1.0)
ax.set_yticks([])
ax.set_xticks([])
for spine in ax.spines.values():
    spine.set_visible(False)

plt.title('全球市场复盘：纳指突破2.5万点，苹果财报与和平预期共振 (2026-05-02)', fontproperties=prop, fontsize=16, pad=25)

# Add a subtle grid
ax.grid(axis='x', linestyle='--', alpha=0.3)

# Save the plot
output_dir = 'images/charts'
os.makedirs(output_dir, exist_ok=True)
output_path = os.path.join(output_dir, '2026-05-02-morning-chart.png')
plt.savefig(output_path, bbox_inches='tight', dpi=150, facecolor=fig.get_facecolor())
plt.close()

print(f"Chart saved to {output_path}")
