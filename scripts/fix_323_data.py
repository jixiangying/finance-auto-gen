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

charts_dir = "/Users/jxy/Documents/Project/finance-auto-gen/images/charts"
os.makedirs(charts_dir, exist_ok=True)

# Generate corrected cards for 3/23 Evening
create_card("上证指数 (3/23收盘)", "3813.28", "-3.63%", f"{charts_dir}/2026-03-23-shanghai.png", "green")
create_card("深证成指 (3/23收盘)", "13345.51", "-3.76%", f"{charts_dir}/2026-03-23-shenzhen.png", "green")
create_card("恒生指数 (3/23收盘)", "24382.47", "-3.54%", f"{charts_dir}/2026-03-23-hangseng.png", "green")
create_card("沪深300 (3/23收盘)", "4401.21", "-3.63%", f"{charts_dir}/2026-03-23-sp300.png", "green")

print("Corrected 3/23 images generated.")
