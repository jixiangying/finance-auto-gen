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
ax.text(0.05, 0.93, "【新周宏观前瞻与核心资产表现】(2026/07/27 周一早报)", fontproperties=prop, fontsize=14, fontweight='bold', color='#1e293b')
ax.axhline(y=0.88, xmin=0.04, xmax=0.96, color='#cbd5e1', linewidth=1.5)

# Left Side: Key Market Events
ax.text(0.06, 0.82, "▌ 新一周市场核心关注要闻", fontproperties=prop, fontsize=12, fontweight='bold', color='#0f172a')

events = [
    ("美联储7月议息会议（美东7月29日）", "市场预期利率区间维持3.50%-3.75%不变", "沃什主持决议，关税生效下通胀言论是焦点"),
    ("超级科技巨头财报决战周（周三/四）", "微软、Meta、苹果、亚马逊密集披露财报", "下半年AI资本支出指引是估值防线或催化剂"),
    ("美国核心数据与通胀大考（周防/五）", "将公布二季度GDP初值及6月PCE物价指数", "若PCE粘性显现，二次通胀风险将浇灭降息预期"),
    ("英国/日本央行政策决议（周四/五）", "关注BoE利率动向及BoJ国债购买与汇率表态", "全球央行流动性回收预期对高估值资产构成压力")
]

y = 0.72
for title, val, note in events:
    ax.text(0.08, y, title, fontproperties=prop, fontsize=10.5, color='#334155', fontweight='bold')
    ax.text(0.08, y-0.035, f"{val}\n{note}", fontproperties=prop, fontsize=9.0, color='#64748b')
    y -= 0.11

# Right Side: Market Indicators & Assets
ax.text(0.56, 0.82, "▌ 核心资产最新行情与全周表现", fontproperties=prop, fontsize=12, fontweight='bold', color='#0f172a')

asset_data = [
    ("纳斯达克综合指数 (NASDAQ)", "24,975.82 (周: -2.10% / 日: -0.64%) 🟢", "科技板块AI估值重塑，英特尔暴跌拖累指数"),
    ("标普 500 指数 (S&P 500)", "7,411.98 (周: -0.60% / 日: +0.05%) 🟢", "防御板块与红利资产坚挺，指数小幅平收"),
    ("道琼斯工业指数 (DJIA)", "51,947.25 (周: -0.40% / 日: +0.46%) 🟢", "大金融与传统价值股护盘，表现相对抗跌"),
    ("布伦特原油期货 (Brent)", "$96.78 (周: +9.50% / 日: -3.88%) 🔴", "中东红海地缘危机，布油周中一度突破百元"),
    ("COMEX 黄金期货 (Gold)", "$4,064.10 (周: -1.80% / 日: +0.52%) 🟢", "美债收益率飙升，黄金高位获利盘大面积离场"),
    ("10年期美债收益率 (US10Y)", "4.69% (周: +13.6BP / 日: -1BP) 🔴", "关税政策正式生效，二次通胀预期推升收益率"),
    ("比特币 (BTC)", "$64,318.25 (周: +1.80% / 24时: -1.13%) 🔴", "加密市场避险情绪回落，面临上方均线压制")
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
output_path = "images/charts/2026-07-27-morning.png"
plt.savefig(output_path, dpi=300, bbox_inches='tight', facecolor=fig.get_facecolor())
plt.close()
print(f"Chart saved to {output_path}")
