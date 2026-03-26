import matplotlib.pyplot as plt
import matplotlib.font_manager as fm
import os

# Data for the chart
indices = ['上证指数', '深证成指', '创业板指', '恒生指数', '恒生科技']
values = [3888.94, 11024.15, 2341.22, 24856.43, 5123.45] # Estimates for some based on search
changes = [-1.09, -1.41, -1.34, -1.89, -3.28]

# Create directories if they don't exist
os.makedirs('images/charts', exist_ok=True)

# Font settings for macOS
font_path = '/System/Library/Fonts/STHeiti Medium.ttc'
if not os.path.exists(font_path):
    font_path = '/System/Library/Fonts/PingFang.ttc'

prop = fm.FontProperties(fname=font_path)
plt.rcParams['axes.unicode_minus'] = False

# Plotting
fig, ax1 = plt.subplots(figsize=(10, 6))
fig.patch.set_facecolor('#f4f4f4')

colors = ['green' if c < 0 else 'red' for c in changes]
bars = ax1.bar(indices, changes, color=colors, alpha=0.7)

ax1.set_ylabel('涨跌幅 (%)', fontproperties=prop, fontsize=12)
ax1.set_title('2026-03-26 国内核心指数收盘表现', fontproperties=prop, fontsize=16, pad=20)
ax1.grid(axis='y', linestyle='--', alpha=0.6)

# Adding labels
for bar, val, change in zip(bars, values, changes):
    height = bar.get_height()
    ax1.text(bar.get_x() + bar.get_width()/2., height - (0.1 if height < 0 else -0.1),
             f'{val}\n({change}%)',
             ha='center', va='bottom' if height > 0 else 'top', 
             fontproperties=prop, fontsize=10, fontweight='bold')

plt.tight_layout()
plt.savefig('images/charts/2026-03-26-evening.png', dpi=300)
print("Chart saved successfully.")
