import matplotlib.pyplot as plt
import matplotlib.patches as patches
from matplotlib.font_manager import FontProperties
import numpy as np
import os

# Explicit Chinese font configuration for macOS
font_path = '/System/Library/Fonts/STHeiti Medium.ttc'
if not os.path.exists(font_path):
    font_path = '/System/Library/Fonts/Supplemental/Songti.ttc'

prop_title = FontProperties(fname=font_path, size=20, weight='bold')
prop_sub = FontProperties(fname=font_path, size=11)
prop_card_title = FontProperties(fname=font_path, size=13, weight='bold')
prop_card_val = FontProperties(fname=font_path, size=24, weight='bold')
prop_card_chg = FontProperties(fname=font_path, size=12, weight='bold')
prop_card_note = FontProperties(fname=font_path, size=9.5)
prop_axis = FontProperties(fname=font_path, size=11)
prop_bar_label = FontProperties(fname=font_path, size=10, weight='bold')

plt.rcParams['font.sans-serif'] = ['STHeiti', 'PingFang SC', 'Heiti TC', 'Arial Unicode MS']
plt.rcParams['axes.unicode_minus'] = False

fig = plt.figure(figsize=(15, 9.5), dpi=160, facecolor='#0d1321')

# Title and Subtitle
fig.text(0.04, 0.94, '2026年10月29日 (周四) 中国及全球核心资产收盘看板', color='#f8fafc', fontproperties=prop_title)
fig.text(0.04, 0.903, 'FOMC如期按兵不动(10:2)但沃什释放鹰派信号 | A股成长股一日回吐，创业板指-4.45%，两市成交1.56万亿缩量719亿', color='#94a3b8', fontproperties=prop_sub)

cards = [
    {"name": "上证指数 (SHCOMP)", "val": "3,651.43", "pct": -0.82, "pts": "-30.04 点", "note": "银行板块领涨护盘 | 沪市成交7,156亿"},
    {"name": "深证成指 (SZSE)", "val": "11,138.20", "pct": -2.92, "pts": "-334.98 点", "note": "科技权重全线重挫"},
    {"name": "创业板指 (CHINEXT)", "val": "2,517.59", "pct": -4.45, "pts": "-117.17 点", "note": "CPO/PCB领跌 | 失守2600点"},
    {"name": "北证50 (BSE 50)", "val": "≈910.09", "pct": -3.88, "pts": "≈-36.74 点", "note": "高贝塔微盘股补跌"},
    {"name": "恒生指数 (HSI)", "val": "22,958.65", "pct": -0.59, "pts": "-136.18 点", "note": "银行航空股逆势护盘"},
    {"name": "恒生科技 (HSTECH)", "val": "≈3,744.2", "pct": -2.84, "pts": "≈-109.4 点", "note": "腾讯跌2.58% | 尾盘一度跌超3%"},
    {"name": "纳斯达克 (NASDAQ)", "val": "26,549.85", "pct": 0.27, "pts": "+72.04 点", "note": "FOMC落地后美股三连涨"},
    {"name": "WTI原油 (NYMEX)", "val": "99.90", "pct": -1.83, "pts": "-1.86 美元", "note": "卡塔尔斡旋美伊 | 油价高位回落"},
]

ax_cards = fig.add_axes([0.04, 0.43, 0.92, 0.44])
ax_cards.set_xlim(0, 4)
ax_cards.set_ylim(0, 2)
ax_cards.axis('off')

for i, c in enumerate(cards):
    col = i % 4
    row = 1 - (i // 4)
    x0 = col * 1.0 + 0.015
    y0 = row * 1.0 + 0.05
    w = 0.97
    h = 0.88

    is_up = c["pct"] >= 0
    bg_color = '#2b161b' if is_up else '#112920'
    border_color = '#ef4444' if is_up else '#10b981'
    chg_color = '#f87171' if is_up else '#34d399'
    arrow = '▲ 上涨' if is_up else '▼ 下跌'
    sign = '+' if is_up else ''

    rect = patches.FancyBboxPatch(
        (x0, y0), w, h,
        boxstyle="round,pad=0.0,rounding_size=0.05",
        facecolor=bg_color, edgecolor=border_color, linewidth=1.8
    )
    ax_cards.add_patch(rect)

    ax_cards.text(x0 + 0.07, y0 + 0.69, c["name"], color='#f1f5f9', fontproperties=prop_card_title)
    ax_cards.text(x0 + 0.07, y0 + 0.42, c["val"], color='#ffffff', fontproperties=prop_card_val)
    ax_cards.text(x0 + 0.07, y0 + 0.21, f"{arrow} {sign}{c['pct']:.2f}% ({c['pts']})", color=chg_color, fontproperties=prop_card_chg)
    ax_cards.text(x0 + 0.07, y0 + 0.07, c["note"], color='#94a3b8', fontproperties=prop_card_note)

# Bottom Bar Chart
ax_bar = fig.add_axes([0.06, 0.08, 0.88, 0.28], facecolor='#161f30')
for spine in ['top', 'right']:
    ax_bar.spines[spine].set_visible(False)
for spine in ['bottom', 'left']:
    ax_bar.spines[spine].set_color('#475569')

labels = [c["name"].split(" ")[0] for c in cards]
values = [c["pct"] for c in cards]
bar_colors = ['#ef4444' if v >= 0 else '#10b981' for v in values]

x_pos = np.arange(len(labels))
bars = ax_bar.bar(x_pos, values, width=0.48, color=bar_colors, edgecolor='#1e293b', linewidth=1.0, zorder=3)

ax_bar.axhline(0, color='#94a3b8', linestyle='--', linewidth=0.9, zorder=2)
ax_bar.set_ylim(-5.4, 1.0)
ax_bar.set_xticks(x_pos)
ax_bar.set_xticklabels(labels, fontproperties=prop_axis, color='#e2e8f0')
ax_bar.tick_params(axis='y', colors='#94a3b8', labelsize=10)
ax_bar.set_title('核心指数单日涨跌幅对比 (%) — 红色代表上涨 (▲) / 绿色代表下跌 (▼)', color='#f1f5f9', fontproperties=prop_sub, pad=10)

for bar, v in zip(bars, values):
    y_text = v + 0.15 if v >= 0 else v - 0.42
    c_text = '#f87171' if v >= 0 else '#34d399'
    sign = '+' if v >= 0 else ''
    ax_bar.text(bar.get_x() + bar.get_width() / 2, y_text, f"{sign}{v:.2f}%",
                ha='center', va='center', color=c_text, fontproperties=prop_bar_label)

os.makedirs('images/charts', exist_ok=True)
output_file = 'images/charts/chart_2026_10_29_evening.png'
plt.savefig(output_file, dpi=160, facecolor=fig.get_facecolor())
plt.close(fig)
print(f"Chart saved successfully to {output_file}")
