#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
2026-09-24 早报行情卡片生成脚本
国际市场（美股9月23日收盘）
"""

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm
import numpy as np
import os

# ── 字体设置 ──────────────────────────────────────────────────────────────────
font_path = '/System/Library/Fonts/STHeiti Medium.ttc'
if not os.path.exists(font_path):
    font_path = '/System/Library/Fonts/Supplemental/Songti.ttc'
prop = fm.FontProperties(fname=font_path)
plt.rcParams['font.family'] = prop.get_name()
plt.rcParams['axes.unicode_minus'] = False

# ── 数据 ──────────────────────────────────────────────────────────────────────
assets = [
    ('标普500',      '7,718.45',  -0.60),
    ('纳指综合',     '26,934',    -1.10),
    ('道琼斯',       '51,503',    -0.70),
    ('纳斯达克100',  '26,936',    -1.18),
    ('费城半导体',   '12,534',    -0.85),
    ('10y美债',      '5.127%',    +1.59),  # 利率上行为负向
    ('美元指数',     '101.01',    +0.58),
    ('现货黄金',     '$4,305',    -1.30),
    ('WTI原油',      '$92.68',    -2.01),
    ('布伦特原油',   '$103.08',   +0.82),
    ('比特币',       '$84,448',   -2.00),
]

# ── 颜色映射（A股习惯：红涨绿跌）────────────────────────────────────────────
# 对于利率/美元：上行未必代表正向市场情绪，但这里仅用原始符号上色
def get_color(chg, asset_name):
    # 美债收益率上升对股市是负面的，但卡片保持数值原色
    if asset_name in ('10y美债', '美元指数'):
        return '#e63946' if chg > 0 else '#2a9d8f'
    return '#e63946' if chg > 0 else '#2a9d8f'

colors = [get_color(c, n) for n, _, c in assets]

# ── 绘图 ──────────────────────────────────────────────────────────────────────
fig, ax = plt.subplots(figsize=(14, 7))
fig.patch.set_facecolor('#0d1117')
ax.set_facecolor('#0d1117')

cols = 4
rows = (len(assets) + cols - 1) // cols

cell_w, cell_h = 1.0 / cols, 1.0 / rows
pad_x, pad_y = 0.01, 0.015

for i, (name, price, chg) in enumerate(assets):
    row = i // cols
    col = i % cols
    x0 = col * cell_w + pad_x
    y0 = 1.0 - (row + 1) * cell_h + pad_y
    w = cell_w - 2 * pad_x
    h = cell_h - 2 * pad_y
    color = colors[i]

    # 卡片背景
    rect = plt.Rectangle((x0, y0), w, h,
                          transform=ax.transAxes, clip_on=False,
                          facecolor='#161b22', edgecolor=color, linewidth=1.5,
                          zorder=2)
    ax.add_patch(rect)

    cx = x0 + w / 2
    arrow = '▲' if chg >= 0 else '▼'
    sign  = '+' if chg >= 0 else ''

    # 资产名称
    ax.text(cx, y0 + h * 0.78, name,
            transform=ax.transAxes, ha='center', va='center',
            fontproperties=prop, fontsize=11, color='#c9d1d9', zorder=3)
    # 价格
    ax.text(cx, y0 + h * 0.48, price,
            transform=ax.transAxes, ha='center', va='center',
            fontsize=13, fontweight='bold', color='white', zorder=3,
            fontproperties=prop)
    # 涨跌幅
    ax.text(cx, y0 + h * 0.18, f'{arrow} {sign}{chg:.2f}%',
            transform=ax.transAxes, ha='center', va='center',
            fontsize=10.5, color=color, zorder=3, fontproperties=prop)

ax.axis('off')
fig.text(0.5, 0.97,
         '2026-09-23（周三）美股/大宗/加密收盘行情',
         ha='center', va='center', fontsize=14, color='#f0f6fc',
         fontproperties=prop, fontweight='bold')
fig.text(0.5, 0.01,
         '数据来源：Yahoo Finance / Investing.com    🔴 上涨  🟢 下跌',
         ha='center', va='center', fontsize=8, color='#8b949e',
         fontproperties=prop)

out_dir  = '/Users/jxy/Documents/Project/finance-auto-gen/images/charts'
out_path = os.path.join(out_dir, 'chart_20260924_morning.png')
os.makedirs(out_dir, exist_ok=True)
plt.tight_layout(rect=[0, 0.03, 1, 0.95])
plt.savefig(out_path, dpi=150, bbox_inches='tight',
            facecolor=fig.get_facecolor())
plt.close()
print(f'✅ 行情卡片已保存至：{out_path}')
