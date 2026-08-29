#!/usr/bin/env python3
# 2026-08-29 早报核心行情数据卡片
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

# 数据（2026-08-28 收盘）
assets = [
    ('标普500', '7,730.99', '+0.72%', True),
    ('纳斯达克', '26,541.35', '+1.57%', True),
    ('道琼斯', '53,569.44', '+0.20%', True),
    ('美10Y收益率', '4.73%', '+4bps', True),
    ('现货黄金', '$4,525', '-3.1%', False),
    ('WTI原油', '$82.82', '-0.5%', False),
    ('比特币BTC', '$79,828', '+1.2%', True),
]

fig, ax = plt.subplots(figsize=(12, 5.5))
ax.set_facecolor('#0d1117')
fig.patch.set_facecolor('#0d1117')
ax.axis('off')

# 标题
ax.text(0.5, 0.97, '🌅  2026-08-29 全球市场早报 · 核心行情数据卡片',
        transform=ax.transAxes, ha='center', va='top', fontsize=15,
        color='#e6edf3', fontproperties=prop_bold)
ax.text(0.5, 0.90, '数据基准：2026-08-28（周五）纽约收盘',
        transform=ax.transAxes, ha='center', va='top', fontsize=9,
        color='#8b949e', fontproperties=prop)

# 卡片布局
cols = 4
rows = 2
card_w = 0.22
card_h = 0.30
x_starts = [0.02, 0.26, 0.50, 0.74]
y_starts = [0.52, 0.12]

for i, (name, price, change, is_up) in enumerate(assets):
    row = i // cols
    col = i % cols
    if row >= rows:
        break
    x = x_starts[col]
    y = y_starts[row]
    color = '#388e3c' if not is_up else '#c62828'  # 绿跌红涨（中国惯例）
    bg_color = '#1a2a1a' if not is_up else '#2a1a1a'

    rect = mpatches.FancyBboxPatch((x, y), card_w, card_h,
                                    boxstyle="round,pad=0.01",
                                    facecolor=bg_color, edgecolor=color,
                                    linewidth=1.5, transform=ax.transAxes)
    ax.add_patch(rect)

    cx = x + card_w / 2
    ax.text(cx, y + card_h - 0.04, name,
            transform=ax.transAxes, ha='center', va='top', fontsize=10,
            color='#c9d1d9', fontproperties=prop)
    ax.text(cx, y + card_h * 0.52, price,
            transform=ax.transAxes, ha='center', va='center', fontsize=12,
            color='white', fontproperties=prop_bold)
    change_color = '#f85149' if is_up else '#3fb950'
    change_symbol = '▲' if is_up else '▼'
    ax.text(cx, y + 0.05, f'{change_symbol} {change}',
            transform=ax.transAxes, ha='center', va='bottom', fontsize=10,
            color=change_color, fontproperties=prop_bold)

# 免责
ax.text(0.5, 0.02, '仅供参考，不构成投资建议',
        transform=ax.transAxes, ha='center', va='bottom', fontsize=7,
        color='#484f58', fontproperties=prop)

output_path = os.path.join(os.path.dirname(__file__), '..', 'images', 'charts', '2026-08-29-morning-chart.png')
os.makedirs(os.path.dirname(output_path), exist_ok=True)
plt.tight_layout(pad=0)
plt.savefig(output_path, dpi=150, bbox_inches='tight', facecolor=fig.get_facecolor())
print(f"Chart saved to: {output_path}")
plt.close()
