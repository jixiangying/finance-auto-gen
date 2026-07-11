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

# Data (July 10, 2026 Friday Closing)
labels = ['S&P 500', 'Nasdaq Composite', 'Dow Jones', 'WTI Crude Oil', 'Spot Gold', 'Bitcoin (BTC)', 'FTSE China A50']
values = ['7,575.39', '26,281.61', '52,637.01', '$71.41', '$4,119.56', '$63,220.69', '15,125.41']
changes = [0.42, 0.29, 0.29, -2.87, -0.06, 1.56, -2.48]

fig, ax = plt.subplots(figsize=(9, 8))
ax.set_facecolor('#f8fafc')
fig.patch.set_facecolor('#ffffff')

# Background border
border = plt.Rectangle((0.01, 0.01), 0.98, 0.98, transform=fig.transFigure, fill=False, color='#e2e8f0', lw=2)
fig.patches.append(border)

for i, (label, value, change) in enumerate(zip(labels, values, changes)):
    color = '#10b981' if change < 0 else '#ef4444' # Green for down, red for up
    sign = '' if change < 0 else '+'
    
    # Draw a box for each index
    rect = plt.Rectangle((0.05, 0.84 - i*0.12), 0.9, 0.09, transform=ax.transAxes, color='white', ec='#e2e8f0', lw=1.5, zorder=1)
    ax.add_patch(rect)
    
    # Accent indicator bar on the left of each box
    accent_bar = plt.Rectangle((0.05, 0.84 - i*0.12), 0.01, 0.09, transform=ax.transAxes, color=color, zorder=2)
    ax.add_patch(accent_bar)
    
    ax.text(0.08, 0.885 - i*0.12, label, transform=ax.transAxes, fontproperties=prop, fontsize=13, fontweight='bold', va='center', color='#1e293b')
    ax.text(0.48, 0.885 - i*0.12, value, transform=ax.transAxes, fontproperties=prop, fontsize=15, color='#334155', fontweight='bold', va='center')
    ax.text(0.78, 0.885 - i*0.12, f'{sign}{change:.2f}%', transform=ax.transAxes, fontproperties=prop, fontsize=14, color=color, fontweight='bold', va='center')

ax.set_axis_off()
plt.title('2026年7月11日 早报 核心资产全球表现回顾', fontproperties=prop, fontsize=18, pad=25, fontweight='bold', color='#0f172a')

output_path = 'images/charts/2026-07-11-morning.png'
os.makedirs(os.path.dirname(output_path), exist_ok=True)
plt.savefig(output_path, dpi=300, bbox_inches='tight')
plt.close()
print(f'Saved to {output_path}')
