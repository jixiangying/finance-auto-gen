#!/usr/bin/env python3
"""Generate market data card for 2026-09-03 morning report (International Markets)."""
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.font_manager import FontProperties
import os

# 中文字体 (macOS)
font_path = '/System/Library/Fonts/STHeiti Medium.ttc'
if not os.path.exists(font_path):
    font_path = '/System/Library/Fonts/Supplemental/Arial Unicode.ttf'
prop = FontProperties(fname=font_path)

assets = [
    ('道琼斯', '53,061', +0.42),
    ('标普500', '7,666', +0.37),
    ('纳斯达克', '26,217', +0.51),
    ('10Y美债\n收益率', '4.80%', +0.06),
    ('黄金\n($/oz)', '4,321', -0.18),
    ('WTI原油\n($/桶)', '90.74', +1.23),
    ('BTC', '77,000', -0.80),
    ('ETH', '2,400', -1.20),
    ('DXY美元\n指数', '99.56', +0.15),
    ('EUR/USD', '1.1585', -0.12),
]

def get_color(chg):
    return '#e74c3c' if chg >= 0 else '#27ae60'

fig, axes = plt.subplots(2, 5, figsize=(16, 7))
fig.patch.set_facecolor('#1a1a2e')

for ax, (name, value, chg) in zip(axes.flatten(), assets):
    color = get_color(chg)
    ax.set_facecolor('#16213e')
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    ax.axis('off')
    rect = mpatches.FancyBboxPatch((0.03, 0.03), 0.94, 0.94,
                                    boxstyle='round,pad=0.02',
                                    linewidth=1.5, edgecolor=color,
                                    facecolor='#16213e')
    ax.add_patch(rect)
    ax.text(0.5, 0.78, name, ha='center', va='center', fontsize=11,
            color='#aaaacc', fontproperties=prop)
    ax.text(0.5, 0.50, value, ha='center', va='center', fontsize=14,
            color='white', fontweight='bold', fontproperties=prop)
    sign = '+' if chg >= 0 else ''
    ax.text(0.5, 0.22, f'{sign}{chg:.2f}%', ha='center', va='center',
            fontsize=12, color=color, fontweight='bold', fontproperties=prop)

fig.text(0.5, 0.97, '2026-09-02 国际市场收盘行情', ha='center', va='top',
         fontsize=16, color='white', fontproperties=prop, fontweight='bold')
fig.text(0.5, 0.01, '数据来源：NYSE / Investing.com / CoinGecko  |  红色=上涨  绿色=下跌',
         ha='center', va='bottom', fontsize=8, color='#666688', fontproperties=prop)

plt.tight_layout(rect=[0, 0.03, 1, 0.95])
output_path = 'images/charts/2026-09-03-morning-chart.png'
os.makedirs(os.path.dirname(output_path), exist_ok=True)
plt.savefig(output_path, dpi=150, bbox_inches='tight', facecolor=fig.get_facecolor())
print(f'Chart saved to {output_path}')
