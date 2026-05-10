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

# Weekly Cumulative Data (Ending May 8, 2026)
labels = ['S&P 500', 'Nasdaq', 'Dow Jones', 'CSI 300', 'Hang Seng', 'Brent Oil', 'Gold', 'Bitcoin']
values = [7398.93, 26247.08, 49609.16, 4871.91, 26393.71, 101.29, 4715.85, 80221.00]
weekly_changes = [2.3, 4.5, 0.2, 1.34, 2.39, -6.0, 2.0, 3.7]

# Colors: Red for Up, Green for Down (Chinese Style)
colors = ['#ff4d4d' if c > 0 else '#2ecc71' for c in weekly_changes]

fig, ax = plt.subplots(figsize=(12, 7), dpi=100)
fig.patch.set_facecolor('#f9f9f9')
ax.set_facecolor('#ffffff')

bars = ax.bar(labels, weekly_changes, color=colors, edgecolor='none', alpha=0.8)

# Add value labels on bars
for bar, change, val in zip(bars, weekly_changes, values):
    height = bar.get_height()
    label_y = height + 0.2 if height > 0 else height - 0.5
    ax.text(bar.get_x() + bar.get_width()/2., label_y,
            f'{val:,.1f}\n({change:+.2f}%)',
            ha='center', va='bottom' if height > 0 else 'top',
            fontproperties=prop, fontsize=9, fontweight='bold',
            color='#333333')

ax.set_title('全球核心资产全周累计涨跌幅 (2026-05-04 至 2026-05-08)', fontproperties=prop, fontsize=18, pad=30)
ax.axhline(0, color='black', linewidth=0.8)

# Set Y axis label
ax.set_ylabel('周涨跌幅 (%)', fontproperties=prop, fontsize=12)

# Remove spines
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)

# Set tick fonts
ax.set_xticklabels(labels, fontproperties=prop, fontsize=11, rotation=15)

plt.tight_layout()

# Save the plot
output_dir = 'images/charts/'
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

output_path = os.path.join(output_dir, '2026-05-10-morning.png')
plt.savefig(output_path, bbox_inches='tight')
print(f"Chart saved to {output_path}")
