import matplotlib.pyplot as plt
import matplotlib.font_manager as fm
import os

# 设置中文字体
font_path = '/System/Library/Fonts/STHeiti Medium.ttc'
if not os.path.exists(font_path):
    font_path = '/System/Library/Fonts/PingFang.ttc'

prop = fm.FontProperties(fname=font_path)
plt.rcParams['font.sans-serif'] = [prop.get_name()]
plt.rcParams['axes.unicode_minus'] = False

# 数据
labels = ['道琼斯', '标普500', '纳斯达克', '十年美债', 'WTI原油', '现货黄金', '比特币']
prices = [50579.70, 7473.47, 26343.97, '4.56%', 96.36, 4502.59, 77310]
changes = [0.58, 0.37, 0.19, -0.22, 0.00, -0.90, -0.40] # 收益率变动以相对值估算

# 颜色
colors = ['#ff4c4c' if c > 0 else '#2ecc71' if c < 0 else '#95a5a6' for c in changes]

fig, ax = plt.subplots(figsize=(10, 6))
bars = ax.bar(labels, [abs(c) if c != 0 else 0.1 for c in changes], color=colors)

# 添加数值标签
for i, bar in enumerate(bars):
    height = bar.get_height()
    label_text = f"{'+' if changes[i] > 0 else ''}{changes[i]}%"
    if labels[i] == '十年美债':
        label_text = '4.56%'
    ax.text(bar.get_x() + bar.get_width()/2., height,
            f"{prices[i]}\n({label_text})",
            ha='center', va='bottom', fontproperties=prop, fontsize=10)

ax.set_title('全球核心资产表现 (2026-05-22 隔夜收盘)', fontproperties=prop, fontsize=16)
ax.set_ylabel('涨跌幅 (%)', fontproperties=prop)
ax.set_xticklabels(labels, fontproperties=prop)

# 保存
output_path = 'images/charts/2026-05-23-morning.png'
os.makedirs(os.path.dirname(output_path), exist_ok=True)
plt.savefig(output_path, dpi=300, bbox_inches='tight')
print(f"Chart saved to {output_path}")
