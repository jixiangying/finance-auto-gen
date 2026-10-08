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

# Core assets for 2026-10-08 Evening (A-Share Post-Holiday Resumption & Domestic Market Rebalancing)
assets = [
    '银行板块(红利)',
    '恒生科技',
    '上证指数',
    '恒生指数',
    '富时中国A50',
    '深证成指',
    '创业板指',
    '科创50'
]

prices = [
    '防御领涨',
    '4,194.49',
    '3,811.90',
    '23,785.79',
    '13,816.0',
    '12,620.90',
    '3,036.66',
    '1,456.32'
]

# Daily changes (%)
changes = [1.25, -0.68, -0.79, -1.43, -1.85, -2.07, -3.15, -4.82]

# Chinese financial chart convention: Red up 🔴, Green down 🟢
colors = ['#ef4444' if c >= 0 else '#22c55e' for c in changes]

fig, ax = plt.subplots(figsize=(10, 6.2), dpi=300)
fig.patch.set_facecolor('#0f172a')
ax.set_facecolor('#1e293b')

bars = ax.barh(assets, changes, color=colors, height=0.56, edgecolor='none')

# Add zero line
ax.axvline(0, color='#64748b', linewidth=1.2, linestyle='--')

# Set labels and title
ax.set_title('2026年10月08日 晚间复盘：A股复市首日放量整固与核心资产涨跌幅', color='#f8fafc', fontsize=14, pad=18, fontproperties=prop, fontweight='bold')
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
ax.set_xlim(min_val - 1.2, max_val + 1.2)

# Grid & Spines
ax.grid(axis='x', linestyle=':', alpha=0.35, color='#475569')
for spine in ax.spines.values():
    spine.set_color('#334155')

plt.tight_layout()
output_file = "images/charts/2026-10-08-evening.png"
plt.savefig(output_file, facecolor=fig.get_facecolor(), edgecolor='none')
plt.close()
print(f"Chart successfully saved to {output_file}")
