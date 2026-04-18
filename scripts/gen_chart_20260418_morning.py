import matplotlib.pyplot as plt
import matplotlib.font_manager as fm
import os

# 资产数据 (2026-04-17 收盘数据)
assets = ['S&P 500', 'Nasdaq', 'Dow Jones', '10Y Yield', 'WTI Crude']
prices = ['7,126.06', '24,468.48', '49,447.43', '4.288%', '90.65']
changes = ['+1.20%', '+1.52%', '+1.79%', '-0.032%', '-11.0%']
# 红色上涨 #e63946, 绿色下跌 #008000
colors = ['#e63946', '#e63946', '#e63946', '#008000', '#008000']

# 设置中文字体 (macOS)
font_path = '/System/Library/Fonts/STHeiti Medium.ttc'
if not os.path.exists(font_path):
    font_path = '/System/Library/Fonts/PingFang.ttc'
prop = fm.FontProperties(fname=font_path)

fig, ax = plt.subplots(figsize=(10, 6))
fig.patch.set_facecolor('#f8f9fa')
ax.set_facecolor('#f8f9fa')

# 隐藏坐标轴
ax.axis('off')

# 绘制标题
plt.text(0.5, 0.95, '全球核心资产行情速览 (2026-04-17 收盘)', 
         fontproperties=prop, fontsize=20, ha='center', va='center', fontweight='bold')

# 绘制表头
headers = ['资产名称', '收盘点位/价格', '涨跌幅']
x_offsets = [0.2, 0.5, 0.8]
for i, header in enumerate(headers):
    plt.text(x_offsets[i], 0.82, header, fontproperties=prop, fontsize=16, ha='center', fontweight='bold')

# 绘制分割线
ax.plot([0.1, 0.9], [0.78, 0.78], color='gray', lw=1)

# 绘制数据行
for i in range(len(assets)):
    y = 0.68 - i * 0.12
    plt.text(x_offsets[0], y, assets[i], fontproperties=prop, fontsize=15, ha='center')
    plt.text(x_offsets[1], y, prices[i], fontproperties=prop, fontsize=15, ha='center', fontweight='bold')
    plt.text(x_offsets[2], y, changes[i], fontproperties=prop, fontsize=15, ha='center', color=colors[i], fontweight='bold')
    # 行间线
    if i < len(assets) - 1:
        ax.plot([0.1, 0.9], [y-0.06, y-0.06], color='#dee2e6', lw=0.5)

# 保存图片
output_path = 'images/charts/2026-04-18-morning.png'
os.makedirs(os.path.dirname(output_path), exist_ok=True)
plt.savefig(output_path, dpi=300, bbox_inches='tight', facecolor=fig.get_facecolor())
print(f"Chart saved to {output_path}")
