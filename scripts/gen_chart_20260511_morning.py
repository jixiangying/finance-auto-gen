import matplotlib.pyplot as plt
import matplotlib.font_manager as fm
import os

# 设置字体以支持中文 (macOS)
font_path = '/System/Library/Fonts/STHeiti Medium.ttc'
if not os.path.exists(font_path):
    font_path = '/System/Library/Fonts/PingFang.ttc'
prop = fm.FontProperties(fname=font_path)

# 数据
labels = ['Nasdaq', 'S&P 500', 'Dow Jones', 'Russell 2000']
prices = [26247.08, 7398.93, 49609.16, 2861.21]
changes = [1.71, 0.84, 0.02, 0.80]
colors = ['#ff4d4d' if c > 0 else '#2ecc71' for c in changes] # 红色上涨，绿色下跌

fig, ax = plt.subplots(figsize=(10, 6))
bars = ax.bar(labels, changes, color=colors)

# 添加数值标签
for bar, change, price in zip(bars, changes, prices):
    height = bar.get_height()
    ax.text(bar.get_x() + bar.get_width()/2., height + 0.05 if height > 0 else height - 0.1,
            f'{price:,.2f}\n({"+" if change > 0 else ""}{change}%)',
            ha='center', va='bottom' if height > 0 else 'top', fontproperties=prop, fontsize=10)

ax.set_ylabel('涨跌幅 (%)', fontproperties=prop)
ax.set_title('全球核心指数上周五收盘表现 (2026-05-08)', fontproperties=prop, fontsize=14)
ax.axhline(0, color='black', linewidth=0.8)

# 显式设置坐标轴字体防止乱码
ax.set_xticklabels(labels, fontproperties=prop)
plt.yticks(fontproperties=prop)

plt.tight_layout()
output_path = 'images/charts/20260511_morning.png'
os.makedirs(os.path.dirname(output_path), exist_ok=True)
plt.savefig(output_path, dpi=300)
print(f"Chart saved to {output_path}")
