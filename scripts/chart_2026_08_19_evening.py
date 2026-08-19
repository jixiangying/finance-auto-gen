#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
行情数据卡片生成脚本 - 2026-08-19 晚报（国内A股/港股·2026-08-19收盘）
"""
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm
import os

# ─── 字体设置（macOS 中文支持）───────────────────────────────────────────────
font_paths = [
    '/System/Library/Fonts/STHeiti Medium.ttc',
    '/System/Library/Fonts/PingFang.ttc',
    '/Library/Fonts/Arial Unicode.ttf',
]
prop = None
for fp in font_paths:
    if os.path.exists(fp):
        prop = fm.FontProperties(fname=fp)
        plt.rcParams['font.family'] = prop.get_name()
        break

if prop is None:
    plt.rcParams['font.sans-serif'] = ['Arial Unicode MS', 'SimHei', 'DejaVu Sans']

plt.rcParams['axes.unicode_minus'] = False

# ─── 行情数据（2026-08-19 A股与港股收盘）─────────────────────────────────────────
assets = [
    ("上证指数",   3894.42,  -2.40),
    ("深证成指",  13890.15,  -5.01),
    ("创业板指",   3473.49,  -6.26),
    ("科创50",     1710.20,  -4.50),
    ("恒生指数",  25495.07,   0.09),
    ("恒生科技",   4682.05,  -1.21),
    ("银行ETF",      1.428,   1.85),
    ("煤炭ETF",      2.105,   2.18),
    ("半导体ETF",    1.152,  -6.88),
]

# 红涨绿跌（A股惯例）
RED   = '#f44b4b'
GREEN = '#2dba5f'
WHITE = '#ffffff'
GRAY  = '#aaaaaa'

fig = plt.figure(figsize=(14, 8), facecolor='#0d1117')
fig.patch.set_facecolor('#0d1117')

# 标题
fig.text(0.5, 0.96, '🇨🇳 国内A股与港股市场行情复盘  |  2026-08-19 收盘',
         ha='center', va='top', fontsize=16, color=WHITE,
         fontproperties=prop, fontweight='bold')
fig.text(0.5, 0.92, '数据来源：东方财富网 / 同花顺 / 证券交易所官方数据',
         ha='center', va='top', fontsize=9, color=GRAY,
         fontproperties=prop)

# 画 9 个卡片：3 行 × 3 列
cols = 3
rows = 3
card_w = 1.0 / cols
card_h = 0.78 / rows

for i, (name, price, pct) in enumerate(assets):
    row = i // cols
    col = i % cols
    x = col * card_w + 0.025
    y = 0.10 + (rows - 1 - row) * card_h + 0.01
    w = card_w - 0.05
    h = card_h - 0.02

    is_up   = pct >= 0
    clr     = RED if is_up else GREEN
    sign    = '+' if is_up else ''
    bg_clr  = '#1c1c2e' if is_up else '#0f2218'

    # 卡片背景
    ax_card = fig.add_axes([x, y, w, h])
    ax_card.set_facecolor(bg_clr)
    for sp in ax_card.spines.values():
        sp.set_edgecolor(clr)
        sp.set_linewidth(1.5)
    ax_card.set_xticks([])
    ax_card.set_yticks([])

    # 资产名称
    ax_card.text(0.08, 0.82, name,
                 ha='left', va='top', fontsize=11, color=GRAY,
                 fontproperties=prop, transform=ax_card.transAxes)

    # 价格
    if abs(price) < 10:
        price_str = f'{price:.3f}'
    elif abs(price) < 10000:
        price_str = f'{price:,.2f}'
    else:
        price_str = f'{price:,.2f}'

    ax_card.text(0.08, 0.52, price_str,
                 ha='left', va='top', fontsize=14, color=WHITE,
                 fontproperties=prop, fontweight='bold',
                 transform=ax_card.transAxes)

    # 涨跌幅
    pct_str = f'{sign}{pct:.2f}%'

    ax_card.text(0.08, 0.22, pct_str,
                 ha='left', va='top', fontsize=13, color=clr,
                 fontproperties=prop, fontweight='bold',
                 transform=ax_card.transAxes)

    # 小箭头
    arrow = '▲' if is_up else '▼'
    ax_card.text(0.85, 0.22, arrow,
                 ha='right', va='top', fontsize=14, color=clr,
                 transform=ax_card.transAxes)

# 输出路径
out_dir = '/Users/jxy/Documents/Project/finance-auto-gen/images/charts'
os.makedirs(out_dir, exist_ok=True)
out_path = os.path.join(out_dir, '2026-08-19-evening.png')
plt.savefig(out_path, dpi=150, bbox_inches='tight', facecolor='#0d1117')
plt.close()
print(f'✅ 行情卡片已保存：{out_path}')
