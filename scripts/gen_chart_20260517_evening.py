import matplotlib.pyplot as plt
import matplotlib.font_manager as fm
import os

# Asset data
assets = ['S&P 500', 'Nasdaq', 'Dow Jones', 'Brent Oil', 'Gold', 'Bitcoin']
prices = ['7,408.50', '26,225.14', '49,526.17', '$109.26', '$4,551.49', '$78,432']
changes = [-1.24, -1.54, -1.07, 3.10, -2.10, -1.52]  # Daily changes for Friday / 24h for BTC

# Colors: Red for positive, Green for negative (Chinese market convention)
colors = ['#27ae60' if c < 0 else '#e74c3c' for c in changes]

# Font settings for macOS
font_path = '/System/Library/Fonts/STHeiti Medium.ttc'
prop = fm.FontProperties(fname=font_path)

fig, ax = plt.subplots(figsize=(10, 6), facecolor='#f8f9fa')
bars = ax.barh(assets, [abs(c) for c in changes], color=colors, height=0.6)

# Add price and change labels
for i, (bar, price, change) in enumerate(zip(bars, prices, changes)):
    width = bar.get_width()
    label_text = f"{price} ({'+' if change > 0 else ''}{change}%)"
    ax.text(width + 0.1, bar.get_y() + bar.get_height()/2, label_text, 
            va='center', fontproperties=prop, fontsize=12, fontweight='bold')

# Styling
ax.set_title('全球核心资产收盘表现 (2026-05-17)', fontproperties=prop, fontsize=18, pad=20)
ax.set_xlabel('涨跌幅绝对值 (%)', fontproperties=prop, fontsize=12)
ax.invert_yaxis()
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
ax.grid(axis='x', linestyle='--', alpha=0.7)

# Ensure axis labels use the font
ax.set_yticklabels(assets, fontproperties=prop, fontsize=12)

plt.tight_layout()
output_path = 'images/charts/2026-05-17-evening.png'
os.makedirs(os.path.dirname(output_path), exist_ok=True)
plt.savefig(output_path, dpi=300, bbox_inches='tight')
print(f"Chart saved to {output_path}")
