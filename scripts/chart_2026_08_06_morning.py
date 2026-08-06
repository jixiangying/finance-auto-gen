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
ax.text(0.05, 0.93, "【美股分化：道指新高五连阳，SpaceX与AMD绩后大跌拖累纳指】(2026/08/06 周四早报)", fontproperties=prop, fontsize=14, fontweight='bold', color='#1e293b')
ax.axhline(y=0.88, xmin=0.04, xmax=0.96, color='#cbd5e1', linewidth=1.5)

# Left Side: Key Market Events / Outlook
ax.text(0.06, 0.82, "▌ 今日市场核心动向要闻", fontproperties=prop, fontsize=12, fontweight='bold', color='#0f172a')

events = [
    ("大摩与高盛聚焦AI物理基建，预期超8000亿开支强劲", "机构策略指出，AI算力在物理端（电力、设备）订单爆满，硬件回流预期高", "高额资本投入及强劲的企业盈利弹性，令美国经济实现2%软着陆概率抬升"),
    ("SpaceX首份季报大额CapEx致亏，股价绩后暴跌逾10%", "SpaceX录得\$7.8B营收，但AI基建开支高达\$15.8B；lock-up解禁期临近施压股价", "AMD虽营收激增50%但因利润率展望保守以及Musk采购竞品芯片，股价跌近6%"),
    ("避险需求与地缘不确定性共振，黄金暴涨超4%", "COMEX黄金暴涨至\$4,258.48/盎司创下历史新高；原油震荡反弹至\$80.35/桶", "谈判虽有进展但海峡货轮袭扰等突发事件不断，促避险买盘全力推升金价"),
    ("美股大市现明显获利回吐，道指独秀再创历史新高", "道指收涨0.5%报54,349.12点；纳指回吐0.8%，标普微调0.2%至7,723.55点", "防御性板块与蓝筹抗跌，科技成长股在大涨后遭遇选择性抛售")
]

y = 0.72
for title, val, note in events:
    ax.text(0.08, y, title, fontproperties=prop, fontsize=10.5, color='#334155', fontweight='bold')
    ax.text(0.08, y-0.035, f"{val}\n{note}", fontproperties=prop, fontsize=9.0, color='#64748b')
    y -= 0.11

# Right Side: Market Indicators & Assets
ax.text(0.56, 0.82, "▌ 核心资产最新价格与变化", fontproperties=prop, fontsize=12, fontweight='bold', color='#0f172a')

asset_data = [
    ("纳斯达克综合指数 (NASDAQ)", "26,363.44 (日: -0.80% / 科技回调) 🟢", "SpaceX与半导体拖累成长股，纳指绩后走弱"),
    ("标普 500 指数 (S&P 500)", "7,723.55 (日: -0.20% / 获利回吐) 🟢", "在大市触及高点后微调，避险资产受捧"),
    ("道琼斯工业指数 (DJIA)", "54,349.12 (日: +0.50% / 五连阳新高) 🔴", "地缘悲观情绪退潮，蓝筹股获强力买盘"),
    ("布伦特原油期货 (Brent)", "\$80.35 (日: +1.25% / 震荡反弹) 🔴", "海峡突发袭扰事件再现，油价跌深反弹站上80"),
    ("COMEX 黄金期货 (Gold)", "\$4,258.48 (日: +4.43% / 狂飙新高) 🔴", "中东局势反复，避险资金强劲流入促金价暴涨"),
    ("10年期美债收益率 (US10Y)", "4.616% (日: -1.4BP / 窄幅震荡) 🟢", "油价反弹使通胀担忧未除，收益率自高点微降"),
    ("比特币 (BTC)", "\$64,939.10 (日: +1.32% / 稳步上扬) 🔴", "ETF资金流入持续，BTC突破6.49万关口")
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
output_path = "images/charts/2026-08-06-morning.png"
plt.savefig(output_path, dpi=300, bbox_inches='tight', facecolor=fig.get_facecolor())
plt.close()
print(f"Chart saved to {output_path}")
