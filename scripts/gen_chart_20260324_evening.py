import matplotlib.pyplot as plt
import matplotlib.font_manager as fm
import os

# Set font for macOS
font_path = '/System/Library/Fonts/STHeiti Medium.ttc'
if not os.path.exists(font_path):
    font_path = '/System/Library/Fonts/Supplemental/Songti.ttc'

prop = fm.FontProperties(fname=font_path)
plt.rcParams['axes.unicode_minus'] = False

# Data (Domestic Close for Tuesday, March 24, 2026)
data = [
    {"name": "上证指数", "price": "3,881.28", "change": "+1.78%"},
    {"name": "深证成指", "price": "13,536.56", "change": "+1.43%"},
    {"name": "创业板指", "price": "3,251.55", "change": "+0.50%"},
    {"name": "沪深300", "price": "4,472.18", "change": "+1.23%"},
    {"name": "恒生指数", "price": "24,782.00", "change": "+1.64%"},
    {"name": "恒生科技", "price": "4,778.95", "change": "+1.41%"}
]

# Plotting
fig, ax = plt.subplots(figsize=(10, 6))
ax.set_facecolor('#fdfdfd')
fig.patch.set_facecolor('#ffffff')

for i, item in enumerate(data):
    color = 'red' if '+' in item['change'] else 'green'
    ax.text(0.05, 0.85 - i*0.14, item['name'], fontsize=20, fontweight='bold', transform=ax.transAxes, fontproperties=prop)
    ax.text(0.45, 0.85 - i*0.14, item['price'], fontsize=20, transform=ax.transAxes, fontproperties=prop)
    ax.text(0.75, 0.85 - i*0.14, item['change'], fontsize=20, color=color, fontweight='bold', transform=ax.transAxes, fontproperties=prop)

ax.set_axis_off()
plt.title('国内核心资产回顾 (2026-03-24 周二收盘)', fontproperties=prop, fontsize=24, pad=20)

output_path = 'images/charts/2026-03-24-evening.png'
os.makedirs(os.path.dirname(output_path), exist_ok=True)
plt.savefig(output_path, bbox_inches='tight', dpi=150)
print(f"Chart saved to {output_path}")
