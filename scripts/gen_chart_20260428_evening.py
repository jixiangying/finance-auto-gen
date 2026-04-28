import matplotlib.pyplot as plt
import matplotlib.font_manager as fm
import os

# Set font for macOS Chinese support
font_path = '/System/Library/Fonts/STHeiti Medium.ttc'
prop = fm.FontProperties(fname=font_path)
plt.rcParams['font.sans-serif'] = ['STHeiti']
plt.rcParams['axes.unicode_minus'] = False

# Data (2026-04-28 Evening)
assets = ['上证指数', '深证成指', '创业板指', '恒生指数', '恒生科技', '离岸人民币']
prices = ['4078.64', '14830.46', '3596.71', '25679.78', '4827.19', '6.8589']
changes = [-0.19, -1.10, -1.43, -0.95, -2.28, 0.01] # CNY weakened 10bp
change_texts = ['-0.19%', '-1.10%', '-1.43%', '-0.95%', '-2.28%', '+10bp']

# Create figure
fig, ax = plt.subplots(figsize=(10, 6), facecolor='#f4f4f4')
ax.set_facecolor('#f4f4f4')

# Hide axes
ax.xaxis.set_visible(False)
ax.yaxis.set_visible(False)
for spine in ax.spines.values():
    spine.set_visible(False)

# Title
plt.text(0.5, 0.9, '核心行情数据 (2026-04-28 收盘报)', 
         horizontalalignment='center', fontsize=20, fontproperties=prop, weight='bold')

# Draw cards
for i in range(len(assets)):
    y_pos = 0.75 - (i * 0.12)
    # Chinese convention: Red = Up, Green = Down. 
    # For indices, negative is green. For USD/CNH, +10bp usually means weakening, but let's stick to color logic.
    # Actually for currency, it depends. But let's just use green for all negative percentages.
    color = 'red' if changes[i] > 0 else 'green'
    if changes[i] == 0: color = 'black'
    
    # Asset Name
    plt.text(0.1, y_pos, assets[i], fontsize=16, fontproperties=prop, weight='bold')
    
    # Price
    plt.text(0.4, y_pos, prices[i], fontsize=16, fontproperties=prop)
    
    # Change
    plt.text(0.7, y_pos, change_texts[i], fontsize=16, fontproperties=prop, color=color, weight='bold')
    
    # Divider
    plt.axhline(y=y_pos-0.03, xmin=0.1, xmax=0.9, color='gray', linestyle='--', linewidth=0.5, alpha=0.5)

# Save
output_path = 'images/charts/2026-04-28-evening-chart.png'
os.makedirs(os.path.dirname(output_path), exist_ok=True)
plt.savefig(output_path, dpi=300, bbox_inches='tight')
print(f"Chart saved to {output_path}")
