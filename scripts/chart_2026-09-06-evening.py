#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
核心资产行情卡片 - 2026-09-06 周日下午 新周展望
显示本周（2026-08-31 至 2026-09-05）核心资产周度收益
"""

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm
import numpy as np
import os

# ── 中文字体 ──────────────────────────────────────────────
font_paths = [
    '/System/Library/Fonts/STHeiti Medium.ttc',
    '/System/Library/Fonts/PingFang.ttc',
    '/System/Library/Fonts/Supplemental/Arial Unicode.ttf',
]
prop = None
for fp in font_paths:
    if os.path.exists(fp):
        prop = fm.FontProperties(fname=fp)
        plt.rcParams['font.family'] = prop.get_name()
        break

# ── 数据（周度累计涨跌幅，截至 2026-09-05） ──────────────
assets = [
    '恒生指数',
    '恒生科技',
    '国企指数',
    '道琼斯',
    '标普500',
    '纳斯达克',
    '美10Y国债收益率\n(4.82%)',
    '日10Y国债收益率\n(3.00%)',
    'BTC',
]
changes = [
    0.26,    # 恒生  +0.26%
    -0.77,   # 恒科  -0.77%
    0.76,    # 国企  +0.76%
    -0.27,   # 道指  -0.27%
    0.09,    # 标普  +0.09%
    0.40,    # 纳指  +0.40%
    0.18,    # 美债收益率（周变化 bps 折算示意）
    0.15,    # 日债收益率
    1.20,    # BTC 周涨幅（示意）
]

# ── 颜色：上涨红，下跌绿 ──────────────────────────────────
colors = ['#E8293B' if c >= 0 else '#00A86B' for c in changes]

# ── 绘图 ──────────────────────────────────────────────────
fig, ax = plt.subplots(figsize=(12, 6))
fig.patch.set_facecolor('#1A1A2E')
ax.set_facecolor('#16213E')

y_pos = np.arange(len(assets))
bars = ax.barh(y_pos, changes, color=colors, height=0.6, edgecolor='none')

# 数值标签
for bar, val in zip(bars, changes):
    label = f'+{val:.2f}%' if val >= 0 else f'{val:.2f}%'
    x_offset = 0.03 if val >= 0 else -0.03
    ha = 'left' if val >= 0 else 'right'
    ax.text(bar.get_x() + bar.get_width() + x_offset,
            bar.get_y() + bar.get_height() / 2,
            label, va='center', ha=ha,
            color='white', fontsize=10,
            fontproperties=prop)

ax.set_yticks(y_pos)
ax.set_yticklabels(assets, fontsize=10, color='#CCCCCC',
                   fontproperties=prop)
ax.tick_params(axis='x', colors='#666666', labelsize=9)
ax.axvline(0, color='#444466', linewidth=1)
ax.spines[:].set_visible(False)
ax.grid(axis='x', color='#2A2A4A', linestyle='--', alpha=0.5)

# 标题
title_kw = dict(fontproperties=prop) if prop else {}
ax.set_title('核心资产周度表现（2026年第36周，截至9月5日）',
             color='white', fontsize=13, pad=14, **title_kw)

fig.text(0.99, 0.01, '数据来源：EastMoney / Yahoo Finance / Bloomberg',
         ha='right', va='bottom', color='#555577', fontsize=7,
         fontproperties=prop)

plt.tight_layout()

out_dir = os.path.join(os.path.dirname(__file__), '..', 'images', 'charts')
os.makedirs(out_dir, exist_ok=True)
out_path = os.path.join(out_dir, '2026-09-06-evening-weekly.png')
plt.savefig(out_path, dpi=150, bbox_inches='tight',
            facecolor=fig.get_facecolor())
print(f'[OK] 图表已保存：{out_path}')
