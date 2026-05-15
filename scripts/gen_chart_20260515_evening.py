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
labels = ['上证指数', '深证成指', '创业板指', '恒生指数', '恒生科技']
values = [4135.00, 10560.00, 2180.00, 25962.73, 4941.14] # 部分点位为估算或近似
changes = [-1.02, -1.17, -0.56, -1.62, -2.66]
colors = ['#00ba50' if c < 0 else '#e60000' for c in changes] # 绿色代表下跌，红色代表上涨

fig, ax1 = plt.subplots(figsize=(10, 6))

# 绘制涨跌幅柱状图
bars = ax1.bar(labels, changes, color=colors, alpha=0.7)

# 添加数值标注
for bar, change in zip(bars, changes):
    height = bar.get_height()
    ax1.text(bar.get_x() + bar.get_width()/2., height + (0.1 if height > 0 else -0.2),
             f'{change}%', ha='center', va='bottom' if height > 0 else 'top', 
             fontproperties=prop, fontsize=12, fontweight='bold')

ax1.set_ylabel('涨跌幅 (%)', fontproperties=prop, fontsize=12)
ax1.set_title('核心指数收盘表现 (2026-05-15)', fontproperties=prop, fontsize=16, pad=20)
ax1.axhline(0, color='black', linewidth=0.8)
ax1.set_xticklabels(labels, fontproperties=prop, fontsize=12)

# 网格线
ax1.yaxis.grid(True, linestyle='--', alpha=0.6)

# 保存图片
output_path = 'images/charts/2026-05-15-evening.png'
os.makedirs(os.path.dirname(output_path), exist_ok=True)
plt.tight_layout()
plt.savefig(output_path, dpi=150)
print(f'Chart saved to {output_path}')
