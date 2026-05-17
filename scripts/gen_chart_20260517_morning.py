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
    {"name": "S&P 500 (Friday)", "price": "7,408.50", "change": "-1.20% (D) | +0.1% (W)"},
    {"name": "Nasdaq (Friday)", "price": "26,225.14", "change": "-1.50% (D) | -0.1% (W)"},
    {"name": "Dow Jones (Friday)", "price": "49,526.17", "change": "-1.10% (D) | -0.2% (W)"},
    {"name": "Brent Oil (Friday)", "price": "$104.80", "change": "+3.50% (W)"},
    {"name": "Gold (Friday)", "price": "$4,575", "change": "-4.00% (W)"},
    {"name": "Bitcoin (Sunday)", "price": "$80,500", "change": "0.00% (W)"}
]

# Plotting
fig, ax = plt.subplots(figsize=(10, 6))
ax.set_facecolor('#fdfdfd')
fig.patch.set_facecolor('#ffffff')

for i, item in enumerate(data):
    # Determine color: Red for gain, Green for loss (Chinese market standard)
    # Check if first percentage is positive or negative
    main_change = item['change'].split('|')[0].strip()
    if '+' in main_change:
        color = 'red'
    elif '-' in main_change:
        color = 'green'
    else:
        color = 'black'
        
    ax.text(0.05, 0.85 - i*0.14, item['name'], fontsize=16, fontweight='bold', transform=ax.transAxes, fontproperties=prop)
    ax.text(0.40, 0.85 - i*0.14, item['price'], fontsize=16, transform=ax.transAxes, fontproperties=prop)
    ax.text(0.65, 0.85 - i*0.14, item['change'], fontsize=16, color=color, fontweight='bold', transform=ax.transAxes, fontproperties=prop)

ax.set_axis_off()
plt.title('全球核心资产回顾 (2026-05-17 周末复盘)', fontproperties=prop, fontsize=20, pad=20)

output_path = 'images/charts/2026-05-17-morning.png'
os.makedirs(os.path.dirname(output_path), exist_ok=True)
plt.savefig(output_path, bbox_inches='tight', dpi=150)
print(f"Chart saved to {output_path}")
