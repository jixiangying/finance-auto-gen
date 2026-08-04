import matplotlib.pyplot as plt
import matplotlib.font_manager as fm
import os

output_dir = "images/charts/"
os.makedirs(output_dir, exist_ok=True)

# 设置中文字体 (macOS)
font_path = "/System/Library/Fonts/STHeiti Medium.ttc"
if not os.path.exists(font_path):
    font_path = "/System/Library/Fonts/PingFang.ttc"
prop = fm.FontProperties(fname=font_path)

fig, ax = plt.subplots(figsize=(11.5, 7.5))
fig.patch.set_facecolor('#f8fafc')
ax.set_facecolor('#ffffff')
ax.set_xlim(0, 1)
ax.set_ylim(0, 1)
ax.axis('off')

# Title
ax.text(0.05, 0.93, "【创业板指狂飙科创板强反弹，两市放量成交突破2.2万亿】(2026/08/04 周二晚报)", fontproperties=prop, fontsize=14, fontweight='bold', color='#1e293b')
ax.axhline(y=0.88, xmin=0.04, xmax=0.96, color='#cbd5e1', linewidth=1.5)

# Left Side: Key Market Events
ax.text(0.06, 0.82, "▌ 今日市场核心动向要闻", fontproperties=prop, fontsize=12, fontweight='bold', color='#0f172a')

events = [
    ("A股三大指数强劲反弹，创业板指暴涨5.64%", "创业板指领涨，深成指大涨3.25%，全市场超3600只个股收涨", "成交额显著放量至2.23万亿元，经历了7月调整后多头信心快速复苏"),
    ("科创50指数大涨4.09%，半导体与CPO板块掀反弹潮", "CPO及光模块板块领涨，中际旭创、天孚通信、新易盛大涨", "博通与英伟达CPO交换机量产出货，集成电路布图保护新规发布提振信心"),
    ("药明康德半年报超预期，CXO及医药板块爆棚涨停潮", "半年报实现营收288.97亿元，归母净利润110.8亿元", "全面上调全年业绩指引，且每10股派派5.1元分红，提振整个医药板块"),
    ("港股走势分化，恒生指数收跌0.60%跌回26000下方", "恒指跌0.60%收25852.92点，恒生科技指数微涨0.21%收4885.61点", "大金融板块（银行、保险）获利盘集中回吐压制大盘，CXO逆势大涨")
]

y = 0.72
for title, val, note in events:
    ax.text(0.08, y, title, fontproperties=prop, fontsize=10.5, color='#334155', fontweight='bold')
    ax.text(0.08, y-0.035, f"{val}\n{note}", fontproperties=prop, fontsize=9.0, color='#64748b')
    y -= 0.11

# Right Side: Market Indicators & Assets
ax.text(0.56, 0.82, "▌ 核心指数表现与涨跌一览", fontproperties=prop, fontsize=12, fontweight='bold', color='#0f172a')

asset_data = [
    ("上证指数 (SSEC)", "3,822.28 (日: +0.33% / 窄幅震荡) 🔴", "大金融板块回调压制指数，个股普遍反弹收红"),
    ("深证成指 (SZI)", "13,885.71 (日: +3.25% / 强劲大涨) 🔴", "成长白马及成长题材股全面爆发，突破多条短期均线"),
    ("创业板指 (CHINEXT)", "3,488.97 (日: +5.64% / 狂飙突进) 🔴", "医药CXO及新能源权重集体飙升，单日录得近年罕见涨幅"),
    ("科创50 (STAR50)", "1,616.36 (日: +4.09% / 全线收复) 🔴", "半导体国产替代及CPO量产预期引爆，几乎收复昨日失地"),
    ("恒生指数 (HSI)", "25,852.92 (日: -0.60% / 震荡回调) 🟢", "大型中资银行股回吐压低恒指，受26000点上方阻力压制"),
    ("恒生科技 (HSTECH)", "4,885.61 (日: +0.21% / 窄幅收红) 🔴", "医药及科技股分化，科网巨头震荡起伏拖累指数涨幅"),
    ("沪深两市成交额 (Turnover)", "2.23万亿 (较前一日放量超2000亿) 🔴", "放量反弹说明场外资金加速流入，交易活跃度大幅回升")
]

y_right = 0.72
for title, val, comment in asset_data:
    ax.text(0.58, y_right, title, fontproperties=prop, fontsize=10.5, color='#334155', fontweight='bold')
    color = '#ef4444' if '🔴' in val else '#10b981'
    clean_val = val.replace('🟢', '').replace('🔴', '')
    
    # Draw value with corresponding color
    ax.text(0.58, y_right-0.032, clean_val, fontproperties=prop, fontsize=9.0, fontweight='bold', color=color)
    # Draw comment next to it
    val_width = len(clean_val) * 0.007 + 0.02
    ax.text(0.58 + val_width, y_right-0.032, f"|  {comment}", fontproperties=prop, fontsize=9.0, color='#64748b')
    
    y_right -= 0.058

plt.tight_layout()
output_path = "images/charts/2026-08-04-evening.png"
plt.savefig(output_path, dpi=300, bbox_inches='tight', facecolor=fig.get_facecolor())
plt.close()
print(f"Chart saved to {output_path}")
