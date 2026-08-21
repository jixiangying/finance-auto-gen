import matplotlib.pyplot as plt
import numpy as np
import matplotlib as mpl

# Set font for Chinese
mpl.rcParams['font.sans-serif'] = ['PingFang SC', 'STHeiti', 'SimHei', 'Arial']
mpl.rcParams['axes.unicode_minus'] = False

labels = ['上证指数', '深证成指', '创业板指', '科创50', '恒生指数', '恒生科技']
changes = [0.04, 0.87, 1.43, 0.04, 0.30, 0.50]
colors = ['#ff4d4f' if x > 0 else '#52c41a' for x in changes]

fig, ax = plt.subplots(figsize=(10, 6))
bars = ax.bar(labels, changes, color=colors, width=0.5)

ax.set_title('今日核心资产表现 (2026-08-21)', fontsize=16, fontweight='bold', pad=20)
ax.set_ylabel('涨跌幅 (%)', fontsize=12)
ax.grid(axis='y', linestyle='--', alpha=0.7)

for bar in bars:
    height = bar.get_height()
    label_y = height + 0.05 if height > 0 else height - 0.1
    ax.text(bar.get_x() + bar.get_width()/2, label_y, f'{height:+.2f}%', 
            ha='center', va='bottom' if height > 0 else 'top', fontsize=11, fontweight='bold')

plt.tight_layout()
plt.savefig('/Users/jxy/Documents/Project/finance-auto-gen/images/charts/2026-08-21-evening.png', dpi=300)
