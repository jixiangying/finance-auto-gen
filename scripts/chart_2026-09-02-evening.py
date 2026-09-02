#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
2026-09-02 收盘行情数据卡片生成脚本
"""
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm
from matplotlib.patches import FancyBboxPatch
import numpy as np
import os

# ── 字体设置（macOS 中文支持）──────────────────────────────────────────────
font_paths = [
    '/System/Library/Fonts/STHeiti Medium.ttc',
    '/System/Library/Fonts/PingFang.ttc',
    '/System/Library/Fonts/Supplemental/Songti.ttc',
    '/Library/Fonts/Arial Unicode MS.ttf',
]
prop = None
for fp in font_paths:
    if os.path.exists(fp):
        prop = fm.FontProperties(fname=fp)
        break

if prop is None:
    prop = fm.FontProperties(family='sans-serif')

plt.rcParams['font.family'] = prop.get_name() if prop else 'sans-serif'
plt.rcParams['axes.unicode_minus'] = False

# ── 数据定义 ───────────────────────────────────────────────────────────────
indices = [
    {'name': '上证指数', 'close': 3941.39, 'change': -0.97, 'market': 'A股'},
    {'name': '深证成指', 'close': 13611.55, 'change': -1.88, 'market': 'A股'},
    {'name': '沪深300',  'close': 4547.96,  'change': -1.38, 'market': 'A股'},
    {'name': '创业板指', 'close': 3312.24,  'change': -2.39, 'market': 'A股'},
    {'name': '科创50',   'close': 1625.81,  'change': -1.32, 'market': 'A股'},
    {'name': '北证50',   'close': None,     'change': +2.50, 'market': 'A股'},
    {'name': '恒生指数', 'close': 25311.21, 'change': -0.07, 'market': '港股'},
    {'name': '恒生科技', 'close': 4517.16,  'change': -0.74, 'market': '港股'},
    {'name': '国企指数', 'close': 8450.10,  'change': -0.15, 'market': '港股'},
]

# ── 画布设置 ──────────────────────────────────────────────────────────────
fig, ax = plt.subplots(figsize=(14, 9))
ax.set_xlim(0, 14)
ax.set_ylim(0, 9)
ax.axis('off')
fig.patch.set_facecolor('#0D1117')
ax.set_facecolor('#0D1117')

# ── 标题 ──────────────────────────────────────────────────────────────────
ax.text(7, 8.5, '📊  2026年09月02日  收盘行情快报',
        ha='center', va='center', fontsize=18, fontweight='bold',
        color='#E6EDF3', fontproperties=prop)
ax.text(7, 8.05, '国内市场 · 晚报  |  成交额：1.82万亿元（缩量≈2300亿）',
        ha='center', va='center', fontsize=10, color='#8B949E', fontproperties=prop)

# ── 分隔线 ────────────────────────────────────────────────────────────────
ax.plot([0.5, 13.5], [7.8, 7.8], color='#30363D', linewidth=1)

# ── 分组标题 ─────────────────────────────────────────────────────────────
ax.text(3.5, 7.55, '🇨🇳  A 股', ha='center', va='center',
        fontsize=13, color='#58A6FF', fontproperties=prop, fontweight='bold')
ax.text(10.8, 7.55, '🇭🇰  港 股', ha='center', va='center',
        fontsize=13, color='#58A6FF', fontproperties=prop, fontweight='bold')
ax.plot([7.0, 7.0], [0.5, 7.7], color='#30363D', linewidth=1, linestyle='--')

def draw_card(ax, x, y, w, h, idx, prop):
    """绘制单个指数卡片"""
    chg = idx['change']
    # 红涨绿跌（A股习惯）
    if chg > 0:
        color_main = '#F85149'   # 红
        color_bg   = '#3D1F1F'
        arrow      = '▲'
    else:
        color_main = '#3FB950'   # 绿
        color_bg   = '#1A2E1A'
        arrow      = '▼'

    rect = FancyBboxPatch((x - w/2, y - h/2), w, h,
                           boxstyle="round,pad=0.05",
                           linewidth=1.2, edgecolor=color_main,
                           facecolor=color_bg, zorder=2)
    ax.add_patch(rect)

    # 名称
    ax.text(x, y + h*0.28, idx['name'],
            ha='center', va='center', fontsize=10.5, fontweight='bold',
            color='#E6EDF3', fontproperties=prop, zorder=3)

    # 点位
    close_str = f"{idx['close']:,.2f}" if idx['close'] else '—'
    ax.text(x, y + h*0.01, close_str,
            ha='center', va='center', fontsize=13, fontweight='bold',
            color=color_main, fontproperties=prop, zorder=3)

    # 涨跌幅
    chg_str = f"{arrow} {abs(chg):.2f}%"
    ax.text(x, y - h*0.28, chg_str,
            ha='center', va='center', fontsize=10,
            color=color_main, fontproperties=prop, zorder=3)

# ── 绘制 A股 卡片（6张，两行3列）────────────────────────────────────────
a_stock = [idx for idx in indices if idx['market'] == 'A股']
a_xs = [1.5, 3.5, 5.5, 1.5, 3.5, 5.5]
a_ys = [6.3, 6.3, 6.3, 4.5, 4.5, 4.5]
for i, idx in enumerate(a_stock[:6]):
    draw_card(ax, a_xs[i], a_ys[i], 1.7, 1.3, idx, prop)

# ── 绘制 港股 卡片（3张，一行3列）────────────────────────────────────────
hk_stock = [idx for idx in indices if idx['market'] == '港股']
hk_xs = [8.3, 10.5, 12.7]
hk_ys = [6.3, 6.3, 6.3]
for i, idx in enumerate(hk_stock):
    draw_card(ax, hk_xs[i], hk_ys[i], 1.9, 1.3, idx, prop)

# ── 主力资金注解 ─────────────────────────────────────────────────────────
ax.plot([0.5, 13.5], [3.6, 3.6], color='#30363D', linewidth=0.8)
ax.text(0.7, 3.35, '主力资金净流向（部分板块）', ha='left', va='center',
        fontsize=10, color='#8B949E', fontproperties=prop)

inflow_text  = '净流入：国防军工 +22亿｜汽车 +10亿｜电路板 +20亿｜液冷服务器 +20亿｜特高压 +10亿'
outflow_text = '净流出：AI新基建/人工智能 -70亿｜非银金融/通信 -30亿｜有色金属/医药 -20亿'

ax.text(0.7, 2.95, inflow_text, ha='left', va='center',
        fontsize=9, color='#F85149', fontproperties=prop)
ax.text(0.7, 2.55, outflow_text, ha='left', va='center',
        fontsize=9, color='#3FB950', fontproperties=prop)

# ── 今日要闻亮点 ─────────────────────────────────────────────────────────
ax.plot([0.5, 13.5], [2.25, 2.25], color='#30363D', linewidth=0.8)
ax.text(0.7, 2.05, '📌 今日要点',
        ha='left', va='center', fontsize=10, color='#8B949E', fontproperties=prop)
highlights = [
    '• 北交所五周年，北证50逆势涨2.5%，超九成个股上涨，多只涨停',
    '• 军工板块领涨：十五五国防装备更新，中报业绩兑现，净流入22亿',
    '• AI主线回调：A股AI概念净流出超70亿，科创50跌1.32%',
    '• 央行维持"适度宽松"基调，OMO归零代表跨月资金平稳过渡',
]
for i, h in enumerate(highlights):
    ax.text(0.7, 1.75 - i * 0.35, h, ha='left', va='center',
            fontsize=8.5, color='#C9D1D9', fontproperties=prop)

# ── 免责声明 ──────────────────────────────────────────────────────────────
ax.text(7, 0.25, '数据来源：东方财富 / 财联社 / 新浪财经   |   内容仅供参考，不构成投资建议',
        ha='center', va='center', fontsize=7.5, color='#484F58', fontproperties=prop)

# ── 保存 ──────────────────────────────────────────────────────────────────
out_dir = '/Users/jxy/Documents/Project/finance-auto-gen/images/charts'
os.makedirs(out_dir, exist_ok=True)
out_path = os.path.join(out_dir, 'chart_2026-09-02-evening.png')
plt.tight_layout(pad=0)
plt.savefig(out_path, dpi=150, bbox_inches='tight',
            facecolor=fig.get_facecolor())
plt.close()
print(f'✅ 图表已保存: {out_path}')
