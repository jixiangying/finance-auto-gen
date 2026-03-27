import matplotlib.pyplot as plt
import os

# Set Chinese font
plt.rcParams['font.sans-serif'] = ['PingFang SC', 'Heiti TC', 'STHeiti']
plt.rcParams['axes.unicode_minus'] = False

def create_card(indices, output_path):
    fig, ax = plt.subplots(figsize=(8, 5))
    fig.patch.set_facecolor('#ffffff')
    ax.axis('off')
    
    y_pos = 0.8
    for name, price, change in indices:
        color = '#d63031' if '+' in change else '#27ae60'
        arrow = '▲' if '+' in change else '▼'
        
        plt.text(0.05, y_pos, name, fontsize=22, fontweight='bold', color='#2d3436')
        plt.text(0.45, y_pos, price, fontsize=22, color='#2d3436')
        plt.text(0.75, y_pos, f"{arrow} {change}", fontsize=22, fontweight='black', color=color)
        y_pos -= 0.18
    
    plt.tight_layout()
    plt.savefig(output_path, dpi=150, bbox_inches='tight')
    plt.close()

charts_dir = "/Users/jxy/Documents/Project/finance-auto-gen/images/charts"
os.makedirs(charts_dir, exist_ok=True)

indices_327 = [
    ("上证指数", "3915.65", "+0.68%"),
    ("深证成指", "13760.19", "+1.13%"),
    ("创业板指", "3313.13", "+0.71%"),
    ("恒生指数", "25031.31", "+0.70%")
]

create_card(indices_327, f"{charts_dir}/2026-03-27-evening.png")
print("Corrected 3/27 chart generated successfully.")
