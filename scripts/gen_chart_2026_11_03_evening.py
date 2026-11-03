#!/usr/bin/env python3
"""
生成 2026-11-03 周二晚报国内与港股核心资产收盘看板（模式A：常规交易日）
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

# ── 核心资产收盘数据（2026年11月3日 收盘终值） ──────────────────
assets = [
    {"name": "上证综合指数",       "val": "3,608.10",  "chg": "-0.82%",    "detail": "-29.93点 | 成交8,108.3亿",   "sub": "险资护盘 韧性守住3,600点整数关",  "up": False},
    {"name": "深证成份指数",       "val": "10,876.99", "chg": "-1.21%",    "detail": "-133.69点 | 成交8,926.1亿",  "sub": "两市合计成交1.70万亿 缩量约803亿","up": False},
    {"name": "创业板指",           "val": "2,391.65",  "chg": "-2.73%",    "detail": "-67.09点 | 成交4,464.6亿",   "sub": "CPO光模块与算力硬件获利回吐",     "up": False},
    {"name": "科创50指数",         "val": "1,151.28",  "chg": "-3.81%",    "detail": "-45.66点 | 半导体链承压回调","sub": "受隔夜费半跌3.37%映射 高位消化",  "up": False},
    {"name": "沪深300指数",        "val": "4,008.87",  "chg": "-0.20%",    "detail": "-8.05点 | 稳守4,000点大关",  "sub": "保险红利与消费蓝筹充当压舱石",    "up": False},
    {"name": "北证50指数",         "val": "855.06",    "chg": "-4.02%",    "detail": "-35.80点 | 弹性标的降温",    "sub": "全市场52股涨停 AI漫剧局部仍活跃", "up": False},
    {"name": "香港恒生指数",       "val": "23,525.97", "chg": "+0.57%",    "detail": "+132.65点 | 成交2,364.0亿港元","sub": "金融峰会释放开放利好 逆势走强", "up": True},
    {"name": "恒生科技指数",       "val": "3,867.73",  "chg": "+0.74%",    "detail": "+28.32点 | 国指 +0.47%",     "sub": "餐饮出行与造车新势力领衔上涨",    "up": True},
    {"name": "南向资金净买入",     "val": "200.48亿",  "chg": "单日爆买",  "detail": "沪135.30亿 | 深65.18亿港元", "sub": "终结净流出 内资大举逢低抢筹港股", "up": True},
    {"name": "央行第3次SFISF招标", "val": "1,000亿元", "chg": "费率10bp",  "detail": "31家机构参投 | 规模创新高",  "sub": "回购再贷款转长期制度 利率降至1%", "up": True},
    {"name": "美元/人民币中间价",  "val": "6.7150",    "chg": "-4bp",      "detail": "前值6.7146 | 汇率稳健锚定",  "sub": "隔夜逆回购投放6,210亿 利率1.25%", "up": False},
    {"name": "比特币 (BTC)",       "val": "$76,500",   "chg": "-2.30%",    "detail": "创逾一月新低 | 观望中期选举","sub": "受美股纳指跌1.07%及风偏降温拖累", "up": False},
]

# ── 底部双维度柱状图：核心宽基涨跌幅 (%) & 跨市场资金/板块结构分化 ──
idx_labels = [
    "恒生科技", "恒生指数", "恒生国指", "沪深300", "上证指数",
    "深证成指", "创业板指", "科创50", "北证50"
]
idx_vals = [0.74, 0.57, 0.47, -0.20, -0.82, -1.21, -2.73, -3.81, -4.02]

struct_labels = [
    "南向净买入(亿港元)", "SFISF第3期(百亿)", "保险/红利护盘", "养殖/餐饮出行",
    "AI漫剧应用", "通信设备(CPO)", "半导体芯片"
]
# 归一化代表当日多空强度指数 / 结构冷热对比（直观展示“港强A弱、权重护盘、硬件退潮”）
struct_vals = [20.05, 10.00, 3.20, 2.65, 1.40, -6.80, -9.50]

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

# ── 底部左图：A股与港股核心指数涨跌幅对比 (%) ──────────────────
ax_left = fig.add_subplot(gs[rows, :2])
ax_left.set_facecolor('#0d1117')
x1 = np.arange(len(idx_labels))
colors1 = ['#ff4d4d' if v >= 0 else '#00cc66' for v in idx_vals]
bars1 = ax_left.bar(x1, idx_vals, width=0.56, color=colors1, edgecolor='#30363d', linewidth=0.8)
ax_left.axhline(0, color='#8b949e', linewidth=1.0)
ax_left.set_xticks(x1)
ax_left.set_xticklabels(idx_labels, fontproperties=prop, color='#e6edf3', fontsize=10.5, rotation=16)
yticks1 = [-5.0, -3.0, -1.0, 0.0, 1.0, 2.0]
ax_left.set_yticks(yticks1)
ax_left.set_yticklabels([f"{t:+.1f}%" for t in yticks1], fontproperties=prop, color='#8b949e', fontsize=10.2)
ax_left.set_ylim(-4.8, 1.8)
ax_left.grid(axis='y', linestyle='--', alpha=0.18, color='#8b949e')
for spine in ax_left.spines.values():
    spine.set_visible(False)
for b, v in zip(bars1, idx_vals):
    offset = 0.12 if v >= 0 else -0.18
    va = 'bottom' if v >= 0 else 'top'
    ax_left.text(b.get_x() + b.get_width() / 2, v + offset, f"{v:+.2f}%",
                 ha='center', va=va, color='white', fontproperties=prop_bold, fontsize=9.5)
ax_left.set_title('港红A绿显著分化：港股三大指数集体飘红，A股沪深300(-0.20%)抗跌、科创成长回调',
                  fontproperties=prop_bold, color='white', fontsize=12, pad=10)

# ── 底部右图：关键增量工具与盘面主线冷热度对比 ────────────────
ax_right = fig.add_subplot(gs[rows, 2:])
ax_right.set_facecolor('#0d1117')
x2 = np.arange(len(struct_labels))
colors2 = ['#ff4d4d' if v >= 0 else '#00cc66' for v in struct_vals]
bars2 = ax_right.bar(x2, struct_vals, width=0.54, color=colors2, edgecolor='#30363d', linewidth=0.8)
ax_right.axhline(0, color='#8b949e', linewidth=1.0)
ax_right.set_xticks(x2)
ax_right.set_xticklabels(struct_labels, fontproperties=prop, color='#e6edf3', fontsize=10.2, rotation=15)
yticks2 = [-10, -5, 0, 5, 10, 15, 20]
ax_right.set_yticks(yticks2)
ax_right.set_yticklabels([f"{t:+d}" for t in yticks2], fontproperties=prop, color='#8b949e', fontsize=10.2)
ax_right.set_ylim(-12.5, 24.5)
ax_right.grid(axis='y', linestyle='--', alpha=0.18, color='#8b949e')
for spine in ax_right.spines.values():
    spine.set_visible(False)
bar_annotations = ["+200.5亿港元", "1,000亿元", "护盘领涨", "逆势活跃", "52股涨停局部热", "高位回吐", "主力净流出居前"]
for b, v, note in zip(bars2, struct_vals, bar_annotations):
    offset = 0.6 if v >= 0 else -0.8
    va = 'bottom' if v >= 0 else 'top'
    ax_right.text(b.get_x() + b.get_width() / 2, v + offset, note,
                  ha='center', va=va, color='white', fontproperties=prop_bold, fontsize=9.0)

legend_patches = [
    mpatches.Patch(color='#ff4d4d', label='上涨 / 增量资金与政策利好 (红涨)'),
    mpatches.Patch(color='#00cc66', label='下跌 / 获利回吐与资金流出 (绿跌)'),
]
leg = ax_right.legend(handles=legend_patches, loc='upper right', facecolor='#161b22', edgecolor='#30363d')
for text in leg.get_texts():
    text.set_fontproperties(prop)
    text.set_color('#e6edf3')
ax_right.set_title('资金“弃高就低+跨江南下”：南向爆买200亿港元，央行千亿SFISF与险资共筑防线',
                   fontproperties=prop_bold, color='white', fontsize=12, pad=10)

plt.suptitle('2026-11-03 周二收盘报  ·  沪指缩量守稳3608点、恒科逆势收涨0.74%：千亿SFISF落地与南向200亿扫货对冲算力回调（模式A）',
             fontsize=15.0, color='white', y=1.01, fontproperties=prop_bold)
plt.tight_layout(pad=0.85)

out_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'images', 'charts')
os.makedirs(out_dir, exist_ok=True)
out_path = os.path.join(out_dir, 'chart_2026_11_03_evening.png')
plt.savefig(out_path, dpi=140, bbox_inches='tight', facecolor=fig.get_facecolor())
print(f"Chart successfully saved to {out_path}")
