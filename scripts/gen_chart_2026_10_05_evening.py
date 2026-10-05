import os
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm

# Ensure directory exists
os.makedirs("images/charts", exist_ok=True)

# Set font for macOS
font_path = "/System/Library/Fonts/STHeiti Medium.ttc"
if os.path.exists(font_path):
    prop = fm.FontProperties(fname=font_path)
    plt.rcParams['font.sans-serif'] = ['STHeiti', 'PingFang SC', 'Heiti TC', 'Arial']
else:
    prop = fm.FontProperties(family='sans-serif')
    plt.rcParams['font.sans-serif'] = ['PingFang SC', 'Heiti TC', 'Arial']

plt.rcParams['axes.unicode_minus'] = False

# Core assets for 2026-10-05 Evening (HK Market Reopen & Global/Offshore Assets)
assets = [
    '恒生科技',
    '恒生指数',
    '恒生国企',
    '纳斯达克',
    '富时A50期指',
    '标普500',
    '现货黄金',
    '离岸人民币(CNH)',
    'WTI原油',
    '比特币(BTC)'
]

prices = [
    '4,261.90',
    '24,356.88',
    '8,612.30',
    '27,190.86',
    '13,912.0',
    '7,722.72',
    '$4,195.80',
    '6.7018',
    '$91.10',
    '$87,620'
]

# Daily changes (%)
changes = [2.50, 1.60, 1.51, 1.19, 0.84, 0.73, 0.08, 0.04, -0.18, -0.26]

# Chinese financial chart convention: Red up 🔴, Green down 🟢
colors = ['#ef4444' if c >= 0 else '#22c55e' for c in changes]

fig, ax = plt.subplots(figsize=(10, 6.5), dpi=300)
fig.patch.set_facecolor('#0f172a')
ax.set_facecolor('#1e293b')

bars = ax.barh(assets, changes, color=colors, height=0.58, edgecolor='none')

# Add zero line
ax.axvline(0, color='#64748b', linewidth=1.2, linestyle='--')

# Set labels and title
ax.set_title('2026年10月05日 晚间复盘：港股先锋反弹与全球及离岸核心资产表现', color='#f8fafc', fontsize=14, pad=18, fontproperties=prop, fontweight='bold')
ax.set_xlabel('当日涨跌幅度 (%)', color='#94a3b8', fontsize=11, fontproperties=prop)

# Customize ticks with explicit fontproperties to prevent garbled text
ax.tick_params(colors='#94a3b8', labelsize=11)
ax.set_yticks(range(len(assets)))
ax.set_yticklabels(assets, fontproperties=prop, color='#f8fafc', fontsize=11)

# Annotate values
for bar, price, change in zip(bars, prices, changes):
    width = bar.get_width()
    offset = 0.08 if width >= 0 else -0.08
    ha = 'left' if width >= 0 else 'right'
    sign = '+' if change > 0 else ''
    text_color = '#ef4444' if change >= 0 else '#22c55e'
    label_text = f"{price} ({sign}{change:.2f}%)"
    ax.text(width + offset, bar.get_y() + bar.get_height()/2, label_text,
            va='center', ha=ha, color=text_color, fontweight='bold', fontsize=10, fontproperties=prop)

# Set symmetric/proper x limits
min_val = min(changes)
max_val = max(changes)
ax.set_xlim(min_val - 0.8, max_val + 1.2)

# Grid & Spines
ax.grid(axis='x', linestyle=':', alpha=0.35, color='#475569')
for spine in ax.spines.values():
    spine.set_color('#334155')

plt.tight_layout()
output_file = "images/charts/2026-10-05-evening.png"
plt.savefig(output_file, facecolor=fig.get_facecolor(), edgecolor='none')
plt.close()
print(f"Chart successfully saved to {output_file}")
