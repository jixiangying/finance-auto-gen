#!/usr/bin/env python3
"""
2026-09-05 国际市场早报 行情数据卡片生成脚本
复盘日期：2026-09-04（周五）美国市场收盘数据
"""
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.font_manager import FontProperties
import os

# ── 字体设置（macOS 中文支持）──────────────────────────────────────────
font_path = '/System/Library/Fonts/STHeiti Medium.ttc'
if os.path.exists(font_path):
    prop = FontProperties(fname=font_path)
    prop_bold = FontProperties(fname=font_path, weight='bold')
else:
    prop = FontProperties()
    prop_bold = FontProperties(weight='bold')

plt.rcParams['axes.unicode_minus'] = False

# ── 行情数据（2026-09-04 收盘）────────────────────────────────────────
assets = [
    {"name": "道琼斯",      "value": "53,414",  "change": "-0.51%", "up": False},
    {"name": "标普500",     "value": "7,718.60", "change": "-0.38%", "up": False},
    {"name": "纳斯达克",    "value": "26,506.99","change": "-0.29%", "up": False},
    {"name": "美债10Y",     "value": "4.78%",    "change": "+0.05%", "up": True},
    {"name": "美元指数DXY", "value": "99.14",    "change": "+0.22%", "up": True},
    {"name": "黄金",        "value": "$4,437.60","change": "-1.12%", "up": False},
    {"name": "WTI原油",     "value": "$91.48",   "change": "-0.17%", "up": False},
    {"name": "比特币BTC",   "value": "$79,200",  "change": "-2.21%", "up": False},
]

# ── 绘图配置 ──────────────────────────────────────────────────────────
n = len(assets)
fig, axes = plt.subplots(2, 4, figsize=(16, 6))
fig.patch.set_facecolor('#0d1117')
fig.suptitle(
    '2026-09-04  国际市场收盘行情',
    fontsize=15, color='white', fontproperties=prop_bold, y=1.02
)

for i, (ax, asset) in enumerate(zip(axes.flat, assets)):
    up = asset["up"]
    card_color = '#1a1a2e'
    accent = '#ff4d4d' if up else '#00c853'   # 红涨绿跌
    arrow = '▲' if up else '▼'

    ax.set_facecolor(card_color)
    for spine in ax.spines.values():
        spine.set_edgecolor(accent)
        spine.set_linewidth(1.5)

    ax.set_xticks([])
    ax.set_yticks([])

    # 资产名称
    ax.text(0.5, 0.80, asset["name"],
            transform=ax.transAxes,
            ha='center', va='center',
            fontsize=13, color='#cccccc',
            fontproperties=prop)

    # 价格
    ax.text(0.5, 0.50, asset["value"],
            transform=ax.transAxes,
            ha='center', va='center',
            fontsize=17, color='white',
            fontproperties=prop_bold)

    # 涨跌幅
    ax.text(0.5, 0.18, f'{arrow} {asset["change"]}',
            transform=ax.transAxes,
            ha='center', va='center',
            fontsize=13, color=accent,
            fontproperties=prop_bold)

plt.tight_layout(pad=1.5)

# ── 保存 ──────────────────────────────────────────────────────────────
out_dir = os.path.join(os.path.dirname(__file__), '..', 'images', 'charts')
os.makedirs(out_dir, exist_ok=True)
out_path = os.path.join(out_dir, '2026-09-05-morning-chart.png')
plt.savefig(out_path, dpi=150, bbox_inches='tight',
            facecolor=fig.get_facecolor())
print(f'✅ 数据卡片已保存：{out_path}')
