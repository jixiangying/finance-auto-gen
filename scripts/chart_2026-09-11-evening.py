#!/usr/bin/env python3
"""
数据信息卡片：2026-09-11 晚报（国内市场收盘行情）
"""
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib import font_manager
import os

# ── 字体设置（macOS 中文支持）──────────────────────────────────────────────
font_paths = [
    '/System/Library/Fonts/STHeiti Medium.ttc',
    '/System/Library/Fonts/PingFang.ttc',
    '/System/Library/Fonts/Supplemental/Songti.ttc',
]
prop = None
for fp in font_paths:
    if os.path.exists(fp):
        prop = font_manager.FontProperties(fname=fp)
        plt.rcParams['font.family'] = prop.get_name()
        break

# ── 数据 ──────────────────────────────────────────────────────────────────
assets = [
    {'name': '上证指数',   'price': '3,888.11', 'change': '-1.18%', 'up': False},
    {'name': '深证成指',   'price': '13,471.26','change': '-1.08%', 'up': False},
    {'name': '创业板指',   'price': '3,322.04', 'change': '-0.49%', 'up': False},
    {'name': '恒生指数',   'price': '24,805.63','change': '-0.60%', 'up': False},
    {'name': '恒生科技',   'price': '4,320.57', 'change': '-0.23%', 'up': False},
]

# ── 配色 ──────────────────────────────────────────────────────────────────
BG_COLOR   = '#1a1a2e'
CARD_UP    = '#c0392b'   # 上涨红
CARD_DOWN  = '#27ae60'   # 下跌绿
TEXT_WHITE = '#ecf0f1'
TEXT_GRAY  = '#bdc3c7'

fig, axes = plt.subplots(1, len(assets), figsize=(16, 4))
fig.patch.set_facecolor(BG_COLOR)

for ax, asset in zip(axes, assets):
    color = CARD_UP if asset['up'] else CARD_DOWN
    ax.set_facecolor(color)
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    ax.axis('off')

    # 资产名称
    ax.text(0.5, 0.78, asset['name'], ha='center', va='center',
            fontsize=15, fontweight='bold', color=TEXT_WHITE,
            fontproperties=prop)
    # 价格
    ax.text(0.5, 0.52, asset['price'], ha='center', va='center',
            fontsize=18, fontweight='bold', color=TEXT_WHITE,
            fontproperties=prop)
    # 涨跌幅
    arrow = '▼' if not asset['up'] else '▲'
    ax.text(0.5, 0.28, f"{arrow} {asset['change']}", ha='center', va='center',
            fontsize=14, color=TEXT_WHITE, fontproperties=prop)

# 标题
fig.suptitle('2026-09-11  国内市场收盘行情', fontsize=16, fontweight='bold',
             color=TEXT_WHITE, fontproperties=prop, y=1.02)

plt.tight_layout(pad=0.5)
out_path = os.path.join(os.path.dirname(__file__), '..', 'images', 'charts',
                        'chart_2026-09-11-evening.png')
out_path = os.path.normpath(out_path)
plt.savefig(out_path, dpi=150, bbox_inches='tight', facecolor=BG_COLOR)
print(f'✅ 图表已保存至：{out_path}')
