import matplotlib.pyplot as plt
import matplotlib.font_manager as fm
import os

# 字体设置 (macOS)
font_path = '/System/Library/Fonts/STHeiti Medium.ttc'
prop = fm.FontProperties(fname=font_path)
plt.rcParams['font.family'] = prop.get_name()
plt.rcParams['axes.unicode_minus'] = False

# 数据
assets = ['纳指', '标普500', '道指', '上证指数', '创业板指', '恒生指数', '现货黄金', 'WTI原油']
weekly_changes = [2.39, 1.43, 0.90, -1.08, 2.53, -0.80, 0.74, -9.15]
prices = ['26972.62', '7580.06', '51032.46', '4068.57', '4037.95', '25182.39', '4542.39', '87.36']

colors = ['#ff4d4d' if x > 0 else '#2ecc71' for x in weekly_changes]

fig, ax = plt.begin_axes = plt.subplots(figsize=(10, 6), dpi=150)
fig.patch.set_facecolor('#f8f9fa')
ax.set_facecolor('#f8f9fa')

bars = ax.barh(assets, weekly_changes, color=colors, height=0.6)

# 添加数值标注
for i, bar in enumerate(bars):
    width = bar.get_width()
    label_x = width + (0.2 if width > 0 else -0.2)
    ax.text(label_x, bar.get_y() + bar.get_height()/2, 
            f'{prices[i]}\n({"+" if weekly_changes[i]>0 else ""}{weekly_changes[i]}%)', 
            va='center', ha='left' if width > 0 else 'right',
            fontproperties=prop, fontsize=10, fontweight='bold',
            color='#2c3e50')

# 装饰
ax.axvline(0, color='black', linewidth=0.8, linestyle='--')
ax.set_title('本周全球核心资产涨跌幅 (5/25 - 5/29)', fontproperties=prop, fontsize=16, pad=20)
ax.set_xlabel('周涨跌幅 (%)', fontproperties=prop, fontsize=12)
ax.set_xlim(-11, 5)

# 设置刻度字体
ax.set_yticklabels(assets, fontproperties=prop)
for label in ax.get_xticklabels():
    label.set_fontproperties(prop)

plt.tight_layout()

# 确保目录存在
os.makedirs('images/charts', exist_ok=True)
plt.savefig('images/charts/2026-05-30-evening.png', bbox_inches='tight')
print("Chart generated successfully at images/charts/2026-05-30-evening.png")
