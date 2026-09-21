#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
2026-09-21 早报行情卡片生成脚本
模式 C：新周展望 — 上周五（9月18日）收盘核心资产数据
"""

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm
import os

# ── 中文字体设置（macOS）──
FONT_PATHS = [
    '/System/Library/Fonts/STHeiti Medium.ttc',
    '/System/Library/Fonts/PingFang.ttc',
    '/System/Library/Fonts/Supplemental/Arial Unicode MS.ttf',
]
prop = None
for fp in FONT_PATHS:
    if os.path.exists(fp):
        prop = fm.FontProperties(fname=fp)
        plt.rcParams['font.family'] = prop.get_name()
        break

if prop is None:
    plt.rcParams['font.family'] = 'Arial'

plt.rcParams['axes.unicode_minus'] = False

# ── 数据定义 ──
assets = [
    {'name': 'S&P 500',    'value': '7,650.50', 'change': '-0.50%', 'up': False},
    {'name': 'Nasdaq',     'value': '26,522.55','change': '-0.73%', 'up': False},
    {'name': 'Dow Jones',  'value': '51,681.51','change': '-0.38%', 'up': False},
    {'name': '美债10Y',    'value': '5.01%',    'change': '+8bps',  'up': False},
    {'name': 'WTI原油',    'value': '$99.53',   'change': '-1.52%', 'up': False},
    {'name': '黄金',       'value': '$2,621',   'change': '+0.31%', 'up': True },
    {'name': 'BTC',        'value': '$81,236',  'change': '+0.45%', 'up': True },
    {'name': '美元指数',   'value': '105.42',   'change': '+0.21%', 'up': True },
]

# ── 绘图 ──
n = len(assets)
fig, axes = plt.subplots(2, 4, figsize=(14, 6))
fig.patch.set_facecolor('#0d1117')
axes_flat = axes.flatten()

for i, (ax, asset) in enumerate(zip(axes_flat, assets)):
    ax.set_facecolor('#161b22')
    color = '#ff4d4d' if asset['up'] else '#00cc66'
    ax.text(0.5, 0.72, asset['name'], transform=ax.transAxes,
            ha='center', va='center', fontsize=13, color='#c9d1d9',
            fontproperties=prop)
    ax.text(0.5, 0.46, asset['value'], transform=ax.transAxes,
            ha='center', va='center', fontsize=16, color='white',
            fontweight='bold', fontproperties=prop)
    ax.text(0.5, 0.22, asset['change'], transform=ax.transAxes,
            ha='center', va='center', fontsize=13, color=color,
            fontproperties=prop)
    for spine in ax.spines.values():
        spine.set_edgecolor('#30363d')
        spine.set_linewidth(1.2)
    ax.set_xticks([])
    ax.set_yticks([])

# 标题
fig.suptitle('核心资产概览  |  2026-09-18（周五）收盘',
             fontsize=15, color='#8b949e', y=0.97,
             fontproperties=prop)
fig.text(0.5, 0.01, '数据来源：NYSE / Yahoo Finance / CoinGecko    仅供参考，不构成投资建议',
         ha='center', fontsize=8, color='#484f58', fontproperties=prop)

plt.tight_layout(rect=[0, 0.04, 1, 0.95])

out_dir = os.path.join(os.path.dirname(__file__), '..', 'images', 'charts')
os.makedirs(out_dir, exist_ok=True)
out_path = os.path.join(out_dir, 'chart_20260921_morning.png')
plt.savefig(out_path, dpi=150, bbox_inches='tight', facecolor=fig.get_facecolor())
plt.close()
print(f'[OK] 行情卡片已保存至: {os.path.abspath(out_path)}')
