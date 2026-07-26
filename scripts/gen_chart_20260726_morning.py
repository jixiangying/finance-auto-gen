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
ax.text(0.05, 0.93, "【周末全球市场与核心资产表现盘点】(2026/07/26 周日早报)", fontproperties=prop, fontsize=14, fontweight='bold', color='#1e293b')
ax.axhline(y=0.88, xmin=0.04, xmax=0.96, color='#cbd5e1', linewidth=1.5)

# Left Side: Key Market Events
ax.text(0.06, 0.82, "▌ 过去48小时及全周重磅事件", fontproperties=prop, fontsize=12, fontweight='bold', color='#0f172a')

events = [
    ("美股三大股指周线尽墨，科技板块领跌", "纳指周跌2.1%，标普跌0.6%，道指跌0.4%", "英特尔暴跌6.5%领跌半导体，大厂AI开支面临重估审视"),
    ("中东及红海局势升级，布油飙升逼近百元", "布油周度大涨近10%收于$96.78，日内冲高回吐3.88%", "Houthi封锁致原油及运费溢价走高，随后多头高位获利了结"),
    ("关税政策生效重燃通胀忧虑，美债收益率冲高", "10年期美债收益率报4.69%，周升13.6BP至年内高位", "特朗普新关税正式生效推升美元，无息资产与避险黄金盘中承压"),
    ("宏观靴子密集，下周迎超级议息与财报周", "下周美联储公布利率决议，微软、苹果等公布财报", "市场处于暴风雨前夕，两市明显缩量，存量资金维持谨慎防守")
]

y = 0.72
for title, val, note in events:
    ax.text(0.08, y, title, fontproperties=prop, fontsize=10.5, color='#334155', fontweight='bold')
    ax.text(0.08, y-0.035, f"{val}\n{note}", fontproperties=prop, fontsize=9.0, color='#64748b')
    y -= 0.11

# Right Side: Market Indicators & Assets
ax.text(0.56, 0.82, "▌ 核心资产全周及隔夜表现", fontproperties=prop, fontsize=12, fontweight='bold', color='#0f172a')

asset_data = [
    ("纳斯达克综合指数 (NASDAQ)", "24,975.82 (周: -2.10% / 日: -0.64%) 🟢", "AI估值回调承压，半导体板块出现集体震荡"),
    ("标普 500 指数 (S&P 500)", "7,411.98 (周: -0.60% / 日: +0.05%) 🟢", "防守型板块上涨抵消科技走弱，大盘几乎平收"),
    ("道琼斯工业指数 (DJIA)", "51,947.25 (周: -0.40% / 日: +0.46%) 🟢", "金融与传统周期板块护盘，指数表现相对坚挺"),
    ("布伦特原油期货 (Brent)", "$96.78 (周: +9.50% / 日: -3.88%) 🔴", "地缘溢价支撑周线上扬，周五多头了结跌破百元"),
    ("COMEX 黄金期货 (Gold)", "$4,064.10 (周: -1.80% / 日: +0.52%) 🟢", "美元走强及收益率飙升压制，黄金周线小幅收跌"),
    ("10年期美债收益率 (US10Y)", "4.69% (周: +13.6BP / 日: -1BP) 🔴", "通胀预期与关税扰动推升收益率，接近年内高点"),
    ("比特币 (BTC)", "$65,052.00 (周: +2.99% / 日: -1.56%) 🔴", "展现一定抗跌韧性，但新关税阴霾导致资金谨慎")
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
output_path = "images/charts/2026-07-26-morning.png"
plt.savefig(output_path, dpi=300, bbox_inches='tight', facecolor=fig.get_facecolor())
plt.close()
print(f"Chart saved to {output_path}")
