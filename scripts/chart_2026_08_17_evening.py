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

fig, ax = plt.subplots(figsize=(14.0, 9.0))
fig.patch.set_facecolor('#f8fafc')
ax.set_facecolor('#ffffff')
ax.set_xlim(0, 1)
ax.set_ylim(0, 1)
ax.axis('off')

# Title
ax.text(0.04, 0.95, "【A股科创板暴涨超4%，港股收复2.5万大关，央行隔夜逆回购启动】(2026/08/17 周一收盘报)", fontproperties=prop, fontsize=13, fontweight='bold', color='#1e293b')
ax.axhline(y=0.90, xmin=0.03, xmax=0.97, color='#cbd5e1', linewidth=1.5)

# Left Side: Key Market Events
ax.text(0.05, 0.86, "▌ 今日全球宏观与核心事件复盘", fontproperties=prop, fontsize=12, fontweight='bold', color='#0f172a')

events = [
    ("A股与港股全线大涨，科创50指数暴涨超4%",
     "科创50收盘暴涨4.14%领跑；上证指数大涨1.41%收报3982.65点",
     "创业板指大涨3.14%；成长风格明显占优，科技创新与国产算力链表现活跃"),
    ("港股强劲反弹收复25,000点，结束四连跌行情",
     "恒指收盘大涨1.34%报25453.23点；恒生科技指数大涨1.58%报4782.03点",
     "中芯国际引领芯片与大科技板块爆发，有色金属、集运及光通信板块亮眼"),
    ("央行出重拳维稳，启动连续三天隔夜逆回购操作",
     "8月17至19日持续开展隔夜逆回购操作，每日额度不超过6000亿元",
     "优化短端流动性调控，引导利率平稳运行；货币政策重申'以我为主'"),
    ("美元指数持续走弱，在岸离岸人民币升破6.74创三年半新高",
     "美元指数逼近5月低点，人民币大涨对新兴市场资产构成系统性利好",
     "美国零售数据疲软令美联储9月加息预期回落，提振全球科技股与大宗")
]

y = 0.77
for title, val, note in events:
    ax.text(0.06, y, title, fontproperties=prop, fontsize=10.5, color='#334155', fontweight='bold')
    ax.text(0.06, y-0.030, val, fontproperties=prop, fontsize=9.0, color='#64748b')
    ax.text(0.06, y-0.054, note, fontproperties=prop, fontsize=8.5, color='#94a3b8')
    y -= 0.115

# Right Side: Market Indicators & Assets
ax.text(0.54, 0.86, "▌ 核心资产今日表现 (8月17日 周一收盘)", fontproperties=prop, fontsize=12, fontweight='bold', color='#0f172a')

asset_data = [
    ("上证指数 (SSEC)", "收盘: 3982.65 / 涨跌: +1.41% 🔴", "大涨55.48点，做多热情高涨，成交额显著放大"),
    ("深证成指 (SZI)", "收盘: 14704.27 / 涨跌: +2.44% 🔴", "上涨349.97点，科技与消费题材迎来全面回暖"),
    ("创业板指 (CHINEXT)", "收盘: 3740.16 / 涨跌: +3.14% 🔴", "大涨超3%，高弹性成长赛道全线走强，个股活跃"),
    ("科创50 (STAR50)", "收盘: 1788.85 / 涨跌: +4.14% 🔴", "大涨超4%领涨两市，国产芯片与自主可控题材爆发"),
    ("恒生指数 (HSI)", "收盘: 25453.23 / 涨跌: +1.34% 🔴", "上涨336.38点，收复2.5万大关，大市值互联网领涨"),
    ("恒生科技 (HSTECH)", "收盘: 4782.03 / 涨跌: +1.58% 🔴", "大涨74.41点，中芯国际大涨引领科技板块反弹"),
    ("COMEX黄金 (Gold)", "现货: 4395-4400 / 涨跌: 温和上涨 🔴", "降息预期重燃叠加避险情绪，金价维持高位强势"),
    ("布伦特原油 (Brent)", "现货: 89.00 / 涨跌: 维持高位 🔴", "中东地缘不确定性高企，霍尔木兹海峡局势提供溢价"),
    ("比特币 (BTC)", "现货: 63,400 / 涨跌: +0.50% 🔴", "在6.3万美元上方震荡，地缘风险导致杠杆爆仓增加"),
]

y_right = 0.77
for title, val, comment in asset_data:
    ax.text(0.56, y_right, title, fontproperties=prop, fontsize=10.0, color='#334155', fontweight='bold')
    if '🔴' in val and '🟢' in val:
        color = '#ef4444' if val.count('🔴') > val.count('🟢') else '#10b981'
    elif '🔴' in val:
        color = '#ef4444'
    elif '🟢' in val:
        color = '#10b981'
    else:
        color = '#334155'
    clean_val = val.replace('🟢', '').replace('🔴', '')
    ax.text(0.56, y_right-0.028, clean_val, fontproperties=prop, fontsize=8.5, fontweight='bold', color=color)
    ax.text(0.56, y_right-0.050, comment, fontproperties=prop, fontsize=8.0, color='#64748b')
    y_right -= 0.078

# Footer
ax.axhline(y=0.04, xmin=0.03, xmax=0.97, color='#e2e8f0', linewidth=1.0)
ax.text(0.05, 0.02, "数据来源：东方财富、新浪财经、外汇管理局 | 本报告仅供参考，不构成投资建议", fontproperties=prop, fontsize=8.5, color='#94a3b8')

plt.tight_layout()
output_path = "images/charts/2026-08-17-evening.png"
plt.savefig(output_path, dpi=300, bbox_inches='tight', facecolor=fig.get_facecolor())
plt.close()
print(f"Chart saved to {output_path}")
