#!/usr/bin/env python3
"""
2026-10-02 国庆节早报 数据信息卡片生成脚本
国庆假期第2天 · 假日模式
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

# --- 数据 (10月1日收盘 / 假期替代指标) ---
# 名称, 数值字符串, 涨跌幅(%), 单位后缀, 分类key
assets = [
    ('富时A50期货',        '13,917',     +0.55,  'pt',   'cn'),
    ('离岸人民币\n(USD/CNH)', '6.710',   -0.15,  '',     'cn_fx'),   # CNH降 = 人民币升值 = 正面
    ('道琼斯\n(10/1收盘)', '50,957',     +0.10,  'pt',   'us'),
    ('标普500\n(10/1收盘)', '7,672.08',  +0.20,  'pt',   'us'),
    ('纳斯达克\n(10/1收盘)', '26,861',   +0.30,  'pt',   'us'),
    ('美债10Y收益率',      '5.233',      +0.02,  '%',    'bond'),
    ('布伦特原油',         '$100.63',    +2.10,  '/bbl', 'oil'),
    ('WTI原油',            '$92.62',     +1.80,  '/bbl', 'oil'),
    ('黄金现货',           '$4,173.50',  +0.35,  '/盎司','gold'),
    ('比特币\nBTC/USD',    '$84,450',    +1.20,  '',     'crypto'),
    ('以太坊\nETH/USD',    '$2,692',     +0.90,  '',     'crypto'),
    ('美元指数\nDXY',      '102.04',     -0.25,  '',     'fx'),
]

def get_color(pct, key=''):
    # 汇率 USD/CNH：数值越低 = 人民币越强 = 正面 → 反转颜色逻辑
    if key == 'cn_fx':
        return '#26A69A' if pct < 0 else '#EF5350'
    # 美债收益率升高对股市是压力 → 这里仍遵循普通上涨红/下跌绿
    return '#EF5350' if pct >= 0 else '#26A69A'

# --- 布局 ---
cols = 4
rows = (len(assets) + cols - 1) // cols  # 3行
fig_w = 16
fig_h = 2.4 * rows + 1.8
fig, ax = plt.subplots(figsize=(fig_w, fig_h))
ax.set_xlim(0, fig_w)
ax.set_ylim(0, fig_h)
ax.axis('off')

fig.patch.set_facecolor('#0d1117')
ax.set_facecolor('#0d1117')

# 标题
title_y = fig_h - 0.55
ax.text(fig_w / 2, title_y,
        '🎊 2026年10月02日 早报 · 国庆假期第2天 · 假日替代指标',
        color='#FFD700', ha='center', va='center', fontsize=15, fontweight='bold',
        fontproperties=font_prop)
ax.text(fig_w / 2, title_y - 0.45,
        '⚠ A股/港股休市（10月1日–7日）  |  美股 NYSE/NASDAQ 正常交易',
        color='#888888', ha='center', va='center', fontsize=9.5,
        fontproperties=font_prop)

# 卡片参数
card_w = 3.5
card_h = 1.75
margin_x = 0.35
margin_y = 0.32
start_x = 0.55
start_y = fig_h - 1.7

for i, asset in enumerate(assets):
    name, value, pct, unit, key = asset
    row = i // cols
    col = i % cols
    x = start_x + col * (card_w + margin_x)
    y = start_y - row * (card_h + margin_y)

    color = get_color(pct, key)
    arrow = '▲' if pct >= 0 else '▼'
    pct_label = f'{arrow} {abs(pct):.2f}%'
    pct_color = '#EF5350' if pct >= 0 else '#26A69A'
    if key == 'cn_fx':
        pct_color = '#26A69A' if pct < 0 else '#EF5350'

    # 卡片背景
    rect = mpatches.FancyBboxPatch(
        (x, y), card_w - 0.1, card_h - 0.12,
        boxstyle="round,pad=0.06",
        facecolor='#161b22', edgecolor=color, linewidth=1.8
    )
    ax.add_patch(rect)

    cx = x + (card_w - 0.1) / 2

    # 资产名称
    ax.text(cx, y + card_h - 0.42, name,
            color='#AAAAAA', ha='center', va='center', fontsize=9,
            fontproperties=font_prop)
    # 数值
    ax.text(cx, y + card_h - 0.92, f'{value}{unit}',
            color='#FFFFFF', ha='center', va='center', fontsize=13, fontweight='bold',
            fontproperties=font_prop)
    # 涨跌幅
    ax.text(cx, y + card_h - 1.38, pct_label,
            color=pct_color, ha='center', va='center', fontsize=10.5, fontweight='bold',
            fontproperties=font_prop)

# 页脚
ax.text(fig_w / 2, 0.18,
        '数据来源：Investing.com / CoinDesk / NYSE · 仅供参考，不构成投资建议',
        color='#444444', ha='center', va='center', fontsize=7.5,
        fontproperties=font_prop)

output_dir = '/Users/jxy/Documents/Project/finance-auto-gen/images/charts'
os.makedirs(output_dir, exist_ok=True)
output_path = os.path.join(output_dir, 'chart_2026_10_02_morning.png')
plt.tight_layout(pad=0.4)
plt.savefig(output_path, dpi=150, bbox_inches='tight', facecolor='#0d1117')
plt.close()
print(f'✅ 图表已保存至: {output_path}')
