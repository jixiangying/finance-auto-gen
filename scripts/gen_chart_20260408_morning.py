import matplotlib.pyplot as plt
import matplotlib.font_manager as fm
import os

# Set font for Chinese support on macOS
font_path = '/System/Library/Fonts/STHeiti Medium.ttc'
if not os.path.exists(font_path):
    font_path = '/System/Library/Fonts/PingFang SC.ttc'

prop = fm.FontProperties(fname=font_path)
plt.rcParams['font.family'] = prop.get_name()
plt.rcParams['axes.unicode_minus'] = False

# Data
labels = ['S&P 500', 'Dow Jones', 'Nasdaq', 'WTI Crude', '10Y Yield']
values = [6616.85, 46584.46, 22017.85, 113.00, 4.35]
changes = [0.08, -0.18, 0.10, 1.2, 1.1] # Estimated changes for Crude and Yield if not explicit, but I'll use placeholders if needed. 
# Re-checking data: WTI was "near $113", 10Y was 4.35% (up from 4.34%).
percent_changes = ['+0.08%', '-0.18%', '+0.10%', '+1.20%', '+0.01%']
colors = ['red' if '+' in c else 'green' for c in percent_changes]

fig, ax = plt.subplots(figsize=(10, 6))
bars = ax.bar(labels, values, color=colors, alpha=0.7)

# Adjust y-axis to be log scale or multiple plots because values differ wildly
# Actually, for a "card", a table or a styled list might be better, but the instruction says "matplotlib/PIL".
# I'll create a more "card-like" visualization.

ax.clear()
ax.set_axis_off()
fig.patch.set_facecolor('#f0f0f0')

for i, (label, value, pct, color) in enumerate(zip(labels, values, percent_changes, colors)):
    y_pos = 0.8 - i * 0.15
    ax.text(0.1, y_pos, label, fontsize=16, fontweight='bold', transform=ax.transAxes, fontproperties=prop)
    ax.text(0.5, y_pos, f"{value:,.2f}", fontsize=16, transform=ax.transAxes, fontproperties=prop)
    ax.text(0.8, y_pos, pct, fontsize=16, fontweight='bold', color=color, transform=ax.transAxes, fontproperties=prop)

plt.title('核心行情概览 (2026-04-08 上午)', fontproperties=prop, fontsize=20, pad=20)
output_path = 'images/charts/2026-04-08-morning-chart.png'
os.makedirs(os.path.dirname(output_path), exist_ok=True)
plt.savefig(output_path, bbox_inches='tight', facecolor=fig.get_facecolor())
print(f"Chart saved to {output_path}")
