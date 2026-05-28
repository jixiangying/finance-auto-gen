import matplotlib.pyplot as plt
import matplotlib.font_manager as fm
import os

# Font path for macOS
font_path = '/System/Library/Fonts/STHeiti Medium.ttc'
prop = fm.FontProperties(fname=font_path)

# Data
indices = ['上证指数', '深证成指', '创业板指', '恒生指数']
values = [4098.64, 15861.89, 4125.07, 24848.00]
changes = [0.12, 0.80, 1.96, -1.90]
colors = ['#ff4d4d' if c > 0 else '#2eb82e' for c in changes] # Red for up, Green for down

fig, ax = plt.subplots(figsize=(10, 6), dpi=100)
fig.patch.set_facecolor('#f8f9fa')
ax.set_facecolor('#f8f9fa')

bars = ax.bar(indices, changes, color=colors, edgecolor='white', linewidth=0.5)

# Add text labels
for bar, val, change in zip(bars, values, changes):
    height = bar.get_height()
    label_y = height + 0.1 if height > 0 else height - 0.2
    ax.text(bar.get_x() + bar.get_width()/2., label_y,
            f'{val:.2f}\n({"+" if change > 0 else ""}{change:.2f}%)',
            ha='center', va='bottom' if height > 0 else 'top', 
            fontproperties=prop, fontsize=12, fontweight='bold',
            color='#333333')

# Aesthetics
ax.axhline(0, color='black', linewidth=0.8)
ax.set_title('核心指数收盘表现 (2026-05-28)', fontproperties=prop, fontsize=16, pad=20)
ax.set_ylabel('涨跌幅 (%)', fontproperties=prop, fontsize=12)
ax.set_xticklabels(indices, fontproperties=prop, fontsize=12)

# Grid
ax.grid(axis='y', linestyle='--', alpha=0.6)
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)

plt.tight_layout()

# Save path
output_dir = 'images/charts'
if not os.path.exists(output_dir):
    os.makedirs(output_dir)
output_path = os.path.join(output_dir, '2026-05-28-evening-chart.png')
plt.savefig(output_path, bbox_inches='tight')
print(f"Chart saved to {output_path}")
