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
labels = ['上证指数', '深证成指', '创业板指', '科创50', '恒生指数', '恒生科技', '富时中国A50']
values = ['3,996.16', '15,046.67', '3,842.73', '2,064.98', '24,175.12', '4,721.66', '15,261.46']
changes = [-1.00, -2.29, -4.37, -5.53, 0.60, -0.21, -2.10]

fig, ax = plt.subplots(figsize=(9, 8))
ax.set_facecolor('#f8fafc')
fig.patch.set_facecolor('#ffffff')

# Background border
border = plt.Rectangle((0.01, 0.01), 0.98, 0.98, transform=fig.transFigure, fill=False, color='#e2e8f0', lw=2)
fig.patches.append(border)

for i, (label, value, change) in enumerate(zip(labels, values, changes)):
    # Red for up, green for down in Chinese market
    color = '#10b981' if change < 0 else '#ef4444'
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
plt.title('2026年7月10日 晚报 国内核心指数收盘表现', fontproperties=prop, fontsize=18, pad=25, fontweight='bold', color='#0f172a')

output_path = 'images/charts/2026-07-10-evening.png'
os.makedirs(os.path.dirname(output_path), exist_ok=True)
plt.savefig(output_path, dpi=300, bbox_inches='tight')
plt.close()
print(f'Saved to {output_path}')
