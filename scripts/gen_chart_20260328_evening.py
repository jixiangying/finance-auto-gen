import matplotlib.pyplot as plt
import matplotlib.font_manager as fm
import os

# Font configuration for macOS
font_path = '/System/Library/Fonts/STHeiti Medium.ttc'
if not os.path.exists(font_path):
    font_path = '/System/Library/Fonts/PingFang.ttc'

prop = fm.FontProperties(fname=font_path)
plt.rcParams['font.sans-serif'] = [prop.get_name()]
plt.rcParams['axes.unicode_minus'] = False

# Data
labels = ['上证指数', '深证成指', '创业板指', '恒生指数', '恒生科技']
prices = [3915.65, 13760.19, 3313.13, 25031.31, 4778.00]
changes = [0.68, 1.13, 0.71, 0.70, 0.30]
colors = ['#e63946' if c > 0 else '#2a9d8f' for c in changes] # Red for up, Green for down

fig, ax = plt.subplots(figsize=(10, 6), dpi=100)
fig.patch.set_facecolor('#f8f9fa')
ax.set_facecolor('#f8f9fa')

bars = ax.bar(labels, changes, color=colors, alpha=0.8, width=0.6)

# Add price and percentage labels
for bar, price, change in zip(bars, prices, changes):
    height = bar.get_height()
    ax.text(bar.get_x() + bar.get_width()/2., height + 0.02,
            f'{price}\n({"+" if change > 0 else ""}{change}%)',
            ha='center', va='bottom', fontproperties=prop, fontsize=12, fontweight='bold', color=bar.get_facecolor())

ax.set_ylabel('当日涨跌幅 (%)', fontproperties=prop, fontsize=12)
ax.set_title('2026-03-27 国内核心指数收盘表现', fontproperties=prop, fontsize=16, fontweight='bold', pad=20)
ax.axhline(0, color='black', linewidth=0.8, linestyle='--')

# Set tick labels font
ax.set_xticklabels(labels, fontproperties=prop, fontsize=12)
for label in ax.get_yticklabels():
    label.set_fontproperties(prop)

plt.tight_layout()
output_path = 'images/charts/2026-03-28-evening.png'
os.makedirs(os.path.dirname(output_path), exist_ok=True)
plt.savefig(output_path, facecolor=fig.get_facecolor())
print(f"Chart saved to {output_path}")
