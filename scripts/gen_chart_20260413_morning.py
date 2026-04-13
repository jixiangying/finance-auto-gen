import matplotlib.pyplot as plt
import matplotlib.font_manager as fm
import os

# Set font for Chinese characters
font_path = '/System/Library/Fonts/PingFang.ttc'  # Common on macOS
if not os.path.exists(font_path):
    font_path = '/System/Library/Fonts/STHeiti Light.ttc'

prop = fm.FontProperties(fname=font_path)

# Data - Monday Morning Opening Reference (2026-04-13)
data = [
    {"name": "WTI 原油 (WTI Crude)", "value": "$107.28", "change": 8.5},
    {"name": "比特币 (BTC)", "value": "$73,500", "change": 0.6},
    {"name": "纳斯达克 (Nasdaq)", "value": "22,998.21", "change": 0.77},
    {"name": "上证指数 (SSE Index)", "value": "3,986.22", "change": 0.51},
    {"name": "A50 期货 (A50 Futures)", "value": "12,650.00", "change": -1.5},
    {"name": "现货黄金 (Spot Gold)", "value": "$4,670.00", "change": -2.0}
]

# Plotting
fig, ax = plt.subplots(figsize=(10, 6))
fig.patch.set_facecolor('#ffffff')
ax.set_facecolor('#ffffff')

y_pos = range(len(data))
colors = ['#e74c3c' if item['change'] > 0 else '#2ecc71' for item in data]

# Create bars
bars = ax.barh(y_pos, [1]*len(data), color=colors, alpha=0.1, height=0.7)

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

plt.title("核心资产新周开盘参考 (2026-04-13)", fontproperties=prop, fontsize=18, fontweight='bold', pad=20)

# Save
output_path = 'images/charts/2026-04-13-morning-chart.png'
os.makedirs(os.path.dirname(output_path), exist_ok=True)
plt.savefig(output_path, dpi=300, bbox_inches='tight', facecolor=fig.get_facecolor())
print(f"Chart saved to {output_path}")
