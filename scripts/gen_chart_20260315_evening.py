import matplotlib.pyplot as plt
from matplotlib import font_manager
import os

# Set font for Chinese characters and minus sign
font_path = '/System/Library/Fonts/STHeiti Medium.ttc'
if not os.path.exists(font_path):
    # Alternative for different macOS versions
    font_path = '/System/Library/Fonts/PingFang.ttc'

prop = font_manager.FontProperties(fname=font_path)
plt.rcParams['axes.unicode_minus'] = False

def create_chart(data, title, output_path):
    fig, ax = plt.subplots(figsize=(10, 6))
    fig.patch.set_facecolor('#f4f4f4')
    ax.set_facecolor('#f4f4f4')
    
    indices = [item[0] for item in data]
    values = [item[1] for item in data]
    changes = [item[2] for item in data]
    colors = ['#e74c3c' if float(c.strip('%')) > 0 else '#2ecc71' for c in changes]
    
    y_pos = range(len(indices))
    bars = ax.barh(y_pos, [1]*len(indices), color=colors, height=0.6)
    
    for i, (index, value, change) in enumerate(data):
        ax.text(0.05, i, index, fontproperties=prop, fontsize=16, va='center', fontweight='bold')
        ax.text(0.4, i, value, fontsize=16, va='center', fontweight='bold')
        ax.text(0.7, i, change, fontsize=16, va='center', fontweight='bold', color=colors[i])
    
    ax.set_xlim(0, 1)
    ax.axis('off')
    plt.title(title, fontproperties=prop, fontsize=20, pad=20, fontweight='bold')
    
    plt.tight_layout()
    plt.savefig(output_path, dpi=300, bbox_inches='tight', facecolor=fig.get_facecolor())
    plt.close()

# Data for Sunday Afternoon (Domestic Friday Close)
domestic_data = [
    ("上证指数", "4095.45", "-0.81%"),
    ("深证成指", "14280.78", "-0.65%"),
    ("创业板指", "3310.28", "-0.22%"),
    ("恒生指数", "25465.60", "-0.98%"),
    ("恒生科技", "4978.08", "-0.99%"),
]

os.makedirs('images/charts', exist_ok=True)
create_chart(domestic_data, "国内核心指数表现 (2026-03-13)", "images/charts/domestic_outlook.png")
print("Chart generated: images/charts/domestic_outlook.png")
