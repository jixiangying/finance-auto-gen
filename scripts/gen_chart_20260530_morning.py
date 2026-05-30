
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm
import os

# Font configuration for macOS
font_path = '/System/Library/Fonts/STHeiti Medium.ttc'
if not os.path.exists(font_path):
    font_path = '/System/Library/Fonts/PingFang.ttc'

prop = fm.FontProperties(fname=font_path)
plt.rcParams['font.family'] = prop.get_name()
plt.rcParams['axes.unicode_minus'] = False

# Data
labels = ['S&P 500', 'Nasdaq', 'Dow Jones', '10Y Yield', 'Gold', 'WTI Oil', 'Bitcoin']
prices = ['7,580.06', '26,972.62', '51,032.46', '4.45%', '$4,541.41', '$87.36', '$73,478']
changes = [0.22, 0.20, 0.72, -0.013, 1.02, -1.7, -0.17]

# Colors: Red for positive, Green for negative (Chinese convention as requested)
colors = ['#ff4d4f' if c >= 0 else '#52c41a' for c in changes]
change_texts = [f'+{c}%' if c >= 0 else f'{c}%' for c in changes]

fig, ax = plt.subplots(figsize=(10, 6))
fig.patch.set_facecolor('#f0f2f5')
ax.set_facecolor('#f0f2f5')

y_pos = range(len(labels))
bars = ax.barh(y_pos, [abs(c) if c != 0 else 0.1 for c in changes], color=colors, height=0.6)

# Add labels and values
for i, (label, price, change_text) in enumerate(zip(labels, prices, change_texts)):
    ax.text(-0.1, i, label, ha='right', va='center', fontproperties=prop, fontsize=12, fontweight='bold')
    ax.text(0.1, i, f'{price} ({change_text})', ha='left', va='center', fontproperties=prop, fontsize=12)

ax.set_yticks([])
ax.set_xticks([])
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
ax.spines['bottom'].set_visible(False)
ax.spines['left'].set_visible(False)

plt.title('全球核心资产表现 (2026-05-29 收盘)', fontproperties=prop, fontsize=16, pad=20)
plt.tight_layout()

output_path = 'images/charts/2026-05-30-morning.png'
os.makedirs(os.path.dirname(output_path), exist_ok=True)
plt.savefig(output_path, dpi=300, bbox_inches='tight', facecolor=fig.get_facecolor())
print(f'Chart saved to {output_path}')
