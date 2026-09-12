#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
周度行情数据卡片 - 2026-09-12 周末复盘版
"""

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm
import os

# ── 字体配置 ──────────────────────────────────────────────────────────────────
FONT_PATHS = [
    '/System/Library/Fonts/STHeiti Medium.ttc',
    '/System/Library/Fonts/Supplemental/Songti.ttc',
    '/Library/Fonts/Arial Unicode MS.ttf',
    '/System/Library/Fonts/PingFang.ttc',
]
prop = None
for fp in FONT_PATHS:
    if os.path.exists(fp):
        prop = fm.FontProperties(fname=fp)
        plt.rcParams['font.family'] = prop.get_name()
        break

def get_font():
    return prop if prop else fm.FontProperties()

# ── 数据定义 ───────────────────────────────────────────────────────────────────
assets = [
    # 国内市场
    {'label': '上证指数',    'value': '3888.11',  'chg_d': -1.18,  'chg_w': -1.07,  'cat': '国内'},
    {'label': '沪深300',    'value': '4535.15',  'chg_d': -1.10,  'chg_w': -1.10,  'cat': '国内'},
    {'label': '创业板指',    'value': '3322.04',  'chg_d': -0.49,  'chg_w': +1.08,  'cat': '国内'},
    {'label': '恒生指数',    'value': '24805.63', 'chg_d': -0.60,  'chg_w': -3.30,  'cat': '港股'},
    {'label': '恒生科技',    'value': '4320.57',  'chg_d': -0.23,  'chg_w': -5.45,  'cat': '港股'},
    # 全球市场
    {'label': '标普500',     'value': '7656.98',  'chg_d': +0.86,  'chg_w': -0.80,  'cat': '美股'},
    {'label': '纳斯达克',    'value': '26333.04', 'chg_d': +0.96,  'chg_w': -0.66,  'cat': '美股'},
    {'label': '道琼斯',      'value': '52573.29', 'chg_d': +0.98,  'chg_w': -1.57,  'cat': '美股'},
    # 大宗商品 & 外汇
    {'label': '黄金(现货)',  'value': '$4394.67', 'chg_d': -1.08,  'chg_w': -0.68,  'cat': '大宗'},
    {'label': 'Brent原油',  'value': '$104.25',  'chg_d': -3.14,  'chg_w': +14.18, 'cat': '大宗'},
    {'label': '美元指数',    'value': '99.09',    'chg_d': +0.02,  'chg_w': -0.76,  'cat': '外汇'},
]

# ── 绘图 ────────────────────────────────────────────────────────────────────────
n = len(assets)
fig, ax = plt.subplots(figsize=(14, 8.5))
fig.patch.set_facecolor('#0f1117')
ax.set_facecolor('#0f1117')
ax.set_xlim(0, 1)
ax.set_ylim(-0.5, n - 0.5)
ax.axis('off')

# 标题
fig.text(0.5, 0.97,
         '全球市场周度复盘卡片  2026年9月12日（周六）',
         ha='center', va='top', fontsize=16, fontweight='bold',
         color='white', fontproperties=get_font())
fig.text(0.5, 0.93,
         '数据截至 2026-09-11（周五）收盘 | 2026年第37周',
         ha='center', va='top', fontsize=11, color='#aaaaaa',
         fontproperties=get_font())

# 列标题
col_x = [0.04, 0.22, 0.42, 0.58, 0.78]
col_labels = ['类别', '资产', '最新收盘价', '周五单日', '全周累计']
for x, lbl in zip(col_x, col_labels):
    ax.text(x, n - 0.1, lbl, transform=ax.transData,
            va='center', fontsize=11, fontweight='bold',
            color='#cccccc', fontproperties=get_font())

ax.axhline(n - 0.3, color='#444444', lw=0.8)

# 数据行
cat_colors = {
    '国内': '#4fc3f7', '港股': '#ce93d8', '美股': '#80cbc4',
    '大宗': '#ffcc80', '外汇': '#ef9a9a',
}
for i, asset in enumerate(reversed(assets)):
    row = i
    cat = asset['cat']
    chg_d_color = '#ff5252' if asset['chg_d'] >= 0 else '#69f0ae'
    chg_w_color = '#ff5252' if asset['chg_w'] >= 0 else '#69f0ae'

    ax.text(col_x[0], row, cat,
            va='center', fontsize=10, color=cat_colors.get(cat, 'white'),
            fontproperties=get_font())
    ax.text(col_x[1], row, asset['label'],
            va='center', fontsize=11, fontweight='bold',
            color='white', fontproperties=get_font())
    ax.text(col_x[2], row, asset['value'],
            va='center', fontsize=11, color='#fffde7', fontproperties=get_font())
    ax.text(col_x[3], row,
            f"{'+' if asset['chg_d'] >= 0 else ''}{asset['chg_d']:.2f}%",
            va='center', fontsize=11, fontweight='bold',
            color=chg_d_color, fontproperties=get_font())
    ax.text(col_x[4], row,
            f"{'+' if asset['chg_w'] >= 0 else ''}{asset['chg_w']:.2f}%",
            va='center', fontsize=11, fontweight='bold',
            color=chg_w_color, fontproperties=get_font())

    if i > 0:
        ax.axhline(row + 0.5, color='#222635', lw=0.5)

# 底部备注
fig.text(0.04, 0.03,
         '注：🔴 红色代表上涨，🟢 绿色代表下跌 | 数据源：公开市场终端收盘价',
         ha='left', va='bottom', fontsize=9, color='#777777',
         fontproperties=get_font())

out_dir = os.path.join(os.path.dirname(__file__), '..', 'images', 'charts')
os.makedirs(out_dir, exist_ok=True)
out_path = os.path.join(out_dir, 'chart_2026-09-12-evening.png')
plt.savefig(out_path, dpi=200, bbox_inches='tight', facecolor=fig.get_facecolor())
plt.close()
print(f"Chart saved to {out_path}")
