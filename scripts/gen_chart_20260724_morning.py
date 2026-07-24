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
ax.text(0.05, 0.93, "【AI资本开支忧虑与中东地缘冲突导致美股大跌】(2026/07/24 周五早)", fontproperties=prop, fontsize=14, fontweight='bold', color='#1e293b')
ax.axhline(y=0.88, xmin=0.04, xmax=0.96, color='#cbd5e1', linewidth=1.5)

# Left Side: Macro & News
ax.text(0.06, 0.82, "▌ 隔夜宏观要闻与政策动态", fontproperties=prop, fontsize=12, fontweight='bold', color='#0f172a')

events = [
    ("美股大跌科技股领跌，AI资本开支引发担忧", "纳指暴跌2.15%，标普跌1.21%，道指跌1.00%", "Alphabet及特斯拉大增CapEx引发回报周期担忧，重挫科技股"),
    ("红海袭击推高地缘溢价，布伦特原油冲破100美元", "布油大涨超5%报$100.69/桶，创5月以来新高", "中东局势紧绷，红海油轮受袭威胁运输安全，油价飙升加剧通胀担忧"),
    ("美元走强与美债收益率攀升，黄金高位回撤", "COMEX黄金收于$4043.00/盎司 (-1.93%)", "10年期美债收益率飙升至52周高点与美元走强对黄金产生压制"),
    ("美债收益率创52周新高，比特币微跌震荡", "10年期美债收益率飙至4.70% (创52周新高)", "通胀压力与紧缩预期升温，高利率压制估值，BTC回落至6.60万美元左右")
]

y = 0.73
for title, val, note in events:
    ax.text(0.08, y, title, fontproperties=prop, fontsize=11, color='#334155', fontweight='bold')
    ax.text(0.08, y-0.045, f"{val}  |  {note}", fontproperties=prop, fontsize=9.5, color='#64748b')
    y -= 0.10

# Right Side: Market Indicators & Assets
ax.text(0.56, 0.82, "▌ 核心资产隔夜收盘数据", fontproperties=prop, fontsize=12, fontweight='bold', color='#0f172a')

asset_data = [
    ("道琼斯指数 (Dow Jones)", "51,695.57", "-523.01 (-1.00%)", "#16a34a"),
    ("标普 500 (S&P 500)", "7,408.30", "-90.66 (-1.21%)", "#16a34a"),
    ("纳斯达克 (Nasdaq)", "25,137.69", "-553.21 (-2.15%)", "#16a34a"),
    ("布伦特原油 (Brent Crude)", "$100.69/桶", "+5.13%", "#dc2626"),
    ("COMEX 黄金 (Gold)", "$4,043.00/盎司", "-1.93%", "#16a34a"),
    ("比特币 (Bitcoin)", "$66,083.46", "-0.64%", "#16a34a")
]

y_right = 0.73
for title, price, change, color in asset_data:
    ax.text(0.58, y_right, title, fontproperties=prop, fontsize=10.5, color='#334155', fontweight='bold')
    ax.text(0.58, y_right-0.04, f"{price}  ", fontproperties=prop, fontsize=9.5, color='#475569')
    ax.text(0.82, y_right-0.04, f"{change}", fontproperties=prop, fontsize=9.5, color=color, fontweight='bold')
    y_right -= 0.075

plt.tight_layout()
output_path = "images/charts/2026-07-24-morning.png"
plt.savefig(output_path, dpi=300, bbox_inches='tight', facecolor=fig.get_facecolor())
plt.close()
print(f"Chart saved to {output_path}")
