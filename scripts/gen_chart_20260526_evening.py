import matplotlib.pyplot as plt
import matplotlib.font_manager as fm
import os

# 字体设置 (macOS)
font_path = '/System/Library/Fonts/STHeiti Medium.ttc'
prop = fm.FontProperties(fname=font_path)
plt.rcParams['font.sans-serif'] = ['STHeiti']
plt.rcParams['axes.unicode_minus'] = False

# 数据
labels = ['上证指数', '深证成指', '创业板指', '恒生指数', '恒生科技', '布伦特原油', '现货黄金']
values = [-0.17, 0.12, 0.54, -0.03, 1.59, 1.95, -1.19] # 涨跌幅 %
prices = ['4145.37', '15876.16', '4043.07', '25599.45', '4946.88', '$99.50', '$4515']

# 绘图
fig, ax = plt.subplots(figsize=(10, 6))
colors = ['green' if x < 0 else 'red' for x in values]

bars = ax.bar(labels, values, color=colors, alpha=0.7)

# 添加数值标注
for bar, price, val in zip(bars, prices, values):
    height = bar.get_height()
    label_text = f"{price}\n({'+' if val > 0 else ''}{val}%)"
    ax.text(bar.get_x() + bar.get_width()/2., height if height > 0 else height - 0.2,
            label_text, ha='center', va='bottom' if height > 0 else 'top', fontproperties=prop, fontsize=10)

ax.set_ylabel('涨跌幅 (%)', fontproperties=prop)
ax.set_title('2026年05月26日 核心资产收盘表现', fontproperties=prop, fontsize=16)
ax.axhline(0, color='black', linewidth=0.8)
ax.set_xticklabels(labels, fontproperties=prop)

# 装饰
ax.grid(axis='y', linestyle='--', alpha=0.6)
plt.tight_layout()

# 保存
output_path = 'images/charts/2026-05-26-evening.png'
os.makedirs(os.path.dirname(output_path), exist_ok=True)
plt.savefig(output_path, dpi=300)
print(f"Chart saved to {output_path}")
