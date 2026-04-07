import matplotlib.pyplot as plt
import matplotlib.font_manager as fm
import os

# Set font for Chinese characters (macOS)
font_path = '/System/Library/Fonts/STHeiti Medium.ttc'
if not os.path.exists(font_path):
    font_path = '/System/Library/Fonts/PingFang.ttc'
prop = fm.FontProperties(fname=font_path)

plt.rcParams['font.family'] = prop.get_name()
plt.rcParams['axes.unicode_minus'] = False

# Data for 2026-04-07 Morning (Monday Close)
assets = [
    'S&P 500', 'Nasdaq', 'Dow Jones', 
    'Gold (June)', 'WTI Crude', 'Bitcoin (BTC)', 'US 10Y Yield'
]
prices = [
    '6,611.83', '21,996.34', '46,669.88', 
    '4,684.45', '112.41', '70,000', '4.33%'
]
changes = [
    0.44, 0.54, 0.36, 
    0.10, 0.78, 4.00, 0.05
]

# Define colors: Red for Up, Green for Down
colors = ['#FF3131' if c > 0 else '#00D100' for c in changes]

fig, ax = plt.subplots(figsize=(10, 6))
fig.patch.set_facecolor('#f4f4f4')
ax.set_facecolor('#f4f4f4')

y_pos = range(len(assets))
bars = ax.barh(y_pos, [abs(c) for c in changes], color=colors, height=0.6)

# Add asset names and prices on the left
for i, (asset, price, change) in enumerate(zip(assets, prices, changes)):
    sign = '+' if change > 0 else ''
    text = f"{asset}\n{price} ({sign}{change}%)"
    ax.text(-0.05, i, text, va='center', ha='right', fontproperties=prop, fontsize=11, fontweight='bold')

# Adjust limits and hide axes
ax.set_xlim(0, max([abs(c) for c in changes]) + 0.5)
ax.set_yticks([])
ax.set_xticks([])
for spine in ax.spines.values():
    spine.set_visible(False)

plt.title('全球市场隔夜复盘：特朗普伊朗最后通牒倒计时 (2026-04-07)', fontproperties=prop, fontsize=16, pad=20)

# Save the plot
output_dir = 'images/charts'
os.makedirs(output_dir, exist_ok=True)
output_path = os.path.join(output_dir, '2026-04-07-morning-chart.png')
plt.savefig(output_path, bbox_inches='tight', dpi=150, facecolor=fig.get_facecolor())
plt.close()

print(f"Chart saved to {output_path}")
