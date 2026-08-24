#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
2026-08-24 Evening Market Data Chart
核心行情数据信息卡片 - 2026年8月24日 晚报
"""

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.font_manager import FontProperties
import numpy as np
import os

# ─── 中文字体配置 ───────────────────────────────────────────
font_paths = [
    '/System/Library/Fonts/STHeiti Medium.ttc',
    '/System/Library/Fonts/Supplemental/Songti.ttc',
    '/Library/Fonts/Arial Unicode MS.ttf',
]
prop = None
for fp in font_paths:
    if os.path.exists(fp):
        prop = FontProperties(fname=fp)
        plt.rcParams['font.family'] = prop.get_name()
        break

if prop is None:
    plt.rcParams['font.family'] = 'PingFang SC'
    prop = FontProperties(family='PingFang SC')

plt.rcParams['axes.unicode_minus'] = False

# ─── 数据定义 ─────────────────────────────────────────────────
assets = [
    {"name": "上证指数",   "value": 3882.01, "change": -0.59, "unit": "点"},
    {"name": "深证成指",   "value": 13794.29, "change": -2.13, "unit": "点"},
    {"name": "创业板指",   "value": 3431.89,  "change": -3.21, "unit": "点"},
    {"name": "恒生指数",   "value": 25517.33, "change": -1.89, "unit": "点"},
    {"name": "恒生科技",   "value": 4584.90,  "change": -3.61, "unit": "点"},
    {"name": "黄金现货",   "value": 4650.00,  "change": +0.80, "unit": "USD/oz"},
    {"name": "布伦特原油", "value": 93.00,    "change": -0.50, "unit": "USD/桶"},
    {"name": "10年美债",   "value": 4.71,     "change": -0.03, "unit": "%"},
    {"name": "美元指数",   "value": 98.75,    "change": -0.20, "unit": ""},
    {"name": "USD/CNY",    "value": 6.7841,   "change": +0.03, "unit": ""},
]

# ─── 颜色函数（A股/港股：红涨绿跌；国际：绿涨红跌）──────────────
def get_color(change, international=False):
    if international:
        return '#27ae60' if change >= 0 else '#e74c3c'
    else:
        return '#e74c3c' if change >= 0 else '#27ae60'

domestic_idx = list(range(5))
international_idx = list(range(5, 10))

# ─── 绘图 ────────────────────────────────────────────────────
fig, axes = plt.subplots(2, 5, figsize=(18, 8))
fig.patch.set_facecolor('#1a1a2e')

title_text = "2026年08月24日（周一）晚报  核心行情收盘数据"
fig.suptitle(title_text, fontsize=15, color='white',
             fontproperties=prop, y=0.97)

all_axes = axes.flatten()

for i, asset in enumerate(assets):
    ax = all_axes[i]
    ax.set_facecolor('#16213e')

    is_intl = i in international_idx
    color = get_color(asset["change"], international=is_intl)
    arrow = "▲" if asset["change"] >= 0 else "▼"
    sign = "+" if asset["change"] >= 0 else ""

    # 资产名称
    ax.text(0.5, 0.82, asset["name"], transform=ax.transAxes,
            ha='center', va='center', fontsize=11, color='#cccccc',
            fontproperties=prop)

    # 数值
    if asset["unit"] in ["点", ""]:
        val_str = f"{asset['value']:,.2f}"
    elif asset["unit"] == "%":
        val_str = f"{asset['value']:.2f}%"
    elif asset["unit"] == "USD/oz":
        val_str = f"${asset['value']:,.0f}"
    else:
        val_str = f"{asset['value']:.2f}"

    ax.text(0.5, 0.53, val_str, transform=ax.transAxes,
            ha='center', va='center', fontsize=14, color='white',
            fontweight='bold', fontproperties=prop)

    # 涨跌
    change_str = f"{arrow} {sign}{asset['change']:.2f}%"
    ax.text(0.5, 0.25, change_str, transform=ax.transAxes,
            ha='center', va='center', fontsize=13, color=color,
            fontweight='bold', fontproperties=prop)

    # 单位小字
    ax.text(0.5, 0.08, asset["unit"], transform=ax.transAxes,
            ha='center', va='center', fontsize=8, color='#888888',
            fontproperties=prop)

    # 边框
    for spine in ax.spines.values():
        spine.set_edgecolor(color)
        spine.set_linewidth(1.5)

    ax.set_xticks([])
    ax.set_yticks([])

# 分组标签
fig.text(0.22, 0.01, "▌ 国内市场（红涨绿跌）", ha='center', fontsize=9,
         color='#aaaaaa', fontproperties=prop)
fig.text(0.72, 0.01, "▌ 国际市场与大宗商品（绿涨红跌）", ha='center',
         fontsize=9, color='#aaaaaa', fontproperties=prop)

plt.tight_layout(rect=[0, 0.04, 1, 0.94])

# ─── 保存 ────────────────────────────────────────────────────
output_dir = '/Users/jxy/Documents/Project/finance-auto-gen/images/charts'
os.makedirs(output_dir, exist_ok=True)
output_path = os.path.join(output_dir, '2026-08-24-evening.png')
plt.savefig(output_path, dpi=150, bbox_inches='tight',
            facecolor=fig.get_facecolor())
plt.close()
print(f"✅ 图表已保存至: {output_path}")
