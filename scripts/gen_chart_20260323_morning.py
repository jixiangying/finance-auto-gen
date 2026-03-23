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
    {"name": "S&P 500 (Friday)", "price": "6,506.48", "change": "-1.50%"},
    {"name": "Nasdaq (Friday)", "price": "21,647.61", "change": "-2.00%"},
    {"name": "Dow Jones (Friday)", "price": "45,577.47", "change": "-1.00%"},
    {"name": "Brent Oil (Friday)", "price": "$108.29", "change": "+8.80% (W)"},
    {"name": "Gold (Friday)", "price": "$4,612.00", "change": "-3.06%"},
    {"name": "BTC (Morning)", "price": "$69,500", "change": "-2.04%"},
    {"name": "USD Index (DXY)", "price": "106.85", "change": "+0.45%"}
]

# Plotting
fig, ax = plt.subplots(figsize=(10, 7))
ax.set_facecolor('#fdfdfd')
fig.patch.set_facecolor('#ffffff')

for i, item in enumerate(data):
    color = 'red' if '+' in item['change'] else 'green'
    ax.text(0.05, 0.90 - i*0.13, item['name'], fontsize=18, fontweight='bold', transform=ax.transAxes, fontproperties=prop)
    ax.text(0.45, 0.90 - i*0.13, item['price'], fontsize=18, transform=ax.transAxes, fontproperties=prop)
    ax.text(0.75, 0.90 - i*0.13, item['change'], fontsize=18, color=color, fontweight='bold', transform=ax.transAxes, fontproperties=prop)

ax.set_axis_off()
plt.title('全球核心资产回顾 (2026-03-23 周一早报)', fontproperties=prop, fontsize=22, pad=20)

output_path = 'images/charts/2026-03-23-morning-chart.png'
os.makedirs(os.path.dirname(output_path), exist_ok=True)
plt.savefig(output_path, bbox_inches='tight', dpi=150)
print(f"Chart saved to {output_path}")
