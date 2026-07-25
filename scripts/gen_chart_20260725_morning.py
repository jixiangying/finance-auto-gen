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
ax.text(0.05, 0.93, "【科技股拖累纳指收跌，布油回撤黄金微涨】(2026/07/25 周六早)", fontproperties=prop, fontsize=14, fontweight='bold', color='#1e293b')
ax.axhline(y=0.88, xmin=0.04, xmax=0.96, color='#cbd5e1', linewidth=1.5)

# Left Side: Macro & News
ax.text(0.06, 0.82, "▌ 隔夜宏观要闻与政策动态", fontproperties=prop, fontsize=12, fontweight='bold', color='#0f172a')

events = [
    ("美股分化科技拖累纳指，Intel领跌半导体", "纳指跌0.64%，标普微涨0.05%，道指涨0.46%", "科技巨头AI开支回报担忧持续，Intel大跌6.5%领跌半导体板块"),
    ("多头高位获利了结，布伦特原油回撤近4%", "布油大跌3.88%报$96.78/桶，跌破百元关口", "中东局势虽紧但避险溢价有所消退，前期多头高位了结导致油价大跌"),
    ("10年期美债收益率微降，黄金低位微幅企稳", "COMEX黄金收于$4064.10/盎司 (+0.52%)", "美债收益率高位回落至4.69%，黄金在整数关口附近获得买盘支撑"),
    ("关税阴霾与避险情绪交织，比特币震荡走弱", "比特币下跌1.56%收于$65,052.00", "特朗普加征关税政策影响全球风险情绪，BTC短期承压下挫")
]

y = 0.73
for title, val, note in events:
    ax.text(0.08, y, title, fontproperties=prop, fontsize=11, color='#334155', fontweight='bold')
    ax.text(0.08, y-0.045, f"{val}  |  {note}", fontproperties=prop, fontsize=9.5, color='#64748b')
    y -= 0.10

# Right Side: Market Indicators & Assets
ax.text(0.56, 0.82, "▌ 核心资产隔夜收盘数据", fontproperties=prop, fontsize=12, fontweight='bold', color='#0f172a')

asset_data = [
    ("道琼斯指数 (Dow Jones)", "51,947.25", "+235.60 (+0.46%)", "#dc2626"),
    ("标普 500 (S&P 500)", "7,411.98", "+3.68 (+0.05%)", "#dc2626"),
    ("纳斯达克 (Nasdaq)", "24,975.82", "-161.87 (-0.64%)", "#16a34a"),
    ("布伦特原油 (Brent Crude)", "$96.78/桶", "-3.88%", "#16a34a"),
    ("COMEX 黄金 (Gold)", "$4,064.10/盎司", "+0.52%", "#dc2626"),
    ("比特币 (Bitcoin)", "$65,052.00", "-1.56%", "#16a34a")
]

y_right = 0.73
for title, price, change, color in asset_data:
    ax.text(0.58, y_right, title, fontproperties=prop, fontsize=10.5, color='#334155', fontweight='bold')
    ax.text(0.58, y_right-0.04, f"{price}  ", fontproperties=prop, fontsize=9.5, color='#475569')
    ax.text(0.82, y_right-0.04, f"{change}", fontproperties=prop, fontsize=9.5, color=color, fontweight='bold')
    y_right -= 0.075

plt.tight_layout()
output_path = "images/charts/2026-07-25-morning.png"
plt.savefig(output_path, dpi=300, bbox_inches='tight', facecolor=fig.get_facecolor())
plt.close()
print(f"Chart saved to {output_path}")
