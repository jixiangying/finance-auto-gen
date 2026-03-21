import matplotlib.pyplot as plt
import os

# Set Chinese font
plt.rcParams['font.sans-serif'] = ['PingFang SC', 'Heiti TC', 'STHeiti']
plt.rcParams['axes.unicode_minus'] = False

def create_card(name, price, change, output_path, color):
    fig, ax = plt.subplots(figsize=(6, 2))
    fig.patch.set_facecolor('#f8f9fa')
    ax.axis('off')
    
    text_color = '#d63031' if color == 'red' else '#27ae60'
    arrow = '▲' if color == 'red' else '▼'
    
    plt.text(0.05, 0.6, name, fontsize=20, fontweight='bold', color='#2d3436')
    plt.text(0.05, 0.2, f"{price} {arrow} {change}", fontsize=24, fontweight='black', color=text_color)
    
    plt.tight_layout()
    plt.savefig(output_path, dpi=150, bbox_inches='tight')
    plt.close()

# Correct data for March 20/21
charts_dir = "/Users/jxy/Documents/Project/finance-auto-gen/images/charts"
os.makedirs(charts_dir, exist_ok=True)

# 1. Fix 3/20深圳成指
create_card("深证成指 (3/20)", "13866.20", "-0.25%", f"{charts_dir}/2026-03-20-shenzhen.png", "green")
# 2. Fix 3/20创业板指
create_card("创业板指 (3/20)", "3352.10", "+1.30%", f"{charts_dir}/2026-03-20-chinext.png", "red")
# 3. Fix 3/21周末复盘总表
create_card("深成/创业板 (3/20收盘)", "13866 / 3352", "结构性分化", f"{charts_dir}/2026-03-21-evening-chart.png", "red")

print("Corrected charts generated successfully.")
