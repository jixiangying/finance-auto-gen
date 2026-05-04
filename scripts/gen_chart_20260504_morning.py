
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm
import os

# 字体设置 (macOS)
font_path = '/System/Library/Fonts/STHeiti Medium.ttc'
if not os.path.exists(font_path):
    font_path = '/System/Library/Fonts/PingFang.ttc'
prop = fm.FontProperties(fname=font_path)

# 数据 (2026-05-01 收盘 / 2026-05-04 晨间调研)
assets = ['标普500', '纳斯达克', '道琼斯', '布伦特原油', '现货黄金', '比特币']
prices = ['7230.12', '25114.44', '49499.27', '$108.72', '$2300', '$79000']
changes = [0.29, 0.89, -0.31, -3.4, 3.5, 0.0] 
colors = ['#ff4d4f' if c > 0 else '#52c41a' for c in changes] # 红涨绿跌

fig, ax = plt.subplots(figsize=(10, 6))
fig.patch.set_facecolor('#f0f2f5')
ax.set_facecolor('#ffffff')

bars = ax.barh(assets, changes, color=colors, height=0.6)

# 添加数值和百分比
for i, bar in enumerate(bars):
    width = bar.get_width()
    # 调整文字位置，避免被边框切掉
    label_x_pos = width + (0.05 if width >= 0 else -0.8)
    ax.text(label_x_pos, bar.get_y() + bar.get_height()/2, 
            f'{prices[i]} ({"+" if changes[i]>0 else ""}{changes[i]}%)', 
            va='center', fontproperties=prop, fontsize=12,
            color='#333333')

# 装饰
ax.set_title('全球核心资产收盘表现 (2026-05-01 / 05-04 晨间)', fontproperties=prop, fontsize=16, pad=20)
ax.set_xlabel('涨跌幅 (%)', fontproperties=prop, fontsize=12)
ax.axvline(0, color='black', linewidth=0.8)
ax.set_yticklabels(assets, fontproperties=prop, fontsize=12)

# 隐藏边框
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)

# 设置 X 轴范围，给文字留出空间
limit = max(abs(min(changes)), abs(max(changes))) + 1.5
ax.set_xlim(-limit, limit)

plt.tight_layout()
output_path = 'images/charts/2026-05-04-morning-chart.png'
os.makedirs(os.path.dirname(output_path), exist_ok=True)
plt.savefig(output_path, dpi=300, facecolor=fig.get_facecolor())
print(f"Chart saved to {output_path}")
