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
ax.text(0.04, 0.94, "【新周展望：周内将迎美CPI终极通胀考验，A股人形机器人首股网上申购】(2026/08/10 周一早报)", fontproperties=prop, fontsize=14, fontweight='bold', color='#1e293b')
ax.axhline(y=0.90, xmin=0.03, xmax=0.97, color='#cbd5e1', linewidth=1.5)

# Left Side: Key Market Events / Outlook
ax.text(0.05, 0.84, "▌ 本周全球市场核心博弈逻辑与前瞻", fontproperties=prop, fontsize=12, fontweight='bold', color='#0f172a')

events = [
    ("美国本周公布重磅通胀与零售，美联储下步行动风向标", 
     "周二公布零售销售（恐怖数据），周三公布CPI，周五公布PCE物价指数。", 
     "非农就业大跌后，若通胀数据同步回落，则美联储9月利率决议降息预期将进一步砸实。"),
    ("具身智能/人形机器人开启新热潮，宇树科技今日网上申购", 
     "“人形机器人第一股”宇树科技于8月10日科创板开启申购，发行价150.80元。", 
     "除了宇树科技，港股亦有超50家具身智能相关企业排队，18C特专科技规则大放异彩。"),
    ("长鑫科技今日起正式纳入MSCI，半导体板块迎被动配置资金", 
     "长鑫科技正式被纳入MSCI中国全股票指数，并于今日（8月10日）生效。", 
     "预计将吸引大批追踪指数的海外被动基金流入，提振国内存储芯片及半导体板块人气。"),
    ("北京购房限制再度松绑，非京籍五环内限购社保/个税2年改1年", 
     "自8月8日起执行新政，非京籍家庭五环内购房门槛降为“1年”。", 
     "政策持续释放暖意，有利于提振北京及全国重点城市二手房和新房市场的成交预期。"),
    ("全球宽松交易周初高位整固，金价创半年最佳，加密市场站稳6.5万", 
     "黄金全周大涨7.2%收于$4384.59，BTC收复6.5万关口后周一平稳运行。", 
     "非农就业降温激发的降息流动性逻辑正被各市场消化，本周重点关注情绪整固。")
]

y = 0.75
for title, val, note in events:
    ax.text(0.06, y, f"• {title}", fontproperties=prop, fontsize=10.5, color='#334155', fontweight='bold')
    ax.text(0.06, y-0.030, f"  焦点: {val}\n  研判: {note}", fontproperties=prop, fontsize=9.0, color='#64748b')
    y -= 0.105

# Right Side: Market Indicators & Assets
ax.text(0.55, 0.84, "▌ 核心资产前一交易日/全周表现", fontproperties=prop, fontsize=12, fontweight='bold', color='#0f172a')

asset_data = [
    ("纳斯达克指数 (NASDAQ)", "26,690.62", "周五: +1.30%  |  全周: +5.20% 🔴"),
    ("标普 500 指数 (S&P 500)", "7,757.64", "周五: +0.62%  |  全周: +3.60% 🔴"),
    ("道琼斯工业指数 (DJIA)", "54,036.93", "周五: +0.28%  |  全周: +3.00% 🔴"),
    ("上证指数 (SSEC)", "3,940.04", "周五: +1.02%  |  全周: +2.81% 🔴"),
    ("沪深 300 指数 (CSI300)", "4,694.44", "周五: +0.93%  |  全周: +1.28% 🔴"),
    ("恒生指数 (HSI)", "25,668.03", "周五: +0.54%  |  全周: -0.84% 🟢"),
    ("COMEX 黄金期货 (Gold)", "$4,384.59", "周五: +1.94%  |  全周: +7.20% 🔴"),
    ("布伦特原油期货 (Brent)", "$83.24", "周五: +0.90%  |  全周: -7.50% 🟢"),
    ("10年期美债收益率 (US10Y)", "4.640%", "周五: -4.0BP   |  全周: -8.6BP 🟢"),
    ("比特币 (BTC)", "$64,905.53", "周五: +0.75%  |  全周: +3.10% 🔴")
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
output_path = "images/charts/2026-08-10-morning.png"
plt.savefig(output_path, dpi=300, bbox_inches='tight', facecolor=fig.get_facecolor())
plt.close()
print(f"Chart saved to {output_path}")
