import matplotlib.pyplot as plt
import matplotlib.patches as patches
import matplotlib.font_manager as fm

# Path to a reliable Chinese font on macOS
font_path = '/System/Library/Fonts/STHeiti Medium.ttc'
prop = fm.FontProperties(fname=font_path)
plt.rcParams['axes.unicode_minus'] = False

data = [
    {"name": "上证指数", "price": "4,152.12", "change": "+53.48", "pct": "+1.31%", "up": True},
    {"name": "深证成指", "price": "16,124.50", "change": "+262.61", "pct": "+1.66%", "up": True},
    {"name": "创业板指", "price": "4,210.35", "change": "+85.28", "pct": "+2.07%", "up": True},
    {"name": "恒生指数", "price": "25,420.33", "change": "+572.33", "pct": "+2.30%", "up": True},
    {"name": "两市成交额", "price": "2.95万亿", "change": "+0.54万亿", "pct": "+22.4%", "up": True},
    {"name": "主力资金动向", "price": "+128.5亿", "change": "北向净流入", "pct": "强势回归", "up": True},
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
plt.savefig('images/charts/2026-05-29-evening-chart.png', dpi=300, bbox_inches='tight')
print("Chart generated successfully with correct fonts.")
