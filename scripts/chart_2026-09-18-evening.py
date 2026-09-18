#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
每日行情数据卡片生成脚本 - 2026-09-18 晚报
"""

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.font_manager import FontProperties
import os

# ── 字体设置（macOS 中文支持）──────────────────────────
font_paths = [
    '/System/Library/Fonts/STHeiti Medium.ttc',
    '/System/Library/Fonts/Supplemental/Songti.ttc',
    '/System/Library/Fonts/PingFang.ttc',
]
prop = None
for fp in font_paths:
    if os.path.exists(fp):
        prop = FontProperties(fname=fp)
        break
if prop is None:
    prop = FontProperties()

plt.rcParams['axes.unicode_minus'] = False

# ── 数据定义 ─────────────────────────────────────────────
assets = [
    {'name': '上证指数', 'price': '3,911.87', 'change': '+0.94%', 'up': True},
    {'name': '深证成指', 'price': '13,640.87', 'change': '+1.72%', 'up': True},
    {'name': '创业板指', 'price': '3,372.68', 'change': '+2.25%', 'up': True},
    {'name': '科创50',   'price': '1,652.63', 'change': '+2.88%', 'up': True},
    {'name': '恒生指数', 'price': '24,750.78', 'change': '+0.60%', 'up': True},
    {'name': '恒生科技', 'price': '4,405.50', 'change': '+2.20%', 'up': True},
]

# ── 画布 ─────────────────────────────────────────────────
fig, ax = plt.subplots(figsize=(12, 5))
ax.set_xlim(0, 12)
ax.set_ylim(0, 5)
ax.axis('off')
fig.patch.set_facecolor('#0d1117')
ax.set_facecolor('#0d1117')

# 标题
ax.text(6, 4.55, '2026-09-18  收盘行情数据卡片',
        ha='center', va='center', fontsize=15, fontproperties=prop,
        color='#e6edf3', fontweight='bold')
ax.text(6, 4.15, '市场集体收涨  半导体全线爆发  成交额破2万亿',
        ha='center', va='center', fontsize=10, fontproperties=prop,
        color='#8b949e')

# 卡片布局（2行×3列）
cols = 3
rows = 2
card_w = 3.6
card_h = 1.4
x_starts = [0.3, 4.2, 8.1]
y_starts = [2.55, 0.9]

for i, asset in enumerate(assets):
    col = i % cols
    row = i // cols
    x = x_starts[col]
    y = y_starts[row]

    color = '#f85149' if asset['up'] else '#3fb950'
    bg_color = '#161b22'
    border_color = color

    rect = mpatches.FancyBboxPatch(
        (x, y), card_w - 0.15, card_h - 0.1,
        boxstyle="round,pad=0.05",
        linewidth=1.5,
        edgecolor=border_color,
        facecolor=bg_color
    )
    ax.add_patch(rect)

    cx = x + (card_w - 0.15) / 2
    # 资产名称
    ax.text(cx, y + card_h - 0.28, asset['name'],
            ha='center', va='center', fontproperties=prop,
            fontsize=12, color='#c9d1d9', fontweight='bold')
    # 点位
    ax.text(cx, y + card_h - 0.72, asset['price'],
            ha='center', va='center', fontproperties=prop,
            fontsize=13, color='#e6edf3', fontweight='bold')
    # 涨跌幅
    arrow = '▲' if asset['up'] else '▼'
    ax.text(cx, y + card_h - 1.12, f"{arrow} {asset['change']}",
            ha='center', va='center', fontproperties=prop,
            fontsize=14, color=color, fontweight='bold')

# 成交额注释
ax.text(6, 0.45,
        '全市场成交额：2.09万亿元  较前日放量 +2,535亿元（+13.6%）  |  北向资金：净流入',
        ha='center', va='center', fontproperties=prop,
        fontsize=8.5, color='#8b949e')

ax.text(6, 0.15,
        '数据来源：新浪财经 / 东方财富 / 金融界  |  仅供参考，不构成投资建议',
        ha='center', va='center', fontproperties=prop,
        fontsize=7, color='#484f58')

# ── 保存 ─────────────────────────────────────────────────
output_path = '/Users/jxy/Documents/Project/finance-auto-gen/images/charts/chart_2026-09-18-evening.png'
os.makedirs(os.path.dirname(output_path), exist_ok=True)
plt.savefig(output_path, dpi=150, bbox_inches='tight',
            facecolor=fig.get_facecolor())
plt.close()
print(f"✅ 图表已保存至: {output_path}")
