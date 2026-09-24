#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
2026-09-24 晚报行情数据卡片生成脚本
"""
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm
import matplotlib.patches as mpatches
import numpy as np
import os

# ── 中文字体设置 ──────────────────────────────────────────────
font_candidates = [
    '/System/Library/Fonts/STHeiti Medium.ttc',
    '/System/Library/Fonts/PingFang.ttc',
    '/Library/Fonts/Arial Unicode MS.ttf',
]
prop = None
for fp in font_candidates:
    if os.path.exists(fp):
        prop = fm.FontProperties(fname=fp)
        plt.rcParams['font.family'] = prop.get_name()
        break
if prop is None:
    plt.rcParams['font.sans-serif'] = ['Arial Unicode MS', 'Heiti TC', 'PingFang SC']

plt.rcParams['axes.unicode_minus'] = False

# ── 数据定义 ──────────────────────────────────────────────────
assets = [
    # 名称,            现价,       涨跌幅,     类别
    ("上证指数",       "3888.37",  "-1.22%",   "A股"),
    ("深证成指",       "13316.97", "-2.34%",   "A股"),
    ("创业板指",       "3288.95",  "-2.68%",   "A股"),
    ("恒生指数",       "24761.13", "-0.29%",   "港股"),
    ("恒生科技",       "4361.13",  "-0.41%",   "港股"),
    ("黄金(现货)",     "4286.85",  "-1.70%",   "大宗"),
    ("WTI原油",        "92.16",    "+1.81%",   "大宗"),
    ("比特币",         "~83000",   "-",        "加密"),
]

# ── 颜色映射（中国惯例：红涨绿跌） ────────────────────────────
def get_color(change_str):
    if change_str == "-":
        return "#888888"
    val = float(change_str.replace('%', '').replace('+', ''))
    if val > 0:
        return "#E5222A"   # 红色 = 上涨
    elif val < 0:
        return "#00A86B"   # 绿色 = 下跌
    else:
        return "#888888"

# ── 绘图 ──────────────────────────────────────────────────────
fig, ax = plt.subplots(figsize=(14, 7))
fig.patch.set_facecolor('#0D1117')
ax.set_facecolor('#0D1117')
ax.axis('off')

# 标题
title_text = "2026年9月24日（周四）· 收盘行情总览"
ax.text(0.5, 0.96, title_text,
        transform=ax.transAxes,
        fontsize=18, fontweight='bold', color='white', ha='center', va='top',
        fontproperties=prop)
ax.text(0.5, 0.90, "⚠ 美联储加息预期升温，全球风险资产承压，A股缩量调整",
        transform=ax.transAxes,
        fontsize=11, color='#AAAAAA', ha='center', va='top',
        fontproperties=prop)

# 卡片布局（4列 × 2行）
n_cols = 4
n_rows = 2
card_w = 0.22
card_h = 0.28
x_starts = [0.01 + i * 0.245 for i in range(n_cols)]
y_starts = [0.52, 0.18]

for idx, (name, price, change, category) in enumerate(assets):
    row = idx // n_cols
    col = idx % n_cols
    x = x_starts[col]
    y = y_starts[row]
    color = get_color(change)

    # 卡片背景
    rect = mpatches.FancyBboxPatch(
        (x, y), card_w, card_h,
        boxstyle="round,pad=0.01",
        linewidth=1.5,
        edgecolor=color,
        facecolor='#161B22',
        transform=ax.transAxes,
        clip_on=False
    )
    ax.add_patch(rect)

    # 类别标签
    ax.text(x + card_w / 2, y + card_h - 0.03, f"[{category}]",
            transform=ax.transAxes,
            fontsize=8.5, color='#666666', ha='center', va='top',
            fontproperties=prop)
    # 资产名称
    ax.text(x + card_w / 2, y + card_h - 0.09, name,
            transform=ax.transAxes,
            fontsize=12, fontweight='bold', color='white', ha='center', va='top',
            fontproperties=prop)
    # 现价
    ax.text(x + card_w / 2, y + card_h - 0.17, price,
            transform=ax.transAxes,
            fontsize=13, fontweight='bold', color='white', ha='center', va='top',
            fontproperties=prop)
    # 涨跌幅
    ax.text(x + card_w / 2, y + card_h - 0.25, change,
            transform=ax.transAxes,
            fontsize=14, fontweight='bold', color=color, ha='center', va='top',
            fontproperties=prop)

# 底部说明
ax.text(0.5, 0.05,
        "数据来源：东方财富 / CME / Yahoo Finance  |  免责声明：仅供参考，不构成投资建议",
        transform=ax.transAxes,
        fontsize=8, color='#555555', ha='center', va='bottom',
        fontproperties=prop)

# ── 保存 ──────────────────────────────────────────────────────
os.makedirs('../images/charts', exist_ok=True)
output_path = '../images/charts/chart_2026_09_24_evening.png'
plt.tight_layout()
plt.savefig(output_path, dpi=150, bbox_inches='tight',
            facecolor=fig.get_facecolor())
plt.close()
print(f"✅ 行情卡片已生成：{output_path}")
