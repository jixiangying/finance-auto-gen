#!/usr/bin/env python3
"""
生成 2026-11-02 周一晚报国内与港股核心资产收盘看板（模式A：常规交易日）
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

# ── 核心资产收盘数据（2026年11月2日 收盘终值） ──────────────────
assets = [
    {"name": "上证综合指数",     "val": "3,638.03",  "chg": "+1.08%", "detail": "+39.01点 | 成交8,474.6亿",  "sub": "强势收复3,600点 迎11月开门红",    "up": True},
    {"name": "深证成份指数",     "val": "11,010.68", "chg": "+1.63%", "detail": "+176.90点 | 成交9,362.3亿", "sub": "重返11,000点关口 成长弹性释放",   "up": True},
    {"name": "创业板指",         "val": "2,458.70",  "chg": "+1.87%", "detail": "+45.07点 | 盘中一度涨超3.5%","sub": "AI漫剧与宁王大涨带动人气回暖",   "up": True},
    {"name": "科创50指数",       "val": "1,196.94",  "chg": "+3.11%", "detail": "+36.10点 | 领涨A股核心宽基", "sub": "半导体与AI算力应用超跌强反弹",   "up": True},
    {"name": "沪深300指数",      "val": "4,016.92",  "chg": "+0.79%", "detail": "+31.42点 | 重返4,000点大关", "sub": "券商白酒发力 宽基ETF显著放量",   "up": True},
    {"name": "北证50指数",       "val": "890.86",    "chg": "+0.58%", "detail": "+5.12点 | 专精特新稳健修复", "sub": "全市场超4,680股飘红 百股涨停",   "up": True},
    {"name": "香港恒生指数",     "val": "23,393.32", "chg": "+0.42%", "detail": "+98.90点 | 成交2,048.4亿港元","sub": "南向净卖出44.69亿 港股延续升势", "up": True},
    {"name": "恒生科技指数",     "val": "3,839.41",  "chg": "+2.25%", "detail": "+84.51点 | 国指 +0.56%",     "sub": "小米涨超6% 中金港股飙升8.90%",   "up": True},
    {"name": "央行隔夜逆回购锚", "val": "1.25%",     "chg": "首日落地","detail": "投放5,410亿元 | 固定利率",  "sub": "短端政策利率换锚 10年国债1.62%", "up": True},
    {"name": "财新中国制造业PMI","val": "52.0",      "chg": "连续11月扩张","detail": "前值52.1 | 产出创半年新高","sub": "中小民企景气韧性对冲官方PMI波动", "up": True},
    {"name": "美元/人民币中间价","val": "6.7146",    "chg": "-8bp",   "detail": "离岸CNH 6.65-6.72区间",      "sub": "汇率稳健护航中国资产估值修复",   "up": False},
    {"name": "WTI原油 (亚欧盘)", "val": "$100.10",   "chg": "-3.10%", "detail": "布伦特回落至$110附近",       "sub": "中东外交缓和预期 贵金属煤炭回调", "up": False},
]

# ── 底部双维度柱状图：核心宽基涨跌幅 & 申万行业主力净流入 (亿元) ──
idx_labels = [
    "科创50", "恒生科技", "创业板指", "深证成指", "上证指数",
    "沪深300", "北证50", "恒生国指", "恒生指数", "10年国债期货", "WTI原油(日内)"
]
idx_vals = [3.11, 2.25, 1.87, 1.63, 1.08, 0.79, 0.58, 0.56, 0.42, 0.09, -3.10]

flow_labels = ["传媒(AI漫剧)", "计算机(AI应用)", "电子(半导体)", "非银金融(券商)", "电力设备", "食品饮料(白酒)", "煤炭开采", "银行"]
flow_vals = [117.5, 105.2, 79.4, 60.8, 52.3, 50.6, -12.4, -18.6]

# ── 画布与网格布局 ────────────────────────────────────────────
cols = 4
rows = (len(assets) + cols - 1) // cols
fig = plt.figure(figsize=(21, rows * 2.85 + 5.4))
fig.patch.set_facecolor('#0d1117')
gs = fig.add_gridspec(rows + 1, cols, height_ratios=[1] * rows + [1.65])

for i, a in enumerate(assets):
    ax = fig.add_subplot(gs[i // cols, i % cols])
    ax.set_facecolor('#0d1117')
    ax.axis('off')
    if a['up']:
        color, bg, arrow = '#ff4d4d', '#220909', '▲ '
    else:
        color, bg, arrow = '#00cc66', '#051f12', '▼ '

    ax.add_patch(mpatches.FancyBboxPatch(
        (0.03, 0.05), 0.94, 0.90, boxstyle="round,pad=0.03", linewidth=1.6,
        edgecolor=color, facecolor=bg, transform=ax.transAxes, zorder=0))
    ax.text(0.5, 0.83, a['name'], transform=ax.transAxes, fontsize=13,
            color='#e6edf3', ha='center', va='center', fontproperties=prop_bold)
    ax.text(0.5, 0.60, a['val'], transform=ax.transAxes, fontsize=17.5,
            color='white', ha='center', va='center', fontproperties=prop_bold)
    ax.text(0.5, 0.39, f"{arrow}{a['chg']}   |   {a['detail']}",
            transform=ax.transAxes, fontsize=10.8,
            color=color, ha='center', va='center', fontproperties=prop_bold)
    ax.text(0.5, 0.17, a['sub'], transform=ax.transAxes, fontsize=10.2,
            color='#8b949e', ha='center', va='center', fontproperties=prop)

# ── 底部左图：核心宽基与跨资产涨跌幅 (%) ───────────────────────
ax_left = fig.add_subplot(gs[rows, :2])
ax_left.set_facecolor('#0d1117')
x1 = np.arange(len(idx_labels))
colors1 = ['#ff4d4d' if v >= 0 else '#00cc66' for v in idx_vals]
bars1 = ax_left.bar(x1, idx_vals, width=0.58, color=colors1, edgecolor='#30363d', linewidth=0.8)
ax_left.axhline(0, color='#8b949e', linewidth=1.0)
ax_left.set_xticks(x1)
ax_left.set_xticklabels(idx_labels, fontproperties=prop, color='#e6edf3', fontsize=10.5, rotation=18)
yticks1 = [-4.0, -2.0, 0.0, 2.0, 4.0]
ax_left.set_yticks(yticks1)
ax_left.set_yticklabels([f"{t:+.1f}%" for t in yticks1], fontproperties=prop, color='#8b949e', fontsize=10.2)
ax_left.set_ylim(-4.2, 4.1)
ax_left.grid(axis='y', linestyle='--', alpha=0.18, color='#8b949e')
for spine in ax_left.spines.values():
    spine.set_visible(False)
for b, v in zip(bars1, idx_vals):
    offset = 0.15 if v >= 0 else -0.22
    va = 'bottom' if v >= 0 else 'top'
    ax_left.text(b.get_x() + b.get_width() / 2, v + offset, f"{v:+.2f}%",
                 ha='center', va=va, color='white', fontproperties=prop_bold, fontsize=9.5)
ax_left.set_title('A股与港股核心指数全线收红：科创50(+3.11%)与恒生科技(+2.25%)领衔反攻',
                  fontproperties=prop_bold, color='white', fontsize=12, pad=10)

# ── 底部右图：申万一级行业主力资金净流向 (亿元) ───────────────
ax_right = fig.add_subplot(gs[rows, 2:])
ax_right.set_facecolor('#0d1117')
x2 = np.arange(len(flow_labels))
colors2 = ['#ff4d4d' if v >= 0 else '#00cc66' for v in flow_vals]
bars2 = ax_right.bar(x2, flow_vals, width=0.55, color=colors2, edgecolor='#30363d', linewidth=0.8)
ax_right.axhline(0, color='#8b949e', linewidth=1.0)
ax_right.set_xticks(x2)
ax_right.set_xticklabels(flow_labels, fontproperties=prop, color='#e6edf3', fontsize=10.5, rotation=15)
yticks2 = [-30, 0, 40, 80, 120]
ax_right.set_yticks(yticks2)
ax_right.set_yticklabels([f"{t:+d}亿" for t in yticks2], fontproperties=prop, color='#8b949e', fontsize=10.2)
ax_right.set_ylim(-35, 138)
ax_right.grid(axis='y', linestyle='--', alpha=0.18, color='#8b949e')
for spine in ax_right.spines.values():
    spine.set_visible(False)
for b, v in zip(bars2, flow_vals):
    offset = 3.5 if v >= 0 else -4.5
    va = 'bottom' if v >= 0 else 'top'
    ax_right.text(b.get_x() + b.get_width() / 2, v + offset, f"{v:+.1f}亿",
                  ha='center', va=va, color='white', fontproperties=prop_bold, fontsize=9.5)

legend_patches = [
    mpatches.Patch(color='#ff4d4d', label='上涨 / 主力资金净流入 (红涨)'),
    mpatches.Patch(color='#00cc66', label='下跌 / 主力资金净流出 (绿跌)'),
]
leg = ax_right.legend(handles=legend_patches, loc='upper right', facecolor='#161b22', edgecolor='#30363d')
for text in leg.get_texts():
    text.set_fontproperties(prop)
    text.set_color('#e6edf3')
ax_right.set_title('风格“弃守转攻”：传媒/计算机各获超百亿净流入，红利避险小幅兑现',
                   fontproperties=prop_bold, color='white', fontsize=12, pad=10)

plt.suptitle('2026-11-02 周一收盘报  ·  两市放量1.78万亿迎11月“开门红”：沪指重返3638点，三部门稳市工具与AI应用共舞（模式A）',
             fontsize=15.5, color='white', y=1.01, fontproperties=prop_bold)
plt.tight_layout(pad=0.85)

out_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'images', 'charts')
os.makedirs(out_dir, exist_ok=True)
out_path = os.path.join(out_dir, 'chart_2026_11_02_evening.png')
plt.savefig(out_path, dpi=140, bbox_inches='tight', facecolor=fig.get_facecolor())
print(f"Chart successfully saved to {out_path}")
