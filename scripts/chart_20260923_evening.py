#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
2026-09-23 晚报行情数据卡片生成脚本
国内市场收盘数据
"""
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.font_manager import FontProperties
import numpy as np
import os

# --- 字体设置（macOS 中文支持）---
font_paths = [
    '/System/Library/Fonts/STHeiti Medium.ttc',
    '/System/Library/Fonts/PingFang.ttc',
    '/Library/Fonts/Arial Unicode MS.ttf',
]
prop = None
for fp in font_paths:
    if os.path.exists(fp):
        prop = FontProperties(fname=fp)
        break

if prop is None:
    prop = FontProperties()

plt.rcParams['font.family'] = 'sans-serif'
plt.rcParams['axes.unicode_minus'] = False

# --- 数据定义 ---
assets = [
    ('上证指数',  3936.52, -0.39),
    ('深证成指',  13636.07, -0.64),
    ('创业板指',  3379.61, -0.60),
    ('北证50',    1074.04, +2.60),
    ('科创50',    1660.85, -0.25),
    ('恒生指数',  24834.12, -1.01),
    ('恒生科技',  4379.07, -1.33),
    ('人民币/美元', 6.7005, -0.08),  # 单位：元（涨跌用点）
]

names    = [a[0] for a in assets]
prices   = [a[1] for a in assets]
changes  = [a[2] for a in assets]

# 颜色：上涨红色，下跌绿色（A股惯例）
colors = ['#E53935' if c >= 0 else '#43A047' for c in changes]
text_colors = colors

# --- 绘图 ---
fig, ax = plt.subplots(figsize=(14, 5.5))
ax.set_facecolor('#0D0D1A')
fig.patch.set_facecolor('#0D0D1A')

n = len(assets)
card_w = 1.55
card_h = 3.2
spacing = 0.15
total_w = n * card_w + (n - 1) * spacing

for i, (name, price, change) in enumerate(assets):
    x = i * (card_w + spacing)
    color = '#E53935' if change >= 0 else '#43A047'
    sign = '+' if change >= 0 else ''

    # 卡片背景
    rect = mpatches.FancyBboxPatch(
        (x, 0.3), card_w - 0.05, card_h - 0.3,
        boxstyle="round,pad=0.05",
        linewidth=1.2, edgecolor=color,
        facecolor='#1A1A2E'
    )
    ax.add_patch(rect)

    # 资产名称
    ax.text(x + (card_w - 0.05) / 2, card_h - 0.05, name,
            ha='center', va='top', fontsize=10.5, color='#CCCCDD',
            fontproperties=prop, fontweight='bold')

    # 价格
    price_str = f'{price:,.2f}' if name != '人民币/美元' else f'{price:.4f}'
    ax.text(x + (card_w - 0.05) / 2, card_h / 2 + 0.25, price_str,
            ha='center', va='center', fontsize=13, color='white',
            fontproperties=prop, fontweight='bold')

    # 涨跌幅
    change_str = f'{sign}{change:.2f}%'
    ax.text(x + (card_w - 0.05) / 2, 0.65, change_str,
            ha='center', va='bottom', fontsize=12, color=color,
            fontproperties=prop, fontweight='bold')

ax.set_xlim(-0.2, total_w + 0.2)
ax.set_ylim(0, card_h + 0.5)
ax.axis('off')

# 标题与数据来源
ax.text(total_w / 2, card_h + 0.35,
        '2026年09月23日（周三）国内市场收盘行情',
        ha='center', va='top', fontsize=13, color='#AAAACC',
        fontproperties=prop, fontweight='bold')

ax.text(total_w / 2, 0.02,
        '数据来源：东方财富 / 港交所 | 仅供参考，不构成投资建议',
        ha='center', va='bottom', fontsize=7.5, color='#666688',
        fontproperties=prop)

plt.tight_layout(pad=0.5)
output_path = 'images/charts/2026-09-23-evening.png'
os.makedirs(os.path.dirname(output_path), exist_ok=True)
plt.savefig(output_path, dpi=150, bbox_inches='tight',
            facecolor=fig.get_facecolor())
plt.close()
print(f"✅ 行情卡片已保存至：{output_path}")
