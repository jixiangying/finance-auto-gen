import matplotlib.pyplot as plt
import matplotlib.font_manager as fm
import os

# Set font for Chinese characters (macOS)
font_path = '/System/Library/Fonts/STHeiti Medium.ttc'
if not os.path.exists(font_path):
    font_path = '/System/Library/Fonts/PingFang.ttc'

prop = fm.FontProperties(fname=font_path)
plt.rcParams['axes.unicode_minus'] = False

# Market Data
data = [
    {"name": "S&P 500", "price": "6,781.48", "change": "-0.21%"},
    {"name": "Nasdaq", "price": "22,697.10", "change": "+0.01%"},
    {"name": "Dow Jones", "price": "47,706.51", "change": "-0.07%"},
    {"name": "Gold", "price": "$5,190.72", "change": "+1.00%"},
    {"name": "WTI Oil", "price": "$86.39", "change": "-8.81%"},
    {"name": "Bitcoin", "price": "$70,305", "change": "+1.72%"}
]

# Plotting
fig, axes = plt.subplots(2, 3, figsize=(15, 8), facecolor='#f4f4f4')
fig.suptitle('国际市场行情快报 (2026-03-11 上午)', fontproperties=prop, fontsize=20, fontweight='bold', y=1.05)

for i, ax in enumerate(axes.flat):
    if i < len(data):
        item = data[i]
        is_up = '+' in item['change']
        color = '#e74c3c' if is_up else '#27ae60'  # Red for up, Green for down as per instructions
        
        ax.set_facecolor('white')
        ax.text(0.5, 0.7, item['name'], fontproperties=prop, fontsize=16, ha='center', va='center', fontweight='bold')
        ax.text(0.5, 0.4, item['price'], fontsize=24, ha='center', va='center', color='#333')
        ax.text(0.5, 0.15, item['change'], fontsize=20, ha='center', va='center', color=color, fontweight='bold')
        
        # Add a border
        for spine in ax.spines.values():
            spine.set_edgecolor('#ddd')
            spine.set_linewidth(2)
        
        ax.set_xticks([])
        ax.set_yticks([])
    else:
        ax.axis('off')

plt.tight_layout()
output_path = 'images/charts/2026-03-11-morning-chart.png'
os.makedirs(os.path.dirname(output_path), exist_ok=True)
plt.savefig(output_path, bbox_inches='tight', dpi=150)
print(f"Chart saved to {output_path}")
