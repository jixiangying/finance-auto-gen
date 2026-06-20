import matplotlib.pyplot as plt
import matplotlib.font_manager as fm
import os

# Set font for macOS
font_path = '/System/Library/Fonts/STHeiti Medium.ttc'
if not os.path.exists(font_path):
    font_path = '/System/Library/Fonts/PingFang.ttc'
if not os.path.exists(font_path):
    font_path = '/System/Library/Fonts/Supplemental/Songti.ttc'

prop = fm.FontProperties(fname=font_path)
plt.rcParams['axes.unicode_minus'] = False

# Data (Domestic Weekend Review - Friday/Thursday Close)
data = [
    {"name": "上证指数", "price": "4,090.48", "change": "周四跌-0.43% (全周涨+1.46%)"},
    {"name": "深证成指", "price": "16,030.70", "change": "周四涨+0.94% (全周涨+7.13%)"},
    {"name": "创业板指", "price": "4,252.39", "change": "周四涨+2.05% (全周涨+11.02%)"},
    {"name": "恒生指数", "price": "23,924.81", "change": "周四跌-1.59% (全周跌-3.21%)"},
    {"name": "恒生科技", "price": "4,604.35", "change": "周四跌-1.39% (全周跌-2.14%)"},
    {"name": "A股全周成交", "price": "3.31万亿", "change": "周四暴增+2200亿 (刷历史纪录)"}
]

# Plotting
fig, ax = plt.subplots(figsize=(11, 7))
ax.set_facecolor('#ffffff')
fig.patch.set_facecolor('#f4f4f5')

# Draw clean card rows
for i, item in enumerate(data):
    # Determine color for the text based on cumulative change or daily change
    # For A股成交 and others, color selection:
    if "涨+" in item['change'] or "暴增" in item['change']:
        color = '#ff4d4f' # Red for up
    elif "跌-" in item['change']:
        color = '#52c41a' # Green for down
    else:
        color = '#8c8c8c' # Gray

    # Grid line
    ax.axhline(0.85 - i*0.14 - 0.05, xmin=0.05, xmax=0.95, color='#e8e8e8', linewidth=1)
    
    # Text columns
    ax.text(0.08, 0.85 - i*0.14, item['name'], fontsize=16, fontweight='bold', transform=ax.transAxes, fontproperties=prop, color='#1f1f1f')
    ax.text(0.35, 0.85 - i*0.14, item['price'], fontsize=16, transform=ax.transAxes, fontproperties=prop, color='#262626')
    ax.text(0.58, 0.85 - i*0.14, item['change'], fontsize=15, color=color, fontweight='bold', transform=ax.transAxes, fontproperties=prop)

ax.set_axis_off()
plt.title('国内及香港核心资产行情 (2026-06-20 周末复盘)', fontproperties=prop, fontsize=20, fontweight='bold', pad=25, color='#1a1a1a')
plt.tight_layout()

output_path = '/Users/jxy/Documents/Project/finance-auto-gen/images/charts/2026-06-20-evening.png'
os.makedirs(os.path.dirname(output_path), exist_ok=True)
plt.savefig(output_path, bbox_inches='tight', dpi=300)
plt.close()
print(f"Chart saved to {output_path}")
