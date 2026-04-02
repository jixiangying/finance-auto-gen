import matplotlib.pyplot as plt
from matplotlib.font_manager import FontProperties
import os

# Set font for Chinese support (macOS)
font_path = '/System/Library/Fonts/STHeiti Medium.ttc'
if not os.path.exists(font_path):
    font_path = '/System/Library/Fonts/PingFang.ttc'
prop = FontProperties(fname=font_path)

# Data
indices = ['上证指数', '深证成指', '创业板指', '恒生指数', '恒生科技']
prices = [3919.37, 10631.14, 2185.63, 24620.60, 4639.71]
changes = [-0.74, -1.60, -2.31, -0.70, -1.63]
colors = ['green' if c < 0 else 'red' for c in changes]

# Create figure
fig, ax = plt.subplots(figsize=(10, 6))
bars = ax.bar(indices, changes, color=colors)

# Customize plot
ax.set_title('2026-04-02 国内及港股核心指数涨跌幅', fontproperties=prop, fontsize=16)
ax.set_ylabel('涨跌幅 (%)', fontproperties=prop, fontsize=12)
ax.axhline(0, color='black', linewidth=0.8)

# Add value labels
for bar in bars:
    height = bar.get_height()
    ax.text(bar.get_x() + bar.get_width()/2., height if height > 0 else height - 0.2,
            f'{height:.2f}%', ha='center', va='bottom' if height > 0 else 'top', fontsize=12)

# Set tick fonts
ax.set_xticklabels(indices, fontproperties=prop, fontsize=12)
for label in ax.get_yticklabels():
    label.set_fontsize(10)

# Save
output_path = 'images/charts/2026-04-02-evening.png'
os.makedirs(os.path.dirname(output_path), exist_ok=True)
plt.tight_layout()
plt.savefig(output_path, dpi=300)
print(f"Chart saved to {output_path}")
