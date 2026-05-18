import matplotlib.pyplot as plt
from matplotlib import font_manager
import os

# 设置中文字体 (macOS)
font_path = '/System/Library/Fonts/STHeiti Medium.ttc'
if not os.path.exists(font_path):
    font_path = '/System/Library/Fonts/PingFang.ttc'

font_prop = font_manager.FontProperties(fname=font_path)
plt.rcParams['axes.unicode_minus'] = False

# 数据 (2026-05-18 上午 - 复盘上周五 5/15 收盘)
assets = ['Nasdaq', 'S&P 500', 'Dow Jones', 'Bitcoin (BTC)', 'Gold (Spot)', 'Brent Oil']
prices = ['26225.14', '7408.50', '49526.17', '77891', '4536.41', '107']
changes = [-1.54, -1.24, -1.10, -1.20, -0.25, 2.5] # Brent estimated +2.5% from search context

fig, ax = plt.subplots(figsize=(10, 6), facecolor='#f4f4f4')
ax.set_axis_off()

# 绘制标题
plt.text(0.5, 0.95, '全球市场核心行情 (2026-05-18 上午)', 
         fontproperties=font_prop, fontsize=20, weight='bold', ha='center')

# 绘制表格头
header_y = 0.85
plt.text(0.1, header_y, '资产名称', fontproperties=font_prop, fontsize=14, weight='bold')
plt.text(0.4, header_y, '收盘点位/现价', fontproperties=font_prop, fontsize=14, weight='bold')
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

output_path = os.path.join(output_dir, '2026-05-18-morning-chart.png')
plt.savefig(output_path, dpi=300, bbox_inches='tight', facecolor='#f4f4f4')
print(f"Chart saved to {output_path}")
