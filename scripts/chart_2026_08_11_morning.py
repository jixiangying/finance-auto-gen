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

# 显式设置 rcParams 以防止乱码
plt.rcParams['font.sans-serif'] = ['STHeiti', 'PingFang SC', 'Heiti TC', 'sans-serif']
plt.rcParams['axes.unicode_minus'] = False

fig, ax = plt.subplots(figsize=(12.0, 8.0))
fig.patch.set_facecolor('#f8fafc')
ax.set_facecolor('#ffffff')
ax.set_xlim(0, 1)
ax.set_ylim(0, 1)
ax.axis('off')

# Title
ax.text(0.04, 0.94, "【常规交易日：美股半导体普跌引发情绪整固，国内政策指引2030金融开放新篇章】(2026/08/11 周二早报)", fontproperties=prop, fontsize=14, fontweight='bold', color='#1e293b')
ax.axhline(y=0.90, xmin=0.03, xmax=0.97, color='#cbd5e1', linewidth=1.5)

# Left Side: Key Market Events / Outlook
ax.text(0.05, 0.84, "▌ 本周全球市场核心博弈逻辑与前瞻", fontproperties=prop, fontsize=12, fontweight='bold', color='#0f172a')

events = [
    ("美股三大股指微跌，半导体板块受Intel增发拖累领跌", 
     "道指微跌0.11%，标普微跌0.06%，纳指下跌0.32%。", 
     "Intel宣布150亿美元增发方案导致股价大跌，费城半导体指数大跌2.94%。"),
    ("国内市场温和反弹，上证收盘涨0.67%站上3960点", 
     "上证收于3966.59点，深成指涨0.04%。两市总成交额2.52万亿元。", 
     "消费股领涨，特别是农林牧渔和食品饮料板块。创业板与科创板微跌。"),
    ("央行发布2026-2030改革规划，推进高水平金融开放", 
     "PBOC稳步扩大人民币全球使用，深化资本市场互联互通机制。", 
     "强化金融支持科技、绿色发展等重点领域，健全宏观审慎政策框架。"),
    ("大宗商品多数回暖，地缘局势推动国际油价大幅反弹", 
     "霍尔木兹海峡及红海运输担忧加剧，WTI原油收涨重回$79.66/桶。", 
     "黄金期货微涨0.11%至$4403.34/盎司，避险资产与风险资产呈现分化表现。"),
    ("宏观流动性预期稳定，市场静待本周二恐怖数据与周三CPI", 
     "美债收益率温和上行至4.697%，BTC站稳6.48万美元区间震荡。", 
     "在通胀考验与零售数据发布前，市场进入情绪整固阶段，估值溢价受考验。")
]

y = 0.75
for title, val, note in events:
    ax.text(0.06, y, f"• {title}", fontproperties=prop, fontsize=10.5, color='#334155', fontweight='bold')
    ax.text(0.06, y-0.030, f"  焦点: {val}\n  研判: {note}", fontproperties=prop, fontsize=9.0, color='#64748b')
    y -= 0.105

# Right Side: Market Indicators & Assets
ax.text(0.55, 0.84, "▌ 核心资产前一交易日表现", fontproperties=prop, fontsize=12, fontweight='bold', color='#0f172a')

asset_data = [
    ("纳斯达克指数 (NASDAQ)", "26,605.36", "周一: -0.32% 🟢"),
    ("标普 500 指数 (S&P 500)", "7,753.11", "周一: -0.06% 🟢"),
    ("道琼斯工业指数 (DJIA)", "53,975.98", "周一: -0.11% 🟢"),
    ("费城半导体指数 (SOX)", "11,993.86", "周一: -2.94% 🟢"),
    ("上证指数 (SSEC)", "3,966.59", "周一: +0.67% 🔴"),
    ("深圳成指 (SZCOMP)", "14,316.96", "周一: +0.04% 🔴"),
    ("COMEX 黄金期货 (Gold)", "$4,403.34", "周一: +0.11% 🔴"),
    ("WTI 原油期货 (WTI)", "$79.66", "周一: +1.08% 🔴"),
    ("10年期美债收益率 (US10Y)", "4.697%", "周一: +3.7BP 🔴"),
    ("比特币 (BTC)", "$64,856.10", "周一: -0.08% 🟢")
]

y_right = 0.75
for title, price, perf in asset_data:
    ax.text(0.57, y_right, title, fontproperties=prop, fontsize=10.0, color='#334155', fontweight='bold')
    
    color = '#ef4444' if '🔴' in perf else '#10b981'
    clean_perf = perf.replace('🟢', '').replace('🔴', '')
    
    # Draw price
    ax.text(0.57, y_right-0.026, f"现价: {price}", fontproperties=prop, fontsize=9.0, color='#475569')
    # Draw performance
    ax.text(0.71, y_right-0.026, f"|  {clean_perf}", fontproperties=prop, fontsize=9.0, fontweight='bold', color=color)
    
    y_right -= 0.054

plt.tight_layout()
output_path = "images/charts/2026-08-11-morning.png"
plt.savefig(output_path, dpi=300, bbox_inches='tight', facecolor=fig.get_facecolor())
plt.close()
print(f"Chart saved to {output_path}")
