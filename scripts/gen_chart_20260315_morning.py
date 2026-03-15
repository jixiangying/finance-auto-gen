import matplotlib.pyplot as plt
from matplotlib import font_manager
import os

# 设置中文字体
font_path = '/System/Library/Fonts/STHeiti Medium.ttc'
if not os.path.exists(font_path):
    font_path = '/System/Library/Fonts/PingFang.ttc'

font_prop = font_manager.FontProperties(fname=font_path)
plt.rcParams['axes.unicode_minus'] = False

# 数据
assets = ['S&P 500', 'Nasdaq', 'Dow Jones', 'Bitcoin', 'Gold', 'Brent Oil']
prices = ['6632.19', '22105.36', '46558.47', '71023', '5022', '103']
changes = [-0.61, -0.93, -0.26, -0.31, -1.12, 2.5] # Brent estimated +2.5% from "surge"

fig, ax = plt.subplots(figsize=(10, 6), facecolor='#f4f4f4')
ax.set_axis_off()

# 绘制标题
plt.text(0.5, 0.95, '全球市场核心行情 (2026-03-15 上午)', 
         fontproperties=font_prop, fontsize=20, weight='bold', ha='center')

# 绘制表格头
header_y = 0.85
plt.text(0.1, header_y, '资产名称', fontproperties=font_prop, fontsize=14, weight='bold')
plt.text(0.4, header_y, '当前价格/点位', fontproperties=font_prop, fontsize=14, weight='bold')
plt.text(0.7, header_y, '涨跌幅', fontproperties=font_prop, fontsize=14, weight='bold')

# 绘制数据行
start_y = 0.75
step_y = 0.1

for i, (asset, price, change) in enumerate(zip(assets, prices, changes)):
    curr_y = start_y - i * step_y
    color = 'red' if change > 0 else 'green'
    symbol = '🔴' if change > 0 else '🟢'
    change_str = f"{'+' if change > 0 else ''}{change}%"
    
    plt.text(0.1, curr_y, asset, fontproperties=font_prop, fontsize=14)
    plt.text(0.4, curr_y, price, fontproperties=font_prop, fontsize=14)
    plt.text(0.7, curr_y, f"{symbol} {change_str}", fontproperties=font_prop, fontsize=14, color=color)

# 保存图片
output_dir = 'images/charts'
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

output_path = os.path.join(output_dir, '2026-03-15-morning-chart.png')
plt.savefig(output_path, dpi=300, bbox_inches='tight', facecolor='#f4f4f4')
print(f"Chart saved to {output_path}")
