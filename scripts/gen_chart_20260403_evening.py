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

# Data
indices = ['上证指数', '深证成指', '创业板指']
prices = [3880.10, 13352.90, 3149.60]
changes = [-1.00, -0.99, -0.73]
colors = ['green' if c < 0 else 'red' for c in changes]

fig, ax = plt.subplots(figsize=(10, 4))
ax.axis('off')
fig.patch.set_facecolor('#f4f4f4')

for i, (name, price, change) in enumerate(zip(indices, prices, changes)):
    color = 'green' if change < 0 else 'red'
    text = f"{name}\n{price:.2f}\n{change:+.2f}%"
    ax.text(0.15 + i*0.35, 0.5, text, ha='center', va='center', 
            fontsize=18, fontweight='bold', color=color, fontproperties=prop)

plt.title("核心行情数据 - 2026年4月3日 收盘", fontproperties=prop, fontsize=20, pad=20)
plt.savefig(os.path.join(output_dir, "2026-04-03-evening.png"), bbox_inches='tight', dpi=150, facecolor=fig.get_facecolor())
print("Chart generated successfully.")
