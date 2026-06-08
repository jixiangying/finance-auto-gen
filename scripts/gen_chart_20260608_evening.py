import matplotlib.pyplot as plt
import matplotlib.patches as patches
import matplotlib.font_manager as fm
import os

# Path to a reliable Chinese font on macOS
font_path = '/System/Library/Fonts/STHeiti Medium.ttc'
if not os.path.exists(font_path):
    font_path = '/System/Library/Fonts/PingFang.ttc'
prop = fm.FontProperties(fname=font_path)
plt.rcParams['axes.unicode_minus'] = False

data = [
    {"name": "上证指数", "price": "3,959.34", "change": "-68.40", "pct": "-1.70%", "up": False},
    {"name": "深证成指", "price": "14,821.19", "change": "-493.51", "pct": "-3.22%", "up": False},
    {"name": "创业板指", "price": "3,811.79", "change": "-146.15", "pct": "-3.69%", "up": False},
    {"name": "恒生指数", "price": "24,657.06", "change": "-304.89", "pct": "-1.22%", "up": False},
    {"name": "恒生科技指数", "price": "4,755.91", "change": "-132.48", "pct": "-2.71%", "up": False},
    {"name": "两市成交额", "price": "2.79万亿", "change": "-0.28万亿", "pct": "-9.01%", "up": False},
]

fig, axes = plt.subplots(2, 3, figsize=(15, 8))
fig.patch.set_facecolor('#f4f4f4')

for i, ax in enumerate(axes.flatten()):
    item = data[i]
    color = '#e74c3c' if item['up'] else '#2ecc71'
    
    bg_color = '#ffffff'
    ax.set_facecolor(bg_color)
    
    # Draw card border
    rect = patches.Rectangle((0.05, 0.05), 0.9, 0.9, linewidth=1, edgecolor='#ddd', facecolor=bg_color, transform=ax.transAxes)
    ax.add_patch(rect)
    
    ax.text(0.5, 0.75, item['name'], ha='center', va='center', fontsize=20, fontweight='bold', fontproperties=prop, transform=ax.transAxes)
    ax.text(0.5, 0.50, item['price'], ha='center', va='center', fontsize=28, fontweight='bold', color='#333', fontproperties=prop, transform=ax.transAxes)
    
    change_text = f"{item['change']} ({item['pct']})"
    ax.text(0.5, 0.25, change_text, ha='center', va='center', fontsize=18, fontweight='bold', color=color, fontproperties=prop, transform=ax.transAxes)
    
    ax.axis('off')

plt.tight_layout(pad=3.0)

# Create output dir if not exists
output_dir = '/Users/jxy/Documents/Project/finance-auto-gen/images/charts/'
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

output_path = os.path.join(output_dir, '2026-06-08-evening.png')
plt.savefig(output_path, dpi=300, bbox_inches='tight')
print(f"Chart saved to {output_path}")
