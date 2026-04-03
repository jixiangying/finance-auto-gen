import matplotlib.pyplot as plt
import matplotlib.font_manager as fm
import os

# Set font for macOS
font_path = '/System/Library/Fonts/STHeiti Medium.ttc'
if not os.path.exists(font_path):
    font_path = '/System/Library/Fonts/PingFang.ttc'

prop = fm.FontProperties(fname=font_path)
plt.rcParams['font.family'] = prop.get_name()
plt.rcParams['axes.unicode_minus'] = False

# Data
labels = ['标普500', '纳斯达克', '道琼斯', '布伦特原油', '黄金', '比特币']
values = [6582.70, 21879.18, 46504.60, 109.03, 2350.00, 65727]
changes = [0.11, 0.18, -0.13, 7.4, -2.4, -0.5] # BTC estimated change for visual
colors = ['#ff4d4f' if c > 0 else '#52c41a' for c in changes]

fig, ax = plt.subplots(figsize=(10, 6), dpi=100)
fig.patch.set_facecolor('#f0f2f5')
ax.set_facecolor('#f0f2f5')

bars = ax.barh(labels, [1]*len(labels), color=colors, height=0.6)

# Add text
for i, (label, val, chg) in enumerate(zip(labels, values, changes)):
    color = '#ff4d4f' if chg > 0 else '#52c41a'
    sign = '+' if chg > 0 else ''
    text = f"{val:,.2f} ({sign}{chg}%)"
    if label == '比特币':
        text = f"{val:,.0f} (回调)"
    ax.text(0.02, i, label, fontproperties=prop, fontsize=14, va='center', color='#333')
    ax.text(0.98, i, text, fontproperties=prop, fontsize=14, va='center', ha='right', color=color, fontweight='bold')

ax.set_xlim(0, 1)
ax.axis('off')
plt.title('全球市场核心指标 (2026-04-02 收盘)', fontproperties=prop, fontsize=18, pad=20)

output_path = 'images/charts/2026-04-03-morning-chart.png'
os.makedirs(os.path.dirname(output_path), exist_ok=True)
plt.savefig(output_path, bbox_inches='tight', facecolor='#f0f2f5')
print(f"Chart saved to {output_path}")
