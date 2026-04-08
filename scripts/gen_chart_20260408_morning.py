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

# Data for April 7, 2026 Close (International)
labels = ['标普500', '纳斯达克', '道琼斯', '10年美债', 'WTI原油', '比特币']
values = ['6616.85', '22017.85', '46584.46', '4.30%', '112.95', '71000']
changes = [0.08, 0.10, -0.18, -0.92, 0.50, 4.41] # 10Y down from 4.34 to 4.30 is -0.92%. BTC up from 68k to 71k is ~4.41%

fig, ax = plt.subplots(figsize=(10, 6))
ax.set_facecolor('#f4f7f6')
fig.patch.set_facecolor('#ffffff')

for i, (label, value, change) in enumerate(zip(labels, values, changes)):
    color = 'green' if change < 0 else 'red'
    if label == '10年美债' and change < 0:
        color = 'green' # Yield down is usually green for tech, but let's stick to simple price-like logic or just keep it green for "down"
    
    sign = '+' if change > 0 else ''
    
    # Draw a box for each index
    rect = plt.Rectangle((0.05, 0.82 - i*0.14), 0.9, 0.12, transform=ax.transAxes, color='white', ec='#e0e0e0', lw=1)
    ax.add_patch(rect)
    
    ax.text(0.1, 0.88 - i*0.14, label, transform=ax.transAxes, fontproperties=prop, fontsize=14, fontweight='bold', va='center')
    ax.text(0.45, 0.88 - i*0.14, value, transform=ax.transAxes, fontproperties=prop, fontsize=16, color='#2c3e50', va='center', fontweight='bold')
    ax.text(0.8, 0.88 - i*0.14, f'{sign}{change}%', transform=ax.transAxes, fontproperties=prop, fontsize=14, color=color, fontweight='bold', va='center')

ax.set_axis_off()
plt.title('2026年4月8日 全球市场早报数据卡片', fontproperties=prop, fontsize=20, pad=30, fontweight='bold', color='#2c3e50')

output_path = 'images/charts/2026-04-08-morning.png'
os.makedirs(os.path.dirname(output_path), exist_ok=True)
plt.savefig(output_path, dpi=300, bbox_inches='tight')
print(f'Saved to {output_path}')
