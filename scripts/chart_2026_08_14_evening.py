#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
2026-08-14 晚报 行情数据卡片生成脚本
基于东方财富 API 真实收盘数据
"""

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.font_manager import FontProperties
import os

font_path = '/System/Library/Fonts/STHeiti Medium.ttc'
if not os.path.exists(font_path):
    font_path = '/System/Library/Fonts/PingFang.ttc'
prop = FontProperties(fname=font_path)

data = [
    {"name": "上证指数",  "price": 3927.18,  "chg": +0.01, "pts": +0.22},
    {"name": "深证成指",  "price": 14354.31, "chg": +0.45, "pts": +64.87},
    {"name": "创业板指",  "price": 3626.30,  "chg": +1.12, "pts": +40.26},
    {"name": "科创50",   "price": 1717.68,  "chg": 0.00,  "pts": -0.07},
    {"name": "上证50",   "price": 2916.13,  "chg": -0.41, "pts": -11.99},
    {"name": "恒生指数",  "price": 25116.85, "chg": -1.10, "pts": -279.66},
]

def get_color(chg):
    return "#D94F4F" if chg >= 0 else "#2CA84F"

n = len(data)
fig, axes = plt.subplots(1, n, figsize=(19, 3.8))
fig.patch.set_facecolor('#1A1A2E')

for ax, item in zip(axes, data):
    color = get_color(item["chg"])
    chg_str = f"+{item['chg']:.2f}%" if item["chg"] >= 0 else f"{item['chg']:.2f}%"
    pts_str = f"+{item['pts']:.2f}" if item["pts"] >= 0 else f"{item['pts']:.2f}"

    ax.set_facecolor('#16213E')
    for spine in ax.spines.values():
        spine.set_edgecolor('#2D2D5E')
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    ax.tick_params(left=False, bottom=False, labelleft=False, labelbottom=False)
    ax.set_xticklabels([], fontproperties=prop)
    ax.set_yticklabels([], fontproperties=prop)

    bar = mpatches.FancyBboxPatch((0.05, 0.82), 0.90, 0.12,
                                   boxstyle="round,pad=0.01",
                                   facecolor=color, edgecolor='none',
                                   transform=ax.transAxes)
    ax.add_patch(bar)

    ax.text(0.5, 0.88, item["name"], ha='center', va='center',
            fontproperties=prop, fontsize=13, fontweight='bold',
            color='white', transform=ax.transAxes)
    ax.text(0.5, 0.62, f"{item['price']:,.2f}", ha='center', va='center',
            fontproperties=prop, fontsize=17, fontweight='bold',
            color=color, transform=ax.transAxes)
    ax.text(0.5, 0.42, chg_str, ha='center', va='center',
            fontproperties=prop, fontsize=15, fontweight='bold',
            color=color, transform=ax.transAxes)
    ax.text(0.5, 0.25, pts_str, ha='center', va='center',
            fontproperties=prop, fontsize=11,
            color='#AAAACC', transform=ax.transAxes)
    ax.text(0.5, 0.08, "收盘 2026-08-14", ha='center', va='center',
            fontproperties=prop, fontsize=8,
            color='#666688', transform=ax.transAxes)

fig.suptitle("2026年08月14日（周五）收盘行情 · 晚报",
             fontproperties=prop, fontsize=14, color='#CCCCEE', y=1.02)

plt.tight_layout(rect=[0, 0, 1, 1])

out_dir = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'images', 'charts')
os.makedirs(out_dir, exist_ok=True)
out_path = os.path.join(out_dir, '2026-08-14-evening.png')
plt.savefig(out_path, dpi=150, bbox_inches='tight', facecolor=fig.get_facecolor())
print(f"[OK] Chart saved to: {out_path}")
plt.close()
