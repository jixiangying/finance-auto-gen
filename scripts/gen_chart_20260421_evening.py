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

# 数据 (2026-04-21 收盘数据)
assets = ['上证指数', '深证成指', '创业板指', '恒生指数']
prices = ['4085.08', '14982.14', '3688.94', '26436']
changes = [0.07, 0.10, 0.31, 0.29] # 涨跌百分比数值
changes_str = ['+0.07%', '+0.10%', '+0.31%', '+0.29%']

# 颜色逻辑：红色上涨，绿色下跌
colors = ['#ff4d4f' if c > 0 else '#52c41a' for c in changes]

fig, ax = plt.subplots(figsize=(10, 6), facecolor='#f8f9fa')
ax.set_axis_off()

# 绘制卡片
for i in range(len(assets)):
    y_pos = 0.8 - i * 0.18
    # 资产名称
    ax.text(0.1, y_pos, assets[i], fontsize=24, fontweight='bold', fontproperties=prop, color='#343a40')
    # 价格
    ax.text(0.4, y_pos, prices[i], fontsize=26, fontweight='bold', color='#212529')
    # 涨跌幅
    ax.text(0.7, y_pos, changes_str[i], fontsize=24, fontweight='bold', color=colors[i], 
            bbox=dict(facecolor=colors[i], alpha=0.1, edgecolor='none', boxstyle='round,pad=0.3'))

plt.title('国内核心指数收盘概览 (2026-04-21 晚报)', fontsize=30, fontweight='bold', fontproperties=prop, pad=40)
plt.text(0.5, 0.05, '全天成交额：2.41万亿元 | 市场情绪：探底回升', 
         transform=ax.transAxes, ha='center', fontsize=16, color='#6c757d', fontproperties=prop)

# 保存路径
output_path = 'images/charts/2026-04-21-evening.png'
os.makedirs(os.path.dirname(output_path), exist_ok=True)
plt.savefig(output_path, dpi=300, bbox_inches='tight')
print(f"Chart saved to {output_path}")
