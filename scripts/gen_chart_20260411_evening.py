import matplotlib.pyplot as plt
import matplotlib.font_manager as fm
import os

# Set font for macOS to support Chinese characters
font_path = '/System/Library/Fonts/PingFang.ttc'
if not os.path.exists(font_path):
    font_path = '/System/Library/Fonts/STHeiti Light.ttc'

# If PingFang/STHeiti not found, try others
if not os.path.exists(font_path):
    font_path = '/System/Library/Fonts/Arial Unicode.ttf'

prop = fm.FontProperties(fname=font_path)

# Data for Weekly Review (Apr 6 - Apr 10)
labels = ['纳斯达克', '创业板指', '深证成指', '标普 500', '上证指数', 'WTI 原油']
# Using Friday Apr 10 Close Values
values = ['22998.21', '3448.79', '14309.47', '6810.71', '3986.22', '98.88']
# Weekly Changes
changes = [14.13, 9.50, 7.16, 3.65, 2.74, -11.35]

fig, ax = plt.subplots(figsize=(10, 6))
ax.set_facecolor('#f8f9fa')
fig.patch.set_facecolor('#ffffff')

for i, (label, value, change) in enumerate(zip(labels, values, changes)):
    color = 'green' if change < 0 else 'red'
    sign = '+' if change > 0 else ''
    
    # Draw a box for each index
    rect = plt.Rectangle((0.05, 0.82 - i*0.14), 0.9, 0.12, transform=ax.transAxes, color='white', ec='#dee2e6', lw=1, zorder=1)
    ax.add_patch(rect)
    
    ax.text(0.1, 0.88 - i*0.14, label, transform=ax.transAxes, fontproperties=prop, fontsize=14, fontweight='bold', va='center', zorder=2)
    ax.text(0.4, 0.88 - i*0.14, value, transform=ax.transAxes, fontproperties=prop, fontsize=16, color='#333333', va='center', zorder=2)
    ax.text(0.75, 0.88 - i*0.14, f'{sign}{change}%', transform=ax.transAxes, fontproperties=prop, fontsize=14, color=color, fontweight='bold', va='center', zorder=2)

ax.set_axis_off()
plt.title('2026年4月第2周 全球核心资产周度表现 (4/6 - 4/10)', fontproperties=prop, fontsize=20, pad=30, fontweight='bold')

# Add subtitle
ax.text(0.5, 0.96, '地缘危机化解引发估值修复，成长股全线爆发', transform=ax.transAxes, fontproperties=prop, fontsize=12, color='#666666', ha='center')

output_path = 'images/charts/2026-04-11-evening.png'
os.makedirs(os.path.dirname(output_path), exist_ok=True)
plt.savefig(output_path, dpi=300, bbox_inches='tight')
print(f'Saved to {output_path}')
