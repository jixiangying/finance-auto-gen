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
    {"name": "上证指数", "price": "3,987.01", "change": "-6.22", "pct": "-0.16%", "up": False},
    {"name": "深证成指", "price": "14,851.98", "change": "-102.12", "pct": "-0.68%", "up": False},
    {"name": "创业板指", "price": "3,811.25", "change": "-43.54", "pct": "-1.13%", "up": False},
    {"name": "恒生指数", "price": "24,249.29", "change": "-158.67", "pct": "-0.65%", "up": False},
    {"name": "恒生科技指数", "price": "4,655.74", "change": "-69.05", "pct": "-1.46%", "up": False},
    {"name": "两市成交额", "price": "2.575万亿", "change": "-693亿", "pct": "-2.62%", "up": False},
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

output_path = os.path.join(output_dir, '2026-06-11-evening.png')
plt.savefig(output_path, dpi=300, bbox_inches='tight')
print(f"Chart saved to {output_path}")
