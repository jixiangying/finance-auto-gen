import matplotlib.pyplot as plt
import matplotlib.font_manager as fm
import os

# Set font for macOS to support Chinese characters
font_path = '/System/Library/Fonts/PingFang.ttc'
if not os.path.exists(font_path):
    font_path = '/System/Library/Fonts/STHeiti Light.ttc'

prop = fm.FontProperties(fname=font_path)
plt.rcParams['font.family'] = prop.get_name()
plt.rcParams['axes.unicode_minus'] = False

# Data
labels = ['S&P 500', 'Nasdaq Composite', 'Dow Jones', 'Bitcoin (BTC)', 'Gold']
values = ['6795.99', '22695.95', '47740.80', '72500', '5102.60']
changes = [0.83, 1.38, 0.50, 4.5, -1.8]

fig, ax = plt.subplots(figsize=(8, 6))
ax.set_facecolor('#f8f9fa')
fig.patch.set_facecolor('#ffffff')

for i, (label, value, change) in enumerate(zip(labels, values, changes)):
    color = 'green' if change < 0 else 'red'
    sign = '' if change < 0 else '+'
    
    # Draw a box for each index
    rect = plt.Rectangle((0.1, 0.82 - i*0.18), 0.8, 0.15, transform=ax.transAxes, color='white', ec='#dee2e6', lw=1)
    ax.add_patch(rect)
    
    ax.text(0.15, 0.85 - i*0.18, label, transform=ax.transAxes, fontproperties=prop, fontsize=14, fontweight='bold', va='center')
    ax.text(0.45, 0.85 - i*0.18, value, transform=ax.transAxes, fontproperties=prop, fontsize=16, color='#333333', va='center')
    ax.text(0.75, 0.85 - i*0.18, f'{sign}{change}%', transform=ax.transAxes, fontproperties=prop, fontsize=14, color=color, fontweight='bold', va='center')

ax.set_axis_off()
plt.title('2026年3月10日 早盘(国际) 核心行情快报', fontproperties=prop, fontsize=18, pad=20)

output_path = 'images/charts/2026-03-10-morning-chart.png'
os.makedirs(os.path.dirname(output_path), exist_ok=True)
plt.savefig(output_path, dpi=300, bbox_inches='tight')
print(f'Saved to {output_path}')
