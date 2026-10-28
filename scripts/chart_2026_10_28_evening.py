import matplotlib.pyplot as plt
import matplotlib.patches as patches
from matplotlib.font_manager import FontProperties
import os

# Set up Chinese font for macOS
font_path = '/System/Library/Fonts/STHeiti Medium.ttc'
if not os.path.exists(font_path):
    font_path = '/System/Library/Fonts/Supplemental/Songti.ttc'
prop_title = FontProperties(fname=font_path, size=20, weight='bold')
prop_sub = FontProperties(fname=font_path, size=12)
prop_card_title = FontProperties(fname=font_path, size=15, weight='bold')
prop_card_price = FontProperties(fname=font_path, size=22, weight='bold')
prop_card_change = FontProperties(fname=font_path, size=14, weight='bold')
prop_card_note = FontProperties(fname=font_path, size=10)
prop_axis = FontProperties(fname=font_path, size=11)

plt.rcParams['font.sans-serif'] = ['STHeiti', 'PingFang SC', 'Arial Unicode MS']
plt.rcParams['axes.unicode_minus'] = False

fig = plt.figure(figsize=(14, 9), dpi=150)
fig.patch.set_facecolor('#0F172A')

# Title
fig.text(0.04, 0.93, '2026年10月28日 (周三) 中国及亚太核心资产收盘看板', fontproperties=prop_title, color='#F8FAFC')
fig.text(0.04, 0.89, 'FOMC决议前夜放量反攻 | 创业板指大涨3.40%，人形机器人与存储芯片爆发，两市成交1.63万亿元（放量约1675亿）', fontproperties=prop_sub, color='#94A3B8')

# Data cards
cards = [
    {"name": "上证指数 (SHCOMP)", "price": "3,681.47", "change": "+0.91%", "diff": "+33.17 点", "note": "放量收复3680 | 成交7510亿", "up": True},
    {"name": "深证成指 (SZSE)", "price": "11,473.18", "change": "+2.02%", "diff": "+227.45 点", "note": "成长赛道强劲修复 | 成交8775亿", "up": True},
    {"name": "创业板指 (CHINEXT)", "price": "2,634.76", "change": "+3.40%", "diff": "+86.61 点", "note": "领涨核心宽基 | 成交4522亿", "up": True},
    {"name": "沪深300 (CSI 300)", "price": "4,083.87", "change": "+0.85%", "diff": "+34.32 点", "note": "权重温和收涨 | 成交4193亿", "up": True},
    {"name": "科创50 (STAR 50)", "price": "1,282.93", "change": "+2.45%", "diff": "+30.65 点", "note": "半导体设备强势反弹 | 成交757亿", "up": True},
    {"name": "北证50 (BSE 50)", "price": "946.83", "change": "+1.63%", "diff": "+15.19 点", "note": "专精特新活跃 | 成交139亿", "up": True},
    {"name": "恒生指数 (HSI)", "price": "23,094.83", "change": "+0.23%", "diff": "+53.51 点", "note": "成交1814亿港元 | 渣打绩后涨超7%", "up": True},
    {"name": "恒生科技 (HSTECH)", "price": "约3,853.6", "change": "+1.40%", "diff": "+53.2 点", "note": "华虹涨8.44% | 南向连续11日净卖出", "up": True},
]

# Top 2x4 Grid of Cards
ax_cards = fig.add_axes([0.04, 0.43, 0.92, 0.42])
ax_cards.set_xlim(0, 4)
ax_cards.set_ylim(0, 2)
ax_cards.axis('off')

for idx, c in enumerate(cards):
    col = idx % 4
    row = 1 - (idx // 4)
    x0 = col + 0.03
    y0 = row + 0.06
    w = 0.94
    h = 0.88

    bg_color = '#2A1215' if c['up'] else '#0F291E'
    border_color = '#EF4444' if c['up'] else '#10B981'
    text_color = '#F87171' if c['up'] else '#34D399'
    badge = '▲ 上涨' if c['up'] else '▼ 下跌'

    rect = patches.FancyBboxPatch((x0, y0), w, h, boxstyle="round,pad=0.02,rounding_size=0.05",
                                  facecolor=bg_color, edgecolor=border_color, linewidth=1.8)
    ax_cards.add_patch(rect)

    ax_cards.text(x0 + 0.05, y0 + h - 0.18, c['name'], fontproperties=prop_card_title, color='#E2E8F0')
    ax_cards.text(x0 + 0.05, y0 + h - 0.46, c['price'], fontproperties=prop_card_price, color='#FFFFFF')
    ax_cards.text(x0 + 0.05, y0 + h - 0.68, f"{badge}  {c['change']} ({c['diff']})", fontproperties=prop_card_change, color=text_color)
    ax_cards.text(x0 + 0.05, y0 + 0.07, c['note'], fontproperties=prop_card_note, color='#94A3B8')

# Bottom Bar Chart for relative comparison
ax_bar = fig.add_axes([0.06, 0.08, 0.88, 0.28])
ax_bar.set_facecolor('#1E293B')

labels = [c['name'].split(' ')[0] for c in cards]
values = [0.91, 2.02, 3.40, 0.85, 2.45, 1.63, 0.23, 1.40]
bar_colors = ['#EF4444' if v > 0 else '#10B981' for v in values]

bars = ax_bar.bar(range(len(labels)), values, color=bar_colors, width=0.5, edgecolor='#334155', linewidth=1)
ax_bar.axhline(0, color='#64748B', linewidth=1, linestyle='--')
ax_bar.set_ylim(-0.5, 4.2)
ax_bar.set_xticks(range(len(labels)))
ax_bar.set_xticklabels(labels, fontproperties=prop_axis, color='#E2E8F0')
for label in ax_bar.get_yticklabels():
    label.set_fontproperties(prop_axis)
    label.set_color('#94A3B8')

ax_bar.set_title('核心指数单日涨跌幅对比 (%) — 红色代表上涨 (▲) / 绿色代表下跌 (▼)', fontproperties=prop_sub, color='#E2E8F0', pad=10)
ax_bar.spines['top'].set_visible(False)
ax_bar.spines['right'].set_visible(False)
ax_bar.spines['left'].set_color('#475569')
ax_bar.spines['bottom'].set_color('#475569')

for bar, v in zip(bars, values):
    y_pos = v + 0.12 if v >= 0 else v - 0.28
    ax_bar.text(bar.get_x() + bar.get_width()/2, y_pos, f"{v:+.2f}%", ha='center', va='center',
                fontproperties=prop_axis, color='#F87171' if v > 0 else '#34D399', fontweight='bold')

os.makedirs('images/charts', exist_ok=True)
output_file = 'images/charts/chart_2026_10_28_evening.png'
plt.savefig(output_file, dpi=150, facecolor=fig.get_facecolor())
print(f"Chart saved to {output_file}")
