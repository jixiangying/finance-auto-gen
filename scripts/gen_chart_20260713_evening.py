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
ax.text(0.05, 0.93, "【核心行情信息图】(2026/07/13 周一晚)", fontproperties=prop, fontsize=14, fontweight='bold', color='#1e293b')
ax.axhline(y=0.88, xmin=0.04, xmax=0.96, color='#cbd5e1', linewidth=1.5)

# Left Side: Key Market Events
ax.text(0.06, 0.82, "▌ 核心事件与市场逻辑", fontproperties=prop, fontsize=12, fontweight='bold', color='#0f172a')

events = [
    ("地缘政治局势突发升级", "美伊空中打击导致局势恶化，原油跳涨超3%", "油价上涨加剧通胀担忧，直接打压风险偏好"),
    ("海外科技股暴跌情绪传导", "韩国KOSPI指数暴跌熔断，三星/海力士重挫", "情绪传导至A股，半导体/存储芯片大面积跌停"),
    ("高位获利抛售与拥挤出逃", "被动元件风华高科等大盘股业绩预警后跌停", "资金高位获利回吐，存量博弈下筹码结构松动"),
    ("中药与红利避险逆势上扬", "中医药“十五五”规划获批，资金寻找避风港", "银行板块稳指数，中药板块陇神戎发等大面积涨停")
]

y = 0.73
for title, val, note in events:
    ax.text(0.08, y, title, fontproperties=prop, fontsize=11, color='#334155', fontweight='bold')
    ax.text(0.08, y-0.045, f"{val}  |  {note}", fontproperties=prop, fontsize=9.5, color='#64748b')
    y -= 0.10

# Right Side: Asset Indicators
ax.text(0.56, 0.82, "▌ 核心资产收盘表现", fontproperties=prop, fontsize=12, fontweight='bold', color='#0f172a')

asset_data = [
    ("上证指数 (SSEC)", "3,913.79 (-2.06%)", "缩量大跌，失守4000点关口"),
    ("深证成指 (SDEC)", "14,522.85 (-3.48%)", "科技成长股遭重挫，行业全线大跌"),
    ("创业板指 (CHINEXT)", "3,723.52 (-3.10%)", "前期热门芯片、商业航天拖累指数"),
    ("恒生指数 (HSI)", "24,213.72 (+0.16%)", "逆势微涨，银行与红利支撑大盘")
]

y_right = 0.73
for title, val, comment in asset_data:
    ax.text(0.58, y_right, title, fontproperties=prop, fontsize=11, color='#334155', fontweight='bold')
    ax.text(0.58, y_right-0.045, f"{val} ({comment})", fontproperties=prop, fontsize=9.5, color='#64748b')
    y_right -= 0.10

plt.tight_layout()
output_path = "images/charts/2026-07-13-evening.png"
plt.savefig(output_path, dpi=300, bbox_inches='tight', facecolor=fig.get_facecolor())
plt.close()
print(f"Chart saved to {output_path}")
