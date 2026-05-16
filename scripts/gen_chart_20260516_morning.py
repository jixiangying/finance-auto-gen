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

# Data
indices = ['S&P 500', 'Nasdaq', 'Dow Jones', 'Bitcoin', 'Gold', 'Brent Oil']
changes = [-1.24, -1.54, -1.07, -2.6, -2.1, 2.36]
colors = ['green' if x < 0 else 'red' for x in changes]

fig, ax = plt.subplots(figsize=(10, 6))
bars = ax.bar(indices, changes, color=colors)

# Add value labels
for bar in bars:
    yval = bar.get_height()
    ax.text(bar.get_x() + bar.get_width()/2, yval + (0.1 if yval > 0 else -0.3), f'{yval}%', ha='center', va='bottom' if yval > 0 else 'top', fontweight='bold')

ax.set_title('全球核心资产涨跌幅 (2026-05-15 收盘)', fontproperties=prop, fontsize=16)
ax.set_ylabel('涨跌幅 (%)', fontproperties=prop)
ax.axhline(0, color='black', linewidth=0.8)

# Set font for tick labels
ax.set_xticklabels(indices, fontproperties=prop)

# Save the chart
output_path = 'images/charts/20260516_morning.png'
os.makedirs(os.path.dirname(output_path), exist_ok=True)
plt.savefig(output_path, dpi=300, bbox_inches='tight')
print(f"Chart saved to {output_path}")
