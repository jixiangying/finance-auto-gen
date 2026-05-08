import matplotlib.pyplot as plt
import matplotlib.font_manager as fm
import os

# 资产数据
assets = [
    {"name": "上证指数", "price": "4179.95", "change": "-0.00%"},
    {"name": "深证成指", "price": "---", "change": "-0.50%"},
    {"name": "创业板指", "price": "---", "change": "-0.96%"},
    {"name": "北证50", "price": "---", "change": "+2.24%"},
    {"name": "恒生指数", "price": "26393.71", "change": "-0.87%"},
    {"name": "恒生科技", "price": "5102.79", "change": "-0.36%"}
]

# 设置中文字体 (macOS)
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
plt.text(0.5, 0.95, "核心行情信息卡 (2026-05-08 收盘)", 
         horizontalalignment='center', fontsize=20, fontproperties=prop, weight='bold', color='#333333')

# 绘制表格
y_start = 0.8
for i, asset in enumerate(assets):
    y_pos = y_start - i * 0.12
    color = 'green' if '-' in asset['change'] and asset['change'] != '-0.00%' else 'red'
    if asset['change'] == '-0.00%':
        color = '#555555'
        icon = '⚪'
    else:
        icon = '🟢' if '-' in asset['change'] else '🔴'
    
    # 指数名称
    plt.text(0.1, y_pos, asset['name'], fontsize=18, fontproperties=prop, color='#555555')
    # 点位
    plt.text(0.4, y_pos, asset['price'], fontsize=18, fontproperties=prop, weight='bold', color='#333333')
    # 涨跌幅
    plt.text(0.7, y_pos, f"{icon} {asset['change']}", fontsize=18, fontproperties=prop, color=color, weight='bold')

# 保存图片
output_path = 'images/charts/2026-05-08-evening.png'
os.makedirs(os.path.dirname(output_path), exist_ok=True)
plt.savefig(output_path, dpi=300, bbox_inches='tight')
print(f"Chart saved to {output_path}")
