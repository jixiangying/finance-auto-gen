import matplotlib.pyplot as plt
import matplotlib.patches as patches
from matplotlib.font_manager import FontProperties
import numpy as np
import os

# 显式设置 macOS 中文字体
font_path = '/System/Library/Fonts/STHeiti Medium.ttc'
if not os.path.exists(font_path):
    font_path = '/System/Library/Fonts/PingFang.ttc'
prop = FontProperties(fname=font_path)
prop_bold = FontProperties(fname=font_path, weight='bold', size=13)
prop_title = FontProperties(fname=font_path, weight='bold', size=18)
prop_sub = FontProperties(fname=font_path, size=11)
prop_card_title = FontProperties(fname=font_path, weight='bold', size=13)
prop_card_val = FontProperties(fname=font_path, weight='bold', size=17)
prop_card_chg = FontProperties(fname=font_path, weight='bold', size=11)
prop_ax = FontProperties(fname=font_path, size=11)

plt.rcParams['font.sans-serif'] = ['STHeiti', 'PingFang SC', 'Heiti TC', 'Arial Unicode MS']
plt.rcParams['axes.unicode_minus'] = False

fig = plt.figure(figsize=(16, 11), dpi=180, facecolor='#0D1117')

# 顶部大标题与副标题
fig.text(0.03, 0.945, '全球金融市场周末复盘与核心资产看板 (2026-10-25 周日早报 · 模式B)', 
         fontproperties=prop_title, color='#F0F6FC')
fig.text(0.03, 0.912, '核心主线：WTI原油破百($100.61)与布油飙至$116.50引爆再通胀 | 黄金失守$4,000创四月最大周跌幅 | 10Y美债返5.00% | A股周五放量1.97万亿深V反攻', 
         fontproperties=prop_sub, color='#8B949E')

# 12 张核心资产信息卡片数据: (名称, 现价/收盘价, 周五单日涨跌, 全周累计涨跌, 单日涨跌方向: 1红 -1绿)
cards_data = [
    ("道琼斯工业 (DJI)", "52,215.16", "周五: -1.23% (-652.82)", "全周: +0.42% (周线三连阳)", -1),
    ("标普 500 (SPX)", "7,623.68", "周五: -0.52% (-39.75)", "全周: -0.48% (周线两连阴)", -1),
    ("纳斯达克 (IXIC)", "25,955.34", "周五: -0.21% (-53.52)", "全周: -0.68% (AI开支余震)", -1),
    ("罗素 2000 (RUT)", "2,775.89", "周五: -0.29% (-8.14)", "全周: +2.01% (小盘股逆势领跑)", -1),
    ("上证指数 (SHCOMP)", "3,690.48", "周五: +0.89% (+32.45)", "全周: -0.69% (深V守住3600)", 1),
    ("创业板指 (CHINEXT)", "2,684.10", "周五: +4.16% (+107.20)", "全周: -3.18% (算力/机器人爆发)", 1),
    ("恒生指数 (HSI)", "23,093.37", "周五: +0.69% (+158.69)", "全周: -5.18% (收复23000大关)", 1),
    ("恒生科技 (HSTECH)", "3,871.66", "周五: +2.05% (+77.73)", "全周: -7.65% (周五超跌反弹)", 1),
    ("WTI / 布伦特原油", "$100.61 / $116.50", "周五: +1.21% / +2.88%", "全周: +6.85% / +8.40% (破百)", 1),
    ("现货黄金 (XAU)", "$3,995.00/oz", "周五: -1.62% (-$65.68)", "全周: -3.85% (失守4000大关)", -1),
    ("10年期美债收益率", "5.00%", "周五: +4bp (前值4.96%)", "全周: +14bp (12月加息押注78%)", 1),
    ("比特币 (BTC)", "$80,500", "周末交投: -1.02% (周五$81,328)", "全周: -4.20% (考验8万关口)", -1),
]

# 上半部分：绘制 3x4 网格卡片
card_ax = fig.add_axes([0.02, 0.43, 0.96, 0.45])
card_ax.set_xlim(0, 4)
card_ax.set_ylim(0, 3)
card_ax.axis('off')

for idx, (name, price, fri_chg, wk_chg, direction) in enumerate(cards_data):
    row = 2 - (idx // 4)
    col = idx % 4
    x0 = col + 0.04
    y0 = row + 0.06
    w = 0.92
    h = 0.86

    # 颜色规范：红色代表上涨 🔴，绿色代表下跌 🟢
    if direction > 0:
        bg_color = '#2A1215'
        border_color = '#F85149'
        accent_color = '#FF7B72'
        tag = '▲ 涨'
    else:
        bg_color = '#0F261A'
        border_color = '#2EA043'
        accent_color = '#56D364'
        tag = '▼ 跌'

    rect = patches.FancyBboxPatch((x0, y0), w, h, boxstyle="round,pad=0.02,rounding_size=0.05",
                                  facecolor=bg_color, edgecolor=border_color, linewidth=1.6)
    card_ax.add_patch(rect)

    card_ax.text(x0 + 0.05, y0 + h - 0.19, f"{name}", fontproperties=prop_card_title, color='#E6EDF3')
    card_ax.text(x0 + w - 0.18, y0 + h - 0.19, tag, fontproperties=prop_card_title, color=accent_color)
    card_ax.text(x0 + 0.05, y0 + h - 0.47, price, fontproperties=prop_card_val, color='#FFFFFF')
    card_ax.text(x0 + 0.05, y0 + h - 0.66, fri_chg, fontproperties=prop_card_chg, color=accent_color)
    card_ax.text(x0 + 0.05, y0 + h - 0.81, wk_chg, fontproperties=prop_sub, color='#C9D1D9')

# 下半部分：绘制“周五单日 vs 全周累计涨跌幅 (%)”对比柱状图
ax = fig.add_axes([0.06, 0.08, 0.90, 0.30], facecolor='#161B22')

labels = [
    '道琼斯\n(DJI)', '标普500\n(SPX)', '纳斯达克\n(IXIC)', '罗素2000\n(RUT)',
    '上证指数\n(SHCOMP)', '深证成指\n(SZSE)', '创业板指\n(CHINEXT)', '恒生指数\n(HSI)',
    '恒生科技\n(HSTECH)', 'WTI原油\n(Crude)', '布伦特原油\n(Brent)', '现货黄金\n(Gold)'
]
fri_vals = [-1.23, -0.52, -0.21, -0.29, 0.89, 2.79, 4.16, 0.69, 2.05, 1.21, 2.88, -1.62]
wk_vals  = [0.42, -0.48, -0.68, 2.01, -0.69, -1.09, -3.18, -5.18, -7.65, 6.85, 8.40, -3.85]

x = np.arange(len(labels))
width = 0.36

fri_colors = ['#F85149' if v >= 0 else '#2EA043' for v in fri_vals]
wk_colors  = ['#FF9F89' if v >= 0 else '#56D364' for v in wk_vals]

bars1 = ax.bar(x - width/2, fri_vals, width, label='周五单日涨跌幅 (%)', color=fri_colors, edgecolor='#0D1117', linewidth=0.8)
bars2 = ax.bar(x + width/2, wk_vals, width, label='全周累计涨跌幅 (%)', color=wk_colors, edgecolor='#0D1117', linewidth=0.8, alpha=0.72, hatch='//')

ax.axhline(0, color='#8B949E', linewidth=1.0, linestyle='--')
ax.set_ylim(-10.0, 10.5)
ax.grid(axis='y', linestyle=':', alpha=0.3, color='#8B949E')

# 防乱码强制代码：显式为坐标轴刻度设置字体
ax.set_xticks(x)
ax.set_xticklabels(labels, fontproperties=prop_ax, color='#E6EDF3')
for tick in ax.get_yticklabels():
    tick.set_fontproperties(prop_ax)
    tick.set_color('#8B949E')

ax.set_ylabel('涨跌幅 (%)  [红涨 / 绿跌]', fontproperties=prop_bold, color='#E6EDF3')
ax.set_title('全球核心资产「周五单日 vs 全周累计」涨跌幅全景对比 (截至 2026-10-25)', fontproperties=prop_bold, color='#F0F6FC', pad=10)

# 数值标注
for bar in bars1:
    h_val = bar.get_height()
    va = 'bottom' if h_val >= 0 else 'top'
    offset = 0.22 if h_val >= 0 else -0.28
    ax.text(bar.get_x() + bar.get_width()/2, h_val + offset, f'{h_val:+.2f}%',
            ha='center', va=va, fontproperties=FontProperties(fname=font_path, size=8.5, weight='bold'),
            color='#FF7B72' if h_val >= 0 else '#56D364')

for bar in bars2:
    h_val = bar.get_height()
    va = 'bottom' if h_val >= 0 else 'top'
    offset = 0.22 if h_val >= 0 else -0.28
    ax.text(bar.get_x() + bar.get_width()/2, h_val + offset, f'{h_val:+.2f}%',
            ha='center', va=va, fontproperties=FontProperties(fname=font_path, size=8.5),
            color='#FFA198' if h_val >= 0 else '#7EE787')

for spine in ['top', 'right']:
    ax.spines[spine].set_visible(False)
for spine in ['bottom', 'left']:
    ax.spines[spine].set_color('#30363D')

# 图例说明
legend_p1 = patches.Patch(facecolor='#F85149', label='实心柱：周五单日涨跌 (红涨 ▲ / 绿跌 ▼)')
legend_p2 = patches.Patch(facecolor='#FF9F89', alpha=0.72, hatch='//', label='斜纹柱：全周累计涨跌 (红涨 ▲ / 绿跌 ▼)')
ax.legend(handles=[legend_p1, legend_p2], loc='upper left', prop=prop_ax, facecolor='#0D1117', edgecolor='#30363D', labelcolor='#E6EDF3')

os.makedirs('images/charts', exist_ok=True)
out_path = 'images/charts/chart_2026_10_25_morning.png'
plt.savefig(out_path, dpi=180, facecolor='#0D1117')
print(f"Chart saved successfully to {out_path}")
