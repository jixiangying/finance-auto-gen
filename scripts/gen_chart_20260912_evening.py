#!/usr/bin/env python3
"""Generate weekly-review market data card for 2026-09-12 evening report (Weekend Recap)."""
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

# (名称, 周五收盘, 周五单日涨跌文本, 全周累计涨跌文本, 全周涨跌数值[用于配色])
assets = [
    ('道琼斯工业', '52,573.29', '+0.98%', '-1.57%', -1.57),
    ('标普500', '7,656.98', '+0.86%', '-0.80%', -0.80),
    ('纳斯达克', '26,333.04', '+0.96%', '-0.66%', -0.66),
    ('10Y美债收益率', '4.97%', '+2bp', '+19bp', 0.19),
    ('美元指数', '99.05', '+0.30%', '-0.80%', -0.80),
    ('COMEX黄金($)', '4,390', '-0.4%', '-1.5%', -1.5),
    ('WTI原油($)', '100.6', '-1.8%', '+10.0%', 10.0),
    ('布伦特原油($)', '104.3', '-2.5%', '+9.2%', 9.2),
    ('比特币($)', '77,300', '+0.7%', '-2.4%', -2.4),
    ('以太坊($)', '2,450', '-1.0%', '-1.7%', -1.7),
    ('上证指数', '3,888.11', '-1.18%', '-1.07%', -1.07),
    ('深证成指', '13,471.26', '-1.08%', '-0.34%', -0.34),
    ('创业板指', '3,322.04', '-0.49%', '+1.08%', 1.08),
    ('恒生指数', '24,805.63', '-0.60%', '-3.30%', -3.30),
    ('恒生科技指数', '4,320.57', '-0.23%', '-5.45%', -5.45),
]

def get_color(chg):
    return '#e74c3c' if chg >= 0 else '#27ae60'

fig, axes = plt.subplots(3, 5, figsize=(16, 10))
fig.patch.set_facecolor('#1a1a2e')

for ax, (name, value, day, week, week_chg) in zip(axes.flatten(), assets):
    color = get_color(week_chg)
    ax.set_facecolor('#16213e')
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    ax.axis('off')
    rect = mpatches.FancyBboxPatch((0.03, 0.03), 0.94, 0.94,
                                    boxstyle='round,pad=0.02',
                                    linewidth=1.5, edgecolor=color,
                                    facecolor='#16213e')
    ax.add_patch(rect)
    ax.text(0.5, 0.84, name, ha='center', va='center', fontsize=11,
            color='#aaaacc', fontproperties=prop)
    ax.text(0.5, 0.62, value, ha='center', va='center', fontsize=14,
            color='white', fontweight='bold', fontproperties=prop)
    ax.text(0.5, 0.38, f'周五  {day}', ha='center', va='center',
            fontsize=10, color='#8888aa', fontproperties=prop)
    ax.text(0.5, 0.16, f'全周  {week}', ha='center', va='center',
            fontsize=12, color=color, fontweight='bold', fontproperties=prop)

fig.text(0.5, 0.98, '2026-09-12 周末复盘：核心资产周五收盘与全周累计表现', ha='center', va='top',
         fontsize=16, color='white', fontproperties=prop, fontweight='bold')
fig.text(0.5, 0.005, '数据来源：NYSE/NASDAQ/FRED/ICE/上期所/港交所/东方财富/CoinMarketCap  |  红色=上涨  绿色=下跌',
         ha='center', va='bottom', fontsize=8, color='#666688', fontproperties=prop)

plt.tight_layout(rect=[0, 0.02, 1, 0.96])
output_path = 'images/charts/2026-09-12-evening-weekly.png'
os.makedirs(os.path.dirname(output_path), exist_ok=True)
plt.savefig(output_path, dpi=150, bbox_inches='tight', facecolor=fig.get_facecolor())
print(f'Chart saved to {output_path}')
