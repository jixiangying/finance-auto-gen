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
fig.text(0.04, 0.93, '2026年10月26日 (周一) 中国及亚太核心资产收盘看板', fontproperties=prop_title, color='#F8FAFC')
fig.text(0.04, 0.89, '指数新规首日落地 & 央行7000亿MLF护航 | 沪指权重托底微涨，双创缩量回调，两市成交1.61万亿元（缩量约3500亿）', fontproperties=prop_sub, color='#94A3B8')

# Data cards
cards = [
    {"name": "上证指数 (SHCOMP)", "price": "3,697.52", "change": "+0.19%", "diff": "+7.04 点", "note": "权重护盘尾盘翻红 | 成交7465亿", "up": True},
    {"name": "深证成指 (SZSE)", "price": "11,534.38", "change": "-1.19%", "diff": "-139.45 点", "note": "成长硬件回调 | 成交8623亿", "up": False},
    {"name": "创业板指 (CHINEXT)", "price": "2,638.23", "change": "-1.71%", "diff": "-45.87 点", "note": "算力光模块获利回吐 | 成交4281亿", "up": False},
    {"name": "沪深300 (CSI 300)", "price": "4,103.54", "change": "-0.04%", "diff": "-1.79 点", "note": "石油银行高股息显著抗跌", "up": False},
    {"name": "科创50 (STAR 50)", "price": "1,315.50", "change": "-2.23%", "diff": "-30.01 点", "note": "科创综指15%上限新规首日实施", "up": False},
    {"name": "北证50 (BSE 50)", "price": "963.95", "change": "-2.13%", "diff": "-20.95 点", "note": "三季报收官期高位筹码震荡", "up": False},
    {"name": "恒生指数 (HSI)", "price": "23,211.81", "change": "+0.51%", "diff": "+118.44 点", "note": "红筹与能源领涨 | 成交1758亿港元", "up": True},
    {"name": "恒生科技 (HSTECH)", "price": "3,857.53", "change": "-0.36%", "diff": "-14.13 点", "note": "国企指数+0.59% | 静待美股云财报", "up": False},
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
values = [0.19, -1.19, -1.71, -0.04, -2.23, -2.13, 0.51, -0.36]
bar_colors = ['#EF4444' if v > 0 else '#10B981' for v in values]

bars = ax_bar.bar(range(len(labels)), values, color=bar_colors, width=0.5, edgecolor='#334155', linewidth=1)
ax_bar.axhline(0, color='#64748B', linewidth=1, linestyle='--')
ax_bar.set_ylim(-2.8, 1.2)
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
output_file = 'images/charts/chart_2026_10_26_evening.png'
plt.savefig(output_file, dpi=150, facecolor=fig.get_facecolor())
print(f"Chart saved to {output_file}")
