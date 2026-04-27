import matplotlib.pyplot as plt
import matplotlib.font_manager as fm
import os

# 资产数据
assets = ['上证指数', '深证成指', '创业板指', '科创50', '恒生指数', '恒生科技']
prices = ['4086.34', '14995.75', '3648.79', '1182.45', '25925', '4938']
changes = ['+0.16%', '+0.37%', '-0.52%', '+3.76%', '-0.20%', '+0.77%']
colors = ['#e15759', '#e15759', '#76b7b2', '#e15759', '#76b7b2', '#e15759'] # 红色上涨，绿色下跌

# 设置字体 (macOS 路径)
font_path = '/System/Library/Fonts/STHeiti Medium.ttc'
if not os.path.exists(font_path):
    font_path = '/System/Library/Fonts/PingFang.ttc'

prop = fm.FontProperties(fname=font_path)

fig, ax = plt.subplots(figsize=(10, 7), facecolor='#f0f2f5')
fig.patch.set_facecolor('#f0f2f5')
ax.set_facecolor('#f0f2f5')

# 隐藏坐标轴
ax.axis('off')

# 绘制标题
plt.text(0.5, 0.92, '今日市场核心数据 (2026-04-27 收盘)', 
         fontproperties=prop, fontsize=20, weight='bold', ha='center')

# 绘制表格表头
headers = ['资产名称', '收盘点位', '当日涨跌']
for i, h in enumerate(headers):
    plt.text(0.2 + i*0.3, 0.8, h, fontproperties=prop, fontsize=14, weight='bold', ha='center')

# 绘制数据行
for i in range(len(assets)):
    y_pos = 0.7 - i*0.09
    # 资产名
    plt.text(0.2, y_pos, assets[i], fontproperties=prop, fontsize=14, ha='center')
    # 价格
    plt.text(0.5, y_pos, prices[i], fontproperties=prop, fontsize=14, ha='center')
    # 涨跌幅
    plt.text(0.8, y_pos, changes[i], fontproperties=prop, fontsize=14, ha='center', color=colors[i], weight='bold')
    
    # 画分割线
    ax.axhline(y_pos - 0.04, xmin=0.1, xmax=0.9, color='gray', linestyle='--', alpha=0.3)

# 页脚
plt.text(0.5, 0.1, '数据来源：东方财富/同花顺/恒生指数官网 | 统计时段：2026-04-27 16:30', 
         fontproperties=prop, fontsize=10, color='gray', ha='center')

# 保存图片
output_path = 'images/charts/2026-04-27-evening.png'
# 确保目录存在
os.makedirs(os.path.dirname(output_path), exist_ok=True)
plt.savefig(output_path, dpi=300, bbox_inches='tight', facecolor='#f0f2f5')
print(f'Chart saved to {output_path}')
