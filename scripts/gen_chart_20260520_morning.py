import matplotlib.pyplot as plt
import matplotlib.font_manager as fm
import os

# Font setup for macOS
font_path = '/System/Library/Fonts/STHeiti Medium.ttc'
if not os.path.exists(font_path):
    font_path = '/System/Library/Fonts/PingFang.ttc'

prop = fm.FontProperties(fname=font_path)

# Data for US Indices (May 19, 2026)
indices = ['S&P 500', 'Nasdaq', 'Dow Jones']
prices = [7353.61, 25870.71, 49363.88]
changes = [-0.67, -0.84, -0.65]

fig, ax = plt.subplots(figsize=(10, 6), facecolor='#f0f0f0')
ax.set_facecolor('#ffffff')

colors = ['#2ca02c' if c > 0 else '#d62728' for c in changes]

bars = ax.bar(indices, changes, color=colors, alpha=0.8)

# Add value labels
for bar, change, price in zip(bars, changes, prices):
    yval = bar.get_height()
    ax.text(bar.get_x() + bar.get_width()/2, yval - 0.05 if yval < 0 else yval + 0.05, 
            f'{change}%', ha='center', va='bottom' if yval > 0 else 'top', 
            fontsize=12, fontweight='bold', fontproperties=prop)
    ax.text(bar.get_x() + bar.get_width()/2, yval - 0.15 if yval < 0 else yval + 0.15, 
            f'({price:,.2f})', ha='center', va='bottom' if yval > 0 else 'top', 
            fontsize=10, fontproperties=prop)

ax.set_title('美股核心指数表现 (2026-05-19)', fontproperties=prop, fontsize=18, fontweight='bold', pad=20)
ax.set_ylabel('涨跌幅 (%)', fontproperties=prop, fontsize=14)
ax.axhline(0, color='black', linewidth=0.8)

# Set tick fonts
ax.set_xticklabels(indices, fontproperties=prop, fontsize=12)
for label in ax.get_yticklabels():
    label.set_fontproperties(prop)

plt.tight_layout()

# Save output
output_dir = 'images/charts'
os.makedirs(output_dir, exist_ok=True)
plt.savefig(f'{output_dir}/2026-05-20-morning.png', dpi=300)
print(f"Chart saved to {output_dir}/2026-05-20-morning.png")
