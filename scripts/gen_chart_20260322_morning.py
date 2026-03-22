import matplotlib.pyplot as plt
import matplotlib.font_manager as fm
import os

# Set font for macOS
font_path = '/System/Library/Fonts/STHeiti Medium.ttc'
if not os.path.exists(font_path):
    font_path = '/System/Library/Fonts/Supplemental/Songti.ttc'

prop = fm.FontProperties(fname=font_path)
plt.rcParams['axes.unicode_minus'] = False

# Data (Last Close / Weekend Update)
data = [
    {"name": "S&P 500 (Friday)", "price": "6,506.48", "change": "-1.51%"},
    {"name": "Nasdaq (Friday)", "price": "21,647.61", "change": "-2.01%"},
    {"name": "Dow Jones (Friday)", "price": "45,577.47", "change": "-0.96%"},
    {"name": "BTC (Weekend)", "price": "$70,943", "change": "+1.70%"},
    {"name": "ETH (Weekend)", "price": "$2,162", "change": "+0.52%"},
    {"name": "Brent Oil (Friday)", "price": "$112.19", "change": "+3.30%"},
    {"name": "Gold (Friday)", "price": "$4,667", "change": "+1.39%"}
]

# Plotting
fig, ax = plt.subplots(figsize=(10, 7))
ax.set_facecolor('#f9f9f9')
fig.patch.set_facecolor('#ffffff')

for i, item in enumerate(data):
    color = 'red' if '+' in item['change'] else 'green'
    ax.text(0.05, 0.90 - i*0.13, item['name'], fontsize=18, fontweight='bold', transform=ax.transAxes, fontproperties=prop)
    ax.text(0.45, 0.90 - i*0.13, item['price'], fontsize=18, transform=ax.transAxes, fontproperties=prop)
    ax.text(0.75, 0.90 - i*0.13, item['change'], fontsize=18, color=color, fontweight='bold', transform=ax.transAxes, fontproperties=prop)

ax.set_axis_off()
plt.title('周末核心资产表现回顾 (2026-03-22 早报)', fontproperties=prop, fontsize=22, pad=20)

output_path = 'images/charts/2026-03-22-morning-chart.png'
os.makedirs(os.path.dirname(output_path), exist_ok=True)
plt.savefig(output_path, bbox_inches='tight', dpi=150)
print(f"Chart saved to {output_path}")
