import matplotlib.pyplot as plt
import matplotlib.font_manager as fm

# Data for the chart
indices = ['上证指数', '深证成指', '创业板指', '恒生指数', '恒生科技', '国企指数']
prices = [4106.26, 15176.58, 3753.96, 26160.33, 5042.68, 8845.02]
changes = [0.52, 1.30, 1.73, -1.22, -1.93, -1.59]

# Colors: Red for positive, Green for negative
colors = ['#ff4d4f' if c > 0 else '#52c41a' for c in changes]

# Font setup for macOS
font_path = '/System/Library/Fonts/STHeiti Medium.ttc'
prop = fm.FontProperties(fname=font_path)

plt.rcParams['font.sans-serif'] = ['STHeiti Medium']
plt.rcParams['axes.unicode_minus'] = False

fig, ax = plt.subplots(figsize=(10, 6))
bars = ax.bar(indices, changes, color=colors)

# Add value labels
for bar, price, change in zip(bars, prices, changes):
    height = bar.get_height()
    label_y = height + 0.1 if height > 0 else height - 0.3
    ax.text(bar.get_x() + bar.get_width()/2., label_y,
            f'{price}\n({change:+.2f}%)',
            ha='center', va='bottom' if height > 0 else 'top',
            fontproperties=prop, fontsize=10, fontweight='bold')

ax.set_title('2026年4月22日 核心行情概览', fontproperties=prop, fontsize=16, pad=20)
ax.set_ylabel('涨跌幅 (%)', fontproperties=prop, fontsize=12)
ax.axhline(0, color='black', linewidth=0.8)
ax.set_ylim(min(changes) - 1, max(changes) + 1)

# Explicitly set font for tick labels to prevent garbled characters
ax.set_xticks(range(len(indices)))
ax.set_xticklabels(indices, fontproperties=prop)

plt.tight_layout()
plt.savefig('images/charts/2026-04-22-evening.png', dpi=300)
print("Chart generated successfully: images/charts/2026-04-22-evening.png")
