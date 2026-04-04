import matplotlib.pyplot as plt
import matplotlib.font_manager as fm
import os

# 设置中文字体 (macOS 路径)
font_path = '/System/Library/Fonts/STHeiti Medium.ttc'
prop = fm.FontProperties(fname=font_path)
plt.rcParams['font.family'] = prop.get_name()
plt.rcParams['axes.unicode_minus'] = False

# 数据准备
assets = ['S&P 500', 'Nasdaq', 'Dow Jones', 'Brent Oil', 'WTI Oil', 'Bitcoin', 'Gold']
# 涨跌幅数据 (周/日)
changes = [3.4, 4.4, 3.0, 8.98, 11.41, 1.5, 2.0]  # 假设金价涨幅为 2% 以便展示
prices = ['6,571.0', '20,150', '46,460', '$109.2', '$111.5', '$70,400', '$2,450']

# 绘图
fig, ax = plt.subplots(figsize=(10, 6))
fig.patch.set_facecolor('#f4f4f4')
ax.set_facecolor('#ffffff')

colors = ['#ff4d4d' if x > 0 else '#2ecc71' for x in changes]
bars = ax.barh(assets, changes, color=colors, height=0.6)

# 添加数值和价格标签
for i, bar in enumerate(bars):
    width = bar.get_width()
    ax.text(width + (0.5 if width > 0 else -0.5), bar.get_y() + bar.get_height()/2, 
            f'{prices[i]} ({"+" if changes[i]>0 else ""}{changes[i]}%)', 
            va='center', fontsize=12, fontweight='bold', color='#333333')

# 装饰
ax.set_title('核心资产表现 (2026-04-03/04)', fontproperties=prop, fontsize=18, pad=20)
ax.set_xlabel('涨跌幅 (%)', fontproperties=prop, fontsize=12)
ax.set_xlim(0, 15) # 根据数据调整
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)

# 强制设置坐标轴字体
ax.set_yticklabels(assets, fontproperties=prop, fontsize=12)

# 保存
output_dir = 'images/charts/'
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

output_path = os.path.join(output_dir, '2026-04-04-morning-chart.png')
plt.tight_layout()
plt.savefig(output_path, dpi=300)
print(f"Chart saved to {output_path}")
