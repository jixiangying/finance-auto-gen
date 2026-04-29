import matplotlib.pyplot as plt
import matplotlib.font_manager as fm
import os

# Set up Chinese font for macOS
font_path = '/System/Library/Fonts/STHeiti Medium.ttc'
if not os.path.exists(font_path):
    font_path = '/System/Library/Fonts/PingFang.ttc'

prop = fm.FontProperties(fname=font_path)
plt.rcParams['font.sans-serif'] = [prop.get_name()]
plt.rcParams['axes.unicode_minus'] = False

# Data
labels = ['标普500', '纳斯达克', '道琼斯', '罗素2000']
values = [7138.80, 24663.80, 49141.93, 2756.05]
changes = [-0.5, -0.9, -0.1, -1.2]
colors = ['#22c55e' if c < 0 else '#ef4444' for c in changes] # Green for down, Red for up

fig, ax = plt.subplots(figsize=(10, 6), facecolor='#f8fafc')
ax.set_facecolor('#f8fafc')

bars = ax.bar(labels, [1]*len(labels), color=colors, alpha=0.1) # Placeholder for background

for i, (label, val, change) in enumerate(zip(labels, values, changes)):
    color = '#22c55e' if change < 0 else '#ef4444'
    ax.text(i, 0.6, f"{val:,.2f}", ha='center', va='center', fontsize=24, fontweight='bold', color='#1e293b')
    ax.text(i, 0.4, f"{change:+.1f}%", ha='center', va='center', fontsize=20, fontweight='bold', color=color)
    ax.text(i, 0.8, label, ha='center', va='center', fontsize=18, fontproperties=prop, color='#64748b')

ax.set_ylim(0, 1)
ax.axis('off')

plt.title('全球核心指数表现 (2026-04-28 收盘)', fontsize=22, fontproperties=prop, pad=20, color='#1e293b')
plt.tight_layout()

output_path = 'images/charts/2026-04-29-morning.png'
os.makedirs(os.path.dirname(output_path), exist_ok=True)
plt.savefig(output_path, dpi=300, bbox_inches='tight')
print(f"Chart saved to {output_path}")
