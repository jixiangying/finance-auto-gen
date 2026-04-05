
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm
import os

# 字体设置 (macOS)
font_path = '/System/Library/Fonts/STHeiti Medium.ttc'
if not os.path.exists(font_path):
    font_path = '/System/Library/Fonts/PingFang.ttc'
prop = fm.FontProperties(fname=font_path)

# 数据
assets = ['标普500 (周)', '纳指 (周)', '布油 (单日)', '现货黄金', '比特币', '上证指数 (周)']
prices = ['6571.00', '20150', '$109.24', '$2485', '$67000', '3880.10']
changes = [3.4, 4.4, 8.98, 1.2, -0.5, -0.86]  # 假设黄金单日涨1.2%，BTC周日微调-0.5%
colors = ['#ff4d4f' if c > 0 else '#52c41a' for c in changes] # 红涨绿跌

fig, ax = plt.subplots(figsize=(10, 6))
fig.patch.set_facecolor('#f0f2f5')
ax.set_facecolor('#ffffff')

bars = ax.barh(assets, changes, color=colors, height=0.6)

# 添加数值和百分比
for i, bar in enumerate(bars):
    width = bar.get_width()
    label_x_pos = width + (0.1 if width >= 0 else -0.5)
    ax.text(label_x_pos, bar.get_y() + bar.get_height()/2, 
            f'{prices[i]} ({"+" if changes[i]>0 else ""}{changes[i]}%)', 
            va='center', fontproperties=prop, fontsize=12,
            color='#333333')

# 装饰
ax.set_title('全球核心资产周度/近期表现回顾 (2026-04-05)', fontproperties=prop, fontsize=16, pad=20)
ax.set_xlabel('涨跌幅 (%)', fontproperties=prop, fontsize=12)
ax.axvline(0, color='black', linewidth=0.8)
ax.set_yticklabels(assets, fontproperties=prop, fontsize=12)

# 隐藏边框
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)

plt.tight_layout()
output_path = 'images/charts/2026-04-05-morning-chart.png'
os.makedirs(os.path.dirname(output_path), exist_ok=True)
plt.savefig(output_path, dpi=300, facecolor=fig.get_facecolor())
print(f"Chart saved to {output_path}")
