import matplotlib.pyplot as plt
import matplotlib.font_manager as fm
import os

# Set font for Chinese characters
font_path = '/System/Library/Fonts/PingFang.ttc'  # Common on macOS
if not os.path.exists(font_path):
    font_path = '/System/Library/Fonts/STHeiti Light.ttc'

prop = fm.FontProperties(fname=font_path)

# Data
data = [
    {"name": "标普500", "value": "6,810.71", "change": -0.20},
    {"name": "道琼斯", "value": "47,872.65", "change": -0.65},
    {"name": "纳斯达克", "value": "22,998.21", "change": 0.77},
    {"name": "现货黄金", "value": "$4,765.60", "change": -1.10},
    {"name": "WTI原油", "value": "$98.88", "change": 2.34},
    {"name": "比特币", "value": "$73,000", "change": 3.50}
]

# Plotting
fig, ax = plt.subplots(figsize=(10, 6))
fig.patch.set_facecolor('#f4f4f4')
ax.set_facecolor('#f4f4f4')

y_pos = range(len(data))
names = [item['name'] for item in data]
changes = [item['change'] for item in data]
colors = ['#e74c3c' if c > 0 else '#2ecc71' for c in changes] # Red for up, Green for down (as per instructions)
# Note: Instructions say "红色代表上涨 🔴，绿色代表下跌 🟢"

# Create bars
bars = ax.barh(y_pos, [1]*len(data), color=colors, height=0.6)

# Add text labels
for i, item in enumerate(data):
    color = '#e74c3c' if item['change'] > 0 else '#2ecc71'
    prefix = "+" if item['change'] > 0 else ""
    ax.text(0.02, i, f"{item['name']}", va='center', fontproperties=prop, fontsize=14, fontweight='bold')
    ax.text(0.4, i, f"{item['value']}", va='center', fontsize=14, fontweight='bold')
    ax.text(0.8, i, f"{prefix}{item['change']}%", va='center', color=color, fontsize=14, fontweight='bold')

# Remove axes
ax.set_xlim(0, 1)
ax.axis('off')

plt.title("核心行情概览 - 2026年04月11日 早报", fontproperties=prop, fontsize=18, fontweight='bold', pad=20)

# Save
output_path = 'images/charts/2026-04-11-morning-chart.png'
plt.savefig(output_path, dpi=300, bbox_inches='tight', facecolor=fig.get_facecolor())
print(f"Chart saved to {output_path}")
