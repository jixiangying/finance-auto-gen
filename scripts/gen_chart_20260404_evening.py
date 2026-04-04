import matplotlib.pyplot as plt
from matplotlib import font_manager
import os

# Ensure directory exists
output_dir = "images/charts"
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

# Set font for Chinese support (macOS)
font_path = "/System/Library/Fonts/STHeiti Medium.ttc"
prop = font_manager.FontProperties(fname=font_path)
plt.rcParams['font.sans-serif'] = ['Heiti TC'] # Fallback
plt.rcParams['axes.unicode_minus'] = False

# Data: Indices, Prices (4/3 Close), Friday Changes, Weekly Changes
indices = ['上证指数', '深证成指', '创业板指']
prices = [3880.10, 13352.90, 3149.60]
fri_changes = [-1.00, -0.99, -0.73]
weekly_changes = [-0.86, -2.96, -4.44]

fig, ax = plt.subplots(figsize=(12, 6))
ax.axis('off')
fig.patch.set_facecolor('#fdfdfd')

for i, (name, price, fri_c, week_c) in enumerate(zip(indices, prices, fri_changes, weekly_changes)):
    # Calculate color based on weekly change
    color = 'green' if week_c < 0 else 'red'
    fri_color = 'green' if fri_c < 0 else 'red'
    
    # Position
    x = 0.18 + i * 0.32
    
    # Draw index name
    ax.text(x, 0.8, name, ha='center', va='center', fontsize=20, fontweight='bold', fontproperties=prop)
    
    # Draw price
    ax.text(x, 0.65, f"{price:.2f}", ha='center', va='center', fontsize=24, fontweight='bold', color='black')
    
    # Draw Friday change
    ax.text(x, 0.45, f"周五: {fri_c:+.2f}%", ha='center', va='center', fontsize=16, color=fri_color, fontproperties=prop)
    
    # Draw Weekly change (Main focus)
    ax.text(x, 0.25, f"全周: {week_c:+.2f}%", ha='center', va='center', fontsize=18, fontweight='bold', color=color, fontproperties=prop)

plt.title("A股全周核心表现汇总 (截至2026年4月3日)", fontproperties=prop, fontsize=24, pad=30)
plt.savefig(os.path.join(output_dir, "2026-04-04-evening.png"), bbox_inches='tight', dpi=150, facecolor=fig.get_facecolor())
print("Weekend summary chart generated successfully.")
