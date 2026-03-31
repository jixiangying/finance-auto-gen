import matplotlib.pyplot as plt
import matplotlib.font_manager as fm
import os

# 资产数据
assets = [
    {"name": "上证综指", "price": "3891.86", "change": "-0.80%"},
    {"name": "深证成指", "price": "13478.06", "change": "-1.81%"},
    {"name": "创业板指", "price": "3184.95", "change": "-2.70%"},
    {"name": "科创50", "price": "1256.33", "change": "-2.59%"},
    {"name": "恒生指数", "price": "24451.77", "change": "-2.00%"},
    {"name": "恒生科技", "price": "4644.37", "change": "-2.80%"}
]

# 设置中文字体
font_path = '/System/Library/Fonts/STHeiti Medium.ttc'
if not os.path.exists(font_path):
    font_path = '/System/Library/Fonts/PingFang.ttc'
prop = fm.FontProperties(fname=font_path)

plt.rcParams['font.sans-serif'] = [prop.get_name()]
plt.rcParams['axes.unicode_minus'] = False

fig, ax = plt.subplots(figsize=(10, 6), facecolor='#f4f4f4')
ax.set_facecolor('#f4f4f4')

# 隐藏坐标轴
ax.axis('off')

# 标题
plt.text(0.5, 0.95, "核心行情信息卡 (2026-03-31 收盘)", 
         horizontalalignment='center', fontsize=20, fontproperties=prop, weight='bold', color='#333333')

# 绘制表格
y_start = 0.8
for i, asset in enumerate(assets):
    y_pos = y_start - i * 0.12
    color = 'green' if '-' in asset['change'] else 'red'
    icon = '🟢' if '-' in asset['change'] else '🔴'
    
    # 指数名称
    plt.text(0.1, y_pos, asset['name'], fontsize=18, fontproperties=prop, color='#555555')
    # 点位
    plt.text(0.4, y_pos, asset['price'], fontsize=18, fontproperties=prop, weight='bold', color='#333333')
    # 涨跌幅
    plt.text(0.7, y_pos, f"{icon} {asset['change']}", fontsize=18, fontproperties=prop, color=color, weight='bold')

# 保存图片
output_path = 'images/charts/2026-03-31-evening.png'
os.makedirs(os.path.dirname(output_path), exist_ok=True)
plt.savefig(output_path, dpi=300, bbox_inches='tight')
print(f"Chart saved to {output_path}")
