import matplotlib.pyplot as plt
from matplotlib import font_manager
import os

# Set font for Chinese characters (macOS)
font_path = '/System/Library/Fonts/STHeiti Medium.ttc'
if not os.path.exists(font_path):
    font_path = '/System/Library/Fonts/PingFang.ttc'
prop = font_manager.FontProperties(fname=font_path)

# Data
indices = ['S&P 500', 'Nasdaq', 'Dow Jones']
values = [7126.06, 24468.48, 49447.43]
changes = [1.20, 1.52, 1.79]
colors = ['#ff4d4f' if c > 0 else '#52c41a' for c in changes] # Red for up, Green for down (standard in China/some regions)
# Note: SKILL.md says "红色代表上涨 🔴，绿色代表下跌 🟢"

fig, ax = plt.subplots(figsize=(10, 4), facecolor='#f0f2f5')
ax.set_facecolor('#ffffff')

# Bars
bars = ax.barh(indices, values, color=colors, height=0.6)

# Labels
for i, (bar, change) in enumerate(zip(bars, changes)):
    width = bar.get_width()
    label_text = f"{values[i]:,.2f} (+{change:.2f}%)"
    ax.text(width + 500, bar.get_y() + bar.get_height()/2, label_text, 
            va='center', fontproperties=prop, fontsize=12, fontweight='bold')

# Formatting
ax.set_title('美股核心指数收盘点位 (2026-04-17)', fontproperties=prop, fontsize=16, pad=20)
ax.set_xlim(0, 55000)
ax.set_xlabel('点位', fontproperties=prop)
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)

# Tick font
ax.set_yticklabels(indices, fontproperties=prop, fontsize=12)
plt.tight_layout()

# Save
output_path = 'images/charts/20260420_morning.png'
os.makedirs(os.path.dirname(output_path), exist_ok=True)
plt.savefig(output_path, dpi=300)
print(f"Chart saved to {output_path}")
