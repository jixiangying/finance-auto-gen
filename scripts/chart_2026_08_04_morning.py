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
ax.text(0.05, 0.93, "【地缘退潮油价暴跌避险回落，PMI强劲超预期美股暴涨】(2026/08/04 周二早报)", fontproperties=prop, fontsize=14, fontweight='bold', color='#1e293b')
ax.axhline(y=0.88, xmin=0.04, xmax=0.96, color='#cbd5e1', linewidth=1.5)

# Left Side: Key Market Events / Outlook
ax.text(0.06, 0.82, "▌ 今日市场核心动向要闻", fontproperties=prop, fontsize=12, fontweight='bold', color='#0f172a')

events = [
    ("特朗普叫停对伊军事打击，布油暴跌近8%", "布伦特原油暴跌至$83.27/桶，回吐中东局势的全部地缘溢价", "地缘冲突降温推动全球避险情绪快速回落，油价暴跌"),
    ("美国7月ISM制造业PMI录得55.6%强劲超预期", "较6月的53.3%大超预期，创2022年5月以来的最高点，制造业强劲", "就业指数33个月来首次实现扩张，缓解衰退担忧，刺激风险偏好"),
    ("通胀担忧大幅退潮，美债收益率自高点回落", "10年期美债收益率下滑7个基点至4.68%，收益率从高位显著回落", "油价大跌极大缓和了二次通胀风险，美债抛压有所减轻"),
    ("美股迎来全面反弹，三大股指集体飙升", "纳指大涨2.13%，标普涨1.48%，道指涨1.32%创下历史新高", "科技成长及顺周期板块共振爆发，降息预期回暖促成估值修复")
]

y = 0.72
for title, val, note in events:
    ax.text(0.08, y, title, fontproperties=prop, fontsize=10.5, color='#334155', fontweight='bold')
    ax.text(0.08, y-0.035, f"{val}\n{note}", fontproperties=prop, fontsize=9.0, color='#64748b')
    y -= 0.11

# Right Side: Market Indicators & Assets
ax.text(0.56, 0.82, "▌ 核心资产最新价格与变化", fontproperties=prop, fontsize=12, fontweight='bold', color='#0f172a')

asset_data = [
    ("纳斯达克综合指数 (NASDAQ)", "25,913.90 (日: +2.13% / 科技暴涨) 🔴", "科技巨头引领风险偏好回归，成长股全线反弹"),
    ("标普 500 指数 (S&P 500)", "7,600.50 (日: +1.48% / 突破关口) 🔴", "成分股普遍上涨，估值修复行情向多板块延伸"),
    ("道琼斯工业指数 (DJIA)", "53,178.41 (日: +1.32% / 历史新高) 🔴", "传统蓝筹与大金融力挺大盘，创下历史新高"),
    ("布伦特原油期货 (Brent)", "$83.27 (日: -7.60% / 地缘退潮) 🟢", "特朗普叫停军事打击转向外交，地缘溢价骤减"),
    ("COMEX 黄金期货 (Gold)", "$4,033.70 (日: -1.53% / 避险降温) 🟢", "风险资产回暖，避险资金从贵金属市场流出"),
    ("10年期美债收益率 (US10Y)", "4.68% (日: -7BP / 通胀降温) 🟢", "油价重挫缓和二次通胀恐慌，收益率高位回落"),
    ("比特币 (BTC)", "$64,000.00 (日: +4.49% / 风险回升) 🔴", "跟随美股反弹重回6.4万美元，忽略黑客袭扰")
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
output_path = "images/charts/2026-08-04-morning.png"
plt.savefig(output_path, dpi=300, bbox_inches='tight', facecolor=fig.get_facecolor())
plt.close()
print(f"Chart saved to {output_path}")
