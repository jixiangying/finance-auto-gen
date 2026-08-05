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
ax.text(0.05, 0.93, "【美伊谈判现曙光地缘退潮，PLTR与CAT业绩暴击美股狂飙】(2026/08/05 周三早报)", fontproperties=prop, fontsize=14, fontweight='bold', color='#1e293b')
ax.axhline(y=0.88, xmin=0.04, xmax=0.96, color='#cbd5e1', linewidth=1.5)

# Left Side: Key Market Events / Outlook
ax.text(0.06, 0.82, "▌ 今日市场核心动向要闻", fontproperties=prop, fontsize=12, fontweight='bold', color='#0f172a')

events = [
    ("Bessent暗示霍尔木兹危机降温，布油大跌逾4%", "美财长称有望今明达成妥协以复航，油价重挫4.70%至$79.36/桶", "地缘溢价退潮使市场避险情绪迅速降温，原油跌破80美元"),
    ("Palantir与卡特彼勒业绩暴击，AI基建需求坚挺", "PLTR营收增93%大超预期；CAT营收破200亿创新高、发电设备订单翻倍", "AI及数据中心强劲资本开支对实体经济及科技股形成强支撑"),
    ("通胀担忧大幅缓解，10年期美债收益率大降6BP", "收益率回落至4.62%，油价大跌缓解二次通胀恐慌，美债收益率走低", "高估值科技股的利率压力显著减轻，为美股上涨扫清估值障碍"),
    ("美股三大股指全面狂欢，标普与道指同创历史新高", "纳指暴涨2.59%领涨，标普涨1.79%，道指飙升1.71%突破54,000大关", "财报利好与地缘局势降温共振，市场呈现强劲的多头普涨特征")
]

y = 0.72
for title, val, note in events:
    ax.text(0.08, y, title, fontproperties=prop, fontsize=10.5, color='#334155', fontweight='bold')
    ax.text(0.08, y-0.035, f"{val}\n{note}", fontproperties=prop, fontsize=9.0, color='#64748b')
    y -= 0.11

# Right Side: Market Indicators & Assets
ax.text(0.56, 0.82, "▌ 核心资产最新价格与变化", fontproperties=prop, fontsize=12, fontweight='bold', color='#0f172a')

asset_data = [
    ("纳斯达克综合指数 (NASDAQ)", "26,584.99 (日: +2.59% / 科技暴涨) 🔴", "PLTR亮眼财报引爆科技成长股，纳指强势领涨"),
    ("标普 500 指数 (S&P 500)", "7,736.52 (日: +1.79% / 历史新高) 🔴", "标普首度攻克7700关口，科技与基建板块领涨"),
    ("道琼斯工业指数 (DJIA)", "54,085.88 (日: +1.71% / 历史新高) 🔴", "CAT业绩狂飙带飞蓝筹，道指大涨逾900点创纪录"),
    ("布伦特原油期货 (Brent)", "$79.36 (日: -4.70% / 跌破八十) 🟢", "Bessent称美伊谈妥在即，霍尔木兹海峡地缘危机降温"),
    ("COMEX 黄金期货 (Gold)", "$4,095.40 (日: +1.53% / 避险抗跌) 🔴", "虽避险退潮，但油轮袭击事件仍支撑金价维持强韧"),
    ("10年期美债收益率 (US10Y)", "4.62% (日: -6BP / 通胀降温) 🟢", "油价重挫大幅缓解通胀恐惧，收益率自高位大跌"),
    ("比特币 (BTC)", "$64,267.64 (日: +0.42% / 高位震荡) 🔴", "跟随美股大市震荡走高，硬件钱包安全担忧限制涨幅")
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
output_path = "images/charts/2026-08-05-morning.png"
plt.savefig(output_path, dpi=300, bbox_inches='tight', facecolor=fig.get_facecolor())
plt.close()
print(f"Chart saved to {output_path}")
