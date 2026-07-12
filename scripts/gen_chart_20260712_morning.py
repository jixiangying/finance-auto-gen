import matplotlib.pyplot as plt
import matplotlib.font_manager as fm
import os

# 资产数据 (2026-07-06 至 2026-07-10 周度复盘)
assets = [
    '纳斯达克 (Nasdaq)', 
    '标普 500 (S&P 500)', 
    '道琼斯 (Dow Jones)', 
    '沪深 300 (CSI 300)', 
    '恒生指数 (Hang Seng)', 
    'WTI 原油 (Crude)', 
    '现货黄金 (Gold)', 
    '比特币 (Bitcoin)'
]
prices = ['26,281.61', '7,575.39', '52,637.01', '4,780.79', '24,175.12', '71.41', '4,119.56', '63,220.69']
weekly_changes = ['+1.74%', '+1.23%', '-0.50%', '-1.27%', '+3.53%', '+3.82%', '-0.12%', '+2.82%']
friday_changes = ['+0.29%', '+0.42%', '+0.29%', '-2.00%', '+0.60%', '-2.87%', '-0.06%', '+1.56%']

# 颜色设置 (红色上涨 #e63946, 绿色下跌 #008000)
weekly_colors = ['#e63946', '#e63946', '#008000', '#008000', '#e63946', '#e63946', '#008000', '#e63946']
friday_colors = ['#e63946', '#e63946', '#e63946', '#008000', '#e63946', '#008000', '#008000', '#e63946']

# 设置中文字体 (macOS)
font_path = '/System/Library/Fonts/STHeiti Medium.ttc'
if not os.path.exists(font_path):
    font_path = '/System/Library/Fonts/PingFang.ttc'
prop = fm.FontProperties(fname=font_path)

fig, ax = plt.subplots(figsize=(12, 9.5))
fig.patch.set_facecolor('#ffffff')
ax.set_facecolor('#ffffff')

# 隐藏坐标轴
ax.axis('off')

# 绘制标题
plt.text(0.5, 0.96, '全球核心资产周度表现汇总 (2026.07.06 - 07.10)', 
         fontproperties=prop, fontsize=22, ha='center', va='center', fontweight='bold', color='#1e293b')

# 绘制表头
headers = ['核心资产', '最新点位/价格', '周五单日表现', '本周累计表现']
x_offsets = [0.15, 0.45, 0.65, 0.85]
for i, header in enumerate(headers):
    plt.text(x_offsets[i], 0.88, header, fontproperties=prop, fontsize=16, ha='center', fontweight='bold', color='#475569')

# 绘制分割线
ax.plot([0.05, 0.95], [0.85, 0.85], color='#1e293b', lw=2)

# 绘制数据行
for i in range(len(assets)):
    y = 0.77 - i * 0.085
    # 资产名称
    plt.text(x_offsets[0], y, assets[i], fontproperties=prop, fontsize=15, ha='center', color='#334155')
    # 最新点位
    plt.text(x_offsets[1], y, prices[i], fontproperties=prop, fontsize=15, ha='center', fontweight='bold', color='#1e293b')
    # 周五表现
    plt.text(x_offsets[2], y, friday_changes[i], fontproperties=prop, fontsize=15, ha='center', color=friday_colors[i], fontweight='bold')
    # 本周累计
    plt.text(x_offsets[3], y, weekly_changes[i], fontproperties=prop, fontsize=16, ha='center', color=weekly_colors[i], fontweight='bold')
    
    # 行间线
    if i < len(assets) - 1:
        ax.plot([0.05, 0.95], [y-0.04, y-0.04], color='#e2e8f0', lw=0.8)

# 添加底部备注
plt.text(0.5, 0.05, '注：红/绿分别代表对应周期的涨/跌。数据截至 2026.07.10 全球收盘。', 
         fontproperties=prop, fontsize=12, ha='center', color='#64748b', style='italic')

# 保存图片
output_path = 'images/charts/2026-07-12-morning.png'
os.makedirs(os.path.dirname(output_path), exist_ok=True)
plt.savefig(output_path, dpi=300, bbox_inches='tight', facecolor=fig.get_facecolor())
plt.close()
print(f"Chart saved to {output_path}")
