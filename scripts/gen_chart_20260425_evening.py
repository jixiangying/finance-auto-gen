import matplotlib.pyplot as plt
import matplotlib.font_manager as fm
import os

# Set font properties for Chinese support on macOS
font_path = '/System/Library/Fonts/STHeiti Medium.ttc'
if not os.path.exists(font_path):
    font_path = '/System/Library/Fonts/PingFang.ttc'

prop = fm.FontProperties(fname=font_path)

# Data
labels = ['S&P 500', 'Nasdaq', '上证指数', '恒生指数', '比特币', '黄金']
# Values: [Price, Day Change%, Week Change%]
# S&P 500: 7165.08, +0.80%, +0.55%
# Nasdaq: 24836.60, +1.63%, +1.50%
# SSE: 4044.13, -1.20%, -0.18%
# HSI: 25450.12, -1.79%, -2.71%
# BTC: 77502, -0.4% (est), +1.2% (est)
# Gold: 4743.80, -1.1% (est), +0.5% (est)

prices = ['7165.08', '24836.60', '4044.13', '25450.12', '77502', '4743.80']
day_changes = [0.80, 1.63, -1.20, -1.79, -0.4, -1.1]
week_changes = [0.55, 1.50, -0.18, -2.71, 1.2, 0.5]

fig, ax = plt.subplots(figsize=(12, 7))
fig.patch.set_facecolor('#f5f5f5')
ax.set_facecolor('#f5f5f5')

# Draw bars for day changes
colors = ['#ff4d4d' if x >= 0 else '#2eb82e' for x in day_changes]
bars = ax.bar(labels, day_changes, color=colors, alpha=0.8)

# Add text labels
for i, bar in enumerate(bars):
    height = bar.get_height()
    color = '#ff4d4d' if day_changes[i] >= 0 else '#2eb82e'
    ax.text(bar.get_x() + bar.get_width()/2., height + (0.1 if height > 0 else -0.3),
            f'{prices[i]}\n({"+" if day_changes[i]>0 else ""}{day_changes[i]}%)',
            ha='center', va='bottom' if height > 0 else 'top', fontsize=12, fontweight='bold', color=color)
    
    # Add week change text below
    ax.text(bar.get_x() + bar.get_width()/2., -3.5 if i < 3 else -3.5,
            f'全周: {"+" if week_changes[i]>0 else ""}{week_changes[i]}%',
            ha='center', va='center', fontsize=10, fontproperties=prop, color='gray')

ax.set_ylim(-4, 3)
ax.axhline(0, color='black', linewidth=0.8)
ax.set_title('核心资产周五及全周涨跌幅 (2026-04-25 周末复盘)', fontproperties=prop, fontsize=16, pad=20)
ax.set_ylabel('涨跌幅 (%)', fontproperties=prop, fontsize=12)

# Set tick fonts
ax.set_xticklabels(labels, fontproperties=prop, fontsize=12)
plt.xticks(rotation=0)

plt.tight_layout()
output_path = 'images/charts/2026-04-25-evening.png'
plt.savefig(output_path, dpi=300, bbox_inches='tight')
print(f'Chart saved to {output_path}')
