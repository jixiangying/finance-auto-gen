#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
2026-09-25 晚报行情数据卡片（A股节前最后收盘·港股正常交易）
自动生成：scripts/gen_chart_20260925_evening.py
"""

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm
import matplotlib.patches as mpatches
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
    # A 股
    {'name': '上证指数',  'price': '3,888.37',  'chg': '-1.22%', 'up': False, 'group': 'A股'},
    {'name': '深证成指',  'price': '13,316.97', 'chg': '-2.34%', 'up': False, 'group': 'A股'},
    {'name': '创业板指',  'price': '3,288.95',  'chg': '-2.68%', 'up': False, 'group': 'A股'},
    {'name': '科创 50',   'price': '—',          'chg': '-2.35%', 'up': False, 'group': 'A股'},
    # 港股
    {'name': '恒生指数',  'price': '24,510.09', 'chg': '-1.01%', 'up': False, 'group': '港股'},
    {'name': '恒生科技',  'price': '4,311.78',  'chg': '-1.13%', 'up': False, 'group': '港股'},
    # 美股（背景参考）
    {'name': '道琼斯',    'price': '51,349.98', 'chg': '-0.31%', 'up': False, 'group': '美股'},
    {'name': '纳斯达克',  'price': '26,939.37', 'chg': '+0.01%', 'up': True,  'group': '美股'},
    {'name': '标普 500',  'price': '7,704.13',  'chg': '-0.02%', 'up': False, 'group': '美股'},
]

# ── 画布 ──────────────────────────────────────────────────────────────────────
fig, ax = plt.subplots(figsize=(14, 6.5))
ax.set_xlim(0, 14)
ax.set_ylim(0, 6.5)
ax.axis('off')
fig.patch.set_facecolor('#0d1117')
ax.set_facecolor('#0d1117')

# 标题
ax.text(7, 6.15, '📊  2026-09-25 晚报  |  核心行情数据卡',
        ha='center', va='center', fontsize=17, fontweight='bold',
        color='#E8E8E8', fontproperties=prop)
ax.text(7, 5.72, 'A股节前最后收盘（9-24）·港股正常交易（9-25）·美股背景参考（9-24）',
        ha='center', va='center', fontsize=9, color='#8B8B8B', fontproperties=prop)

# ── 分区标签 ─────────────────────────────────────────────────────────────────
group_labels = [
    (0.5, 5.28, '🇨🇳 A股（节前）', '#60a5fa'),
    (0.5, 3.18, '🇭🇰 港股', '#a78bfa'),
    (7.5, 3.18, '🇺🇸 美股（前日背景）', '#f59e0b'),
]
for gx, gy, gtxt, gcol in group_labels:
    ax.text(gx, gy, gtxt, ha='left', va='center', fontsize=9.5, fontweight='bold',
            color=gcol, fontproperties=prop)

# ── 卡片绘制 ─────────────────────────────────────────────────────────────────
card_w, card_h = 2.9, 1.4
pad_x = 0.3

# A股：4 张，第一行
a_start_x = 0.5
a_y0 = 3.6
for i, a in enumerate(assets[:4]):
    x0 = a_start_x + i * (card_w + pad_x)
    y0 = a_y0
    bg_color    = '#1a2a1a' if a['up'] else '#2a1a1a'
    border_color = '#22c55e' if a['up'] else '#ef4444'
    chg_color   = '#22c55e' if a['up'] else '#ef4444'
    arrow       = '▲' if a['up'] else '▼'
    rect = mpatches.FancyBboxPatch((x0, y0), card_w, card_h,
        boxstyle='round,pad=0.05', linewidth=1.5,
        edgecolor=border_color, facecolor=bg_color)
    ax.add_patch(rect)
    cx = x0 + card_w / 2
    ax.text(cx, y0 + card_h - 0.23, a['name'],
            ha='center', va='center', fontsize=11, fontweight='bold',
            color='#D4D4D4', fontproperties=prop)
    ax.text(cx, y0 + card_h / 2 - 0.05, a['price'],
            ha='center', va='center', fontsize=13, fontweight='bold', color='#FAFAFA')
    ax.text(cx, y0 + 0.24, f'{arrow} {a["chg"]}',
            ha='center', va='center', fontsize=11, fontweight='bold',
            color=chg_color, fontproperties=prop)

# 港股：2 张，第二行左侧
hk_start_x = 0.5
hk_y0 = 1.6
for i, a in enumerate(assets[4:6]):
    x0 = hk_start_x + i * (card_w + pad_x)
    y0 = hk_y0
    bg_color    = '#1a2a1a' if a['up'] else '#2a1a1a'
    border_color = '#22c55e' if a['up'] else '#ef4444'
    chg_color   = '#22c55e' if a['up'] else '#ef4444'
    arrow       = '▲' if a['up'] else '▼'
    rect = mpatches.FancyBboxPatch((x0, y0), card_w, card_h,
        boxstyle='round,pad=0.05', linewidth=1.5,
        edgecolor=border_color, facecolor=bg_color)
    ax.add_patch(rect)
    cx = x0 + card_w / 2
    ax.text(cx, y0 + card_h - 0.23, a['name'],
            ha='center', va='center', fontsize=11, fontweight='bold',
            color='#D4D4D4', fontproperties=prop)
    ax.text(cx, y0 + card_h / 2 - 0.05, a['price'],
            ha='center', va='center', fontsize=13, fontweight='bold', color='#FAFAFA')
    ax.text(cx, y0 + 0.24, f'{arrow} {a["chg"]}',
            ha='center', va='center', fontsize=11, fontweight='bold',
            color=chg_color, fontproperties=prop)

# 美股：3 张，第二行右侧
us_start_x = 7.5
us_y0 = 1.6
for i, a in enumerate(assets[6:]):
    x0 = us_start_x + i * (card_w + pad_x)
    y0 = us_y0
    bg_color    = '#1a2a1a' if a['up'] else '#1c1a0a'
    border_color = '#22c55e' if a['up'] else '#f59e0b'
    chg_color   = '#22c55e' if a['up'] else '#fbbf24'
    arrow       = '▲' if a['up'] else '▼'
    rect = mpatches.FancyBboxPatch((x0, y0), card_w, card_h,
        boxstyle='round,pad=0.05', linewidth=1.5,
        edgecolor=border_color, facecolor=bg_color)
    ax.add_patch(rect)
    cx = x0 + card_w / 2
    ax.text(cx, y0 + card_h - 0.23, a['name'],
            ha='center', va='center', fontsize=11, fontweight='bold',
            color='#D4D4D4', fontproperties=prop)
    ax.text(cx, y0 + card_h / 2 - 0.05, a['price'],
            ha='center', va='center', fontsize=13, fontweight='bold', color='#FAFAFA')
    ax.text(cx, y0 + 0.24, f'{arrow} {a["chg"]}',
            ha='center', va='center', fontsize=11, fontweight='bold',
            color=chg_color, fontproperties=prop)

# ── 关键注记 ─────────────────────────────────────────────────────────────────
notes = [
    (0.5,  0.95, '💡 沪深成交额 1.65 万亿元  |  个股 1119↑ / 4299↓  |  资金避险流向煤炭·银行高股息板块', '#9ca3af'),
    (0.5,  0.58, '🏦 PBOC：MLF净投放2000亿  |  节前隔夜逆回购上限→10000亿/日  |  "适度宽松"政策不变', '#93c5fd'),
    (0.5,  0.22, '⚠️  以上数据仅供参考，不构成投资建议', '#555555'),
]
for nx, ny, ntxt, ncol in notes:
    ax.text(nx, ny, ntxt, ha='left', va='center', fontsize=8.5,
            color=ncol, fontproperties=prop)

# ── 保存 ─────────────────────────────────────────────────────────────────────
out_dir = '/Users/jxy/Documents/Project/finance-auto-gen/images/charts'
os.makedirs(out_dir, exist_ok=True)
out_path = os.path.join(out_dir, '2026-09-25-evening-chart.png')
plt.tight_layout()
plt.savefig(out_path, dpi=160, bbox_inches='tight', facecolor='#0d1117')
plt.close()
print(f'[✓] 图表已保存：{out_path}')
