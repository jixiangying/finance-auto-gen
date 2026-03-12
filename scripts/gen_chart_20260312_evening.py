import matplotlib.pyplot as plt
import matplotlib.font_manager as fm
import os

# Set Chinese font for macOS
font_path = '/System/Library/Fonts/STHeiti Medium.ttc'
if not os.path.exists(font_path):
    font_path = '/System/Library/Fonts/PingFang.ttc'

prop = fm.FontProperties(fname=font_path)
plt.rcParams['axes.unicode_minus'] = False

# Data
labels = ['上证指数', '深证成指', '创业板指', '恒生指数', '恒生科技']
values = [4129.30, 14374.25, 3317.37, 25542.00, 5026.49]
changes = [-0.10, -0.63, -0.96, -1.38, -0.56]

# Create figure
fig, ax = plt.subplots(figsize=(10, 6), facecolor='#f4f4f4')
ax.set_facecolor('#f4f4f4')

# Determine colors
colors = ['#00ba50' if c < 0 else '#e11d48' for c in changes] # Green for down, Red for up

# Plot bars
bars = ax.barh(labels, [1]*len(labels), color=colors, height=0.6)

# Hide axes
ax.get_xaxis().set_visible(False)
ax.get_yaxis().set_visible(False)
for spine in ax.spines.values():
    spine.set_visible(False)

# Add text
for i, (label, val, chg) in enumerate(zip(labels, values, changes)):
    color = '#00ba50' if chg < 0 else '#e11d48'
    symbol = '▼' if chg < 0 else '▲'
    
    # Label
    ax.text(0.05, i, label, fontproperties=prop, fontsize=16, va='center', ha='left', color='#333333')
    
    # Value
    ax.text(0.45, i, f'{val:,.2f}', fontsize=16, va='center', ha='right', color='#333333', fontweight='bold')
    
    # Change
    ax.text(0.55, i, f'{symbol} {abs(chg):.2f}%', fontsize=16, va='center', ha='left', color=color, fontweight='bold')

# Title
ax.text(0.5, 5, '核心行情速览 (2026-03-12 收盘)', fontproperties=prop, fontsize=20, va='center', ha='center', fontweight='bold', color='#1a1a1a')

# Save
output_path = 'images/charts/2026-03-12-evening.png'
plt.tight_layout()
plt.savefig(output_path, dpi=300, bbox_inches='tight', facecolor='#f4f4f4')
print(f"Chart saved to {output_path}")
