
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm
import os

# 资产数据
assets = ['上证指数', '深证成指', '创业板指', '科创50', '恒生指数']
prices = [4160.17, 15459.62, 3778.16, 1656.95, 26213.78]
changes = [1.17, 2.33, 2.75, 5.47, 1.22]

# 设置中文字体 (macOS 路径)
font_path = '/System/Library/Fonts/STHeiti Medium.ttc'
if not os.path.exists(font_path):
    font_path = '/System/Library/Fonts/PingFang.ttc'

prop = fm.FontProperties(fname=font_path)
plt.rcParams['font.family'] = prop.get_name()
plt.rcParams['axes.unicode_minus'] = False

# 创建画布
fig, ax = plt.subplots(figsize=(10, 6), facecolor='#0f172a')
ax.set_facecolor('#0f172a')

# 绘图
bars = ax.barh(assets, changes, color='#ef4444', height=0.6)

# 添加数值标注
for bar, price, change in zip(bars, prices, changes):
    width = bar.get_width()
    ax.text(width + 0.1, bar.get_y() + bar.get_height()/2, 
            f'{price:,.2f} ({change:+.2f}%)', 
            va='center', color='white', fontsize=12, fontproperties=prop)

# 设置样式
ax.set_title('核心行情复盘 (2026-05-06)', color='white', fontsize=18, pad=20, fontproperties=prop)
ax.set_xlim(0, max(changes) + 1.5)
ax.tick_params(axis='both', colors='white', labelsize=12)
ax.set_yticklabels(assets, fontproperties=prop)

# 隐藏边框
for spine in ax.spines.values():
    spine.set_visible(False)

ax.grid(axis='x', color='white', linestyle='--', alpha=0.1)

# 保存图片
output_path = 'images/charts/20260506_evening.png'
os.makedirs(os.path.dirname(output_path), exist_ok=True)
plt.tight_layout()
plt.savefig(output_path, dpi=200, facecolor='#0f172a')
print(f'Chart saved to {output_path}')
