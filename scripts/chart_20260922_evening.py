#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
生成 2026-09-22 晚报国内市场核心行情数据卡片
"""

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm
import matplotlib.patches as mpatches
import numpy as np
import os

# ── 字体配置（macOS 中文支持）──────────────────────────────
FONT_PATHS = [
    '/System/Library/Fonts/STHeiti Medium.ttc',
    '/System/Library/Fonts/PingFang.ttc',
    '/Library/Fonts/Arial Unicode MS.ttf',
]
font_path = next((p for p in FONT_PATHS if os.path.exists(p)), None)
prop_title = fm.FontProperties(fname=font_path, size=15) if font_path else fm.FontProperties(size=15)
prop_label = fm.FontProperties(fname=font_path, size=12) if font_path else fm.FontProperties(size=12)
prop_value = fm.FontProperties(fname=font_path, size=13) if font_path else fm.FontProperties(size=13)
prop_small  = fm.FontProperties(fname=font_path, size=10) if font_path else fm.FontProperties(size=10)

if font_path:
    plt.rcParams['font.family'] = fm.FontProperties(fname=font_path).get_name()

# ── 数据定义 ─────────────────────────────────────────────────
assets = [
    # (名称,            点位/值,       涨跌幅%,  成交额/备注)
    ("上证指数",        "3,952.13",    -0.16,    "1.57万亿"),
    ("深证成指",        "13,723.74",   -0.05,    ""),
    ("沪深300",         "4,544.59",    +0.11,    ""),
    ("创业板指",        "3,399.93",    +0.01,    ""),
    ("科创50",          "1,665.04",    +0.46,    ""),
    ("恒生指数",        "25,087.75",   +0.18,    ""),
    ("恒生科技",        "4,438.21",    +0.34,    ""),
]

# ── 画布 ─────────────────────────────────────────────────────
fig, ax = plt.subplots(figsize=(13, 6))
ax.set_facecolor('#0d1117')
fig.patch.set_facecolor('#0d1117')
ax.axis('off')

# 标题
ax.text(0.5, 0.97,
        "🏮 国内市场核心行情卡片  2026-09-22（晚报）",
        transform=ax.transAxes, ha='center', va='top',
        color='#e6edf3', fontproperties=prop_title)

# 分隔线
ax.plot([0.02, 0.98], [0.90, 0.90], color='#30363d', linewidth=0.8,
        transform=ax.transAxes)

n = len(assets)
cols = 4  if n > 5 else 3
rows = -(-n // cols)  # ceil div
cell_w = 0.90 / cols
cell_h = 0.75 / rows

for i, (name, price, pct, vol) in enumerate(assets):
    col = i % cols
    row = i // cols
    x = 0.05 + col * cell_w + cell_w * 0.05
    y = 0.85 - row * cell_h

    # 颜色：涨红跌绿（A股惯例）
    color = '#f85149' if pct > 0 else ('#3fb950' if pct < 0 else '#8b949e')
    bg    = '#1f2937' if pct > 0 else ('#0f2d1e' if pct < 0 else '#161b22')
    sign  = '+' if pct >= 0 else ''

    # 背景框
    rect = mpatches.FancyBboxPatch(
        (x - 0.01, y - cell_h + 0.04), cell_w * 0.90, cell_h - 0.05,
        boxstyle="round,pad=0.01", linewidth=1,
        edgecolor=color, facecolor=bg,
        transform=ax.transAxes, clip_on=False
    )
    ax.add_patch(rect)

    # 资产名称
    ax.text(x + cell_w * 0.40, y - 0.02, name,
            transform=ax.transAxes, ha='center', va='top',
            color='#e6edf3', fontproperties=prop_label)
    # 点位
    ax.text(x + cell_w * 0.40, y - 0.10, price,
            transform=ax.transAxes, ha='center', va='top',
            color='#e6edf3', fontproperties=prop_value,
            fontweight='bold')
    # 涨跌幅
    ax.text(x + cell_w * 0.40, y - 0.18, f"{sign}{pct:.2f}%",
            transform=ax.transAxes, ha='center', va='top',
            color=color, fontproperties=prop_value, fontweight='bold')
    # 成交额（若有）
    if vol:
        ax.text(x + cell_w * 0.40, y - 0.26, f"成交额：{vol}",
                transform=ax.transAxes, ha='center', va='top',
                color='#8b949e', fontproperties=prop_small)

# 底部水印
ax.text(0.5, 0.01,
        "数据来源：东方财富 / 富途 / 新浪财经  |  仅供参考，不构成投资建议",
        transform=ax.transAxes, ha='center', va='bottom',
        color='#484f58', fontproperties=prop_small)

# 保存
out_path = 'images/charts/chart_20260922_evening.png'
os.makedirs(os.path.dirname(out_path), exist_ok=True)
plt.tight_layout(pad=0)
plt.savefig(out_path, dpi=150, bbox_inches='tight',
            facecolor=fig.get_facecolor())
plt.close()
print(f"✅ 图表已保存至 {out_path}")
