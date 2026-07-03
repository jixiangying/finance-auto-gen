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
labels = ['S&P 500', 'Nasdaq Composite', 'Dow Jones', 'WTI Crude Oil', 'Spot Gold', 'Bitcoin (BTC)']
values = ['7,483.24', '25,832.67', '52,900.07', '$67.31', '$4,067.67', '$61,330.70']
changes = [0.00, -0.80, 1.14, -1.01, 1.46, 1.65]

fig, ax = plt.subplots(figsize=(9, 7.5))
ax.set_facecolor('#f8fafc')
fig.patch.set_facecolor('#ffffff')

# Background border
border = plt.Rectangle((0.01, 0.01), 0.98, 0.98, transform=fig.transFigure, fill=False, color='#e2e8f0', lw=2)
fig.patches.append(border)

for i, (label, value, change) in enumerate(zip(labels, values, changes)):
    color = '#10b981' if change < 0 else '#ef4444' # Tailwind green-500 and red-500
    sign = '' if change < 0 else '+'
    if change == 0.00:
        sign = '+'
    
    # Draw a box for each index
    rect = plt.Rectangle((0.05, 0.82 - i*0.13), 0.9, 0.10, transform=ax.transAxes, color='white', ec='#e2e8f0', lw=1.5, zorder=1)
    ax.add_patch(rect)
    
    # Accent indicator bar on the left of each box
    accent_bar = plt.Rectangle((0.05, 0.82 - i*0.13), 0.01, 0.10, transform=ax.transAxes, color=color, zorder=2)
    ax.add_patch(accent_bar)
    
    ax.text(0.08, 0.87 - i*0.13, label, transform=ax.transAxes, fontproperties=prop, fontsize=13, fontweight='bold', va='center', color='#1e293b')
    ax.text(0.48, 0.87 - i*0.13, value, transform=ax.transAxes, fontproperties=prop, fontsize=15, color='#334155', fontweight='bold', va='center')
    ax.text(0.78, 0.87 - i*0.13, f'{sign}{change:.2f}%', transform=ax.transAxes, fontproperties=prop, fontsize=14, color=color, fontweight='bold', va='center')

ax.set_axis_off()
plt.title('2026年7月3日 早盘(国际) 核心行情快报', fontproperties=prop, fontsize=18, pad=25, fontweight='bold', color='#0f172a')

output_path = 'images/charts/2026-07-03-morning.png'
os.makedirs(os.path.dirname(output_path), exist_ok=True)
plt.savefig(output_path, dpi=300, bbox_inches='tight')
plt.close()
print(f'Saved to {output_path}')
