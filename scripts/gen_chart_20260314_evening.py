import matplotlib.pyplot as plt
import matplotlib.patches as patches
import os

# Set font for Chinese characters (macOS STHeiti Medium)
plt.rcParams['font.sans-serif'] = ['STHeiti Medium', 'PingFang SC', 'Heiti TC', 'Arial Unicode MS']
plt.rcParams['axes.unicode_minus'] = False

def create_card(title, price, change_pct, color, ax, x, y):
    # Draw background box
    box_width = 0.42
    box_height = 0.18
    rect = patches.FancyBboxPatch((x, y), box_width, box_height, boxstyle="round,pad=0.02", 
                                  linewidth=1, edgecolor='#cccccc', facecolor='#f9f9f9', antialiased=True)
    ax.add_patch(rect)
    
    # Title
    ax.text(x + 0.05, y + 0.12, title, fontsize=14, fontweight='bold', color='#333333')
    
    # Price
    ax.text(x + 0.05, y + 0.05, str(price), fontsize=18, fontweight='bold', color=color)
    
    # Change %
    arrow = "▲" if "+" in change_pct else "▼"
    ax.text(x + 0.28, y + 0.05, f"{arrow} {change_pct}", fontsize=14, fontweight='bold', color=color)

# Updated data for 2026-03-14 Weekend Review (Friday 3/13 Close)
data = [
    ("沪指 (SSE)", "4095.45", "-0.81%", "green"),
    ("深成指 (SZSE)", "14280.78", "-0.65%", "green"),
    ("创业板指 (ChiNext)", "3310.28", "-0.22%", "green"),
    ("恒生指数 (HSI)", "25465.60", "-0.98%", "green"),
    ("恒生科技 (HSTECH)", "4978.08", "-0.99%", "green"),
    ("比特币 (BTC)", "$71,500", "+2.10%", "red"),
    ("WTI原油 (WTI)", "$93.40", "-1.00%", "green"),
    ("黄金 (Gold)", "$2,150.00", "-3.00%", "green")
]

fig, ax = plt.subplots(figsize=(10, 7))
ax.set_xlim(0, 1)
ax.set_ylim(0, 1)
ax.axis('off')

# Title on image
ax.text(0.5, 0.95, "本周核心行情汇总 (截至 2026-03-13 收盘)", fontsize=22, fontweight='bold', ha='center')

# Draw cards in a grid
for i, (title, price, change, color) in enumerate(data):
    row = i // 2
    col = i % 2
    create_card(title, price, change, color, ax, 0.05 + col * 0.46, 0.72 - row * 0.20)

# Footer text
ax.text(0.5, 0.05, "数据来源：财联社、东方财富及公开市场数据", fontsize=10, color='#666666', ha='center')

# Ensure directory exists
os.makedirs('images/charts', exist_ok=True)
output_path = 'images/charts/2026-03-14-evening.png'
plt.savefig(output_path, dpi=200, bbox_inches='tight', transparent=False, facecolor='white')
print(f"Chart saved to {output_path}")
