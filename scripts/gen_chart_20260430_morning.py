import matplotlib.pyplot as plt
import matplotlib.font_manager as fm
import os

# Font path for macOS as specified in SKILL.md
font_path = '/System/Library/Fonts/STHeiti Medium.ttc'
if not os.path.exists(font_path):
    font_path = '/System/Library/Fonts/Cache/PingFang.ttc' # Fallback for some macOS versions

prop = fm.FontProperties(fname=font_path)
plt.rcParams['font.family'] = prop.get_name()
plt.rcParams['axes.unicode_minus'] = False

# Data
assets = ['S&P 500', 'Dow Jones', 'Nasdaq', 'Brent Oil', 'Bitcoin']
prices = ['7,135.95', '48,861.81', '24,673.24', '$118.00', '$75,440']
changes = [-0.04, -0.6, 0.04, 6.0, -2.0]
colors = ['green' if c >= 0 else 'red' for c in changes]
change_texts = [f'+{c}%' if c >= 0 else f'{c}%' for c in changes]

fig, ax = plt.subplots(figsize=(10, 6), dpi=100)
ax.set_facecolor('#f9f9f9')
fig.patch.set_facecolor('#ffffff')

y_pos = range(len(assets))
bars = ax.barh(y_pos, [abs(c) for c in changes], color=colors, height=0.6)

# Add text labels
for i, (p, c_text) in enumerate(zip(prices, change_texts)):
    ax.text(0.1, i, f'{assets[i]}: {p} ({c_text})', 
            va='center', fontproperties=prop, fontsize=14, fontweight='bold')

ax.set_yticks(y_pos)
ax.set_yticklabels(assets, fontproperties=prop, fontsize=12)
ax.set_title('全球核心资产表现 (2026-04-30 早报)', fontproperties=prop, fontsize=18, pad=20)
ax.set_xlabel('涨跌幅绝对值 (%)', fontproperties=prop, fontsize=12)

# Hide spines
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)

plt.tight_layout()
output_path = 'images/charts/20260430_morning.png'
os.makedirs(os.path.dirname(output_path), exist_ok=True)
plt.savefig(output_path)
print(f'Chart saved to {output_path}')
