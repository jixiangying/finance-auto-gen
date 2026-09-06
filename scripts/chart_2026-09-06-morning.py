#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
周度行情数据卡片 - 2026-09-06 周日上午 周末复盘版（第37周）
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

# ── 数据定义（基于2026-09-04周五收盘，2026第36周） ─────────────────────────────
assets = [
    # 国内市场
    {'label': '上证指数',    'value': '3930.12',   'chg_d': -0.30,  'chg_w': -0.56,  'cat': '国内'},
    {'label': '沪深300',    'value': '4548.05',   'chg_d': -0.10,  'chg_w': -0.51,  'cat': '国内'},
    {'label': '创业板指',    'value': '3286.55',   'chg_d': -0.78,  'chg_w': -4.03,  'cat': '国内'},
    # 港股市场
    {'label': '恒生指数',    'value': '25650.87',  'chg_d': +1.74,  'chg_w': +0.26,  'cat': '港股'},
    {'label': '恒生科技',    'value': '4569.80',   'chg_d': +2.27,  'chg_w': -0.77,  'cat': '港股'},
    # 美股市场
    {'label': '标普500',     'value': '7718.60',   'chg_d': -0.38,  'chg_w': +0.10,  'cat': '美股'},
    {'label': '纳斯达克',    'value': '26506.99',  'chg_d': -0.29,  'chg_w': +0.40,  'cat': '美股'},
    {'label': '道琼斯',      'value': '53414.25',  'chg_d': -0.51,  'chg_w': -0.30,  'cat': '美股'},
    # 大宗商品 & 固收
    {'label': '黄金(现货)',  'value': '4539.90',   'chg_d': -1.51,  'chg_w': -0.40,  'cat': '大宗'},
    {'label': 'WTI原油',    'value': '91.48',     'chg_d': +0.20,  'chg_w': +3.50,  'cat': '大宗'},
    {'label': '10Y美债',    'value': '4.78%',     'chg_d': +0.08,  'chg_w': +0.20,  'cat': '固收'},
    # 加密货币
    {'label': 'BTC',        'value': '$80,800',   'chg_d': +1.20,  'chg_w': +4.00,  'cat': '加密'},
    {'label': 'ETH',        'value': '$2,450',    'chg_d': +0.50,  'chg_w': +2.30,  'cat': '加密'},
]

# ── 绘图 ────────────────────────────────────────────────────────────────────────
n = len(assets)
fig, ax = plt.subplots(figsize=(14, 9.5))
fig.patch.set_facecolor('#0f1117')
ax.set_facecolor('#0f1117')
ax.set_xlim(0, 1)
ax.set_ylim(-0.5, n - 0.5)
ax.axis('off')

# 标题
fig.text(0.5, 0.97,
         '全球市场周度复盘卡片  2026年9月6日（周日）',
         ha='center', va='top', fontsize=16, fontweight='bold',
         color='white', fontproperties=get_font())
fig.text(0.5, 0.935,
         '数据截至 2026-09-04（周五）收盘 | 2026年第36周',
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
    '大宗': '#ffcc80', '固收': '#f48fb1', '加密': '#a5d6a7',
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
            va='center', fontsize=12, fontweight='bold',
            color=chg_w_color, fontproperties=get_font())

    # 分隔线
    if row < n - 1:
        ax.axhline(row + 0.45, color='#2a2a3a', lw=0.5)

# 注释
fig.text(0.5, 0.01,
         '🔴 上涨  🟢 下跌 | 数据来源：东方财富、新浪财经、Yahoo Finance | 仅供参考，不构成投资建议',
         ha='center', va='bottom', fontsize=9, color='#666666',
         fontproperties=get_font())

plt.tight_layout(rect=[0, 0.03, 1, 0.92])
out_path = 'images/charts/chart_2026-09-06-morning.png'
os.makedirs(os.path.dirname(out_path), exist_ok=True)
plt.savefig(out_path, dpi=150, bbox_inches='tight', facecolor=fig.get_facecolor())
plt.close()
print(f'✅ 图表已保存：{out_path}')
