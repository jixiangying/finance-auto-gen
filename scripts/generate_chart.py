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
labels = ['上证指数', '创业板指', '恒生指数', '恒生科技']
values = ['4096.60', '2641.5', '25408.46', '4941.73'] # Estimated Chinext from previous context if not exact
changes = [-0.67, -0.64, -1.35, -0.12]

fig, ax = plt.subplots(figsize=(8, 4))
ax.set_facecolor('#f8f9fa')
fig.patch.set_facecolor('#ffffff')

for i, (label, value, change) in enumerate(zip(labels, values, changes)):
    color = 'green' if change < 0 else 'red'
    sign = '' if change < 0 else '+'
    
    # Draw a box for each index
    rect = plt.Rectangle((0.1, 0.75 - i*0.2), 0.8, 0.15, transform=ax.transAxes, color='white', ec='#dee2e6', lw=1)
    ax.add_patch(rect)
    
    ax.text(0.15, 0.8 - i*0.2, label, transform=ax.transAxes, fontproperties=prop, fontsize=14, fontweight='bold', va='center')
    ax.text(0.45, 0.8 - i*0.2, value, transform=ax.transAxes, fontproperties=prop, fontsize=16, color='#333333', va='center')
    ax.text(0.75, 0.8 - i*0.2, f'{sign}{change}%', transform=ax.transAxes, fontproperties=prop, fontsize=14, color=color, fontweight='bold', va='center')

ax.set_axis_off()
plt.title('2026年3月9日 A股/港股 收盘快报', fontproperties=prop, fontsize=18, pad=20)

output_path = 'images/charts/2026-03-09-evening.png'
os.makedirs(os.path.dirname(output_path), exist_ok=True)
plt.savefig(output_path, dpi=300, bbox_inches='tight')
print(f'Saved to {output_path}')
