import matplotlib.pyplot as plt
import matplotlib.font_manager as fm
import os

# 设置中文字体
font_path = '/System/Library/Fonts/STHeiti Medium.ttc'
if not os.path.exists(font_path):
    font_path = '/System/Library/Fonts/PingFang.ttc'

prop = fm.FontProperties(fname=font_path)
plt.rcParams['font.sans-serif'] = [prop.get_name()]
plt.rcParams['axes.unicode_minus'] = False

# 数据
labels = ['上证指数', '深证成指', '创业板指', '科创综指', '恒生指数']
values = [0.11, -0.09, -0.27, 3.42, -1.39]
points = ['4112.16', '15107.55', '3677.15', '1950.43', '25748.00']
colors = ['#ff4d4f' if v > 0 else '#52c41a' for v in values]

fig, ax = plt.subplots(figsize=(10, 6))
bars = ax.bar(labels, values, color=colors)

# 添加数值和百分比
for bar, point, val in zip(bars, points, values):
    height = bar.get_height()
    label_text = f'{point}\n({"+" if val > 0 else ""}{val}%)'
    ax.text(bar.get_x() + bar.get_width()/2., height if height > 0 else height - 0.2,
            label_text, ha='center', va='bottom' if height > 0 else 'top', 
            fontproperties=prop, fontsize=10, fontweight='bold')

# 美化
ax.axhline(0, color='black', linewidth=0.8)
ax.set_title('2026年4月30日 核心市场收盘表现', fontproperties=prop, fontsize=16)
ax.set_ylabel('涨跌幅 (%)', fontproperties=prop)
ax.set_ylim(min(values) - 1, max(values) + 1)
ax.set_xticklabels(labels, fontproperties=prop)

# 保存
output_path = 'images/charts/20260430_evening.png'
plt.savefig(output_path, dpi=300, bbox_inches='tight')
print(f"Chart saved to {output_path}")
