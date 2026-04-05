
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm
import os

# 字体设置 (macOS)
font_path = '/System/Library/Fonts/STHeiti Medium.ttc'
if not os.path.exists(font_path):
    font_path = '/System/Library/Fonts/PingFang.ttc'
prop = fm.FontProperties(fname=font_path)

# 数据 (更新至周日晚间)
assets = ['布伦特原油 (周末场外)', '现货黄金 (避险情绪)', '比特币 (周末表现)', '美债2年期收益率', '标普500 (上周五)', '纳指 (上周五)']
prices = ['$114.00', '$2495', '$67078', '3.88%', '6571', '20150']
# 涨跌幅对比上周五收盘或周末表现
changes = [4.36, 0.40, 0.12, 0.52, 0.0, 0.0] 
colors = ['#ff4d4f' if c > 0 else '#52c41a' for c in changes]

fig, ax = plt.subplots(figsize=(10, 6))
fig.patch.set_facecolor('#f0f2f5')
ax.set_facecolor('#ffffff')

bars = ax.barh(assets, changes, color=colors, height=0.6)

# 添加数值和百分比
for i, bar in enumerate(bars):
    width = bar.get_width()
    label_x_pos = width + (0.05 if width >= 0 else -0.2)
    ax.text(label_x_pos, bar.get_y() + bar.get_height()/2, 
            f'{prices[i]} ({"+" if changes[i]>0 else ""}{changes[i]}%)', 
            va='center', fontproperties=prop, fontsize=12,
            color='#333333')

# 装饰
ax.set_title('新一周市场开盘核心资产预警 (2026-04-05 Evening)', fontproperties=prop, fontsize=16, pad=20)
ax.set_xlabel('周末溢价 / 涨跌幅 (%)', fontproperties=prop, fontsize=12)
ax.axvline(0, color='black', linewidth=0.8)
ax.set_yticklabels(assets, fontproperties=prop, fontsize=12)

# 隐藏边框
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)

plt.tight_layout()
output_path = 'images/charts/2026-04-05-evening.png'
os.makedirs(os.path.dirname(output_path), exist_ok=True)
plt.savefig(output_path, dpi=300, facecolor=fig.get_facecolor())
print(f"Chart saved to {output_path}")
