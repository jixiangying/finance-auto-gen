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
ax.text(0.05, 0.93, "【A股收盘普涨三大股指红盘与港股反弹走强】(2026/07/23 周四晚)", fontproperties=prop, fontsize=14, fontweight='bold', color='#1e293b')
ax.axhline(y=0.88, xmin=0.04, xmax=0.96, color='#cbd5e1', linewidth=1.5)

# Left Side: Macro & News
ax.text(0.06, 0.82, "▌ 核心解读与政策要闻", fontproperties=prop, fontsize=12, fontweight='bold', color='#0f172a')

events = [
    ("A股三大指数午后翻红，个股呈现普涨态势", "超4200只个股上涨，成交额缩量至2.2万亿元", "半导体等科技股调整致科创50疲软收跌3.78%"),
    ("电网设备与新能源大涨，有色电力板块活跃", "碳酸锂期货大涨带动锂矿拉升，电网油气全天强势", "避险情绪与大宗涨价逻辑主导行业板块领涨"),
    ("港股强势回升涨超1%，恒指重回2.5万关口", "恒生指数收涨1.00%报25141.64点", "昨日大跌后资金逢低戏纳，市场信心温和修复"),
    ("宏观政策与外资看好，资金环境保持适度宽松", "财政金融协同促内需，央行维持逆回购利率1.40%", "花旗调高中国股票至“超配”，上海发布科创金融新政")
]

y = 0.73
for title, val, note in events:
    ax.text(0.08, y, title, fontproperties=prop, fontsize=11, color='#334155', fontweight='bold')
    ax.text(0.08, y-0.045, f"{val}  |  {note}", fontproperties=prop, fontsize=9.5, color='#64748b')
    y -= 0.10

# Right Side: Market Indicators & Assets
ax.text(0.56, 0.82, "▌ 核心资产收盘数据 (A/港股)", fontproperties=prop, fontsize=12, fontweight='bold', color='#0f172a')

asset_data = [
    ("上证指数 (Shanghai)", "3,876.78", "+0.25%", "#dc2626"),
    ("深证成指 (Shenzhen)", "14,123.31", "+0.44%", "#dc2626"),
    ("创业板指 (ChiNext)", "3,575.52", "+0.25%", "#dc2626"),
    ("科创50 (STAR 50)", "1,044.36", "-3.78%", "#16a34a"),
    ("恒生指数 (Hang Seng)", "25,141.64", "+1.00%", "#dc2626"),
    ("恒生科技 (HS Tech)", "4,698.57", "+0.65%", "#dc2626")
]

y_right = 0.73
for title, price, change, color in asset_data:
    ax.text(0.58, y_right, title, fontproperties=prop, fontsize=10.5, color='#334155', fontweight='bold')
    ax.text(0.58, y_right-0.04, f"{price}  ", fontproperties=prop, fontsize=9.5, color='#475569')
    ax.text(0.82, y_right-0.04, f"{change}", fontproperties=prop, fontsize=9.5, color=color, fontweight='bold')
    y_right -= 0.075

plt.tight_layout()
output_path = "images/charts/2026-07-23-evening.png"
plt.savefig(output_path, dpi=300, bbox_inches='tight', facecolor=fig.get_facecolor())
plt.close()
print(f"Chart saved to {output_path}")
