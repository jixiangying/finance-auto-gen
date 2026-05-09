import matplotlib.pyplot as plt
import matplotlib.font_manager as fm
import os

# Set up Chinese font for macOS
font_path = '/System/Library/Fonts/STHeiti Medium.ttc'
if not os.path.exists(font_path):
    font_path = '/System/Library/Fonts/PingFang.ttc'
prop = fm.FontProperties(fname=font_path)

plt.rcParams['font.sans-serif'] = [prop.get_name()]
plt.rcParams['axes.unicode_minus'] = False

# Data (Friday May 8 US Market Close)
labels = ['S&P 500', 'Nasdaq', 'Dow Jones', 'Brent Oil', 'Bitcoin', 'Gold']
values = [7398.93, 26247.08, 49609.16, 101.16, 80140.17, 4710.00]
changes = [0.84, 1.71, 0.02, 1.40, 0.03, 0.45]

# Colors: Red for Up, Green for Down (Chinese Style)
colors = ['#ff4d4d' if c > 0 else '#2ecc71' for c in changes]

fig, ax = plt.subplots(figsize=(10, 6), dpi=100)
fig.patch.set_facecolor('#f9f9f9')
ax.set_facecolor('#ffffff')

bars = ax.bar(labels, changes, color=colors, edgecolor='none', alpha=0.8)

# Add value labels on bars
for bar, change, val in zip(bars, changes, values):
    height = bar.get_height()
    label_y = height + 0.05 if height > 0 else height - 0.1
    ax.text(bar.get_x() + bar.get_width()/2., label_y,
            f'{val:,.2f}\n({change:+.2f}%)',
            ha='center', va='bottom' if height > 0 else 'top',
            fontproperties=prop, fontsize=10, fontweight='bold',
            color='#333333')

ax.set_title('全球核心资产行情表现 (2026-05-09 晨间)', fontproperties=prop, fontsize=16, pad=20)
ax.axhline(0, color='black', linewidth=0.8)

# Remove spines
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)

# Set tick fonts
ax.set_xticklabels(labels, fontproperties=prop, fontsize=11)

plt.tight_layout()

# Save the plot
output_dir = 'images/charts/'
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

output_path = os.path.join(output_dir, '2026-05-09-morning.png')
plt.savefig(output_path, bbox_inches='tight')
print(f"Chart saved to {output_path}")
