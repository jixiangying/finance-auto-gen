#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
行情数据卡片生成脚本 - 2026-09-14 早报（新周展望·本周核心资产周度收盘）
数据来源：Yahoo Finance API（截至2026-09-11周五收盘）
"""

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.font_manager import FontProperties
import os

# ── 中文字体 ──────────────────────────────────────────
font_candidates = [
    '/System/Library/Fonts/STHeiti Medium.ttc',
    '/System/Library/Fonts/PingFang.ttc',
    '/Library/Fonts/Arial Unicode MS.ttf',
]
font_path = None
for fp in font_candidates:
    if os.path.exists(fp):
        font_path = fp
        break

if font_path:
    prop      = FontProperties(fname=font_path, size=11)
    prop_sm   = FontProperties(fname=font_path, size=9)
    prop_lg   = FontProperties(fname=font_path, size=13)
    prop_ttl  = FontProperties(fname=font_path, size=15)
else:
    prop = prop_sm = prop_lg = prop_ttl = FontProperties(size=11)

# ── 数据 ─────────────────────────────────────────────
assets = [
    # (资产名称,  周五收盘,  单位,    日涨跌%,  周涨跌%)
    ('标普500',   7656.98,  'pts',  +0.86,   -0.80),
    ('纳斯达克',  26333.04, 'pts',  +0.96,   -0.66),
    ('道琼斯',   52573.29,  'pts',  +0.98,   -1.57),
    ('10Y美债',    4.890,   '%',   -1.07,   +3.99),
    ('美元指数',   99.13,   '',    +0.29,   +1.31),
    ('黄金现货',   4394.67, '$/oz', -1.08,  -0.79),
    ('WTI原油',    99.88,  '$/桶', -2.43,   +9.40),
    ('比特币',    77314,   '$',    +0.73,   -2.91),
]

# ── 布局 ─────────────────────────────────────────────
n = len(assets)
fig_w, fig_h = 13, 6.8
fig, axes = plt.subplots(2, 4, figsize=(fig_w, fig_h))
fig.patch.set_facecolor('#0D1117')
axes = axes.flatten()

UP_COLOR   = '#FF4D4D'   # 上涨 红
DOWN_COLOR = '#00C853'   # 下跌 绿
CARD_BG    = '#161B22'
BORDER_UP  = '#FF4D4D'
BORDER_DN  = '#00C853'

for i, (name, price, unit, day_pct, wk_pct) in enumerate(assets):
    ax = axes[i]
    ax.set_facecolor(CARD_BG)
    for sp in ax.spines.values():
        sp.set_edgecolor(UP_COLOR if day_pct >= 0 else DOWN_COLOR)
        sp.set_linewidth(1.8)

    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    ax.axis('off')

    # 资产名
    ax.text(0.5, 0.90, name, ha='center', va='top',
            color='#E6EDF3', fontproperties=prop_lg)

    # 价格
    if isinstance(price, float) and price < 10:
        price_str = f'{price:.3f}{unit}'
    elif isinstance(price, float):
        price_str = f'{price:,.2f} {unit}'.strip()
    else:
        price_str = f'{price:,} {unit}'.strip()
    ax.text(0.5, 0.65, price_str, ha='center', va='top',
            color='#E6EDF3', fontproperties=prop_lg,
            fontsize=12, fontweight='bold')

    # 日涨跌
    day_color = UP_COLOR if day_pct >= 0 else DOWN_COLOR
    day_sym   = '▲' if day_pct >= 0 else '▼'
    ax.text(0.5, 0.41,
            f'周五  {day_sym}{abs(day_pct):.2f}%',
            ha='center', va='top', color=day_color,
            fontproperties=prop)

    # 周涨跌
    wk_color = UP_COLOR if wk_pct >= 0 else DOWN_COLOR
    wk_sym   = '▲' if wk_pct >= 0 else '▼'
    ax.text(0.5, 0.20,
            f'全周  {wk_sym}{abs(wk_pct):.2f}%',
            ha='center', va='top', color=wk_color,
            fontproperties=prop)

# ── 标题 ─────────────────────────────────────────────
fig.suptitle('2026-09-14  全球核心资产 · 上周周度收盘行情\n（截至 2026-09-11 周五收盘）',
             color='#E6EDF3', fontproperties=prop_ttl,
             y=1.01, va='bottom')

plt.tight_layout(rect=[0, 0, 1, 1])

# ── 输出 ─────────────────────────────────────────────
out_path = 'images/charts/2026-09-14-morning-chart.png'
os.makedirs(os.path.dirname(out_path), exist_ok=True)
plt.savefig(out_path, dpi=150, bbox_inches='tight',
            facecolor=fig.get_facecolor())
plt.close()
print(f'✅  已保存: {out_path}')
