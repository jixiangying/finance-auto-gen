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
    {"name": "上证指数", "price": "4,057.78", "change": "-26.19", "pct": "-0.64%", "up": False},
    {"name": "深证成指", "price": "15,661.57", "change": "-43.14", "pct": "-0.27%", "up": False},
    {"name": "创业板指", "price": "4,088.88", "change": "-34.11", "pct": "-0.83%", "up": False},
    {"name": "恒生指数", "price": "25,253.40", "change": "-379.81", "pct": "-1.48%", "up": False},
    {"name": "恒生科技指数", "price": "4,975.36", "change": "-81.61", "pct": "-1.61%", "up": False},
    {"name": "两市成交额", "price": "2.76万亿", "change": "-0.37万亿", "pct": "-11.82%", "up": False},
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

output_path = os.path.join(output_dir, '2026-06-04-evening.png')
plt.savefig(output_path, dpi=300, bbox_inches='tight')
print(f"Chart saved to {output_path}")
