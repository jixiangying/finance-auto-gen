import matplotlib.pyplot as plt
import matplotlib.font_manager as fm
import os

# Set Chinese font
font_path = '/System/Library/Fonts/STHeiti Medium.ttc'
if not os.path.exists(font_path):
    font_path = '/System/Library/Fonts/PingFang.ttc'
prop = fm.FontProperties(fname=font_path)

plt.rcParams['font.sans-serif'] = ['Arial'] # Fallback
plt.rcParams['axes.unicode_minus'] = False

# Data: Index, Weekly Change, Friday Change (if relevant, but for weekend review we focus on weekly)
indices = ['上证指数', '沪深300', '深证成指', '恒生指数', '道琼斯', '标普500', '纳斯达克']
weekly_changes = [-0.54, -0.30, 1.93, -1.62, 2.10, 0.90, 0.50]
colors = ['green' if x < 0 else 'red' for x in weekly_changes]

fig, ax = plt.subplots(figsize=(10, 6))
bars = ax.bar(indices, weekly_changes, color=colors)

# Add labels
for bar in bars:
    height = bar.get_height()
    ax.text(bar.get_x() + bar.get_width()/2., height + (0.1 if height > 0 else -0.2),
            f'{height:+.2f}%', ha='center', va='bottom' if height > 0 else 'top', 
            fontproperties=prop, fontsize=12, fontweight='bold')

ax.set_title('全球核心指数本周涨跌幅 (5月18日-5月22日)', fontproperties=prop, fontsize=16)
ax.set_ylabel('涨跌幅 (%)', fontproperties=prop)
ax.axhline(0, color='black', linewidth=0.8)
ax.set_xticklabels(indices, fontproperties=prop, fontsize=11)

plt.tight_layout()
output_path = 'images/charts/2026-05-23-evening.png'
os.makedirs(os.path.dirname(output_path), exist_ok=True)
plt.savefig(output_path, dpi=300)
print(f'Chart saved to {output_path}')
