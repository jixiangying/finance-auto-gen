#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
2026-09-21 晚报行情数据卡片
自动生成：scripts/gen_chart_20260921_evening.py
"""

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm
import matplotlib.patches as mpatches
import numpy as np
import os

# ── 字体配置 ──────────────────────────────────────────────────────────────────
FONT_PATHS = [
    '/System/Library/Fonts/STHeiti Medium.ttc',
    '/System/Library/Fonts/PingFang.ttc',
    '/System/Library/Fonts/Supplemental/PingFang.ttc',
]
prop = None
for fp in FONT_PATHS:
    if os.path.exists(fp):
        prop = fm.FontProperties(fname=fp)
        plt.rcParams['font.family'] = prop.get_name()
        break
if prop is None:
    plt.rcParams['font.family'] = 'sans-serif'

# ── 数据 ──────────────────────────────────────────────────────────────────────
assets = [
    {'name': '上证指数', 'price': '3,949.85', 'chg': '+0.97%', 'up': True},
    {'name': '深证成指', 'price': '13,730.02', 'chg': '+0.65%', 'up': True},
    {'name': '创业板指', 'price': '3,399.59',  'chg': '+0.80%', 'up': True},
    {'name': '科创 50',  'price': '—',          'chg': '+0.29%', 'up': True},
    {'name': '北证 50',  'price': '—',          'chg': '+1.33%', 'up': True},
    {'name': '恒生指数', 'price': '25,042.71', 'chg': '+1.18%', 'up': True},
    {'name': '恒生科技', 'price': '4,423.29',  'chg': '+0.40%', 'up': True},
]

# ── 画布 ──────────────────────────────────────────────────────────────────────
fig, ax = plt.subplots(figsize=(12, 5))
ax.set_xlim(0, 12)
ax.set_ylim(0, 5)
ax.axis('off')
fig.patch.set_facecolor('#0d1117')
ax.set_facecolor('#0d1117')

# 标题
ax.text(6, 4.65, '📊 2026-09-21 晚报  核心行情数据卡',
        ha='center', va='center', fontsize=16, fontweight='bold',
        color='#E8E8E8', fontproperties=prop)

ax.text(6, 4.25, '成交额：2.03 万亿元   超 4,500 只个股上涨   节前博弈期',
        ha='center', va='center', fontsize=9, color='#8B8B8B', fontproperties=prop)

# ── 卡片绘制 ─────────────────────────────────────────────────────────────────
cols = 4
card_w, card_h = 2.6, 1.35
pad_x, pad_y = 0.25, 0.2
start_x = (12 - cols * card_w - (cols - 1) * pad_x) / 2
rows_y = [3.55, 2.05]

for i, a in enumerate(assets):
    row = i // cols
    col = i % cols
    x0 = start_x + col * (card_w + pad_x)
    y0 = rows_y[row]

    bg_color = '#1a2a1a' if a['up'] else '#2a1a1a'
    border_color = '#22c55e' if a['up'] else '#ef4444'
    chg_color   = '#22c55e' if a['up'] else '#ef4444'
    arrow       = '▲' if a['up'] else '▼'

    rect = mpatches.FancyBboxPatch(
        (x0, y0), card_w, card_h,
        boxstyle='round,pad=0.05',
        linewidth=1.5,
        edgecolor=border_color,
        facecolor=bg_color,
    )
    ax.add_patch(rect)

    cx = x0 + card_w / 2
    ax.text(cx, y0 + card_h - 0.22, a['name'],
            ha='center', va='center', fontsize=11, fontweight='bold',
            color='#D4D4D4', fontproperties=prop)
    ax.text(cx, y0 + card_h / 2 - 0.05, a['price'],
            ha='center', va='center', fontsize=13, fontweight='bold',
            color='#FAFAFA')
    ax.text(cx, y0 + 0.22, f'{arrow} {a["chg"]}',
            ha='center', va='center', fontsize=11, fontweight='bold',
            color=chg_color, fontproperties=prop)

# 主力资金流向小区
ax.text(0.18, 1.7, '🔥 主力资金净流入 TOP3',
        ha='left', va='center', fontsize=9, fontweight='bold',
        color='#22c55e', fontproperties=prop)
inflows = [
    '化学制药  +27.62亿',
    '通信设备  +25.99亿',
    '元件       +14.77亿',
]
for k, t in enumerate(inflows):
    ax.text(0.18, 1.35 - k * 0.32, f'  {t}',
            ha='left', va='center', fontsize=8.5, color='#86efac', fontproperties=prop)

ax.text(6.2, 1.7, '❄️ 主力资金净流出 TOP3',
        ha='left', va='center', fontsize=9, fontweight='bold',
        color='#ef4444', fontproperties=prop)
outflows = [
    '半导体  -49.78亿',
    '电池     -17.46亿',
    '专用设备 -13.36亿',
]
for k, t in enumerate(outflows):
    ax.text(6.2, 1.35 - k * 0.32, f'  {t}',
            ha='left', va='center', fontsize=8.5, color='#fca5a5', fontproperties=prop)

# 免责
ax.text(6, 0.12, '⚠️  以上数据仅供参考，不构成投资建议',
        ha='center', va='center', fontsize=7.5, color='#555555', fontproperties=prop)

# ── 保存 ─────────────────────────────────────────────────────────────────────
out_dir = '/Users/jxy/Documents/Project/finance-auto-gen/images/charts'
os.makedirs(out_dir, exist_ok=True)
out_path = os.path.join(out_dir, '20260921_evening.png')
plt.tight_layout()
plt.savefig(out_path, dpi=160, bbox_inches='tight', facecolor='#0d1117')
plt.close()
print(f'[✓] 图表已保存：{out_path}')
