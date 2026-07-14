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

fig, ax = plt.subplots(figsize=(10.5, 6.8))
fig.patch.set_facecolor('#f8fafc')
ax.set_facecolor('#ffffff')
ax.set_xlim(0, 1)
ax.set_ylim(0, 1)
ax.axis('off')

# Title
ax.text(0.05, 0.93, "【核心行情信息图】(2026/07/14 周二晚)", fontproperties=prop, fontsize=14, fontweight='bold', color='#1e293b')
ax.axhline(y=0.88, xmin=0.04, xmax=0.96, color='#cbd5e1', linewidth=1.5)

# Left Side: Key Market Events
ax.text(0.06, 0.82, "▌ 核心事件与市场逻辑", fontproperties=prop, fontsize=12, fontweight='bold', color='#0f172a')

events = [
    ("亚太市场企稳回暖深V反弹", "韩国KOSPI收涨0.73%，三星/海力士大涨超3.3%", "韩股大跌后回暖带动亚太情绪，A股午后大举逆弹"),
    ("“十五五”扩大消费与健康规划印发", "两大“十五五”规划批复，首提创新药为新质生产力核心", "持续巩固资本市场向好态势，增加财产性收入提振内需"),
    ("中报预告密集披露业绩为王", "7月15日中报强制预增披露前夕，绩优股现涨停潮", "资金加速向有业绩支撑的硬科技及绩优成长板块聚集"),
    ("科技与硬赛道爆发领涨两市", "PCB、通信设备、CPO、存储芯片等大涨", "创业板指大涨3.43%，电子、电力设备等板块涨幅居前")
]

y = 0.73
for title, val, note in events:
    ax.text(0.08, y, title, fontproperties=prop, fontsize=11, color='#334155', fontweight='bold')
    ax.text(0.08, y-0.045, f"{val}  |  {note}", fontproperties=prop, fontsize=9.5, color='#64748b')
    y -= 0.10

# Right Side: Asset Indicators
ax.text(0.56, 0.82, "▌ 核心资产收盘表现", fontproperties=prop, fontsize=12, fontweight='bold', color='#0f172a')

asset_data = [
    ("上证指数 (SSEC)", "3,967.13 (+1.36%)", "午后走强，成功收复3900点大关"),
    ("深证成指 (SDEC)", "14,924.87 (+2.77%)", "指数大涨近2.8%，全场超4200只个股上涨"),
    ("创业板指 (CHINEXT)", "3,851.14 (+3.43%)", "半导体、光模块及科技成长大爆发"),
    ("恒生指数 (HSI)", "24,340.73 (+0.52%)", "港股跟随反弹，三大指数集体收涨")
]

y_right = 0.73
for title, val, comment in asset_data:
    ax.text(0.58, y_right, title, fontproperties=prop, fontsize=11, color='#334155', fontweight='bold')
    ax.text(0.58, y_right-0.045, f"{val} ({comment})", fontproperties=prop, fontsize=9.5, color='#64748b')
    y_right -= 0.10

plt.tight_layout()
output_path = "images/charts/2026-07-14-evening.png"
plt.savefig(output_path, dpi=300, bbox_inches='tight', facecolor=fig.get_facecolor())
plt.close()
print(f"Chart saved to {output_path}")
