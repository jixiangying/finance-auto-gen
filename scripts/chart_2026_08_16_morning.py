#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
行情数据卡片生成脚本 - 2026-08-16 新周展望（国际+国内核心资产本周收盘）
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

# ─── 行情数据（2026-08-15 本周收盘 / 新周展望）────────────────────────────────
# 格式: (名称, 收盘价, 周度涨跌幅%)
assets = [
    ("S&P 500",    7785.76,  +0.36),
    ("纳斯达克",   26729.16, +0.14),
    ("道琼斯",     53732.41, -0.56),
    ("上证指数",    3927.18, -0.99),
    ("沪深300",    4665.88,  +0.04),
    ("恒生指数",   25116.85, -2.15),
    ("COMEX 黄金",  4380.40,  +0.43),
    ("布伦特原油",    88.52,  +0.91),
    ("美债10Y",       4.696,  +0.0),  # -0.3BP ≈ 0
    ("比特币",    63001.00,  -2.93),
]

# 配色
RED   = '#f44b4b'
GREEN = '#2dba5f'
WHITE = '#ffffff'
GRAY  = '#aaaaaa'

fig = plt.figure(figsize=(14, 9), facecolor='#0d1117')
fig.patch.set_facecolor('#0d1117')

# 标题
fig.text(0.5, 0.97, '🌐 全球市场本周收盘  |  2026-08-15  新周前瞻',
         ha='center', va='top', fontsize=16, color=WHITE,
         fontproperties=prop, fontweight='bold')
fig.text(0.5, 0.93, '数据来源：Yahoo Finance API  |  周五收盘价',
         ha='center', va='top', fontsize=9, color=GRAY,
         fontproperties=prop)

# 10 个卡片：2 行 × 5 列
cols = 5
rows = 2
card_w = 1.0 / cols
card_h = 0.78 / rows

for i, (name, price, pct) in enumerate(assets):
    row = i // cols
    col = i % cols
    x = col * card_w + 0.012
    y = 0.08 + (rows - 1 - row) * card_h + 0.01
    w = card_w - 0.024
    h = card_h - 0.025

    is_up  = pct >= 0
    clr    = RED if is_up else GREEN
    sign   = '+' if is_up else ''
    bg_clr = '#1c1c2e' if is_up else '#0f2218'

    ax_card = fig.add_axes([x, y, w, h])
    ax_card.set_facecolor(bg_clr)
    for sp in ax_card.spines.values():
        sp.set_edgecolor(clr)
        sp.set_linewidth(1.5)
    ax_card.set_xticks([])
    ax_card.set_yticks([])

    # 资产名称
    ax_card.text(0.08, 0.84, name,
                 ha='left', va='top', fontsize=10, color=GRAY,
                 fontproperties=prop, transform=ax_card.transAxes)

    # 价格
    if abs(price) < 100:
        price_str = f'{price:.3f}'
    else:
        price_str = f'{price:,.2f}'

    ax_card.text(0.08, 0.55, price_str,
                 ha='left', va='top', fontsize=13, color=WHITE,
                 fontproperties=prop, fontweight='bold',
                 transform=ax_card.transAxes)

    # 涨跌幅
    if name == '美债10Y':
        pct_str = f'{sign}{pct*100:.1f} bps'
    else:
        pct_str = f'{sign}{pct:.2f}%'

    ax_card.text(0.08, 0.22, pct_str,
                 ha='left', va='top', fontsize=12, color=clr,
                 fontproperties=prop, fontweight='bold',
                 transform=ax_card.transAxes)

    arrow = '▲' if is_up else '▼'
    ax_card.text(0.88, 0.22, arrow,
                 ha='right', va='top', fontsize=13, color=clr,
                 transform=ax_card.transAxes)

# 输出路径
out_dir = '/Users/jxy/Documents/Project/finance-auto-gen/images/charts'
os.makedirs(out_dir, exist_ok=True)
out_path = os.path.join(out_dir, '2026-08-16-morning.png')
plt.savefig(out_path, dpi=150, bbox_inches='tight', facecolor='#0d1117')
plt.close()
print(f'✅ 行情卡片已保存：{out_path}')
