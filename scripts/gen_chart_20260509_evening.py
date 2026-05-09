
import matplotlib.pyplot as plt
from matplotlib import font_manager
import os

# Data for 2026-05-09 Weekend Review
# Index: [Friday Change %, Weekly Change %]
labels = ['标普500', '纳斯达克', '上证指数', '恒生指数', '布伦特原油']
fri_changes = [0.84, 1.71, 0.00, -0.87, 1.40]
week_changes = [2.63, 5.44, 1.65, 2.51, 5.20]

# Prices for labeling
prices = ['7398.93', '26247.08', '4179.95', '26393.71', '$101.16']

# Colors: Red for up, Green for down (Global/A-share mixed, will use Red for >0)
fri_colors = ['#e74c3c' if c >= 0 else '#27ae60' for c in fri_changes]
week_colors = ['#c0392b' if c >= 0 else '#1e8449' for c in week_changes]

# Font setup for macOS
font_path = '/System/Library/Fonts/STHeiti Medium.ttc'
if not os.path.exists(font_path):
    font_path = '/System/Library/Fonts/PingFang.ttc'
prop = font_manager.FontProperties(fname=font_path)

plt.rcParams['font.sans-serif'] = [prop.get_name()]
plt.rcParams['axes.unicode_minus'] = False

fig, ax = plt.subplots(figsize=(12, 7), dpi=150)
fig.patch.set_facecolor('#fdfcf0') # Warm background for weekend review
ax.set_facecolor('#fdfcf0')

x = range(len(labels))
width = 0.35

rects1 = ax.bar([i - width/2 for i in x], fri_changes, width, label='周五涨跌 (%)', color=fri_colors, alpha=0.6)
rects2 = ax.bar([i + width/2 for i in x], week_changes, width, label='全周累计 (%)', color=week_colors, alpha=0.9)

# Add text labels for Weekly changes
for i, rect in enumerate(rects2):
    height = rect.get_height()
    ax.text(rect.get_x() + rect.get_width()/2., height + 0.1,
            f'{prices[i]}\n({week_changes[i]:+.2f}%)',
            ha='center', va='bottom', fontsize=9, fontweight='bold', fontproperties=prop)

# Add text labels for Friday changes
for i, rect in enumerate(rects1):
    height = rect.get_height()
    ax.text(rect.get_x() + rect.get_width()/2., height + 0.1 if height >=0 else height - 0.4,
            f'{fri_changes[i]:+.2f}%',
            ha='center', va='bottom' if height >=0 else 'top', fontsize=8, fontproperties=prop)

ax.set_title('核心资产本周表现回顾 (2026-05-04 ~ 05-08)', fontsize=18, pad=25, fontproperties=prop)
ax.set_ylabel('涨跌幅 (%)', fontproperties=prop)
ax.set_xticks(x)
ax.set_xticklabels(labels, fontproperties=prop)
ax.legend(prop=prop)

# Grid
ax.yaxis.grid(True, linestyle='--', alpha=0.5)
ax.axhline(0, color='black', linewidth=0.8) # Baseline

# Remove spines
for spine in ['top', 'right']:
    ax.spines[spine].set_visible(False)

# Set tick fonts
for label in ax.get_yticklabels():
    label.set_fontproperties(prop)

plt.tight_layout()
output_path = 'images/charts/2026-05-09-evening.png'
os.makedirs(os.path.dirname(output_path), exist_ok=True)
plt.savefig(output_path, facecolor=fig.get_facecolor())
print(f'Chart saved to {output_path}')
