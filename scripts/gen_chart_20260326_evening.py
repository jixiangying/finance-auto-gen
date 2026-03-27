import matplotlib.pyplot as plt
import matplotlib.font_manager as fm
import os

# Correct Data for 2026-03-26
indices = ['上证指数', '深证成指', '创业板指', '恒生指数', '恒生科技']
values = [3889.08, 13606.44, 3272.49, 24856.43, 4761.54]
changes = [-1.09, -1.41, -1.34, -1.89, -3.28]

# Create directories if they don't exist
os.makedirs('images/charts', exist_ok=True)

# Font settings for macOS
font_path = '/System/Library/Fonts/STHeiti Medium.ttc'
if not os.path.exists(font_path):
    font_path = '/System/Library/Fonts/PingFang.ttc'

prop = fm.FontProperties(fname=font_path)
plt.rcParams['axes.unicode_minus'] = False

# Plotting
fig, ax1 = plt.subplots(figsize=(10, 6))
fig.patch.set_facecolor('#ffffff')

colors = ['#27ae60' if c < 0 else '#d63031' for c in changes]
bars = ax1.bar(indices, changes, color=colors, alpha=0.8, width=0.6)

# FIX: Explicitly set font for x-axis ticks
ax1.set_xticks(range(len(indices)))
ax1.set_xticklabels(indices, fontproperties=prop, fontsize=12)

ax1.set_ylabel('涨跌幅 (%)', fontproperties=prop, fontsize=12)
ax1.set_title('2026-03-26 国内核心指数收盘表现', fontproperties=prop, fontsize=18, pad=25)
ax1.grid(axis='y', linestyle='--', alpha=0.3)

# Adding labels on top/bottom of bars
for bar, val, change in zip(bars, values, changes):
    height = bar.get_height()
    # Adjust text position based on bar height
    y_offset = -0.15 if height < 0 else 0.05
    va = 'top' if height < 0 else 'bottom'
    
    ax1.text(bar.get_x() + bar.get_width()/2., height + y_offset,
             f'{val}\n({change}%)',
             ha='center', va=va, 
             fontproperties=prop, fontsize=11, fontweight='bold', color='#2d3436')

# Add a horizontal line at 0
ax1.axhline(0, color='black', linewidth=0.8, alpha=0.5)

plt.tight_layout()
plt.savefig('images/charts/2026-03-26-evening.png', dpi=300, bbox_inches='tight')
print("Corrected chart saved to images/charts/2026-03-26-evening.png")
