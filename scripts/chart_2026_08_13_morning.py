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

fig, ax = plt.subplots(figsize=(12.0, 8.5))
fig.patch.set_facecolor('#f8fafc')
ax.set_facecolor('#ffffff')
ax.set_xlim(0, 1)
ax.set_ylim(0, 1)
ax.axis('off')

# Title
ax.text(0.04, 0.95, "【常规交易日：CPI符合预期引发缓解反弹，美债下行黄金暴涨】(2026/08/13 周四早报)", fontproperties=prop, fontsize=14, fontweight='bold', color='#1e293b')
ax.axhline(y=0.91, xmin=0.03, xmax=0.97, color='#cbd5e1', linewidth=1.5)

# Left Side: Key Market Events / Outlook
ax.text(0.05, 0.86, "▌ 本周全球市场核心博弈逻辑与前瞻", fontproperties=prop, fontsize=12, fontweight='bold', color='#0f172a')

events = [
    ("7月CPI数据符合预期，通胀保持回落势头", 
     " headline CPI同比+3.4%，环比+0.1%；核心CPI同比+2.5%，环比+0.2%。", 
     "整体数据无惊无险，确认去通胀趋势仍存，缓解了市场对二次通胀的担忧。"),
    ("美股三大股指多数温和上涨，纳指与半导体领跑", 
     "纳指涨0.59%，标普500涨0.26%，道指微跌0.04%。SOX指数大涨1.68%。", 
     "通胀落地引发“缓解性反弹”，AI相关硬科技成长股再次成为资金流入重点。"),
    ("沪深两市温和反弹，成交额第13天维持在两万亿之上", 
     "上证指数收涨0.32%收复3940点，深证成指大涨1.09%，成交2.15万亿。", 
     "虽然较前一日缩量，但成交量依旧高企，表明市场做多动能和流动性依旧充沛。"),
    ("大宗商品表现分化，避险情绪升温推高黄金", 
     " 黄金期货大涨2.26%收于4482.30美元/盎司，WTI原油回调2.15%至82.76美元/桶。", 
     "中东地缘局势悬而未决，黄金作为终极避险资产飙升；而油价在前日暴涨后小幅整固。"),
    ("美联储货币政策前景扑朔迷离，9月加息争议不减", 
     "10年期美债收益率微降至4.682%，比特币震荡小跌0.23%至63,537.56美元。", 
     "Warsh的“去前瞻指引”增加波动性，劳动力市场的疲软使得9月加息概率依然在40-50%拉锯。")
]

y = 0.77
for title, val, note in events:
    ax.text(0.06, y, f"• {title}", fontproperties=prop, fontsize=10.5, color='#334155', fontweight='bold')
    ax.text(0.06, y-0.030, f"  焦点: {val}\n  研判: {note}", fontproperties=prop, fontsize=9.0, color='#64748b')
    y -= 0.11

# Right Side: Market Indicators & Assets
ax.text(0.55, 0.86, "▌ 核心资产前一交易日表现", fontproperties=prop, fontsize=12, fontweight='bold', color='#0f172a')

asset_data = [
    ("纳斯达克指数 (NASDAQ)", "26,601.14", "周三: +0.59% 🔴"),
    ("标普 500 指数 (S&P 500)", "7,748.50", "周三: +0.26% 🔴"),
    ("道琼斯工业指数 (DJIA)", "53,770.27", "周三: -0.04% 🟢"),
    ("费城半导体指数 (SOX)", "12,399.38", "周三: +1.68% 🔴"),
    ("罗素 2000 指数 (Russell 2000)", "3,045.48", "周三: +0.60% 🔴"),
    ("上证指数 (SSEC)", "3,946.68", "周三: +0.32% 🔴"),
    ("深圳成指 (SZCOMP)", "14,414.43", "周三: +1.09% 🔴"),
    ("COMEX 黄金期货 (Gold)", "4,482.30 美元", "周三: +2.26% 🔴"),
    ("WTI 原油期货 (WTI)", "82.76 美元", "周三: -2.15% 🟢"),
    ("10年期美债收益率 (US10Y)", "4.682%", "周三: -0.1BP 🟢"),
    ("比特币 (BTC)", "63,537.56 美元", "周三: -0.23% 🟢")
]

y_right = 0.77
for title, price, perf in asset_data:
    ax.text(0.57, y_right, title, fontproperties=prop, fontsize=10.0, color='#334155', fontweight='bold')
    
    color = '#ef4444' if '🔴' in perf else '#10b981'
    clean_perf = perf.replace('🟢', '').replace('🔴', '')
    
    # Draw price
    ax.text(0.57, y_right-0.024, f"现价: {price}", fontproperties=prop, fontsize=9.0, color='#475569')
    # Draw performance
    ax.text(0.71, y_right-0.024, f"|  {clean_perf}", fontproperties=prop, fontsize=9.0, fontweight='bold', color=color)
    
    y_right -= 0.050

plt.tight_layout()
output_path = "images/charts/2026-08-13-morning.png"
plt.savefig(output_path, dpi=300, bbox_inches='tight', facecolor=fig.get_facecolor())
plt.close()
print(f"Chart saved to {output_path}")
