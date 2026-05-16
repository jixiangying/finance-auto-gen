import matplotlib.pyplot as plt
import matplotlib.font_manager as fm
import os

# Set Chinese font for macOS
font_path = '/System/Library/Fonts/PingFang.ttc'
if not os.path.exists(font_path):
    font_path = '/System/Library/Fonts/STHeiti Medium.ttc'

prop = fm.FontProperties(fname=font_path)
plt.rcParams['font.family'] = prop.get_name()
plt.rcParams['axes.unicode_minus'] = False

# Data
assets = [
    'S&P 500', 'Nasdaq', '上证指数', '沪深300', 
    '恒生指数', '布伦特原油', '比特币', '美元/人民币'
]
prices = [
    '7408.50', '26225.14', '4135.39', '4859.59',
    '25962.73', '$108.11', '$79105', '6.8099'
]
changes = [
    0.1, -0.1, -1.07, -0.25,
    -1.63, 8.1, -1.29, 0.13
]

# Colors: Red for up, Green for down
colors = ['#ff4d4f' if c > 0 else '#52c41a' for c in changes]
change_labels = [f'{"+" if c > 0 else ""}{c}%' for c in changes]

fig, ax = plt.subplots(figsize=(10, 6))
fig.patch.set_facecolor('#f0f2f5')
ax.set_facecolor('#ffffff')

y_pos = range(len(assets))
bars = ax.barh(y_pos, [abs(c) for c in changes], color=colors, height=0.6)

# Labels
for i, (price, change_label) in enumerate(zip(prices, change_labels)):
    ax.text(0.1, i, f'{assets[i]} | {price} | {change_label}', 
            va='center', fontproperties=prop, fontsize=12, fontweight='bold',
            color='black' if changes[i] == 0 else ('#cf1322' if changes[i] > 0 else '#389e0d'))

ax.set_yticks(y_pos)
ax.set_yticklabels(assets, fontproperties=prop)
ax.invert_yaxis()
ax.set_xlabel('周涨跌幅 (%)', fontproperties=prop)
ax.set_title('核心资产本周表现回顾 (2026-05-11至05-15)', fontproperties=prop, fontsize=16, pad=20)

# Remove spines
for spine in ['top', 'right']:
    ax.spines[spine].set_visible(False)

plt.tight_layout()
output_path = 'images/charts/2026-05-16-evening.png'
plt.savefig(output_path, dpi=300, bbox_inches='tight')
print(f'Chart saved to {output_path}')
