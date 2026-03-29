
import matplotlib.pyplot as plt
from matplotlib import font_manager
import os

# Data
labels = ['S&P 500', 'Nasdaq', 'Dow Jones', 'Gold', 'Brent Oil', 'Bitcoin']
prices = ['6,368.85', '20,948.36', '45,166.64', '4,515.26', '113.00', '66,800']
changes = [-1.67, -2.15, -1.73, 3.2, 7.0, 0.5]
colors = ['#27ae60' if c > 0 else '#e74c3c' for c in changes]
change_labels = [f'{"+" if c > 0 else ""}{c}%' for c in changes]

# Font setup for macOS
font_path = '/System/Library/Fonts/STHeiti Medium.ttc'
if not os.path.exists(font_path):
    font_path = '/System/Library/Fonts/PingFang.ttc'
prop = font_manager.FontProperties(fname=font_path)

plt.rcParams['font.sans-serif'] = [prop.get_name()]
plt.rcParams['axes.unicode_minus'] = False

fig, ax = plt.subplots(figsize=(10, 6), dpi=150)
fig.patch.set_facecolor('#f8f9fa')
ax.set_facecolor('#f8f9fa')

bars = ax.bar(labels, [abs(c) for c in changes], color=colors, alpha=0.8)

# Add text labels
for i, bar in enumerate(bars):
    height = bar.get_height()
    ax.text(bar.get_x() + bar.get_width()/2., height + 0.1,
            f'{prices[i]}\n({change_labels[i]})',
            ha='center', va='bottom', fontsize=10, fontweight='bold', fontproperties=prop)

ax.set_title('全球资产表现回顾 (2026-03-29)', fontsize=16, pad=20, fontproperties=prop)
ax.set_ylabel('涨跌幅绝对值 (%)', fontproperties=prop)
ax.set_ylim(0, max([abs(c) for c in changes]) + 2)

# Grid
ax.yaxis.grid(True, linestyle='--', alpha=0.7)
ax.set_axisbelow(True)

# Remove spines
for spine in ['top', 'right']:
    ax.spines[spine].set_visible(False)

# Set tick fonts
ax.set_xticklabels(labels, fontproperties=prop)
for label in ax.get_yticklabels():
    label.set_fontproperties(prop)

plt.tight_layout()
output_path = 'images/charts/2026-03-29-morning-chart.png'
os.makedirs(os.path.dirname(output_path), exist_ok=True)
plt.savefig(output_path, facecolor=fig.get_facecolor())
print(f'Chart saved to {output_path}')
