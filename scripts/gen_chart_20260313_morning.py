import matplotlib.pyplot as plt
import matplotlib.patches as patches
import matplotlib.font_manager as fm

# Path to a reliable Chinese font on macOS
font_path = '/System/Library/Fonts/STHeiti Medium.ttc'
prop = fm.FontProperties(fname=font_path)
plt.rcParams['axes.unicode_minus'] = False

data = [
    {"name": "标普 500", "price": "6,672.62", "change": "-103.18", "pct": "-1.52%", "up": False},
    {"name": "纳斯达克", "price": "22,311.98", "change": "-404.16", "pct": "-1.78%", "up": False},
    {"name": "道琼斯", "price": "46,677.85", "change": "-739.42", "pct": "-1.56%", "up": False},
    {"name": "布伦特原油", "price": "$100.24", "change": "+5.24", "pct": "+5.52%", "up": True},
    {"name": "现货黄金", "price": "$5,178.50", "change": "+42.50", "pct": "+0.83%", "up": True},
    {"name": "比特币", "price": "$71,636.00", "change": "+1,657.0", "pct": "+2.37%", "up": True},
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
    ax.text(0.5, 0.50, item['price'], ha='center', va='center', fontsize=28, fontweight='bold', color='#333', transform=ax.transAxes)
    
    change_text = f"{item['change']} ({item['pct']})"
    ax.text(0.5, 0.25, change_text, ha='center', va='center', fontsize=18, fontweight='bold', color=color, transform=ax.transAxes)
    
    ax.axis('off')

plt.tight_layout(pad=3.0)
plt.savefig('images/charts/2026-03-13-morning-chart.png', dpi=300, bbox_inches='tight')
print("Chart generated successfully with correct fonts.")
