import matplotlib.pyplot as plt
import matplotlib.font_manager as fm
import os

# Set font for macOS
font_path = '/System/Library/Fonts/STHeiti Medium.ttc'
if not os.path.exists(font_path):
    font_path = '/System/Library/Fonts/Supplemental/Songti.ttc'

prop = fm.FontProperties(fname=font_path)
plt.rcParams['axes.unicode_minus'] = False

# Data (Overnight Close for Friday, March 27, 2026)
data = [
    {"name": "Nasdaq Composite", "price": "20,948.36", "change": "-2.10%"},
    {"name": "S&P 500", "price": "6,368.85", "change": "-1.70%"},
    {"name": "Dow Jones", "price": "45,167.00", "change": "-1.72%"},
    {"name": "WTI Oil", "price": "$100.51", "change": "+6.38%"},
    {"name": "Gold", "price": "$4,534.90", "change": "+2.86%"},
    {"name": "BTC", "price": "$66,009.32", "change": "-3.60%"}
]

# Plotting
fig, ax = plt.subplots(figsize=(10, 6))
ax.set_facecolor('#fdfdfd')
fig.patch.set_facecolor('#ffffff')

for i, item in enumerate(data):
    # Red for up, Green for down (Chinese convention as per SKILL.md)
    color = 'red' if '+' in item['change'] else 'green'
    ax.text(0.05, 0.90 - i*0.14, item['name'], fontsize=18, fontweight='bold', transform=ax.transAxes, fontproperties=prop)
    ax.text(0.45, 0.90 - i*0.14, item['price'], fontsize=18, transform=ax.transAxes, fontproperties=prop)
    ax.text(0.75, 0.90 - i*0.14, item['change'], fontsize=18, color=color, fontweight='bold', transform=ax.transAxes, fontproperties=prop)

ax.set_axis_off()
plt.title('全球核心资产回顾 (2026-03-28 周六早报)', fontproperties=prop, fontsize=22, pad=20)

output_path = 'images/charts/2026-03-28-morning-chart.png'
os.makedirs(os.path.dirname(output_path), exist_ok=True)
plt.savefig(output_path, bbox_inches='tight', dpi=150)
print(f"Chart saved to {output_path}")
