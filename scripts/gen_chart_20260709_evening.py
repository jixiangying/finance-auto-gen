import matplotlib.pyplot as plt
from matplotlib import font_manager
import os

# Data (2026-07-09 Thursday Closing)
labels = ['上证指数', '深证成指', '创业板指', '科创50']
prices = ['4036.59', '15398.73', '4018.17', '2185.83']
changes = [1.65, 3.07, 4.49, 8.41]
colors = ['#e74c3c' if c > 0 else '#27ae60' for c in changes]  # Red for up, green for down in China
change_labels = [('+' if c > 0 else '') + f'{c}%' for c in changes]

# Font setup for macOS
font_path = '/System/Library/Fonts/STHeiti Medium.ttc'
if not os.path.exists(font_path):
    font_path = '/System/Library/Fonts/PingFang.ttc'
prop = font_manager.FontProperties(fname=font_path)

plt.rcParams['font.sans-serif'] = [prop.get_name()]
plt.rcParams['axes.unicode_minus'] = False

fig, ax = plt.subplots(figsize=(10, 6), dpi=150)
fig.patch.set_facecolor('#1a1a2e')
ax.set_facecolor('#16213e')

bars = ax.bar(labels, changes, color=colors, alpha=0.85, edgecolor='white', linewidth=0.5)

# Add line at y=0
ax.axhline(0, color='white', linewidth=0.8, alpha=0.5)

# Add text labels
for i, bar in enumerate(bars):
    height = bar.get_height()
    if height >= 0:
        va = 'bottom'
        offset = 0.1
    else:
        va = 'top'
        offset = -0.1
    ax.text(bar.get_x() + bar.get_width()/2., height + offset,
            f'{prices[i]}\n({change_labels[i]})',
            ha='center', va=va, fontsize=10, fontweight='bold',
            fontproperties=prop, color='white')

ax.set_title('国内核心指数收盘表现 (2026-07-09)', fontsize=16, pad=20, fontproperties=prop, color='white')
ax.set_ylabel('涨跌幅 (%)', fontproperties=prop, color='#aaaaaa')

# Set limits with some padding
y_max = max(changes)
y_min = min(changes)
ax.set_ylim(0, y_max + 1.0)

# Grid
ax.yaxis.grid(True, linestyle='--', alpha=0.4, color='#555555')
ax.set_axisbelow(True)

# Remove spines
for spine in ['top', 'right']:
    ax.spines[spine].set_visible(False)
for spine in ['bottom', 'left']:
    ax.spines[spine].set_color('#555555')

ax.tick_params(colors='#aaaaaa')

# Set tick fonts
ax.set_xticks(range(len(labels)))
ax.set_xticklabels(labels, fontproperties=prop, color='white')
for label in ax.get_yticklabels():
    label.set_fontproperties(prop)

plt.tight_layout()
output_path = 'images/charts/2026-07-09-evening.png'
os.makedirs(os.path.dirname(output_path), exist_ok=True)
plt.savefig(output_path, facecolor=fig.get_facecolor())
plt.close()
print(f'Chart saved to {output_path}')
