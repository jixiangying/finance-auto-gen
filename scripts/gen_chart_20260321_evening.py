import matplotlib.pyplot as plt
import matplotlib.font_manager as fm
import os

# Set font for macOS
font_path = '/System/Library/Fonts/STHeiti Medium.ttc'
if not os.path.exists(font_path):
    font_path = '/System/Library/Fonts/Supplemental/Songti.ttc'

prop = fm.FontProperties(fname=font_path)
plt.rcParams['axes.unicode_minus'] = False

# Data (Domestic Weekend Review - Friday Close)
data = [
    {"name": "上证指数", "price": "3,957.05", "change": "-1.24%"},
    {"name": "深证成指", "price": "14,271.83", "change": "-0.25%"},
    {"name": "创业板指", "price": "3,400.66", "change": "+1.30%"},
    {"name": "恒生指数", "price": "25,277.32", "change": "-0.88%"},
    {"name": "恒生科技", "price": "4,872.38", "change": "-2.48%"},
    {"name": "全市场成交", "price": "2.30万亿", "change": "+1760亿"}
]

# Plotting
fig, ax = plt.subplots(figsize=(10, 6))
ax.set_facecolor('#f9f9f9')
fig.patch.set_facecolor('#ffffff')

for i, item in enumerate(data):
    color = 'red' if '+' in item['change'] else 'green'
    # Use fontproperties=prop for Chinese text
    ax.text(0.1, 0.85 - i*0.14, item['name'], fontsize=18, fontweight='bold', transform=ax.transAxes, fontproperties=prop)
    ax.text(0.4, 0.85 - i*0.14, item['price'], fontsize=18, transform=ax.transAxes, fontproperties=prop)
    ax.text(0.7, 0.85 - i*0.14, item['change'], fontsize=18, color=color, fontweight='bold', transform=ax.transAxes, fontproperties=prop)

ax.set_axis_off()
plt.title('国内核心资产行情 (2026-03-21 周末复盘)', fontproperties=prop, fontsize=22, pad=20)

output_path = 'images/charts/2026-03-21-evening-chart.png'
os.makedirs(os.path.dirname(output_path), exist_ok=True)
plt.savefig(output_path, bbox_inches='tight', dpi=150)
print(f"Chart saved to {output_path}")
