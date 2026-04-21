import matplotlib.pyplot as plt
import matplotlib.font_manager as fm
import os

# 配置中文字体 (macOS)
font_path = '/System/Library/Fonts/STHeiti Medium.ttc'
if not os.path.exists(font_path):
    font_path = '/System/Library/Fonts/PingFang.ttc'

prop = fm.FontProperties(fname=font_path)
plt.rcParams['font.family'] = prop.get_name()
plt.rcParams['axes.unicode_minus'] = False

# 数据 (2026-04-20 收盘数据，用于 04-21 早报)
assets = ['标普500', '纳斯达克', '道琼斯', 'WTI原油', '现货黄金', 'A50期货', '离岸人民币']
prices = ['7109.14', '24404.39', '49442.56', '89.61', '4820.00', '15506', '6.8160']
changes = [-0.24, -0.26, -0.01, 6.87, -1.0, 0.61, -0.15] # 涨跌百分比数值
changes_str = ['-0.24%', '-0.26%', '-0.01%', '+6.87%', '-1.00%', '+0.61%', '-0.15%']

# 颜色逻辑：红色上涨，绿色下跌 (符合 SKILL.md)
colors = ['#ff4d4f' if c > 0 else '#52c41a' for c in changes]

fig, ax = plt.subplots(figsize=(10, 8), facecolor='#f8f9fa')
ax.set_axis_off()

# 绘制卡片
for i in range(len(assets)):
    y_pos = 0.85 - i * 0.12
    # 资产名称
    ax.text(0.1, y_pos, assets[i], fontsize=20, fontweight='bold', fontproperties=prop, color='#343a40')
    # 价格
    ax.text(0.4, y_pos, prices[i], fontsize=22, fontweight='bold', color='#212529')
    # 涨跌幅
    ax.text(0.7, y_pos, changes_str[i], fontsize=20, fontweight='bold', color=colors[i], 
            bbox=dict(facecolor=colors[i], alpha=0.1, edgecolor='none', boxstyle='round,pad=0.3'))

plt.title('核心资产行情概览 (2026-04-21 早报)', fontsize=26, fontweight='bold', fontproperties=prop, pad=40)
plt.text(0.5, 0.02, '注：离岸人民币下跌代表汇率走强；数据来源：Bloomberg / Reuters', 
         transform=ax.transAxes, ha='center', fontsize=12, color='#6c757d', fontproperties=prop)

# 保存路径
output_path = 'images/charts/2026-04-21-morning.png'
os.makedirs(os.path.dirname(output_path), exist_ok=True)
plt.savefig(output_path, dpi=300, bbox_inches='tight')
print(f"Chart saved to {output_path}")
