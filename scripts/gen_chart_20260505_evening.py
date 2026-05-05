import matplotlib.pyplot as plt
import matplotlib.font_manager as fm
import os

# Set font for Chinese characters (macOS)
font_path = '/System/Library/Fonts/STHeiti Medium.ttc'
if not os.path.exists(font_path):
    font_path = '/System/Library/Fonts/PingFang.ttc'
prop = fm.FontProperties(fname=font_path)

# Data
assets = ['富时中国 A50', '离岸人民币 (CNH)', '比特币 (BTC)', '布伦特原油']
values = ['15,580', '6.8450', '$80,210', '$114.44']
changes = [-0.57, -0.18, -0.48, 5.80]

# Colors: Red for up, Green for down (Chinese convention: Red Up, Green Down)
# Note: For CNH, an increase in the number means depreciation, but here we show 'change' as value change.
colors = ['#e63946' if c > 0 else '#2a9d8f' for c in changes]
change_texts = [f'+{c}%' if c > 0 else f'{c}%' for c in changes]

# Plot
fig, ax = plt.subplots(figsize=(10, 5), facecolor='#f8f9fa')
ax.set_facecolor('#f8f9fa')

bars = ax.barh(assets, [1]*len(assets), color=colors, height=0.6)

# Add text labels
for i, (asset, value, change, text) in enumerate(zip(assets, values, changes, change_texts)):
    ax.text(0.02, i, asset, va='center', fontsize=14, fontweight='bold', fontproperties=prop)
    ax.text(0.4, i, value, va='center', fontsize=14, fontproperties=prop)
    ax.text(0.8, i, text, va='center', fontsize=14, fontweight='bold', color=colors[i], fontproperties=prop)

# Customization
ax.set_xlim(0, 1)
ax.set_xticks([])
ax.set_yticks([])
ax.invert_yaxis()
for spine in ax.spines.values():
    spine.set_visible(False)

plt.title('假期末端替代指标表现 (2026-05-05)', fontproperties=prop, fontsize=18, pad=20)
plt.tight_layout()

# Save
output_path = 'images/charts/20260505_evening.png'
os.makedirs(os.path.dirname(output_path), exist_ok=True)
plt.savefig(output_path, dpi=200, bbox_inches='tight')
print(f'Chart saved to {output_path}')
