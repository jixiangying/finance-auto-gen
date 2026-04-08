import matplotlib.pyplot as plt
import matplotlib.font_manager as fm
import os

# Set font for Chinese characters (macOS specific)
font_path = '/System/Library/Fonts/STHeiti Medium.ttc'
if not os.path.exists(font_path):
    font_path = '/System/Library/Fonts/PingFang.ttc'

prop = fm.FontProperties(fname=font_path)

# Data for April 8, 2026 (Evening)
indices = ['上证指数', '深证成指', '创业板指', '恒生指数', '恒生科技']
values = [3995.00, 14042.00, 2985.50, 25893.02, 4923.25]
changes = [2.69, 4.79, 5.12, 3.09, 5.22]
colors = ['#e63946' if c > 0 else '#2a9d8f' for c in changes]

fig, ax = plt.subplots(figsize=(10, 6), facecolor='#f8f9fa')
bars = ax.barh(indices, changes, color=colors, height=0.6)

# Add value labels
for i, (bar, change, val) in enumerate(zip(bars, changes, values)):
    width = bar.get_width()
    label_x = width + 0.1
    ax.text(label_x, bar.get_y() + bar.get_height()/2, 
            f'{val:,.2f} ({"+" if change > 0 else ""}{change}%)', 
            va='center', fontproperties=prop, fontsize=12, fontweight='bold')

# Styling
ax.set_title('2026年04月08日 国内及港股核心指数表现 (收盘)', fontproperties=prop, fontsize=16, pad=20)
ax.set_xlabel('涨跌幅 (%)', fontproperties=prop, fontsize=12)
ax.set_xlim(0, 6.5)
ax.invert_yaxis()  # Labels read top-to-bottom
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
ax.grid(axis='x', linestyle='--', alpha=0.7)

# Set tick labels font
ax.set_yticklabels(indices, fontproperties=prop, fontsize=12)

# Save the chart
output_dir = 'images/charts'
os.makedirs(output_dir, exist_ok=True)
output_path = os.path.join(output_dir, '2026-04-08-evening.png')
plt.tight_layout()
plt.savefig(output_path, dpi=150)
print(f'Chart saved to {output_path}')
