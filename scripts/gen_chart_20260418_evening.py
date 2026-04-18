import matplotlib.pyplot as plt
import matplotlib.font_manager as fm
import os

# 资产数据 (2026-04-13 至 2026-04-17 周度复盘)
assets = ['纳斯达克 (Nasdaq)', '创业板指 (ChiNext)', '标普 500 (S&P 500)', '上证指数 (SH Comp)', 'WTI 原油 (Crude)']
prices = ['24,468.48', '3,678.13', '7,126.06', '4,051.50', '90.65']
weekly_changes = ['+6.84%', '+6.65%', '+4.54%', '+1.64%', '-11.0%']
friday_changes = ['+1.52%', '+1.43%', '+1.20%', '-0.10%', '-11.0%']

# 颜色设置 (红色上涨 #e63946, 绿色下跌 #008000)
weekly_colors = ['#e63946', '#e63946', '#e63946', '#e63946', '#008000']
friday_colors = ['#e63946', '#e63946', '#e63946', '#008000', '#008000']

# 设置中文字体 (macOS)
font_path = '/System/Library/Fonts/STHeiti Medium.ttc'
if not os.path.exists(font_path):
    font_path = '/System/Library/Fonts/PingFang.ttc'
prop = fm.FontProperties(fname=font_path)

fig, ax = plt.subplots(figsize=(12, 7))
fig.patch.set_facecolor('#ffffff')
ax.set_facecolor('#ffffff')

# 隐藏坐标轴
ax.axis('off')

# 绘制标题
plt.text(0.5, 0.95, '全球核心资产周度表现汇总 (2026.04.13 - 04.17)', 
         fontproperties=prop, fontsize=22, ha='center', va='center', fontweight='bold')

# 绘制表头
headers = ['核心资产', '最新点位/价格', '周五表现', '本周累计']
x_offsets = [0.15, 0.45, 0.65, 0.85]
for i, header in enumerate(headers):
    plt.text(x_offsets[i], 0.85, header, fontproperties=prop, fontsize=16, ha='center', fontweight='bold', color='#495057')

# 绘制分割线
ax.plot([0.05, 0.95], [0.82, 0.82], color='#212529', lw=2)

# 绘制数据行
for i in range(len(assets)):
    y = 0.72 - i * 0.12
    # 资产名称
    plt.text(x_offsets[0], y, assets[i], fontproperties=prop, fontsize=15, ha='center')
    # 最新点位
    plt.text(x_offsets[1], y, prices[i], fontproperties=prop, fontsize=15, ha='center', fontweight='bold')
    # 周五表现
    plt.text(x_offsets[2], y, friday_changes[i], fontproperties=prop, fontsize=15, ha='center', color=friday_colors[i], fontweight='bold')
    # 本周累计
    plt.text(x_offsets[3], y, weekly_changes[i], fontproperties=prop, fontsize=16, ha='center', color=weekly_colors[i], fontweight='bold')
    
    # 行间线
    if i < len(assets) - 1:
        ax.plot([0.05, 0.95], [y-0.06, y-0.06], color='#dee2e6', lw=0.8)

# 添加底部备注
plt.text(0.5, 0.10, '注：红/绿分别代表对应周期的涨/跌。数据截至 2026.04.17 收盘。', 
         fontproperties=prop, fontsize=12, ha='center', color='#6c757d', style='italic')

# 保存图片
output_path = 'images/charts/2026-04-18-evening.png'
os.makedirs(os.path.dirname(output_path), exist_ok=True)
plt.savefig(output_path, dpi=300, bbox_inches='tight', facecolor=fig.get_facecolor())
print(f"Chart saved to {output_path}")
