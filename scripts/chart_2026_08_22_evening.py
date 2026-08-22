import matplotlib.pyplot as plt
import numpy as np
import matplotlib as mpl
import os

# Set font for Chinese
mpl.rcParams['font.sans-serif'] = ['PingFang SC', 'STHeiti', 'Arial Unicode MS', 'SimHei', 'sans-serif']
mpl.rcParams['axes.unicode_minus'] = False

labels = ['上证指数', '深证成指', '创业板指', '恒生指数', '标普500', '纳斯达克']
friday_changes = [0.04, 0.87, 1.43, 1.21, 0.35, 0.42]
weekly_changes = [-0.56, -0.32, -2.23, 3.55, -1.43, -2.05]

x = np.arange(len(labels))
width = 0.35

fig, ax = plt.subplots(figsize=(11, 6))

rects1 = ax.bar(x - width/2, friday_changes, width, label='周五单日涨跌 (%)', color='#ff7875', edgecolor='#ff4d4f', alpha=0.9)
rects2 = ax.bar(x + width/2, weekly_changes, width, label='全周累计涨跌 (%)', color='#4096ff', edgecolor='#1677ff', alpha=0.9)

ax.set_title('核心资产周度/日度表现对比 (2026-08-22 周末复盘)', fontsize=15, fontweight='bold', pad=15)
ax.set_ylabel('涨跌幅 (%)', fontsize=12)
ax.set_xticks(x)
ax.set_xticklabels(labels, fontsize=11, fontweight='bold')
ax.axhline(0, color='gray', linewidth=0.8, linestyle='--')
ax.grid(axis='y', linestyle=':', alpha=0.6)
ax.legend(loc='upper right', fontsize=11)

def autolabel(rects, is_friday=True):
    for rect in rects:
        height = rect.get_height()
        va = 'bottom' if height >= 0 else 'top'
        y_pos = height + 0.08 if height >= 0 else height - 0.20
        ax.annotate(f'{height:+.2f}%',
                    xy=(rect.get_x() + rect.get_width() / 2, y_pos),
                    xytext=(0, 0),
                    textcoords="offset points",
                    ha='center', va=va, fontsize=9.5, fontweight='bold')

autolabel(rects1, True)
autolabel(rects2, False)

plt.tight_layout()
os.makedirs('/Users/jxy/Documents/Project/finance-auto-gen/images/charts', exist_ok=True)
plt.savefig('/Users/jxy/Documents/Project/finance-auto-gen/images/charts/2026-08-22-evening.png', dpi=300)
print("Chart generated successfully at images/charts/2026-08-22-evening.png")
