#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
周末复盘行情卡片 2026-09-26
"""
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib import font_manager
import os

# ── 字体设置 ──────────────────────────────────────────────────────────────────
FONT_PATHS = [
    '/System/Library/Fonts/STHeiti Medium.ttc',
    '/System/Library/Fonts/PingFang.ttc',
    '/Library/Fonts/Arial Unicode.ttf',
]
prop = None
for fp in FONT_PATHS:
    if os.path.exists(fp):
        prop = font_manager.FontProperties(fname=fp)
        plt.rcParams['font.family'] = prop.get_name()
        break

def fp_kw():
    return {'fontproperties': prop} if prop else {}

# ── 数据 ──────────────────────────────────────────────────────────────────────
# (name, price_str, change_pct, is_rise)
assets = [
    # 中国
    ("上证指数",  "3,888",  "-0.25%", False),
    ("沪深300",   "4,439",  "-0.87%", False),
    ("恒生指数",  "24,510", "-0.97%", False),
    # 美股
    ("标普500",   "7,738",  "-0.35%", False),
    ("纳斯达克",  "N/A",    "+1.2%",  True),
    # 商品 / 汇率
    ("黄金(现货)","4,275",  "-0.3%",  False),
    ("WTI原油",   "$92.41", "-2.33%", False),
    ("美元指数",  "100.97", "-0.31%", False),
    # 加密
    ("比特币",    "$84,000","+4%+",   True),
    ("以太坊",    "$2,695", "+3.21%", True),
]

UP_COLOR   = "#e8534a"   # 红 = 涨
DOWN_COLOR = "#2ab06f"   # 绿 = 跌
BG_COLOR   = "#0d1117"
CARD_BG    = "#161b22"
TEXT_LIGHT = "#e6edf3"
TEXT_DIM   = "#8b949e"

fig, axes = plt.subplots(2, 5, figsize=(20, 7))
fig.patch.set_facecolor(BG_COLOR)

for idx, ax in enumerate(axes.flat):
    name, price, change, is_rise = assets[idx]
    color = UP_COLOR if is_rise else DOWN_COLOR

    ax.set_facecolor(CARD_BG)
    for spine in ax.spines.values():
        spine.set_edgecolor('#30363d')
        spine.set_linewidth(1.5)
    ax.set_xticks([])
    ax.set_yticks([])

    # 资产名称
    ax.text(0.5, 0.72, name, ha='center', va='center',
            fontsize=13, color=TEXT_DIM, transform=ax.transAxes, **fp_kw())
    # 价格
    ax.text(0.5, 0.48, price, ha='center', va='center',
            fontsize=17, fontweight='bold', color=TEXT_LIGHT,
            transform=ax.transAxes, **fp_kw())
    # 涨跌幅
    arrow = "▲" if is_rise else "▼"
    ax.text(0.5, 0.22, f"{arrow} {change}", ha='center', va='center',
            fontsize=13, color=color, transform=ax.transAxes, **fp_kw())

# 标题
fig.suptitle("本周收盘行情总览（2026年9月21-25日）",
             fontsize=18, color=TEXT_LIGHT, y=1.01, **fp_kw())

fig.text(0.5, -0.02,
         "数据来源：东方财富 / 新浪财经 / Investing.com  |  仅供参考，不构成投资建议",
         ha='center', fontsize=9, color=TEXT_DIM, **fp_kw())

plt.tight_layout(pad=0.8)

out_dir = os.path.join(os.path.dirname(__file__), '..', 'images', 'charts')
os.makedirs(out_dir, exist_ok=True)
out_path = os.path.join(out_dir, 'chart_2026-09-26-weekend.png')
plt.savefig(out_path, dpi=150, bbox_inches='tight', facecolor=BG_COLOR)
print(f"[OK] 图表已保存至: {out_path}")
plt.close()
