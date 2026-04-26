import matplotlib.pyplot as plt
import matplotlib.font_manager as fm
import os

# Font path for macOS
font_path = '/System/Library/Fonts/STHeiti Medium.ttc'
prop = fm.FontProperties(fname=font_path)

# Data for New Week Outlook (Closing/Weekly stats)
labels = ['上证指数', '纳斯达克', '标普500', '比特币', '现货黄金', '布伦特原油']
# Values: Weekly change from latest research
values = [0.70, 1.50, 0.55, 4.20, -3.30, 17.00]
colors = ['#ff4d4d' if v > 0 else '#2ecc71' for v in values] # Red for up, Green for down (CN style)

fig, ax = plt.subplots(figsize=(10, 6))
bars = ax.bar(labels, values, color=colors)

# Customizing the chart
ax.set_title('本周全球核心资产累计涨跌幅 (2026/04/20 - 2026/04/24)', fontproperties=prop, fontsize=16)
ax.set_ylabel('涨跌幅 (%)', fontproperties=prop, fontsize=12)
ax.axhline(0, color='black', linewidth=0.8)

# Adding values on top of bars
for bar in bars:
    height = bar.get_height()
    ax.text(bar.get_x() + bar.get_width()/2., height + (0.5 if height > 0 else -1.5),
            f'{height:+.2f}%', ha='center', va='bottom', fontsize=12, fontweight='bold')

# Setting font for tick labels
ax.set_xticklabels(labels, fontproperties=prop, fontsize=12)

# Save the chart
output_dir = 'images/charts'
if not os.path.exists(output_dir):
    os.makedirs(output_dir)
output_path = os.path.join(output_dir, '2026-04-26-evening.png')
plt.tight_layout()
plt.savefig(output_path, dpi=150)
print(f"Chart saved to {output_path}")
