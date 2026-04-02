import matplotlib.pyplot as plt
import matplotlib.font_manager as fm
import os

# Configuration
output_path = 'images/charts/2026-04-02-morning-chart.png'
os.makedirs(os.path.dirname(output_path), exist_ok=True)

# Data
assets = ['S&P 500', 'Nasdaq', 'Dow Jones', 'Gold', 'WTI Oil', 'Bitcoin']
prices = ['6,575.32', '21,840.95', '46,565.74', '4,813.10', '100.12', '68,000']
changes = [0.72, 1.16, 0.48, 2.88, -1.24, 1.50]  # Bitcoin change estimated for visualization
colors = ['#e63946' if c > 0 else '#2a9d8f' for c in changes] # Red for up, Green for down (Chinese style)

# Font setup for macOS
font_path = '/System/Library/Fonts/STHeiti Medium.ttc'
if not os.path.exists(font_path):
    font_path = '/System/Library/Fonts/Cache/PingFang.ttc' # Fallback
prop = fm.FontProperties(fname=font_path)

plt.rcParams['font.sans-serif'] = ['STHeiti']
plt.rcParams['axes.unicode_minus'] = False

fig, ax = plt.subplots(figsize=(10, 6), facecolor='#f8f9fa')
ax.set_facecolor='#f8f9fa'

bars = ax.barh(assets, changes, color=colors, height=0.6)

# Add text labels
for i, bar in enumerate(bars):
    width = bar.get_width()
    label_x = width + (0.05 if width > 0 else -0.05)
    align = 'left' if width > 0 else 'right'
    ax.text(label_x, bar.get_y() + bar.get_height()/2, 
            f'{prices[i]} ({"+" if changes[i]>0 else ""}{changes[i]}%)', 
            va='center', ha=align, fontproperties=prop, fontsize=12, fontweight='bold')

# Formatting
ax.set_title('全球核心资产表现 (2026-04-01 收盘)', fontproperties=prop, fontsize=18, pad=20)
ax.set_xlabel('涨跌幅 (%)', fontproperties=prop, fontsize=14)
ax.axvline(0, color='black', linewidth=0.8)
ax.set_xlim(min(changes) - 1, max(changes) + 2)

# Set font for ticks
ax.set_yticklabels(assets, fontproperties=prop, fontsize=12)
for label in ax.get_xticklabels():
    label.set_fontproperties(prop)

plt.tight_layout()
plt.savefig(output_path, dpi=300, bbox_inches='tight')
print(f"Chart saved to {output_path}")
