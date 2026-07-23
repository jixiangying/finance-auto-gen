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
ax.text(0.05, 0.93, "【隔夜美股震荡走低与地缘溢价推升黄金油价】(2026/07/23 周四早)", fontproperties=prop, fontsize=14, fontweight='bold', color='#1e293b')
ax.axhline(y=0.88, xmin=0.04, xmax=0.96, color='#cbd5e1', linewidth=1.5)

# Left Side: Macro & News
ax.text(0.06, 0.82, "▌ 隔夜宏观要闻与政策动态", fontproperties=prop, fontsize=12, fontweight='bold', color='#0f172a')

events = [
    ("美股冲高回落集体收跌，科技股分化调整", "纳指跌0.57%，标普跌0.14%，道指跌0.01%", "财报前软件板块疲软抵消芯片板块微涨，市场以观望为主"),
    ("中东地缘局势担忧升级，国际油价飙涨约3%", "WTI原油报$86.83/桶 (+2.95%)，创逾六周高位", "中东冲突威胁能源供应，地缘溢价驱动油价大幅反弹"),
    ("避险买盘推动，黄金价格延续强势再创新高", "COMEX黄金收于$4083.70/盎司 (+0.31%)", "避险黄金受中东地缘紧绷及通胀担忧支持表现出众"),
    ("美债收益率升至两月高位，比特币区间震荡", "10年期美债收益率升至4.66% (+3bp)", "通胀压力压制科技成长股估值，BTC持稳于6.58万美元左右")
]

y = 0.73
for title, val, note in events:
    ax.text(0.08, y, title, fontproperties=prop, fontsize=11, color='#334155', fontweight='bold')
    ax.text(0.08, y-0.045, f"{val}  |  {note}", fontproperties=prop, fontsize=9.5, color='#64748b')
    y -= 0.10

# Right Side: Market Indicators & Assets
ax.text(0.56, 0.82, "▌ 核心资产隔夜收盘数据", fontproperties=prop, fontsize=12, fontweight='bold', color='#0f172a')

asset_data = [
    ("道琼斯指数 (Dow Jones)", "52,218.58", "-6.06 (-0.01%)", "#16a34a"),
    ("标普 500 (S&P 500)", "7,498.96", "-10.24 (-0.14%)", "#16a34a"),
    ("纳斯达克 (Nasdaq)", "25,690.90", "-146.31 (-0.57%)", "#16a34a"),
    ("WTI 原油 (Crude Oil)", "$86.83/桶", "+2.95%", "#dc2626"),
    ("COMEX 黄金 (Gold)", "$4,083.70/盎司", "+0.31%", "#dc2626"),
    ("比特币 (Bitcoin)", "$65,850.00", "+1.00%", "#dc2626")
]

y_right = 0.73
for title, price, change, color in asset_data:
    ax.text(0.58, y_right, title, fontproperties=prop, fontsize=10.5, color='#334155', fontweight='bold')
    ax.text(0.58, y_right-0.04, f"{price}  ", fontproperties=prop, fontsize=9.5, color='#475569')
    ax.text(0.82, y_right-0.04, f"{change}", fontproperties=prop, fontsize=9.5, color=color, fontweight='bold')
    y_right -= 0.075

plt.tight_layout()
output_path = "images/charts/2026-07-23-morning.png"
plt.savefig(output_path, dpi=300, bbox_inches='tight', facecolor=fig.get_facecolor())
plt.close()
print(f"Chart saved to {output_path}")
