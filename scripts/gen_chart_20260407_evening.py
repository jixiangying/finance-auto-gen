import matplotlib.pyplot as plt
import matplotlib.font_manager as fm
import os

# 设置中文字体
font_path = '/System/Library/Fonts/STHeiti Medium.ttc'
if not os.path.exists(font_path):
    font_path = '/System/Library/Fonts/PingFang.ttc'

prop = fm.FontProperties(fname=font_path)

# 数据准备
assets = ['上证指数', '深证成指', '创业板指', '两市成交', '恒生指数']
prices = ['3890.16', '13400.41', '3160.82', '1.61万亿', '休市']
changes = [0.26, 0.36, 0.36, -2.54, 0.00]  # 百分比
colors = ['red' if c > 0 else ('green' if c < 0 else 'gray') for c in changes]
change_labels = [f'+{c}%' if c > 0 else (f'{c}%' if c < 0 else '0.00%') for c in changes]

# 修正成交额标签
change_labels[3] = f'-2.54%' # 缩量

# 创建画布
fig, ax = plt.subplots(figsize=(10, 6), dpi=100)
fig.patch.set_facecolor('#f4f4f4')
ax.set_facecolor('#f4f4f4')

# 隐藏坐标轴
ax.axis('off')

# 标题
plt.text(0.5, 0.9, 'A股收盘复盘：清明后首日“开门红” (2026-04-07)', 
         horizontalalignment='center', fontsize=20, fontproperties=prop, fontweight='bold')

# 绘制卡片
for i in range(len(assets)):
    y_pos = 0.7 - i * 0.15
    # 资产名
    plt.text(0.2, y_pos, assets[i], fontsize=16, fontproperties=prop, verticalalignment='center')
    # 价格
    plt.text(0.5, y_pos, prices[i], fontsize=16, fontweight='bold', verticalalignment='center', fontproperties=prop)
    # 涨跌幅
    plt.text(0.8, y_pos, change_labels[i], fontsize=16, color=colors[i], fontweight='bold', verticalalignment='center', fontproperties=prop)
    # 分隔线
    ax.axhline(y_pos - 0.07, xmin=0.15, xmax=0.85, color='gray', linestyle='--', linewidth=0.5, alpha=0.5)

# 保存图片
output_path = 'images/charts/2026-04-07-evening.png'
os.makedirs(os.path.dirname(output_path), exist_ok=True)
plt.savefig(output_path, bbox_inches='tight', facecolor=fig.get_facecolor())
print(f"Chart saved to {output_path}")
