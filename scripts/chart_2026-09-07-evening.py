#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
核心资产行情卡片 - 2026-09-07 周一下午 收盘复盘
"""

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm
import numpy as np
import os

# ── 中文字体设置 ──────────────────────────────────────────
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

# ── 数据（2026-09-07 拆盘表现） ──────────────────────────
assets = [
    '创业板指\n(3398.68)',
    '科创50\n(1615.53)',
    '沪深300\n(4575.02)',
    '上证指数\n(3932.70)',
    '恒生科技\n(4527.71)',
    '恒生指数\n(25413.12)',
    '国企指数\n(8429.73)'
]
changes = [
    3.41,   # 创业板指 +3.41%
    2.42,   # 科创50 +2.42%
    0.59,   # 沪深300 +0.59%
    0.07,   # 上证指数 +0.07%
    -0.92,  # 恒生科技 -0.92%
    -0.93,  # 恒生指数 -0.93%
    -1.46   # 国企指数 -1.46%
]

# ── 颜色：国内习惯 上涨红 🔴，下跌绿 🟢 ─────────────
colors = ['#E8293B' if c >= 0 else '#00A86B' for c in changes]

# ── 绘图 ──────────────────────────────────────────────────
fig, ax = plt.subplots(figsize=(10, 5))
fig.patch.set_facecolor('#1A1A2E')
ax.set_facecolor('#16213E')

y_pos = np.arange(len(assets))
bars = ax.barh(y_pos, changes, color=colors, height=0.55, edgecolor='none')

# 数值标签
for bar, val in zip(bars, changes):
    label = f'+{val:.2f}%' if val >= 0 else f'{val:.2f}%'
    x_offset = 0.08 if val >= 0 else -0.08
    ha = 'left' if val >= 0 else 'right'
    ax.text(bar.get_x() + bar.get_width() + x_offset,
            bar.get_y() + bar.get_height() / 2,
            label, va='center', ha=ha,
            color='white', fontsize=10, fontweight='bold',
            fontproperties=prop)

ax.set_yticks(y_pos)
ax.set_yticklabels(assets, fontsize=10, color='#CCCCCC', fontproperties=prop)
ax.tick_params(axis='x', colors='#666666', labelsize=9)
ax.axvline(0, color='#444466', linewidth=1)
ax.spines[:].set_visible(False)
ax.grid(axis='x', color='#2A2A4A', linestyle='--', alpha=0.5)

title_kw = dict(fontproperties=prop) if prop else {}
ax.set_title('核心资产收盘表现（2026年9月7日）', color='white', fontsize=13, pad=14, **title_kw)

fig.text(0.99, 0.01, '数据来源：EastMoney / 官方交易所收盘终值 (美股劳动节休市)',
         ha='right', va='bottom', color='#555577', fontsize=8, fontproperties=prop)

plt.tight_layout()

out_dir = os.path.join(os.path.dirname(__file__), '..', 'images', 'charts')
os.makedirs(out_dir, exist_ok=True)
out_path = os.path.join(out_dir, '2026-09-07-evening.png')
plt.savefig(out_path, dpi=150, bbox_inches='tight', facecolor=fig.get_facecolor())
print(f'[OK] 图表已成功生成：{out_path}')
