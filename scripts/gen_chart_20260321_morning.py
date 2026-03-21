import matplotlib.pyplot as plt
import matplotlib.font_manager as fm
import os

# Set font for macOS
font_path = '/System/Library/Fonts/STHeiti Medium.ttc'
if not os.path.exists(font_path):
    font_path = '/System/Library/Fonts/Supplemental/Songti.ttc'

prop = fm.FontProperties(fname=font_path)
plt.rcParams['axes.unicode_minus'] = False

# Data
data = [
    {"name": "S&P 500", "price": "6,506.48", "change": "-1.51%"},
    {"name": "Dow Jones", "price": "45,577.47", "change": "-0.96%"},
    {"name": "Nasdaq", "price": "21,647.61", "change": "-2.01%"},
    {"name": "BTC", "price": "$70,733", "change": "-0.65%"},
    {"name": "Gold", "price": "$4,667", "change": "+1.39%"}, # Calculated from +64 on ~4603
    {"name": "Brent Oil", "price": "$112.19", "change": "+3.30%"}
]

# Plotting
fig, ax = plt.subplots(figsize=(10, 6))
ax.set_facecolor('#f0f0f0')
fig.patch.set_facecolor('#ffffff')

for i, item in enumerate(data):
    color = 'red' if '+' in item['change'] else 'green'
    ax.text(0.1, 0.85 - i*0.15, item['name'], fontsize=18, fontweight='bold', transform=ax.transAxes)
    ax.text(0.4, 0.85 - i*0.15, item['price'], fontsize=18, transform=ax.transAxes)
    ax.text(0.7, 0.85 - i*0.15, item['change'], fontsize=18, color=color, fontweight='bold', transform=ax.transAxes)

ax.set_axis_off()
plt.title('全球核心资产行情 (2026-03-21 早报)', fontproperties=prop, fontsize=22, pad=20)

output_path = 'images/charts/2026-03-21-morning-chart.png'
os.makedirs(os.path.dirname(output_path), exist_ok=True)
plt.savefig(output_path, bbox_inches='tight', dpi=150)
print(f"Chart saved to {output_path}")
