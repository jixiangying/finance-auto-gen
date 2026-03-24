import matplotlib.pyplot as plt
import matplotlib.font_manager as fm
import os

# Set font for macOS
font_path = '/System/Library/Fonts/STHeiti Medium.ttc'
if not os.path.exists(font_path):
    font_path = '/System/Library/Fonts/Supplemental/Songti.ttc'

prop = fm.FontProperties(fname=font_path)
plt.rcParams['axes.unicode_minus'] = False

# Data (Overnight Close for Monday, March 23, 2026)
data = [
    {"name": "Dow Jones", "price": "46,208.53", "change": "+1.38%"},
    {"name": "S&P 500", "price": "6,586.77", "change": "+1.23%"},
    {"name": "Nasdaq", "price": "21,946.76", "change": "+1.38%"},
    {"name": "WTI Oil", "price": "$88.13", "change": "-10.28%"},
    {"name": "Brent Oil", "price": "$99.96", "change": "-10.90%"},
    {"name": "Gold", "price": "$4,404.10", "change": "-3.64%"},
    {"name": "BTC", "price": "$71,000", "change": "+4.82%"},
    {"name": "10Y Treasury", "price": "4.334%", "change": "-0.05%"}
]

# Plotting
fig, ax = plt.subplots(figsize=(10, 8))
ax.set_facecolor('#fdfdfd')
fig.patch.set_facecolor('#ffffff')

for i, item in enumerate(data):
    color = 'red' if '+' in item['change'] else 'green'
    ax.text(0.05, 0.90 - i*0.11, item['name'], fontsize=18, fontweight='bold', transform=ax.transAxes, fontproperties=prop)
    ax.text(0.45, 0.90 - i*0.11, item['price'], fontsize=18, transform=ax.transAxes, fontproperties=prop)
    ax.text(0.75, 0.90 - i*0.11, item['change'], fontsize=18, color=color, fontweight='bold', transform=ax.transAxes, fontproperties=prop)

ax.set_axis_off()
plt.title('全球核心资产回顾 (2026-03-24 周二早报)', fontproperties=prop, fontsize=22, pad=20)

output_path = 'images/charts/2026-03-24-morning-chart.png'
os.makedirs(os.path.dirname(output_path), exist_ok=True)
plt.savefig(output_path, bbox_inches='tight', dpi=150)
print(f"Chart saved to {output_path}")
