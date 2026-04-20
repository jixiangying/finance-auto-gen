import matplotlib.pyplot as plt
from matplotlib import font_manager
import os

# Data
indices = ['上证指数', '深证成指', '创业板指', '恒生指数', '恒生科技']
prices = [4082.13, 14966.75, 3677.58, 26361.07, 5065.63]
changes = [0.76, 0.55, -0.02, 0.77, 0.46]

# Set font for macOS
font_path = '/System/Library/Fonts/STHeiti Medium.ttc'
prop = font_manager.FontProperties(fname=font_path)
plt.rcParams['font.family'] = prop.get_name()
plt.rcParams['axes.unicode_minus'] = False

fig, ax = plt.subplots(figsize=(10, 6))
colors = ['#ff4d4d' if c > 0 else '#2ecc71' for c in changes]

bars = ax.bar(indices, changes, color=colors)

# Add value labels
for bar, change, price in zip(bars, changes, prices):
    height = bar.get_height()
    label = f'{price:.2f}\n({"+" if change > 0 else ""}{change:.2f}%)'
    ax.text(bar.get_x() + bar.get_width()/2., height + (0.02 if height > 0 else -0.05),
            label, ha='center', va='bottom' if height > 0 else 'top', fontproperties=prop)

ax.set_title('2026年4月20日 主要指数收盘表现', fontproperties=prop, fontsize=16)
ax.set_ylabel('涨跌幅 (%)', fontproperties=prop)
ax.axhline(0, color='black', linewidth=0.8)
ax.set_xticklabels(indices, fontproperties=prop)

# Add grid
ax.grid(axis='y', linestyle='--', alpha=0.7)

plt.tight_layout()
output_dir = 'images/charts'
os.makedirs(output_dir, exist_ok=True)
plt.savefig(os.path.join(output_dir, '2026-04-20-evening.png'), dpi=300)
print("Chart generated successfully.")
