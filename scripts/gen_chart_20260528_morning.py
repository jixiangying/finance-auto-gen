import matplotlib.pyplot as plt
import matplotlib.patches as patches
import matplotlib.font_manager as fm

# Path to a reliable Chinese font on macOS
font_path = '/System/Library/Fonts/STHeiti Medium.ttc'
prop = fm.FontProperties(fname=font_path)
plt.rcParams['axes.unicode_minus'] = False

data = [
    {"name": "标普 500", "price": "7,520.36", "change": "+1.24", "pct": "+0.02%", "up": True},
    {"name": "纳斯达克", "price": "26,674.73", "change": "+18.55", "pct": "+0.07%", "up": True},
    {"name": "道琼斯", "price": "50,644.28", "change": "+182.60", "pct": "+0.36%", "up": True},
    {"name": "WTI 原油", "price": "$88.50", "change": "-5.35", "pct": "-5.71%", "up": False},
    {"name": "现货黄金", "price": "$4,433.85", "change": "-72.15", "pct": "-1.60%", "up": False},
    {"name": "10年期美债收益率", "price": "4.48%", "change": "-0.01", "pct": "-0.22%", "up": False},
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
plt.savefig('images/charts/2026-05-28-morning-chart.png', dpi=300, bbox_inches='tight')
print("Chart generated successfully with correct fonts.")
