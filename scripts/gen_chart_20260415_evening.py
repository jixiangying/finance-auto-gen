import matplotlib.pyplot as plt
import matplotlib.font_manager as fm
import os

# 设置中文字体
font_path = '/System/Library/Fonts/STHeiti Medium.ttc'
if not os.path.exists(font_path):
    font_path = '/System/Library/Fonts/PingFang.ttc' # 备选

prop = fm.FontProperties(fname=font_path)
plt.rcParams['font.family'] = prop.get_name()
plt.rcParams['axes.unicode_minus'] = False

# 数据
labels = ['上证指数', '深证成指', '创业板指', '恒生指数', '恒生科技']
prices = [4027.21, 14498.45, 3514.96, 25947.32, 4911.79]
pct_changes = [0.01, -0.97, -1.22, 0.29, 1.23]
colors = ['#ff4c4c' if x >= 0 else '#00ad00' for x in pct_changes] # 红色上涨，绿色下跌

fig, ax1 = plt.subplots(figsize=(10, 6))

# 柱状图显示价格（对齐不同量级，这里其实不太好画在一起，改为显示涨跌幅比较直观）
# 重新设计：显示涨跌幅的条形图
bars = ax1.bar(labels, pct_changes, color=colors)

# 添加数值标注
for bar, pct in zip(bars, pct_changes):
    yval = bar.get_height()
    ax1.text(bar.get_x() + bar.get_width()/2, yval + (0.05 if yval > 0 else -0.15), 
             f'{pct:+.2f}%', ha='center', va='bottom' if yval > 0 else 'top', 
             fontproperties=prop, fontsize=12, fontweight='bold')

ax1.axhline(0, color='black', linewidth=0.8)
ax1.set_title('2026-04-15 收盘主要指数表现', fontproperties=prop, fontsize=16)
ax1.set_ylabel('涨跌幅 (%)', fontproperties=prop)
ax1.set_xticklabels(labels, fontproperties=prop)

# 保存图片
output_path = 'images/charts/2026-04-15-evening.png'
os.makedirs(os.path.dirname(output_path), exist_ok=True)
plt.savefig(output_path, dpi=300, bbox_inches='tight')
print(f"Chart saved to {output_path}")
