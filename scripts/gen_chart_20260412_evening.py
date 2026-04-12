import matplotlib.pyplot as plt
import matplotlib.font_manager as fm
import os

# 资产数据
assets = ['FTSE A50', 'USD/CNH', 'Bitcoin', 'WTI Crude']
prices = ['15,038', '6.8263', '$72,840', '$92']
changes = ['+1.78%', '-0.12%', '+0.85%', '-13.4%']
colors = ['#e15759', '#76b7b2', '#e15759', '#76b7b2'] # 红色上涨，绿色下跌

# 设置字体 (macOS 路径)
font_path = '/System/Library/Fonts/STHeiti Medium.ttc'
if not os.path.exists(font_path):
    font_path = '/System/Library/Fonts/PingFang.ttc'

prop = fm.FontProperties(fname=font_path)

fig, ax = plt.subplots(figsize=(10, 6), facecolor='#f0f2f5')
fig.patch.set_facecolor('#f0f2f5')
ax.set_facecolor('#f0f2f5')

# 隐藏坐标轴
ax.axis('off')

# 绘制标题
plt.text(0.5, 0.9, '核心资产新周开盘参考 (2026-04-12)', 
         fontproperties=prop, fontsize=20, weight='bold', ha='center')

# 绘制表格表头
headers = ['资产名称', '当前价格/点位', '近24h/周变动']
for i, h in enumerate(headers):
    plt.text(0.2 + i*0.3, 0.75, h, fontproperties=prop, fontsize=14, weight='bold', ha='center')

# 绘制数据行
for i in range(len(assets)):
    y_pos = 0.6 - i*0.12
    # 资产名
    plt.text(0.2, y_pos, assets[i], fontproperties=prop, fontsize=14, ha='center')
    # 价格
    plt.text(0.5, y_pos, prices[i], fontproperties=prop, fontsize=14, ha='center')
    # 涨跌幅
    plt.text(0.8, y_pos, changes[i], fontproperties=prop, fontsize=14, ha='center', color=colors[i], weight='bold')
    
    # 画分割线
    ax.axhline(y_pos - 0.05, xmin=0.1, xmax=0.9, color='gray', linestyle='--', alpha=0.3)

# 页脚
plt.text(0.5, 0.1, '数据来源：路透/东方财富/币安 | 提示：A50及油价为期货收盘或预期', 
         fontproperties=prop, fontsize=10, color='gray', ha='center')

# 保存图片
output_path = 'images/charts/2026-04-12-evening.png'
plt.savefig(output_path, dpi=300, bbox_inches='tight', facecolor='#f0f2f5')
print(f'Chart saved to {output_path}')
