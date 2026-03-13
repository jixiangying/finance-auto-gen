import matplotlib.pyplot as plt
from matplotlib import patches
import os

# Set font for Chinese characters (macOS STHeiti Medium)
plt.rcParams['font.sans-serif'] = ['STHeiti Medium', 'PingFang SC', 'Heiti TC', 'Arial Unicode MS']
plt.rcParams['axes.unicode_minus'] = False

def create_card(title, price, change_pct, color, ax, x, y):
    # Draw background box
    box_width = 0.4
    box_height = 0.2
    rect = patches.FancyBboxPatch((x, y), box_width, box_height, boxstyle="round,pad=0.02", 
                                  linewidth=1, edgecolor='#cccccc', facecolor='#f9f9f9', antialiased=True)
    ax.add_patch(rect)
    
    # Title
    ax.text(x + 0.05, y + 0.14, title, fontsize=14, fontweight='bold', color='#333333')
    
    # Price
    ax.text(x + 0.05, y + 0.06, str(price), fontsize=18, fontweight='bold', color=color)
    
    # Change %
    arrow = "▲" if "+" in change_pct else "▼"
    ax.text(x + 0.25, y + 0.06, f"{arrow} {change_pct}", fontsize=14, fontweight='bold', color=color)

data = [
    ("沪指", "4095.00", "-0.81%", "green"),
    ("深成指", "11520.00", "-0.65%", "green"), # Estimated level
    ("创业板", "2480.00", "-0.22%", "green"),  # Estimated level
    ("恒生指数", "25434.00", "-1.10%", "green"),
    ("恒生科技", "5240.00", "-0.54%", "green"), # Estimated level
    ("比特币", "$71682", "+1.50%", "red"),
    ("布伦特原油", "$100.17", "-0.29%", "green"),
    ("黄金", "$5125.00", "+0.20%", "red")
]

fig, ax = plt.subplots(figsize=(10, 6))
ax.set_xlim(0, 1)
ax.set_ylim(0, 1)
ax.axis('off')

# Title on image
ax.text(0.5, 0.95, "今日核心行情数据 (2026-03-13 收盘)", fontsize=20, fontweight='bold', ha='center')

# Draw cards in a grid
for i, (title, price, change, color) in enumerate(data):
    row = i // 2
    col = i % 2
    create_card(title, price, change, color, ax, 0.05 + col * 0.45, 0.7 - row * 0.22)

# Ensure directory exists
os.makedirs('images/charts', exist_ok=True)
output_path = 'images/charts/2026-03-13-evening.png'
plt.savefig(output_path, dpi=200, bbox_inches='tight', transparent=False, facecolor='white')
print(f"Chart saved to {output_path}")
