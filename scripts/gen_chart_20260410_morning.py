import matplotlib.pyplot as plt
import matplotlib.font_manager as fm
import os

# Set font for macOS Chinese support
font_path = '/System/Library/Fonts/STHeiti Medium.ttc'
prop = fm.FontProperties(fname=font_path)
plt.rcParams['font.sans-serif'] = ['STHeiti']
plt.rcParams['axes.unicode_minus'] = False

# Data
assets = ['S&P 500', 'Nasdaq', 'Dow Jones', 'BTC', 'Gold Spot', 'WTI Oil']
prices = ['6,824.66', '22,822.42', '48,185.80', '$72,127.92', '$4,727.60', '$97.87']
changes = [0.62, 0.83, 0.58, 0.0, 0.0, 3.7] # Assuming 0 for BTC/Gold if not specified in search but they are usually included
change_texts = ['+0.62%', '+0.83%', '+0.58%', '-', '-', '+3.7%']

# Create figure
fig, ax = plt.subplots(figsize=(10, 6), facecolor='#f4f4f4')
ax.set_facecolor('#f4f4f4')

# Hide axes
ax.xaxis.set_visible(False)
ax.yaxis.set_visible(False)
for spine in ax.spines.values():
    spine.set_visible(False)

# Title
plt.text(0.5, 0.9, '核心行情数据 (2026-04-10 早报)', 
         horizontalalignment='center', fontsize=20, fontproperties=prop, weight='bold')

# Draw cards
for i in range(len(assets)):
    y_pos = 0.75 - (i * 0.12)
    color = 'red' if changes[i] >= 0 else 'green'
    
    # Asset Name
    plt.text(0.1, y_pos, assets[i], fontsize=16, fontproperties=prop, weight='bold')
    
    # Price
    plt.text(0.4, y_pos, prices[i], fontsize=16, fontproperties=prop)
    
    # Change
    plt.text(0.7, y_pos, change_texts[i], fontsize=16, fontproperties=prop, color=color, weight='bold')
    
    # Divider
    plt.axhline(y=y_pos-0.03, xmin=0.1, xmax=0.9, color='gray', linestyle='--', linewidth=0.5, alpha=0.5)

# Save
output_path = 'images/charts/2026-04-10-morning-chart.png'
os.makedirs(os.path.dirname(output_path), exist_ok=True)
plt.savefig(output_path, dpi=300, bbox_inches='tight')
print(f"Chart saved to {output_path}")
