import matplotlib.pyplot as plt
import matplotlib.font_manager as fm
import os

# 配置中文字体 (macOS)
font_path = '/System/Library/Fonts/STHeiti Medium.ttc'
prop = fm.FontProperties(fname=font_path)
plt.rcParams['font.family'] = prop.get_name()
plt.rcParams['axes.unicode_minus'] = False

# 数据
labels = ['上证指数', '沪深300', '恒生指数', '布伦特原油', '比特币']
prices = ['3989.00', '4631.00', '25587.26', '107.28', '73500']
changes = [0.07, -0.12, -1.2, 8.5, 2.5]

# 颜色：红涨绿跌
colors = ['#ff4d4f' if c > 0 else '#52c41a' for c in changes]
change_texts = [f'{"+" if c > 0 else ""}{c}%' for c in changes]

fig, ax = plt.subplots(figsize=(10, 6))
fig.patch.set_facecolor('#f0f2f5')
ax.set_facecolor('#f0f2f5')

# 绘制条形图
bars = ax.bar(labels, [abs(c) for c in changes], color=colors, alpha=0.8)

# 添加价格和涨跌幅文本
for i, bar in enumerate(bars):
    height = bar.get_height()
    ax.text(bar.get_x() + bar.get_width()/2., height + 0.1,
            f'{prices[i]}\n({change_texts[i]})',
            ha='center', va='bottom', fontsize=12, fontweight='bold', color=colors[i])

# 设置样式
ax.set_title('今日市场核心指标收盘表现 (2026-04-13 Evening)', fontproperties=prop, fontsize=16, pad=20)
ax.set_ylabel('涨跌幅绝对值 (%)', fontproperties=prop, fontsize=12)
ax.set_ylim(0, max([abs(c) for c in changes]) + 2)
ax.set_xticklabels(labels, fontproperties=prop, fontsize=12)

# 移除边框
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)

# 保存图片
output_dir = 'images/charts'
if not os.path.exists(output_dir):
    os.makedirs(output_dir)
output_path = os.path.join(output_dir, '2026-04-13-evening.png')
plt.savefig(output_path, dpi=300, bbox_inches='tight')
print(f"Chart saved to {output_path}")
