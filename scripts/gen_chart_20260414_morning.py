import matplotlib.pyplot as plt
import matplotlib.font_manager as fm
import os

# 配置中文字体
font_path = '/System/Library/Fonts/STHeiti Medium.ttc'
if not os.path.exists(font_path):
    font_path = '/System/Library/Fonts/PingFang.ttc'

prop = fm.FontProperties(fname=font_path)
plt.rcParams['font.family'] = prop.get_name()
plt.rcParams['axes.unicode_minus'] = False

# 数据
assets = ['标普500', '纳斯达克', '道琼斯', '布伦特原油']
prices = ['6886.24', '23183.74', '48218.25', '99.36']
changes = ['+1.02%', '+1.23%', '+0.63%', '+4.40%']
colors = ['#e63946', '#e63946', '#e63946', '#e63946'] # 全部上涨，使用红色

fig, ax = plt.subplots(figsize=(10, 6), facecolor='#f8f9fa')
ax.set_axis_off()

# 绘制卡片
for i in range(len(assets)):
    y_pos = 0.8 - i * 0.2
    # 资产名称
    ax.text(0.1, y_pos, assets[i], fontsize=20, fontweight='bold', fontproperties=prop, color='#343a40')
    # 价格
    ax.text(0.4, y_pos, prices[i], fontsize=22, fontweight='bold', color='#212529')
    # 涨跌幅
    ax.text(0.7, y_pos, changes[i], fontsize=20, fontweight='bold', color=colors[i], bbox=dict(facecolor=colors[i], alpha=0.1, edgecolor='none', boxstyle='round,pad=0.3'))

plt.title('核心资产行情概览 (2026-04-14 早报)', fontsize=24, fontweight='bold', fontproperties=prop, pad=30)
plt.text(0.5, 0.05, '数据来源：Bloomberg / Reuters', transform=ax.transAxes, ha='center', fontsize=12, color='#6c757d', fontproperties=prop)

# 保存路径
output_path = 'images/charts/2026-04-14-morning-chart.png'
os.makedirs(os.path.dirname(output_path), exist_ok=True)
plt.savefig(output_path, dpi=300, bbox_inches='tight')
print(f"Chart saved to {output_path}")
