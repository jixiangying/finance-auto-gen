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
ax.text(0.05, 0.93, "【核心行情复盘与重要要闻】(2026/07/30 周四早报)", fontproperties=prop, fontsize=14, fontweight='bold', color='#1e293b')
ax.axhline(y=0.88, xmin=0.04, xmax=0.96, color='#cbd5e1', linewidth=1.5)

# Left Side: Key Market Events
ax.text(0.06, 0.82, "▌ 核心解读与市场逻辑", fontproperties=prop, fontsize=12, fontweight='bold', color='#0f172a')

events = [
    ("中东局势骤然升级，地缘避险爆发", "伊朗向约旦美军发射弹道导弹均被拦截", "美沙随即发起空袭报复，地缘危机急剧蔓延"),
    ("美伊谈判破裂，原油报复暴涨超7%", "导弹事件与油轮遭袭重创供应预期", "布油狂飙至$90.25/桶，地缘溢价再次拉满"),
    ("美联储按兵不动，但现鹰派分裂", "联储维持利率不变，却有三名委员偏向加息", "高通胀风险下美联储内部鹰派异议打击市场情绪"),
    ("避险情绪肆虐，美股遭遇千点暴跌", "鹰派分裂与通胀风险引发滞胀忧虑", "道指大跌超1150点（-2.19%），三大股指普跌")
]

y = 0.72
for title, val, note in events:
    ax.text(0.08, y, title, fontproperties=prop, fontsize=10.5, color='#334155', fontweight='bold')
    ax.text(0.08, y-0.035, f"{val}\n{note}", fontproperties=prop, fontsize=9.0, color='#64748b')
    y -= 0.11

# Right Side: Market Indicators & Assets
ax.text(0.56, 0.82, "▌ 核心资产最新行情与表现", fontproperties=prop, fontsize=12, fontweight='bold', color='#0f172a')

asset_data = [
    ("纳斯达克综合指数 (NASDAQ)", "24,442.94 (日: -1.74%) 🟢", "地缘大乱与加息预期抬头，科技大盘遭遇抛售"),
    ("标普 500 指数 (S&P 500)", "7,316.15 (日: -1.52%) 🟢", "油价飙升与美债收益率反弹，大盘普遍下挫"),
    ("道琼斯工业指数 (DJIA)", "51,594.14 (日: -2.19%) 🟢", "避险无处藏身，传统成份蓝筹板块遭暴烈砸盘"),
    ("布伦特原油期货 (Brent)", "$90.25 (日: +7.76%) 🔴", "伊朗导弹袭击美军，中东海运供给威胁重燃"),
    ("COMEX 黄金期货 (Gold)", "$4,075.95 (日: +1.17%) 🔴", "地缘全面冲突爆发，强烈激发黄金避险配置"),
    ("10年期美债收益率 (US10Y)", "4.621% (日: +2BP) 🔴", "鹰派分裂与油价暴涨重燃通胀担忧，收益率上行"),
    ("比特币 (BTC)", "$63,944.00 (日: +0.62%) 🔴", "虽承压但受到避险资金部分分流支撑，微涨防守")
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
output_path = "images/charts/2026-07-30-morning.png"
plt.savefig(output_path, dpi=300, bbox_inches='tight', facecolor=fig.get_facecolor())
plt.close()
print(f"Chart saved to {output_path}")
