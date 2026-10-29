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
fig.text(0.03, 0.945, '全球金融市场隔夜收盘核心行情看板 (2026-10-29 周四早报 · 模式A)',
         fontproperties=prop_title, color='#F0F6FC')
fig.text(0.03, 0.912, '核心主线：美联储10-2分裂投票按兵不动(3.75%-4.00%) | 微软Azure +48%大超预期 | 谷歌云+103%但EPS失手盘后下挫 | 沙特炼厂遇袭油价重返$102',
         fontproperties=prop_sub, color='#8B949E')

# 12 张核心资产信息卡片数据: (名称, 收盘价, 单日涨跌, 备注, 方向: 1红 -1绿)
cards_data = [
    ("道琼斯工业 (DJI)", "52,475.10", "隔夜: +0.19% (+97.53)", "FOMC后温和收涨 三连阳", 1),
    ("标普 500 (SPX)", "7,743.98", "隔夜: +0.28% (+21.38)", "距10/6纪录高点仅-0.96%", 1),
    ("纳斯达克 (IXIC)", "26,549.85", "隔夜: +0.27% (+72.04)", "存储链领涨 英伟达-1.17%拖累", 1),
    ("费城半导体 (SOX)", "11,684.00", "隔夜: +1.75% (+201.50)", "SK海力士效应 美光+5.86%", 1),
    ("罗素 2000 (RUT)", "2,830.51", "隔夜: +0.41% (+11.64)", "小盘股延续三连涨", 1),
    ("纳斯达克 100 (NDX)", "29,813.16", "隔夜: +0.55% (+161.72)", "科技巨头财报前抢筹", 1),
    ("10年期美债收益率", "5.05%", "隔夜: +5bp (前值4.99%)", "FOMC鹰派分裂 12月加息押注升温", 1),
    ("WTI 原油", "$102.51", "隔夜: +1.62% (+$1.63)", "沙特炼厂遇袭 供应风险回归", 1),
    ("现货黄金 (XAU)", "$4,035.48", "隔夜: -0.60% (-$22.72)", "鹰派分裂+收益率上行承压", -1),
    ("比特币 (BTC)", "$79,000附近", "隔夜: 延续回调", "EMA50压制 短线趋势走弱", -1),
    ("微软 (MSFT) 盘后财报", "营收$92.3B", "同比: +19% | Azure +48%", "GAAP EPS $4.92 全面超预期", 1),
    ("谷歌 (GOOGL) 盘后财报", "营收$127.6B", "同比: +25% | 云+103%", "EPS失手+现金流转负 盘后下挫", -1),
]

# 上半部分：绘制 3x4 网格卡片
card_ax = fig.add_axes([0.02, 0.43, 0.96, 0.45])
card_ax.set_xlim(0, 4)
card_ax.set_ylim(0, 3)
card_ax.axis('off')

for idx, (name, price, day_chg, note, direction) in enumerate(cards_data):
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
    card_ax.text(x0 + 0.05, y0 + h - 0.66, day_chg, fontproperties=prop_card_chg, color=accent_color)
    card_ax.text(x0 + 0.05, y0 + h - 0.81, note, fontproperties=prop_sub, color='#C9D1D9')

# 下半部分：绘制“隔夜单日涨跌幅 (%)”柱状图
ax = fig.add_axes([0.06, 0.08, 0.90, 0.30], facecolor='#161B22')

labels = [
    '道琼斯\n(DJI)', '标普500\n(SPX)', '纳斯达克\n(IXIC)', '纳斯达克100\n(NDX)',
    '费城半导体\n(SOX)', '罗素2000\n(RUT)', '富时100\n(FTSE)', '法国CAC40\n(CAC)',
    'WTI原油\n(Crude)', '现货黄金\n(Gold)'
]
day_vals = [0.19, 0.28, 0.27, 0.55, 1.75, 0.41, 0.07, 0.00, 1.62, -0.60]

x = np.arange(len(labels))
width = 0.55
colors = ['#F85149' if v >= 0 else '#2EA043' for v in day_vals]
bars = ax.bar(x, day_vals, width, color=colors, edgecolor='#0D1117', linewidth=0.8)

ax.axhline(0, color='#8B949E', linewidth=1.0, linestyle='--')
ax.set_ylim(-1.2, 2.3)
ax.grid(axis='y', linestyle=':', alpha=0.3, color='#8B949E')

# 防乱码强制代码：显式为坐标轴刻度设置字体
ax.set_xticks(x)
ax.set_xticklabels(labels, fontproperties=prop_ax, color='#E6EDF3')
for tick in ax.get_yticklabels():
    tick.set_fontproperties(prop_ax)
    tick.set_color('#8B949E')

ax.set_ylabel('涨跌幅 (%)  [红涨 / 绿跌]', fontproperties=prop_bold, color='#E6EDF3')
ax.set_title('全球核心资产隔夜收盘涨跌幅全景 (美东时间 2026-10-28 收盘)', fontproperties=prop_bold, color='#F0F6FC', pad=10)

# 数值标注
for bar in bars:
    h_val = bar.get_height()
    va = 'bottom' if h_val >= 0 else 'top'
    offset = 0.06 if h_val >= 0 else -0.08
    ax.text(bar.get_x() + bar.get_width()/2, h_val + offset, f'{h_val:+.2f}%',
            ha='center', va=va, fontproperties=FontProperties(fname=font_path, size=9.5, weight='bold'),
            color='#FF7B72' if h_val >= 0 else '#56D364')

for spine in ['top', 'right']:
    ax.spines[spine].set_visible(False)
for spine in ['bottom', 'left']:
    ax.spines[spine].set_color('#30363D')

os.makedirs('images/charts', exist_ok=True)
out_path = 'images/charts/chart_2026_10_29_morning.png'
plt.savefig(out_path, dpi=180, facecolor='#0D1117')
print(f"Chart saved successfully to {out_path}")
