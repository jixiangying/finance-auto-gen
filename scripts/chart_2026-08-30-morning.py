#!/usr/bin/env python3
# 2026-08-30 早报（周末复盘）核心资产表现数据卡片
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.font_manager import FontProperties
import os

# 中文字体支持 (macOS)
font_path = '/System/Library/Fonts/STHeiti Medium.ttc'
if not os.path.exists(font_path):
    font_path = '/System/Library/Fonts/Supplemental/Songti.ttc'
prop = FontProperties(fname=font_path)
prop_bold = FontProperties(fname=font_path, weight='bold')

plt.rcParams['axes.unicode_minus'] = False

# 核心资产数据（最新点位、周五单日涨跌、全周累计涨跌、周涨跌是否为正）
assets = [
    ('标普500', '7,730.99', '周五 +0.72%', '全周 +1.42%', True),
    ('纳斯达克', '26,541.35', '周五 +1.57%', '全周 +2.65%', True),
    ('道琼斯', '53,569.44', '周五 +0.20%', '全周 +0.48%', True),
    ('美10Y收益率', '4.73%', '周五 +4bps', '全周 +11bps', True),
    ('现货黄金', '$4,525/oz', '周五 -3.10%', '全周 -2.38%', False),
    ('WTI原油', '$82.82/bbl', '周五 -0.50%', '全周 -1.82%', False),
    ('比特币BTC', '$79,828', '周五 +1.20%', '全周 +3.76%', True),
    ('恒生科技指数', '5,420.10', '周五 +1.35%', '全周 +1.80%', True),
]

fig, ax = plt.subplots(figsize=(13, 6))
ax.set_facecolor('#0d1117')
fig.patch.set_facecolor('#0d1117')
ax.axis('off')

# 标题与副标题
ax.text(0.5, 0.97, '2026-08-30 全球市场周末复盘 · 核心资产周度/日度表现',
        transform=ax.transAxes, ha='center', va='top', fontsize=15,
        color='#e6edf3', fontproperties=prop_bold)
ax.text(0.5, 0.90, '统计周期：2026-08-24 至 2026-08-28 收盘及周末基准',
        transform=ax.transAxes, ha='center', va='top', fontsize=9,
        color='#8b949e', fontproperties=prop)

# 卡片布局
cols = 4
rows = 2
card_w = 0.22
card_h = 0.32
x_starts = [0.02, 0.26, 0.50, 0.74]
y_starts = [0.50, 0.12]

for i, (name, price, daily_change, weekly_change, is_up) in enumerate(assets):
    row = i // cols
    col = i % cols
    if row >= rows:
        break
    x = x_starts[col]
    y = y_starts[row]
    border_color = '#c62828' if is_up else '#388e3c'  # 红涨绿跌
    bg_color = '#2a1a1a' if is_up else '#1a2a1a'

    rect = mpatches.FancyBboxPatch((x, y), card_w, card_h,
                                    boxstyle="round,pad=0.01",
                                    facecolor=bg_color, edgecolor=border_color,
                                    linewidth=1.5, transform=ax.transAxes)
    ax.add_patch(rect)

    cx = x + card_w / 2
    # 资产名
    ax.text(cx, y + card_h - 0.035, name,
            transform=ax.transAxes, ha='center', va='top', fontsize=11,
            color='#c9d1d9', fontproperties=prop_bold)
    # 最新点位
    ax.text(cx, y + card_h * 0.56, price,
            transform=ax.transAxes, ha='center', va='center', fontsize=12,
            color='white', fontproperties=prop_bold)
    # 单日变动
    ax.text(cx, y + card_h * 0.32, daily_change,
            transform=ax.transAxes, ha='center', va='center', fontsize=9,
            color='#8b949e', fontproperties=prop)
    # 周度累计变动
    change_color = '#f85149' if is_up else '#3fb950'
    change_symbol = '▲' if is_up else '▼'
    ax.text(cx, y + 0.035, f'{change_symbol} {weekly_change}',
            transform=ax.transAxes, ha='center', va='bottom', fontsize=10,
            color=change_color, fontproperties=prop_bold)

# 免责声明
ax.text(0.5, 0.02, '仅供参考，不构成投资建议',
        transform=ax.transAxes, ha='center', va='bottom', fontsize=7,
        color='#484f58', fontproperties=prop)

output_path = os.path.join(os.path.dirname(__file__), '..', 'images', 'charts', '2026-08-30-morning-chart.png')
os.makedirs(os.path.dirname(output_path), exist_ok=True)
plt.tight_layout(pad=0)
plt.savefig(output_path, dpi=150, bbox_inches='tight', facecolor=fig.get_facecolor())
print(f"Chart saved to: {output_path}")
plt.close()
