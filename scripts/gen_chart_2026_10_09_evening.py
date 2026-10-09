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

# Core assets for 2026-10-09 Evening (A-Share Intra-day Reversal & Sector Performance)
assets = [
    '算力硬件(分化)',
    '风电设备(回调)',
    '上证指数',
    '深证成指',
    '创业板指',
    '券商板块(反攻)',
    '恒生科技',
    '恒生指数',
    '北证50'
]

prices = [
    '获利回吐',
    '承压整理',
    '3,813.79',
    '12,641.86',
    '3,043.33',
    '午后护盘',
    '4,136.75',
    '24,211.35',
    '1,037.31'
]

# Daily changes (%)
changes = [-1.82, -1.25, 0.05, 0.17, 0.22, 1.38, 1.55, 1.79, 2.49]

# Chinese financial chart convention: Red up 🔴, Green down 🟢
colors = ['#ef4444' if c >= 0 else '#22c55e' for c in changes]

fig, ax = plt.subplots(figsize=(10, 6.5), dpi=300)
fig.patch.set_facecolor('#0f172a')
ax.set_facecolor('#1e293b')

bars = ax.barh(assets, changes, color=colors, height=0.56, edgecolor='none')

# Add zero line
ax.axvline(0, color='#64748b', linewidth=1.2, linestyle='--')

# Set labels and title
ax.set_title('2026年10月09日 晚间复盘：A股探底回升与核心资产涨跌幅', color='#f8fafc', fontsize=14, pad=18, fontproperties=prop, fontweight='bold')
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
output_file = "images/charts/2026-10-09-evening.png"
plt.savefig(output_file, facecolor=fig.get_facecolor(), edgecolor='none')
plt.close()
print(f"Chart successfully saved to {output_file}")
