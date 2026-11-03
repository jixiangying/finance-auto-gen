#!/usr/bin/env python3
"""
生成 2026-11-03 周二早报全球核心资产隔夜收盘行情看板（模式A：常规交易日）
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

# ── 核心资产隔夜收盘数据（2026-11-02 周一收盘终值） ────────────────
assets = [
    {"name": "道琼斯工业指数",       "val": "51,983.98", "chg": "+0.41%", "early": "+213.67点 逆势收红",   "sub": "油价暴跌利好消费与建材工业股", "up": True},
    {"name": "标普500指数",          "val": "7,541.40",  "chg": "-0.51%", "early": "-38.67点 冲高回落",    "sub": "科技与能源板块双双承压拖累",   "up": False},
    {"name": "纳斯达克综合指数",     "val": "25,164.32", "chg": "-1.07%", "early": "-272.68点 延续调整",   "sub": "纳指100较10月高点回撤逾10%",   "up": False},
    {"name": "费城半导体指数",       "val": "10,328.33", "chg": "-3.37%", "early": "-360.47点 领跌美股",   "sub": "AI资本开支担忧 周二盘后迎AMD", "up": False},
    {"name": "纳斯达克金龙指数",     "val": "5,518.10",  "chg": "+2.25%", "early": "+121.35点 逆势领跑",   "sub": "阿里拼多多小鹏B站集体走强",    "up": True},
    {"name": "上证综合指数 (周一)",  "val": "3,638.03",  "chg": "+1.08%", "early": "恒生指数 +0.42%",      "sub": "央行1.25%隔夜逆回购换锚首秀",  "up": True},
    {"name": "Apple (盘后财报)",     "val": "$338.32",   "chg": "-3.60%", "early": "盘后跌破$330关口",     "sub": "Q4营收$1145亿超预期 毛利47.9%", "up": False},
    {"name": "Palantir (盘后财报)",  "val": "$178.44",   "chg": "-3.50%", "early": "盘后回落至$171附近",   "sub": "Q3营收飙96%破$23亿 估值恐高",   "up": False},
    {"name": "WTI原油期货 (结算)",   "val": "$97.58",    "chg": "-6.36%", "early": "盘中深跌破$96关口",    "sub": "美伊多哈谈判进展刺破百元油价", "up": False},
    {"name": "布伦特原油 (结算)",    "val": "$104.77",   "chg": "-7.60%", "early": "地缘溢价大幅回吐",     "sub": "伊朗提议霍尔木兹两日缓和方案", "up": False},
    {"name": "COMEX黄金 (结算)",     "val": "$3,956.90", "chg": "+1.83%", "early": "美元指数软化 101.66",  "sub": "油价跳水缓和加息恐慌提振金价", "up": True},
    {"name": "10年期美债 / BTC",     "val": "4.90%",     "chg": "-2.0bp", "early": "比特币 $78,020 (+0.91%)", "sub": "美财政部下调Q4净借款至$6180亿", "up": None},
]

bar_labels = [
    "中概金龙", "恒生科技", "COMEX黄金", "上证指数", "比特币",
    "恒生指数", "道琼斯", "罗素2000", "标普500", "纳斯达克",
    "费城半导体", "Palantir盘后", "Apple盘后", "WTI原油", "布伦特原油"
]
bar_vals = [2.25, 2.25, 1.83, 1.08, 0.91, 0.42, 0.41, -0.35, -0.51, -1.07, -3.37, -3.50, -3.60, -6.36, -7.60]

# ── 画布与网格布局 ────────────────────────────────────────────
cols = 4
rows = (len(assets) + cols - 1) // cols
fig = plt.figure(figsize=(21, rows * 2.85 + 5.2))
fig.patch.set_facecolor('#0d1117')
gs = fig.add_gridspec(rows + 1, cols, height_ratios=[1] * rows + [1.60])

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
            transform=ax.transAxes, fontsize=10.8,
            color=color, ha='center', va='center', fontproperties=prop_bold)
    ax.text(0.5, 0.17, a['sub'], transform=ax.transAxes, fontsize=10.0,
            color='#8b949e', ha='center', va='center', fontproperties=prop)

# ── 底部柱状图：全球跨资产隔夜涨跌幅全景对比 ──────────────────────
axb = fig.add_subplot(gs[rows, :])
axb.set_facecolor('#0d1117')

x = np.arange(len(bar_labels))
colors = ['#ff4d4d' if v > 0 else '#00cc66' for v in bar_vals]
bars = axb.bar(x, bar_vals, width=0.56, color=colors, edgecolor='#30363d', linewidth=0.8)

axb.axhline(0, color='#8b949e', linewidth=1.0)
axb.set_xticks(x)
axb.set_xticklabels(bar_labels, fontproperties=prop, color='#e6edf3', fontsize=10.5, rotation=12)

yticks = [-8.0, -6.0, -4.0, -2.0, 0.0, 2.0, 4.0]
axb.set_yticks(yticks)
axb.set_yticklabels([f"{t:+.1f}%" for t in yticks], fontproperties=prop, color='#8b949e', fontsize=10.5)
axb.set_ylim(-8.8, 3.4)
axb.grid(axis='y', linestyle='--', alpha=0.18, color='#8b949e')
for spine in axb.spines.values():
    spine.set_visible(False)

for b, v in zip(bars, bar_vals):
    offset = 0.18 if v >= 0 else -0.22
    va = 'bottom' if v >= 0 else 'top'
    axb.text(b.get_x() + b.get_width() / 2, v + offset, f"{v:+.2f}%",
             ha='center', va=va, color='white', fontproperties=prop_bold, fontsize=9.5)

legend_patches = [
    mpatches.Patch(color='#ff4d4d', label='隔夜收涨 / 逆势走强资产 (红涨)'),
    mpatches.Patch(color='#00cc66', label='隔夜收跌 / 盘后回调与油价暴跌 (绿跌)'),
]
leg = axb.legend(handles=legend_patches, loc='lower left', facecolor='#161b22', edgecolor='#30363d')
for text in leg.get_texts():
    text.set_fontproperties(prop)
    text.set_color('#e6edf3')

axb.set_title('隔夜跨资产剧烈分化：美伊谈判传进展令原油暴跌逾7%、黄金反弹1.83%，中概逆势涨2.25%，Apple与Palantir超预期后仍遭获利了结',
              fontproperties=prop_bold, color='white', fontsize=12.0, pad=10)

plt.suptitle('2026-11-03 周二早报  ·  全球金融市场隔夜收盘行情看板（决战美国中期选举投票日 · 模式A）',
             fontsize=15.5, color='white', y=1.01, fontproperties=prop_bold)
plt.tight_layout(pad=0.85)

out_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'images', 'charts')
os.makedirs(out_dir, exist_ok=True)
out_path = os.path.join(out_dir, 'chart_2026_11_03_morning.png')
plt.savefig(out_path, dpi=140, bbox_inches='tight', facecolor=fig.get_facecolor())
print(f"Chart successfully saved to {out_path}")
