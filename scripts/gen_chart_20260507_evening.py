import matplotlib.pyplot as plt
import matplotlib.font_manager as fm
import os

# 配置中文字体
font_path = '/System/Library/Fonts/STHeiti Medium.ttc'
if not os.path.exists(font_path):
    font_path = '/System/Library/Fonts/PingFang.ttc'

prop = fm.FontProperties(fname=font_path)
plt.rcParams['font.family'] = prop.get_name()
plt.rcParams['axes.unicode_minus'] = False

# 数据
labels = ['上证指数', '深证成指', '创业板指', '恒生指数']
prices = [4180.00, 15642.00, 3833.00, 26630.00]
changes = [0.48, 1.18, 1.45, 1.57]
colors = ['#e63946' if c > 0 else '#2a9d8f' for c in changes] # 红涨绿跌

fig, ax = plt.subplots(figsize=(10, 6), dpi=100)
fig.patch.set_facecolor('#f8f9fa')
ax.set_facecolor('#f8f9fa')

bars = ax.bar(labels, changes, color=colors, edgecolor='white', linewidth=1.5)

# 隐藏边框
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
ax.spines['left'].set_visible(False)
ax.get_yaxis().set_visible(False)

# 设置标题
ax.set_title('核心行情概览 (2026-05-07 收盘)', fontproperties=prop, fontsize=18, pad=20, color='#333')

# 添加数值标注
for bar, price, change in zip(bars, prices, changes):
    height = bar.get_height()
    ax.text(bar.get_x() + bar.get_width()/2., height + 0.05,
            f'{price:,.2f}\n({"+" if change > 0 else ""}{change}%)',
            ha='center', va='bottom', fontproperties=prop, fontsize=12, color=bar.get_facecolor())

ax.set_xticklabels(labels, fontproperties=prop, fontsize=14)

# 保存
output_dir = 'images/charts'
os.makedirs(output_dir, exist_ok=True)
output_path = os.path.join(output_dir, '2026-05-07-evening.png')
plt.savefig(output_path, bbox_inches='tight', facecolor=fig.get_facecolor())
print(f"Chart saved to {output_path}")
