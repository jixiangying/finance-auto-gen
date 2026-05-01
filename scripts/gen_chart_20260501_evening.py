import matplotlib.pyplot as plt
import matplotlib.font_manager as fm
import os

# 设置中文字体支持 (macOS)
prop = fm.FontProperties(fname='/System/Library/Fonts/STHeiti Medium.ttc')
plt.rcParams['font.sans-serif'] = ['STHeiti']
plt.rcParams['axes.unicode_minus'] = False

# 核心资产数据
assets = ['富时A50期货', '离岸人民币', '比特币(BTC)', '标普500', '纳斯达克', '道琼斯']
changes = [1.4, 0.23, 1.96, 1.02, 0.89, 1.62]
colors = ['#ff4d4d' if x > 0 else '#2ecc71' for x in changes]
labels = ['+1.40%', '+0.23%', '+1.96%', '+1.02%', '+0.89%', '+1.62%']

fig, ax = plt.subplots(figsize=(10, 6))
bars = ax.barh(assets, changes, color=colors, height=0.6)

# 添加数值标签
for i, bar in enumerate(bars):
    width = bar.get_width()
    ax.text(width + 0.05, bar.get_y() + bar.get_height()/2, 
            labels[i], va='center', fontsize=12, fontweight='bold', color=colors[i])

# 样式美化
ax.set_title('全球核心资产表现 (2026-05-01 晚间)', fontproperties=prop, fontsize=18, pad=20)
ax.set_xlim(0, 2.5)
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
ax.set_yticklabels(assets, fontproperties=prop, fontsize=12)
ax.set_xlabel('涨跌幅 (%)', fontproperties=prop, fontsize=12)

plt.tight_layout()

# 保存路径
output_dir = 'images/charts/'
if not os.path.exists(output_dir):
    os.makedirs(output_dir)
output_path = os.path.join(output_dir, '20260501_evening.png')
plt.savefig(output_path, dpi=300)
print(f"Chart saved to {output_path}")
