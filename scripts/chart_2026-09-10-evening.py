#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
2026-09-10 收盘晚报 — 行情数据卡片
"""

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.font_manager import FontProperties
import os

# ── 字体设置（macOS 中文支持）──────────────────────────────────────────────────
font_paths = [
    '/System/Library/Fonts/STHeiti Medium.ttc',
    '/System/Library/Fonts/Supplemental/STHeiti Medium.ttc',
    '/System/Library/Fonts/PingFang.ttc',
]
prop = None
for fp in font_paths:
    if os.path.exists(fp):
        prop = FontProperties(fname=fp)
        break
if prop is None:
    prop = FontProperties(family='PingFang SC')

plt.rcParams['font.family'] = 'sans-serif'

# ── 数据 ───────────────────────────────────────────────────────────────────────
assets = [
    {'name': '上证指数',    'value': '3,934.40', 'change': '-0.43%', 'up': False},
    {'name': '深证成指',    'value': '13,617.67','change': '-0.77%', 'up': False},
    {'name': '创业板指',    'value': '3,338.42', 'change': '-0.49%', 'up': False},
    {'name': '恒生指数',    'value': '24,954.47','change': '-1.27%', 'up': False},
    {'name': '恒生科技',    'value': '4,330.49', 'change': '-2.04%', 'up': False},
    {'name': '国企指数',    'value': '8,274.78', 'change': '-1.13%', 'up': False},
]

# ── 画布 ───────────────────────────────────────────────────────────────────────
fig, axes = plt.subplots(1, len(assets), figsize=(18, 4))
fig.patch.set_facecolor('#1a1a2e')

for ax, asset in zip(axes, assets):
    color = '#e74c3c' if asset['up'] else '#2ecc71'
    ax.set_facecolor('#16213e')

    # 资产名称
    ax.text(0.5, 0.78, asset['name'],
            ha='center', va='center', fontproperties=prop,
            fontsize=13, color='#ecf0f1', transform=ax.transAxes, fontweight='bold')

    # 点位
    ax.text(0.5, 0.50, asset['value'],
            ha='center', va='center', fontproperties=prop,
            fontsize=16, color='#f0f0f0', transform=ax.transAxes, fontweight='bold')

    # 涨跌幅
    ax.text(0.5, 0.22, asset['change'],
            ha='center', va='center', fontproperties=prop,
            fontsize=14, color=color, transform=ax.transAxes, fontweight='bold')

    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    ax.axis('off')

    # 边框
    for spine in ['top', 'bottom', 'left', 'right']:
        ax.spines[spine].set_color(color)
        ax.spines[spine].set_linewidth(1.5)
        ax.spines[spine].set_visible(True)

# 标题
fig.suptitle('2026年09月10日（周四）收盘行情', fontproperties=prop,
             fontsize=15, color='#bdc3c7', y=1.02)

plt.tight_layout(pad=0.8)
output_path = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))),
                           'images', 'charts', 'chart_2026-09-10-evening.png')
os.makedirs(os.path.dirname(output_path), exist_ok=True)
plt.savefig(output_path, dpi=160, bbox_inches='tight',
            facecolor=fig.get_facecolor())
plt.close()
print(f'[OK] 图表已保存至: {output_path}')
