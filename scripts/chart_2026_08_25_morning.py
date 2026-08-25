#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
2026-08-25 早报核心行情数据卡片生成脚本
"""

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm
import os

# ── 中文字体设置 ──
font_candidates = [
    '/System/Library/Fonts/STHeiti Medium.ttc',
    '/System/Library/Fonts/Supplemental/Songti.ttc',
    '/Library/Fonts/Arial Unicode MS.ttf',
]
prop = None
for fp in font_candidates:
    if os.path.exists(fp):
        prop = fm.FontProperties(fname=fp)
        plt.rcParams['font.family'] = prop.get_name()
        break

if prop is None:
    plt.rcParams['font.sans-serif'] = ['PingFang SC', 'Heiti SC', 'Arial Unicode MS']
    plt.rcParams['axes.unicode_minus'] = False

# ── 数据：上周五（Aug 21）收盘 ──
assets = [
    {"name": "标普 500",      "value": "7,674.37",  "change": -1.43, "unit": "pts"},
    {"name": "纳斯达克",      "value": "26,180.45", "change": -2.05, "unit": "pts"},
    {"name": "道琼斯",        "value": "53,277.01", "change": -0.85, "unit": "pts"},
    {"name": "美10Y国债",     "value": "4.74%",     "change": +0.12, "unit": "%"},
    {"name": "美30Y国债",     "value": "5.28%",     "change": +0.09, "unit": "%"},
    {"name": "WTI原油",       "value": "$86.68",    "change": +8.20, "unit": "/桶"},
    {"name": "现货黄金",      "value": "$4,605",    "change": +5.10, "unit": "/盎司"},
    {"name": "比特币",        "value": "$77,050",   "change": +22.0, "unit": "USD"},
]

n = len(assets)
fig, axes = plt.subplots(2, 4, figsize=(18, 7))
fig.patch.set_facecolor('#0D1117')

def get_colors(chg):
    if chg > 0:
        return '#FF4C4C', '#FF8080'   # 红涨
    else:
        return '#00C878', '#66FFAA'   # 绿跌

for idx, ax in enumerate(axes.flat):
    asset = assets[idx]
    chg = asset["change"]
    bg_col, txt_col = get_colors(chg)
    sign = "▲" if chg > 0 else "▼"
    chg_str = f"{sign} {abs(chg):.2f}%（周涨跌）"

    ax.set_facecolor('#161B22')
    for spine in ax.spines.values():
        spine.set_edgecolor(bg_col)
        spine.set_linewidth(1.5)
    ax.set_xticks([])
    ax.set_yticks([])

    # 资产名称
    ax.text(0.5, 0.78, asset["name"], transform=ax.transAxes,
            fontsize=13, fontweight='bold', color='#FFFFFF',
            ha='center', va='center',
            fontproperties=prop)
    # 价格
    ax.text(0.5, 0.50, asset["value"], transform=ax.transAxes,
            fontsize=18, fontweight='bold', color='#FFFFFF',
            ha='center', va='center')
    # 涨跌
    ax.text(0.5, 0.22, chg_str, transform=ax.transAxes,
            fontsize=11, color=txt_col,
            ha='center', va='center',
            fontproperties=prop)

fig.suptitle("2026-08-25 早报 · 全球核心资产（截至上周五收盘）",
             fontsize=16, fontweight='bold', color='#E6EDF3',
             fontproperties=prop, y=1.01)

plt.tight_layout(pad=1.2)

out_dir = os.path.join(os.path.dirname(__file__), '..', 'images', 'charts')
os.makedirs(out_dir, exist_ok=True)
out_path = os.path.join(out_dir, '2026-08-25-morning-chart.png')
plt.savefig(out_path, dpi=150, bbox_inches='tight', facecolor=fig.get_facecolor())
plt.close()
print(f"✅ 图表已保存至: {out_path}")
