
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm
import os

# 配置中文字体 (macOS)
font_path = '/System/Library/Fonts/STHeiti Medium.ttc'
if not os.path.exists(font_path):
    font_path = '/System/Library/Fonts/PingFang.ttc'

prop = fm.FontProperties(fname=font_path)
plt.rcParams['font.family'] = prop.get_name()
plt.rcParams['axes.unicode_minus'] = False

# 市场数据 (2026-05-14 收盘)
data = [
    {"name": "标普500 (S&P 500)", "price": "7,501.24", "change": "+0.77%"},
    {"name": "纳斯达克 (Nasdaq)", "price": "26,635.22", "change": "+0.88%"},
    {"name": "道琼斯 (Dow Jones)", "price": "50,063.46", "change": "+0.75%"},
    {"name": "10年美债收益率", "price": "4.980%", "change": "+50.1bp"},
    {"name": "WTI原油", "price": "$105.42", "change": "+2.30%"}
]

# 绘图
fig, ax = plt.subplots(figsize=(10, 6), dpi=100)
ax.set_facecolor('#f9f9f9')
fig.patch.set_facecolor('#ffffff')

y_pos = range(len(data))
colors = ['#e63946' if '+' in d['change'] else '#2a9d8f' for d in data]

# 绘制条形图背景（占位）
ax.barh(y_pos, [1]*len(data), color='white', edgecolor='#dddddd', height=0.6)

# 添加文字
for i, d in enumerate(data):
    # 资产名称
    ax.text(0.05, i, d['name'], va='center', ha='left', fontsize=14, fontproperties=prop, color='#333333')
    # 现价
    ax.text(0.5, i, d['price'], va='center', ha='center', fontsize=16, fontweight='bold', color='#222222')
    # 涨跌幅
    ax.text(0.85, i, d['change'], va='center', ha='right', fontsize=16, fontweight='bold', color=colors[i])

# 隐藏坐标轴
ax.set_yticks([])
ax.set_xticks([])
for spine in ax.spines.values():
    spine.set_visible(False)

plt.title("全球核心资产行情 (2026-05-14 收盘)", fontproperties=prop, fontsize=18, pad=20)
plt.tight_layout()

# 确保保存目录存在
os.makedirs('images/charts', exist_ok=True)
output_path = 'images/charts/2026-05-15-morning.png'
plt.savefig(output_path, bbox_inches='tight')
print(f"Chart saved to {output_path}")
