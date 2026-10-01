#!/usr/bin/env python3
"""
2026-10-01 国庆节晚报 数据信息卡片生成脚本
国庆节假日模式：展示仍在交易的替代指标
"""

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.font_manager import FontProperties
import os

# --- 字体设置 ---
font_paths = [
    '/System/Library/Fonts/STHeiti Medium.ttc',
    '/System/Library/Fonts/Supplemental/STHeiti Medium.ttc',
    '/System/Library/Fonts/PingFang.ttc',
]
font_prop = None
for fp in font_paths:
    if os.path.exists(fp):
        font_prop = FontProperties(fname=fp, size=12)
        plt.rcParams['font.family'] = font_prop.get_name()
        break

if font_prop is None:
    plt.rcParams['font.sans-serif'] = ['Arial Unicode MS', 'SimHei', 'DejaVu Sans']

plt.rcParams['axes.unicode_minus'] = False

# --- 数据 ---
assets = [
    # 名称, 数值, 涨跌幅(%), 单位, 类别
    ('富时A50期货', '13841.0', -0.26, 'pt', 'cn'),
    ('离岸人民币\n(USD/CNH)', '6.7148', +0.09, '', 'cn_fx'),   # 人民币贬值 CNH升, 用红色
    ('比特币\nBTC/USD', '$83,742', +0.12, '', 'crypto'),
    ('标普500\n(9/30收盘)', '7,651.54', -0.25, 'pt', 'us'),
    ('纳斯达克\n(9/30收盘)', '26,861.06', +0.24, 'pt', 'us'),
    ('布伦特原油', '$97.5', -0.51, '/bbl', 'oil'),
    ('WTI原油', '$89.3', -0.62, '/bbl', 'oil'),
]

# 颜色规则：上涨红色，下跌绿色
# 离岸人民币特殊处理：CNH数值升高 = 人民币贬值 = 负面
def get_color(pct, key=''):
    if key == 'cn_fx':  # 汇率升高=人民币贬值=负面
        return '#EF5350' if pct > 0 else '#26A69A'
    return '#EF5350' if pct >= 0 else '#26A69A'

fig, ax = plt.subplots(figsize=(14, 6))
ax.set_xlim(0, 14)
ax.set_ylim(0, 6)
ax.axis('off')

# 背景
fig.patch.set_facecolor('#1a1a2e')
ax.set_facecolor('#1a1a2e')

# 标题
title_font = FontProperties(fname=font_paths[0] if font_prop else None, size=16) if font_prop else None
ax.text(7, 5.6, '🎊 2026年10月01日 国庆节晚报 · 假日替代指标', color='#FFD700',
        ha='center', va='center', fontsize=14,
        fontproperties=font_prop if font_prop else None, fontweight='bold')
ax.text(7, 5.15, '⚠ A股/港股休市（10月1日–7日）', color='#999999',
        ha='center', va='center', fontsize=10,
        fontproperties=font_prop if font_prop else None)

# 卡片布局
cols = 4
card_w = 3.0
card_h = 1.6
margin_x = 0.35
margin_y = 0.3
start_x = 0.7

positions = []
for i, asset in enumerate(assets):
    row = i // cols
    col = i % cols
    x = start_x + col * (card_w + margin_x)
    y = 3.9 - row * (card_h + margin_y)
    positions.append((x, y))

for i, (asset, pos) in enumerate(zip(assets, positions)):
    name, value, pct, unit, key = asset
    x, y = pos
    color = get_color(pct, key)
    arrow = '▲' if pct >= 0 else '▼'
    pct_label = f'({arrow} {abs(pct):.2f}%)'
    pct_display_color = '#EF5350' if pct >= 0 else '#26A69A'

    # 卡片背景
    rect = mpatches.FancyBboxPatch((x, y), card_w - 0.1, card_h - 0.1,
                                    boxstyle="round,pad=0.05",
                                    facecolor='#16213e', edgecolor=color, linewidth=1.5)
    ax.add_patch(rect)

    # 资产名称
    ax.text(x + (card_w - 0.1) / 2, y + card_h - 0.38, name,
            color='#CCCCCC', ha='center', va='center', fontsize=9,
            fontproperties=font_prop if font_prop else None)

    # 数值
    ax.text(x + (card_w - 0.1) / 2, y + card_h - 0.85, f'{value}{unit}',
            color='#FFFFFF', ha='center', va='center', fontsize=13, fontweight='bold',
            fontproperties=font_prop if font_prop else None)

    # 涨跌幅
    ax.text(x + (card_w - 0.1) / 2, y + card_h - 1.25, pct_label,
            color=pct_display_color, ha='center', va='center', fontsize=10, fontweight='bold',
            fontproperties=font_prop if font_prop else None)

# 免责声明
ax.text(7, 0.15, '数据来源：investing.com / coindesk / nyse · 仅供参考，不构成投资建议',
        color='#555555', ha='center', va='center', fontsize=7.5,
        fontproperties=font_prop if font_prop else None)

output_dir = '/Users/jxy/Documents/Project/finance-auto-gen/images/charts'
os.makedirs(output_dir, exist_ok=True)
output_path = os.path.join(output_dir, 'chart_2026_10_01_evening.png')
plt.tight_layout()
plt.savefig(output_path, dpi=150, bbox_inches='tight', facecolor='#1a1a2e')
plt.close()
print(f'✅ 图表已保存至: {output_path}')
