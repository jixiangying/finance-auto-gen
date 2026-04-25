import matplotlib.pyplot as plt
import matplotlib.font_manager as fm
import os

# Set font for Chinese characters (macOS)
font_path = '/System/Library/Fonts/STHeiti Medium.ttc'
prop = fm.FontProperties(fname=font_path)
plt.rcParams['font.sans-serif'] = ['STHeiti']
plt.rcParams['axes.unicode_minus'] = False

# Data
labels = ['S&P 500', 'Nasdaq', 'Dow Jones', 'BTC', 'A50 Futures']
values = [7165.08, 24836.60, 49230.71, 77502, 15642]
changes = [0.80, 1.63, -0.16, -1.89, 0.25] # BTC % is estimated from 79k peak mentioned
colors = ['#ff4d4d' if c > 0 else '#2ecc71' for c in changes]
change_labels = [f'+{c}%' if c > 0 else f'{c}%' for c in changes]

fig, ax = plt.subplots(figsize=(10, 6), dpi=100)
fig.patch.set_facecolor('#f8f9fa')
ax.set_facecolor('#f8f9fa')

bars = ax.bar(labels, values, color=colors, alpha=0.8)

# Add values and percentages on top of bars
for bar, val, chg in zip(bars, values, change_labels):
    height = bar.get_height()
    ax.text(bar.get_x() + bar.get_width()/2., height,
            f'{val:,.2f}\n({chg})',
            ha='center', va='bottom', fontsize=12, fontweight='bold')

ax.set_title('全球核心资产行情 (2026-04-25 早报)', fontproperties=prop, fontsize=16, pad=20)
ax.set_ylabel('点位/价格', fontproperties=prop, fontsize=12)
ax.tick_params(axis='x', labelsize=12)
ax.set_xticklabels(labels, fontproperties=prop)

# Remove spines
for spine in ['top', 'right']:
    ax.spines[spine].set_visible(False)

plt.tight_layout()

# Ensure directory exists
os.makedirs('images/charts', exist_ok=True)
output_path = 'images/charts/2026-04-25-morning.png'
plt.savefig(output_path, facecolor=fig.get_facecolor())
print(f'Chart saved to {output_path}')
