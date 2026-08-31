import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.font_manager import FontProperties
import numpy as np

# 中文字体支持 (macOS)
font_path = '/System/Library/Fonts/STHeiti Medium.ttc'
prop = FontProperties(fname=font_path)
prop_bold = FontProperties(fname=font_path, weight='bold')

fig, ax = plt.subplots(figsize=(14, 7))
fig.patch.set_facecolor('#0d1117')
ax.set_facecolor('#0d1117')

# 数据
assets = [
    '上证指数', '深证成指', '创业板指', '科创50', '沪深300',
    '恒生指数', '恒生科技'
]
closes = [3986.30, 14015.00, 3438.68, 1684.39, 4625.09, 25566.99, 4557.55]
changes = [+0.86, +0.44, +0.42, +1.34, +0.35, -0.07, +0.32]

colors = ['#ff4d4d' if c > 0 else '#00cc66' for c in changes]
text_colors = ['#ff6666' if c > 0 else '#33ff99' for c in changes]
arrows = ['▲' if c > 0 else '▼' for c in changes]

# 画卡片背景
card_width = 1.6
card_height = 3.0
x_positions = np.arange(len(assets)) * (card_width + 0.3)

for i, (asset, close, change, color, tcolor, arrow) in enumerate(
        zip(assets, closes, changes, colors, text_colors, arrows)):
    x = x_positions[i]

    # 卡片矩形
    rect = mpatches.FancyBboxPatch(
        (x - card_width/2, 0), card_width, card_height,
        boxstyle="round,pad=0.08",
        linewidth=1.5,
        edgecolor=color,
        facecolor='#161b22'
    )
    ax.add_patch(rect)

    # 资产名称
    ax.text(x, card_height - 0.35, asset,
            ha='center', va='center', fontsize=11,
            fontproperties=prop_bold, color='#e6edf3')

    # 收盘价
    close_str = f'{close:,.2f}'
    ax.text(x, card_height / 2 + 0.2, close_str,
            ha='center', va='center', fontsize=13,
            fontproperties=prop_bold, color='white')

    # 涨跌幅
    change_str = f'{arrow} {abs(change):.2f}%'
    ax.text(x, 0.55, change_str,
            ha='center', va='center', fontsize=11.5,
            fontproperties=prop_bold, color=tcolor)

ax.set_xlim(-card_width, x_positions[-1] + card_width)
ax.set_ylim(-0.3, card_height + 0.6)
ax.axis('off')

# 标题
ax.text((x_positions[0] + x_positions[-1]) / 2, card_height + 0.35,
        '2026年08月31日（周一）国内市场收盘行情',
        ha='center', va='center', fontsize=14,
        fontproperties=prop_bold, color='#58a6ff')

# 副标题
ax.text((x_positions[0] + x_positions[-1]) / 2, -0.18,
        '沪深成交额：21,310亿元  |  主力净流出约300亿  |  三大A股指数全线飘红',
        ha='center', va='center', fontsize=9,
        fontproperties=prop, color='#8b949e')

plt.tight_layout(pad=0.5)
import os
os.makedirs('/Users/jxy/Documents/Project/finance-auto-gen/images/charts', exist_ok=True)
plt.savefig('/Users/jxy/Documents/Project/finance-auto-gen/images/charts/2026-08-31-evening-chart.png',
            dpi=150, bbox_inches='tight', facecolor='#0d1117')
print('Chart saved successfully.')
