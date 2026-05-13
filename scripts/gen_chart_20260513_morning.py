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

# Data for May 13, 2026 (Morning report covers May 12 close)
labels = ['S&P 500', 'Nasdaq', 'Dow Jones', 'Oil (WTI)', 'Bitcoin (BTC)', 'US 10Y Yield']
values = ['7,402.00', '19,100.00', '49,761.00', '$101.53', '$80,517.20', '4.45%']
changes = [-0.15, -0.80, 0.11, 3.53, -0.96, 0.04] # 0.04 represents +4bps for visual consistency or I can handle bps separately

fig, ax = plt.subplots(figsize=(8, 7))
ax.set_facecolor('#f8f9fa')
fig.patch.set_facecolor('#ffffff')

for i, (label, value, change) in enumerate(zip(labels, values, changes)):
    color = 'green' if change < 0 else 'red'
    if label == 'US 10Y Yield':
        sign = '+'
        change_text = '+4bps'
    else:
        sign = '' if change < 0 else '+'
        change_text = f'{sign}{change}%'
    
    # Draw a box for each index
    rect = plt.Rectangle((0.1, 0.85 - i*0.15), 0.8, 0.12, transform=ax.transAxes, color='white', ec='#dee2e6', lw=1)
    ax.add_patch(rect)
    
    ax.text(0.15, 0.88 - i*0.15, label, transform=ax.transAxes, fontproperties=prop, fontsize=14, fontweight='bold', va='center')
    ax.text(0.45, 0.88 - i*0.15, value, transform=ax.transAxes, fontproperties=prop, fontsize=16, color='#333333', va='center')
    ax.text(0.75, 0.88 - i*0.15, change_text, transform=ax.transAxes, fontproperties=prop, fontsize=14, color=color, fontweight='bold', va='center')

ax.set_axis_off()
plt.title('2026年5月13日 早报(国际) 核心行情快报', fontproperties=prop, fontsize=18, pad=20)

output_path = 'images/charts/2026-05-13-morning-chart.png'
os.makedirs(os.path.dirname(output_path), exist_ok=True)
plt.savefig(output_path, dpi=300, bbox_inches='tight')
print(f'Saved to {output_path}')
