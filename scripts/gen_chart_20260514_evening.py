import matplotlib.pyplot as plt
import matplotlib.font_manager as fm
import os

# 设置中文字体 (macOS)
font_path = '/System/Library/Fonts/STHeiti Medium.ttc'
prop = fm.FontProperties(fname=font_path)
plt.rcParams['font.family'] = prop.get_name()
plt.rcParams['axes.unicode_minus'] = False

# 数据
indices = ['上证指数', '深证成指', '创业板指', '科创50', '恒生指数']
values = [4177.92, 15745.43, 3951.10, 1725.01, 26389.04]
changes = [-1.52, -2.14, -2.16, -2.55, 0.00]
colors = ['green' if c < 0 else 'red' if c > 0 else 'gray' for c in changes]

fig, ax1 = plt.subplots(figsize=(10, 6))

# 柱状图显示点位
bars = ax1.bar(indices, values, color='lightgray', alpha=0.3)
ax1.set_ylabel('收盘点位', fontproperties=prop)
ax1.tick_params(axis='y')

# 在柱状图上方标注具体数值
for bar, val in zip(bars, values):
    ax1.text(bar.get_x() + bar.get_width()/2, bar.get_height(), f'{val:.2f}', 
             ha='center', va='bottom', fontsize=10)

# 折线图或散点图显示涨跌幅
ax2 = ax1.twinx()
ax2.axhline(0, color='black', linewidth=0.8, linestyle='--')
points = ax2.scatter(indices, changes, color=colors, s=100, zorder=3)
for i, txt in enumerate(changes):
    ax2.annotate(f'{txt:+.2f}%', (indices[i], changes[i]), xytext=(0, 10 if changes[i]>=0 else -15), 
                 textcoords='offset points', ha='center', color=colors[i], fontproperties=prop, fontweight='bold')

ax2.set_ylabel('涨跌幅 (%)', fontproperties=prop)
ax2.set_ylim(min(changes)-1, max(changes)+1)

plt.title('2026年5月14日 核心指数收盘表现', fontproperties=prop, fontsize=16)
ax1.set_xticklabels(indices, fontproperties=prop)

# 保存图片
output_dir = 'images/charts'
os.makedirs(output_dir, exist_ok=True)
output_path = os.path.join(output_dir, '20260514_evening.png')
plt.tight_layout()
plt.savefig(output_path, dpi=300)
print(f'Chart saved to {output_path}')
