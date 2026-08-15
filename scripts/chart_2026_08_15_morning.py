#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
行情数据卡片 - 2026-08-15 早报（国际市场）
数据来源：Finviz / Yahoo Finance / 2026-08-14 收盘
"""

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib import font_manager
import os

# ── 字体配置（macOS 中文支持）─────────────────────────────────────────────────
FONT_PATHS = [
    '/System/Library/Fonts/STHeiti Medium.ttc',
    '/System/Library/Fonts/STHeiti Light.ttc',
    '/Library/Fonts/Arial Unicode.ttf',
]
prop = None
for fp in FONT_PATHS:
    if os.path.exists(fp):
        prop = font_manager.FontProperties(fname=fp)
        plt.rcParams['font.family'] = prop.get_name()
        break
if prop is None:
    plt.rcParams['font.family'] = 'DejaVu Sans'

# ── 行情数据 ────────────────────────────────────────────────────────────────────
assets = [
    # (名称,         收盘价,      涨跌幅%)
    ('标普500 SPX',  '7,785.76',  -0.17),
    ('道琼斯 DJI',   '53,732',    -0.20),
    ('纳斯达克 COMP','26,729',    -0.28),
    ('罗素2000 IWM', '305.09',    +0.52),
    ('黄金 GC',      '$4,432',    +0.38),
    ('WTI原油 CL',   '$82.40',    +1.42),
    ('VIX 恐慌指数', '15.60',     -2.76),
    ('美元指数 DXY', '99.54',     -0.30),
    ('比特币 BTC',   '$62,954',   -0.43),
    ('以太坊 ETH',   '$1,879',    -0.05),
]

# ── 绘图 ────────────────────────────────────────────────────────────────────────
BG      = '#0f1117'
CARD_UP = '#1a3a1e'   # 深绿背景 → 上涨
CARD_DN = '#3a1a1a'   # 深红背景 → 下跌
CLR_UP  = '#4ade80'   # 亮绿
CLR_DN  = '#f87171'   # 亮红
CLR_TXT = '#e2e8f0'   # 正文浅灰
CLR_SUB = '#94a3b8'   # 次要灰

fig = plt.figure(figsize=(14, 8), facecolor=BG)
fig.suptitle(
    '2026年08月14日  美市收盘行情  国际市场早报',
    fontproperties=prop if prop else None,
    color=CLR_TXT, fontsize=15, fontweight='bold', y=0.97
)

COLS, ROWS = 5, 2
for idx, (name, price, pct) in enumerate(assets):
    ax = fig.add_subplot(ROWS, COLS, idx + 1)
    is_up = pct >= 0
    bg_c  = CARD_UP if is_up else CARD_DN
    clr_p = CLR_UP  if is_up else CLR_DN
    sign  = '▲' if is_up else '▼'

    ax.set_facecolor(bg_c)
    for spine in ax.spines.values():
        spine.set_visible(False)
    ax.set_xticks([])
    ax.set_yticks([])

    # 资产名称
    ax.text(0.5, 0.78, name,
            transform=ax.transAxes,
            ha='center', va='center',
            fontsize=10.5, color=CLR_SUB,
            fontproperties=prop if prop else None)
    # 价格
    ax.text(0.5, 0.50, price,
            transform=ax.transAxes,
            ha='center', va='center',
            fontsize=15, color=CLR_TXT, fontweight='bold',
            fontproperties=prop if prop else None)
    # 涨跌幅
    ax.text(0.5, 0.20, f'{sign} {abs(pct):.2f}%',
            transform=ax.transAxes,
            ha='center', va='center',
            fontsize=12, color=clr_p, fontweight='bold',
            fontproperties=prop if prop else None)

plt.subplots_adjust(left=0.02, right=0.98, top=0.90, bottom=0.04,
                    hspace=0.35, wspace=0.18)

# ── 保存 ────────────────────────────────────────────────────────────────────────
OUT_DIR = os.path.join(os.path.dirname(__file__), '..', 'images', 'charts')
os.makedirs(OUT_DIR, exist_ok=True)
OUT_PATH = os.path.join(OUT_DIR, '2026-08-15-morning.png')
plt.savefig(OUT_PATH, dpi=150, bbox_inches='tight', facecolor=BG)
plt.close()
print(f'[OK] 图表已保存至: {OUT_PATH}')
