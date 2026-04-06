import matplotlib.pyplot as plt
import matplotlib.font_manager as fm
import os

# 设置中文字体
font_path = '/System/Library/Fonts/STHeiti Medium.ttc'
if not os.path.exists(font_path):
    font_path = '/System/Library/Fonts/PingFang.ttc'

prop = fm.FontProperties(fname=font_path)

# 数据准备
assets = ['A50期货', '离岸人民币', '比特币', '现货黄金', 'WTI原油']
prices = ['14,600', '6.880', '69,520', '4,680', '113.2']
changes = [0.42, -0.12, 2.65, -0.45, 1.25]  # 百分比
colors = ['red' if c > 0 else 'green' for c in changes]
change_labels = [f'+{c}%' if c > 0 else f'{c}%' for c in changes]

# 创建画布
fig, ax = plt.subplots(figsize=(10, 6), dpi=100)
fig.patch.set_facecolor('#f4f4f4')
ax.set_facecolor('#f4f4f4')

# 隐藏坐标轴
ax.axis('off')

# 标题
plt.text(0.5, 0.9, '清明假期：全球代偿资产及宏观指标 (2026-04-06)', 
         horizontalalignment='center', fontsize=20, fontproperties=prop, fontweight='bold')

# 绘制卡片
for i in range(len(assets)):
    y_pos = 0.7 - i * 0.15
    # 资产名
    plt.text(0.2, y_pos, assets[i], fontsize=16, fontproperties=prop, verticalalignment='center')
    # 价格
    plt.text(0.5, y_pos, prices[i], fontsize=16, fontweight='bold', verticalalignment='center')
    # 涨跌幅
    plt.text(0.8, y_pos, change_labels[i], fontsize=16, color=colors[i], fontweight='bold', verticalalignment='center')
    # 分隔线
    ax.axhline(y_pos - 0.07, xmin=0.15, xmax=0.85, color='gray', linestyle='--', linewidth=0.5, alpha=0.5)

# 保存图片
output_path = 'images/charts/2026-04-06-evening.png'
os.makedirs(os.path.dirname(output_path), exist_ok=True)
plt.savefig(output_path, bbox_inches='tight', facecolor=fig.get_facecolor())
print(f"Chart saved to {output_path}")
