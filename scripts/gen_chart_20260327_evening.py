import matplotlib.pyplot as plt
import matplotlib.font_manager as fm
import os

# Set font for macOS
font_path = '/System/Library/Fonts/STHeiti Medium.ttc'
if not os.path.exists(font_path):
    font_path = '/System/Library/Fonts/Supplemental/Songti.ttc'

prop = fm.FontProperties(fname=font_path)
plt.rcParams['axes.unicode_minus'] = False

# Data (Friday, March 27, 2026 Afternoon)
data = [
    {"name": "上证指数", "price": "3845.21", "change": "-1.12%"},
    {"name": "深证成指", "price": "10864.50", "change": "-1.45%"},
    {"name": "创业板指", "price": "2302.45", "change": "-1.65%"},
    {"name": "恒生指数", "price": "24380.12", "change": "-1.92%"},
    {"name": "恒生科技", "price": "4980.60", "change": "-2.79%"},
    {"name": "成交额 (A股)", "price": "1.85万亿", "change": "缩量"}
]

# Plotting
fig, ax = plt.subplots(figsize=(10, 6))
ax.set_facecolor('#fdfdfd')
fig.patch.set_facecolor('#ffffff')

for i, item in enumerate(data):
    # Red for up, Green for down (Chinese convention)
    if '-' in item['change']:
        color = 'green'
    elif '+' in item['change']:
        color = 'red'
    else:
        color = 'black'
        
    ax.text(0.05, 0.90 - i*0.14, item['name'], fontsize=18, fontweight='bold', transform=ax.transAxes, fontproperties=prop)
    ax.text(0.45, 0.90 - i*0.14, item['price'], fontsize=18, transform=ax.transAxes, fontproperties=prop)
    ax.text(0.75, 0.90 - i*0.14, item['change'], fontsize=18, color=color, fontweight='bold', transform=ax.transAxes, fontproperties=prop)

ax.set_axis_off()
plt.title('国内核心指数收盘表现 (2026-03-27 周五收盘)', fontproperties=prop, fontsize=22, pad=20)

output_path = 'images/charts/2026-03-27-evening.png'
os.makedirs(os.path.dirname(output_path), exist_ok=True)
plt.savefig(output_path, bbox_inches='tight', dpi=150)
print(f"Chart saved to {output_path}")
