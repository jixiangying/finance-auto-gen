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

# 数据 (2026-04-17 收盘数据)
assets = ['上证指数', '深证成指', '创业板指', '恒生指数', '恒生科技']
prices = ['4051.50', '14885.10', '3678.13', '26160.33', '5042.68']
changes = ['-0.10%', '+0.60%', '+1.43%', '-0.89%', '-0.97%']
# 红色上涨 🔴 (#e63946)，绿色下跌 🟢 (#2a9d8f)
colors = ['#2a9d8f', '#e63946', '#e63946', '#2a9d8f', '#2a9d8f'] 

fig, ax = plt.subplots(figsize=(10, 7), facecolor='#f8f9fa')
ax.set_axis_off()

# 绘制卡片
for i in range(len(assets)):
    y_pos = 0.85 - i * 0.18
    # 资产名称
    ax.text(0.05, y_pos, assets[i], fontsize=20, fontweight='bold', fontproperties=prop, color='#343a40')
    # 价格
    ax.text(0.45, y_pos, prices[i], fontsize=22, fontweight='bold', color='#212529')
    # 涨跌幅
    ax.text(0.8, y_pos, changes[i], fontsize=20, fontweight='bold', color=colors[i], 
            bbox=dict(facecolor=colors[i], alpha=0.1, edgecolor='none', boxstyle='round,pad=0.3'))

plt.title('核心指数收盘表现 (2026-04-17)', fontsize=26, fontweight='bold', fontproperties=prop, pad=40)
plt.text(0.5, 0.02, '数据来源：EastMoney / Wind (收盘：2026-04-17)', 
         transform=ax.transAxes, ha='center', fontsize=12, color='#6c757d', fontproperties=prop)

# 保存路径
output_path = 'images/charts/2026-04-17-evening.png'
os.makedirs(os.path.dirname(output_path), exist_ok=True)
plt.savefig(output_path, dpi=300, bbox_inches='tight')
print(f"Chart saved to {output_path}")
