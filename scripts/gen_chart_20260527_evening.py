import matplotlib.pyplot as plt
import matplotlib.patches as patches
import matplotlib.font_manager as fm

# Path to a reliable Chinese font on macOS
font_path = '/System/Library/Fonts/STHeiti Medium.ttc'
prop = fm.FontProperties(fname=font_path)
plt.rcParams['axes.unicode_minus'] = False

data = [
    {"name": "上证指数", "price": "4093.73", "change": "-51.85", "pct": "-1.25%", "up": False},
    {"name": "深证成指", "price": "15736.47", "change": "-139.73", "pct": "-0.88%", "up": False},
    {"name": "创业板指", "price": "4045.77", "change": "+2.83", "pct": "+0.07%", "up": True},
    {"name": "恒生指数", "price": "25315.32", "change": "-284.13", "pct": "-1.10%", "up": False},
    {"name": "恒生科技", "price": "4901.76", "change": "-45.12", "pct": "-0.90%", "up": False},
    {"name": "A股总成交", "price": "3.24万亿", "change": "放量", "pct": "天量", "up": True},
]

fig, axes = plt.subplots(2, 3, figsize=(15, 8))
fig.patch.set_facecolor('#f4f4f4')

for i, ax in enumerate(axes.flatten()):
    item = data[i]
    # Instruction: "红色代表上涨 🔴，绿色代表下跌 🟢"
    color = '#e74c3c' if item['up'] else '#2ecc71'
    
    bg_color = '#ffffff'
    ax.set_facecolor(bg_color)
    
    # Draw card border
    rect = patches.Rectangle((0.05, 0.05), 0.9, 0.9, linewidth=1, edgecolor='#ddd', facecolor=bg_color, transform=ax.transAxes)
    ax.add_patch(rect)
    
    ax.text(0.5, 0.75, item['name'], ha='center', va='center', fontsize=20, fontweight='bold', fontproperties=prop, transform=ax.transAxes)
    ax.text(0.5, 0.50, item['price'], ha='center', va='center', fontsize=28, fontweight='bold', color='#333', fontproperties=prop if '万亿' in item['price'] else None, transform=ax.transAxes)
    
    change_text = f"{item['change']} ({item['pct']})"
    ax.text(0.5, 0.25, change_text, ha='center', va='center', fontsize=18, fontweight='bold', color=color, fontproperties=prop if '放量' in item['change'] else None, transform=ax.transAxes)
    
    ax.axis('off')

plt.tight_layout(pad=3.0)
plt.savefig('images/charts/2026-05-27-evening-chart.png', dpi=300, bbox_inches='tight')
print("Chart generated successfully with correct fonts.")
