import matplotlib.pyplot as plt
import matplotlib.font_manager as fm
import os

# 字体设置
font_path = '/System/Library/Fonts/STHeiti Medium.ttc'
prop = fm.FontProperties(fname=font_path)
plt.rcParams['font.family'] = prop.get_name()
plt.rcParams['axes.unicode_minus'] = False

# 数据
data = [
    ("标普500", 7165.08, 0.80),
    ("纳斯达克", 24836.60, 1.63),
    ("道琼斯", 49230.71, -0.16),
    ("日经225", 60013.98, 0.50),
    ("黄金", 4722.19, 0.33),
    ("布伦特原油", 105.33, -0.25)
]

fig, ax = plt.subplots(figsize=(10, 6), facecolor='#f4f4f4')
ax.set_facecolor('#f4f4f4')

y_pos = range(len(data))
names = [d[0] for d in data]
values = [d[1] for d in data]
changes = [d[2] for d in data]
colors = ['#e15759' if c > 0 else '#76b7b2' for c in changes] # 红色涨，绿色跌

bars = ax.barh(y_pos, [1]*len(data), color=colors, height=0.6)

# 隐藏坐标轴
ax.axis('off')

# 绘制文本
for i, (name, val, change) in enumerate(data):
    color = '#e15759' if change > 0 else '#76b7b2'
    ax.text(0.05, i, name, va='center', ha='left', fontsize=16, fontproperties=prop, color='#333333')
    ax.text(0.4, i, f"{val:,.2f}", va='center', ha='left', fontsize=16, fontweight='bold', color='#333333')
    sign = "+" if change > 0 else ""
    ax.text(0.75, i, f"{sign}{change:.2f}%", va='center', ha='left', fontsize=16, fontweight='bold', color=color)

plt.title("核心资产行情看板 (2026-04-27 Morning)", fontproperties=prop, fontsize=20, pad=20)
plt.tight_layout()

output_path = 'images/charts/2026-04-27-morning.png'
os.makedirs(os.path.dirname(output_path), exist_ok=True)
plt.savefig(output_path, dpi=200, bbox_inches='tight')
print(f"Chart saved to {output_path}")
