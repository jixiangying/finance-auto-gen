import matplotlib.pyplot as plt
import matplotlib.font_manager as fm
import os

# Set font properties for Chinese support on macOS
font_path = '/System/Library/Fonts/STHeiti Medium.ttc'
if not os.path.exists(font_path):
    font_path = '/System/Library/Fonts/PingFang.ttc'

prop = fm.FontProperties(fname=font_path)
plt.rcParams['font.sans-serif'] = [prop.get_name()]
plt.rcParams['axes.unicode_minus'] = False

# Data for core assets (Weekly Performance)
assets = [
    ('标普500', '7230.12', 0.9),
    ('纳斯达克', '25114.44', 1.1),
    ('道琼斯', '49499.27', 0.5),
    ('10年美债', '4.39%', 1.86),
    ('WTI原油', '102.62', 8.16),
    ('黄金', '4607.70', -2.13),
    ('上证指数', '4112.16', 0.12),
    ('恒生指数', '25776.53', -0.78)
]

fig, ax = plt.subplots(figsize=(10, 6))
fig.patch.set_facecolor('#f5f5f5')
ax.set_facecolor('#ffffff')

y_pos = range(len(assets))
names = [x[0] for x in assets]
values = [x[1] for x in assets]
changes = [x[2] for x in assets]

# Create bars
colors = ['#ff4d4f' if x[2] > 0 else '#52c41a' for x in assets]

bars = ax.barh(y_pos, [x[2] for x in assets], color=colors, height=0.6)

# Add text labels
for i, (name, val, change) in enumerate(assets):
    color = '#ff4d4f' if change > 0 else '#52c41a'
    prefix = '+' if change > 0 else ''
    text = f"{val} ({prefix}{change}%)"
    ax.text(change + (0.1 if change > 0 else -0.1), i, text, 
            va='center', ha='left' if change > 0 else 'right',
            fontproperties=prop, fontsize=12, color=color, fontweight='bold')

ax.set_yticks(y_pos)
ax.set_yticklabels(names, fontproperties=prop, fontsize=14)
ax.invert_yaxis()  # top-to-bottom

ax.set_title('核心资产本周表现回顾 (截至2026年5月1日)', fontproperties=prop, fontsize=18, pad=20)
ax.set_xlabel('周度涨跌幅 (%)', fontproperties=prop, fontsize=12)

# Remove spines
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
ax.axvline(0, color='black', linewidth=0.8)

plt.tight_layout()

# Save the chart
output_dir = 'images/charts'
if not os.path.exists(output_dir):
    os.makedirs(output_dir)
output_path = os.path.join(output_dir, '2026-05-03-morning.png')
plt.savefig(output_path, dpi=300, bbox_inches='tight')
print(f"Chart saved to {output_path}")
