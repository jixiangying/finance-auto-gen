import matplotlib.pyplot as plt
import matplotlib.font_manager as fm
import os

# Set font for Chinese characters
font_path = '/System/Library/Fonts/PingFang.ttc'  # Common on macOS
if not os.path.exists(font_path):
    font_path = '/System/Library/Fonts/STHeiti Light.ttc'

prop = fm.FontProperties(fname=font_path)

# Data - Weekly Performance (Week ending April 10, 2026)
data = [
    {"name": "纳斯达克 (Nasdaq)", "value": "22,902.89", "change": 4.7},
    {"name": "日经 225 (Nikkei)", "value": "56,924.11", "change": 7.1},
    {"name": "沪深 300 (CSI 300)", "value": "4,636.57", "change": 4.41},
    {"name": "标普 500 (S&P 500)", "value": "6,816.89", "change": 3.6},
    {"name": "道琼斯 (Dow Jones)", "value": "47,916.57", "change": 3.0},
    {"name": "德国 DAX 40", "value": "23,804.00", "change": 2.7},
    {"name": "英国 FTSE 100", "value": "10,601.00", "change": 1.6},
    {"name": "恒生指数 (HSI)", "value": "25,893.54", "change": 0.7}
]

# Plotting
fig, ax = plt.subplots(figsize=(10, 8))
fig.patch.set_facecolor('#ffffff')
ax.set_facecolor('#ffffff')

y_pos = range(len(data))
colors = ['#e74c3c' if item['change'] > 0 else '#2ecc71' for item in data]

# Create bars
bars = ax.barh(y_pos, [1]*len(data), color=colors, alpha=0.1, height=0.6)

# Add text labels
for i, item in enumerate(data):
    color = '#e74c3c' if item['change'] > 0 else '#2ecc71'
    prefix = "+" if item['change'] > 0 else ""
    ax.text(0.02, i, f"{item['name']}", va='center', fontproperties=prop, fontsize=14, fontweight='bold')
    ax.text(0.45, i, f"{item['value']}", va='center', fontsize=14, fontweight='bold')
    ax.text(0.85, i, f"{prefix}{item['change']}%", va='center', color=color, fontsize=14, fontweight='bold')

# Remove axes
ax.set_xlim(0, 1)
ax.axis('off')

plt.title("全球核心资产周度表现回顾 (04.06-04.10)", fontproperties=prop, fontsize=18, fontweight='bold', pad=20)

# Save
output_path = 'images/charts/2026-04-12-morning-chart.png'
os.makedirs(os.path.dirname(output_path), exist_ok=True)
plt.savefig(output_path, dpi=300, bbox_inches='tight', facecolor=fig.get_facecolor())
print(f"Chart saved to {output_path}")
