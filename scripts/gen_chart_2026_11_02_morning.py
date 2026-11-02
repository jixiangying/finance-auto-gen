#!/usr/bin/env python3
"""
生成 2026-11-02 周一早报全球核心资产开盘基准与周末跨资产动态看板（模式C：新周展望）
红色代表上涨，绿色代表下跌；显式配置 macOS 中文字体防止乱码。
"""
import os
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.font_manager import FontProperties

# ── 中文字体设置 (macOS) ───────────────────────────────────────
FONT_PATH = "/System/Library/Fonts/STHeiti Medium.ttc"
prop = FontProperties(fname=FONT_PATH)
prop_bold = FontProperties(fname=FONT_PATH, weight='bold')
plt.rcParams['font.sans-serif'] = ['PingFang SC', 'STHeiti', 'Arial Unicode MS']
plt.rcParams['axes.unicode_minus'] = False

# ── 核心资产数据（上周五收盘基准 & 周一08:00期指/7×24h最新动态） ──
assets = [
    {"name": "标普500 (基准/期指)", "val": "7,580.07",  "chg": "-1.82%", "early": "期指 +0.19% (7,628)", "sub": "周线三连阴 今晚冬令时22:30开盘", "up": False},
    {"name": "纳斯达克 (基准/期指)", "val": "25,437.00", "chg": "-2.86%", "early": "纳指100期指 +0.34%",  "sub": "盘后迎Apple与Palantir财报大考", "up": False},
    {"name": "道琼斯工业指数",       "val": "51,770.31", "chg": "-1.09%", "early": "期指持平微涨",        "sub": "能源护盘 明迎美国中期选举投票", "up": False},
    {"name": "费城半导体指数",       "val": "10,688.80", "chg": "-7.20%", "early": "周二盘后AMD放榜",     "sub": "AI资本开支审判与芯片毛利重估",  "up": False},
    {"name": "日经225指数",          "val": "63,290.11", "chg": "-2.12%", "early": "全周回落调整",        "sub": "受美股半导体巨震拖累承压",      "up": False},
    {"name": "香港恒生指数",         "val": "23,294.42", "chg": "+1.46%", "early": "全周逆势 +0.87%",     "sub": "中国资产估值优势获南向资金加持", "up": True},
    {"name": "上证综合指数",         "val": "3,599.02",  "chg": "-1.44%", "early": "国新诚通拟增2000亿贷", "sub": "央行今日启用1.25%隔夜逆回购锚", "up": False},
    {"name": "中概金龙指数",         "val": "5,396.75",  "chg": "-0.27%", "early": "全周跌 -1.38%",       "sub": "离岸人民币稳守6.6533强韧区间",  "up": False},
    {"name": "比特币 (7×24h实时)",   "val": "$77,950",   "chg": "+0.82%", "early": "较周五低点反弹+2.38%", "sub": "FBI定性窃案 币安重开BTC提现",   "up": True},
    {"name": "WTI原油 (周一早盘)",   "val": "$104.15",   "chg": "+1.32%", "early": "布油高位破$117预期",   "sub": "OPEC+周日确认12月维持配额不变", "up": True},
    {"name": "伦敦现黄金 / 期金",    "val": "$3,880",    "chg": "-2.10%", "early": "COMEX基准 $3,937.0", "sub": "百元油价引发鹰派通胀担忧压制",  "up": False},
    {"name": "10年期美债收益率",     "val": "4.93%",     "chg": "-8.0bp", "early": "周五聚焦10月非农",     "sub": "美联储分歧下紧盯ISM与就业韧性", "up": None},
]

bar_labels = [
    "恒生(周五)", "WTI原油(周五)", "比特币(周末)", "纳指100期指", "标普期指",
    "中概金龙", "道琼斯", "上证指数", "标普500", "COMEX黄金", "日经225", "纳斯达克", "费城半导体"
]
bar_vals = [1.46, 1.32, 0.82, 0.34, 0.19, -0.27, -1.09, -1.44, -1.82, -2.10, -2.12, -2.86, -7.20]

# ── 画布与网格布局 ────────────────────────────────────────────
cols = 4
rows = (len(assets) + cols - 1) // cols
fig = plt.figure(figsize=(21, rows * 2.85 + 5.0))
fig.patch.set_facecolor('#0d1117')
gs = fig.add_gridspec(rows + 1, cols, height_ratios=[1] * rows + [1.55])

for i, a in enumerate(assets):
    ax = fig.add_subplot(gs[i // cols, i % cols])
    ax.set_facecolor('#0d1117')
    ax.axis('off')
    if a['up'] is None:
        color, bg, arrow = '#d4a017', '#1c1605', '◆ '
    elif a['up']:
        color, bg, arrow = '#ff4d4d', '#220909', '▲ '
    else:
        color, bg, arrow = '#00cc66', '#051f12', '▼ '

    ax.add_patch(mpatches.FancyBboxPatch(
        (0.03, 0.05), 0.94, 0.90, boxstyle="round,pad=0.03", linewidth=1.6,
        edgecolor=color, facecolor=bg, transform=ax.transAxes, zorder=0))
    ax.text(0.5, 0.83, a['name'], transform=ax.transAxes, fontsize=13,
            color='#e6edf3', ha='center', va='center', fontproperties=prop_bold)
    ax.text(0.5, 0.60, a['val'], transform=ax.transAxes, fontsize=17,
            color='white', ha='center', va='center', fontproperties=prop_bold)
    ax.text(0.5, 0.39, f"{arrow}{a['chg']}   |   {a['early']}",
            transform=ax.transAxes, fontsize=11,
            color=color, ha='center', va='center', fontproperties=prop_bold)
    ax.text(0.5, 0.17, a['sub'], transform=ax.transAxes, fontsize=10.2,
            color='#8b949e', ha='center', va='center', fontproperties=prop)

# ── 底部柱状图：上周五收盘冲击 vs 周一早盘期指/加密企稳对比 ─────────
axb = fig.add_subplot(gs[rows, :])
axb.set_facecolor('#0d1117')

x = np.arange(len(bar_labels))
colors = ['#ff4d4d' if v > 0 else '#00cc66' for v in bar_vals]
bars = axb.bar(x, bar_vals, width=0.56, color=colors, edgecolor='#30363d', linewidth=0.8)

axb.axhline(0, color='#8b949e', linewidth=1.0)
axb.set_xticks(x)
axb.set_xticklabels(bar_labels, fontproperties=prop, color='#e6edf3', fontsize=11, rotation=10)

yticks = [-8.0, -6.0, -4.0, -2.0, 0.0, 2.0, 3.0]
axb.set_yticks(yticks)
axb.set_yticklabels([f"{t:+.1f}%" for t in yticks], fontproperties=prop, color='#8b949e', fontsize=10.5)
axb.set_ylim(-8.3, 2.8)
axb.grid(axis='y', linestyle='--', alpha=0.18, color='#8b949e')
for spine in axb.spines.values():
    spine.set_visible(False)

for b, v in zip(bars, bar_vals):
    offset = 0.18 if v >= 0 else -0.22
    va = 'bottom' if v >= 0 else 'top'
    axb.text(b.get_x() + b.get_width() / 2, v + offset, f"{v:+.2f}%",
             ha='center', va=va, color='white', fontproperties=prop_bold, fontsize=9.8)

legend_patches = [
    mpatches.Patch(color='#ff4d4d', label='上涨 / 周一早盘企稳反弹 (红涨)'),
    mpatches.Patch(color='#00cc66', label='下跌 / 上周五收盘回调幅度 (绿跌)'),
]
leg = axb.legend(handles=legend_patches, loc='lower left', facecolor='#161b22', edgecolor='#30363d')
for text in leg.get_texts():
    text.set_fontproperties(prop)
    text.set_color('#e6edf3')

axb.set_title('新周开盘跨资产定位：美股期指与BTC周末企稳，OPEC+锁产至12月稳守百元油价，国内迎央行换锚与两千亿级增持贷款利好',
              fontproperties=prop_bold, color='white', fontsize=12.2, pad=10)

plt.suptitle('2026-11-02 周一早报  ·  全球金融市场新周展望与开盘基准看板（11月2日–11月6日超级宏观周 · 模式C）',
             fontsize=15.5, color='white', y=1.01, fontproperties=prop_bold)
plt.tight_layout(pad=0.85)

out_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'images', 'charts')
os.makedirs(out_dir, exist_ok=True)
out_path = os.path.join(out_dir, 'chart_2026_11_02_morning.png')
plt.savefig(out_path, dpi=140, bbox_inches='tight', facecolor=fig.get_facecolor())
print(f"Chart successfully saved to {out_path}")
