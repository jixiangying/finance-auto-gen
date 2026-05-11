import matplotlib.pyplot as plt
import matplotlib.font_manager as fm
import os

# Font setup for macOS
font_path = '/System/Library/Fonts/STHeiti Medium.ttc'
if not os.path.exists(font_path):
    font_path = '/System/Library/Fonts/PingFang.ttc'

prop = fm.FontProperties(fname=font_path)

# Data
indices = ['上证指数', '深证成指', '创业板指', '成交额(万亿)']
values = [4225.18, 14544.11, 3956.41, 3.59]
changes = [1.08, 2.16, 3.50, 15.8] # 15.8% increase in volume approx (from 3.1 to 3.59)
colors = ['#e63946' if c > 0 else '#2a9d8f' for c in changes]

fig, ax = plt.subplots(figsize=(10, 6))
fig.patch.set_facecolor('#f8f9fa')
ax.set_facecolor('#f8f9fa')

bars = ax.bar(indices, values, color=colors, alpha=0.8)

# Add value labels
for bar, change in zip(bars, changes):
    height = bar.get_height()
    ax.text(bar.get_x() + bar.get_width()/2., height + 0.05,
            f'{height:,.2f}\n({"+" if change > 0 else ""}{change}%)',
            ha='center', va='bottom', fontproperties=prop, fontsize=12, fontweight='bold')

ax.set_title('A股核心指数收盘表现 (2026-05-11)', fontproperties=prop, fontsize=18, pad=20)
ax.set_ylabel('点位 / 成交额', fontproperties=prop, fontsize=14)
ax.tick_params(axis='x', labelsize=12)
ax.set_xticklabels(indices, fontproperties=prop)

# Remove top and right spines
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)

plt.tight_layout()
plt.savefig('images/charts/20260511_evening.png', dpi=300)
print("Chart saved to images/charts/20260511_evening.png")
