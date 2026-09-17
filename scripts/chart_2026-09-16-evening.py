#!/usr/bin/env python3
"""
数据信息卡片：2026-09-16 晚报（国内市场收盘行情）
"""
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib import font_manager
import matplotlib.patches as mpatches
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
    {'name': '上证指数',   'price': '3,891.60', 'change': '+0.71%', 'up': True},
    {'name': '深证成指',   'price': '13,454.74','change': '+1.26%', 'up': True},
    {'name': '创业板指',   'price': '3,311.47', 'change': '+1.96%', 'up': True},
    {'name': '恒生指数',   'price': '24,713.78','change': '+0.19%', 'up': True},
    {'name': '恒生科技',   'price': '4,325.45', 'change': '+0.79%', 'up': True},
]

# ── 配色 ──────────────────────────────────────────────────────────────────
BG_COLOR   = '#0f172a'   # 深色背景
CARD_UP    = '#b91c1c'   # 上涨红
CARD_DOWN  = '#15803d'   # 下跌绿
TEXT_WHITE = '#ffffff'
TEXT_GRAY  = '#cbd5e1'

fig, axes = plt.subplots(1, len(assets), figsize=(16, 4))
fig.patch.set_facecolor(BG_COLOR)

for ax, asset in zip(axes, assets):
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    ax.axis('off')

    # 绘制带圆角的卡片背景
    card_color = CARD_UP if asset['up'] else CARD_DOWN
    rect = mpatches.FancyBboxPatch((0.05, 0.05), 0.9, 0.9,
                                  boxstyle="round,pad=0.03,rounding_size=0.1",
                                  facecolor=card_color,
                                  edgecolor='none',
                                  transform=ax.transAxes)
    ax.add_patch(rect)

    # 资产名称
    ax.text(0.5, 0.72, asset['name'], ha='center', va='center',
            fontsize=15, fontweight='bold', color=TEXT_WHITE,
            fontproperties=prop)
    # 价格
    ax.text(0.5, 0.48, asset['price'], ha='center', va='center',
            fontsize=18, fontweight='bold', color=TEXT_WHITE,
            fontproperties=prop)
    # 涨跌幅
    arrow = '▲' if asset['up'] else '▼'
    ax.text(0.5, 0.25, f"{arrow} {asset['change']}", ha='center', va='center',
            fontsize=14, fontweight='bold', color=TEXT_WHITE, fontproperties=prop)

# 标题
fig.suptitle('2026-09-16  国内市场收盘行情', fontsize=16, fontweight='bold',
             color=TEXT_WHITE, fontproperties=prop, y=1.02)

plt.tight_layout(pad=0.5)
out_path = os.path.join(os.path.dirname(__file__), '..', 'images', 'charts',
                        'chart_2026-09-16-evening.png')
out_path = os.path.normpath(out_path)
os.makedirs(os.path.dirname(out_path), exist_ok=True)
plt.savefig(out_path, dpi=150, bbox_inches='tight', facecolor=BG_COLOR)
print(f'✅ 图表已保存至：{out_path}')
