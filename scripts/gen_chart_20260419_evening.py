import matplotlib.pyplot as plt
import matplotlib.font_manager as fm
import os

# 资产数据 (截至 2026-04-19 展望)
assets = ['纳斯达克 (Nasdaq)', '标普 500 (S&P 500)', '比特币 (Bitcoin)', 'WTI 原油 (Crude)', 'USD/CNH (离岸)']
prices = ['24,468.48', '7,126.06', '75,644', '83.85', '6.8149']
changes = ['+1.52%', '+1.20%', '+2.1% (Weekend)', '-10.84% (Crash)', '-0.15% (CNY Strong)']

# 颜色设置 (红色上涨 #e63946, 绿色下跌 #008000)
colors = ['#e63946', '#e63946', '#e63946', '#008000', '#008000']

# 设置中文字体 (macOS)
font_path = '/System/Library/Fonts/STHeiti Medium.ttc'
if not os.path.exists(font_path):
    font_path = '/System/Library/Fonts/PingFang.ttc'
prop = fm.FontProperties(fname=font_path)

fig, ax = plt.subplots(figsize=(10, 6))
fig.patch.set_facecolor('#ffffff')
ax.set_facecolor('#ffffff')

# 隐藏坐标轴
ax.axis('off')

# 绘制标题
plt.text(0.5, 0.95, '新周市场前瞻：核心资产最新动态 (2026.04.19)', 
         fontproperties=prop, fontsize=20, ha='center', va='center', fontweight='bold')

# 绘制表头
headers = ['核心资产', '最新点位/价格', '近期变动/状态']
x_offsets = [0.2, 0.5, 0.8]
for i, header in enumerate(headers):
    plt.text(x_offsets[i], 0.85, header, fontproperties=prop, fontsize=16, ha='center', fontweight='bold', color='#495057')

# 绘制分割线
ax.plot([0.1, 0.9], [0.82, 0.82], color='#212529', lw=2)

# 绘制数据行
for i in range(len(assets)):
    y = 0.72 - i * 0.12
    # 资产名称
    plt.text(x_offsets[0], y, assets[i], fontproperties=prop, fontsize=14, ha='center')
    # 最新点位
    plt.text(x_offsets[1], y, prices[i], fontproperties=prop, fontsize=14, ha='center', fontweight='bold')
    # 变动
    plt.text(x_offsets[2], y, changes[i], fontproperties=prop, fontsize=14, ha='center', color=colors[i], fontweight='bold')
    
    # 行间线
    if i < len(assets) - 1:
        ax.plot([0.1, 0.9], [y-0.06, y-0.06], color='#dee2e6', lw=0.8)

# 添加底部备注
plt.text(0.5, 0.10, '注：数据反映 4.17 收盘及周末场外行情。红/绿代表看涨/看跌情绪。', 
         fontproperties=prop, fontsize=12, ha='center', color='#6c757d', style='italic')

# 保存图片
output_path = 'images/charts/2026-04-19-evening.png'
os.makedirs(os.path.dirname(output_path), exist_ok=True)
plt.savefig(output_path, dpi=300, bbox_inches='tight', facecolor=fig.get_facecolor())
print(f"Chart saved to {output_path}")
