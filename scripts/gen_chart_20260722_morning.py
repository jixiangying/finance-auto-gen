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
ax.text(0.05, 0.93, "【美股隔夜收盘与全球核心资产反弹】(2026/07/22 周三早)", fontproperties=prop, fontsize=14, fontweight='bold', color='#1e293b')
ax.axhline(y=0.88, xmin=0.04, xmax=0.96, color='#cbd5e1', linewidth=1.5)

# Left Side: Macro & News
ax.text(0.06, 0.82, "▌ 隔夜宏观要闻与政策动态", fontproperties=prop, fontsize=12, fontweight='bold', color='#0f172a')

events = [
    ("美股三大指数强劲反弹，芯片半导体领涨", "纳指涨1.29%，标普涨0.89%，道指涨0.74%", "半导体指数大涨超5%，市场情绪自前期回调中修复"),
    ("美光股价暴涨超10%，重返万亿市值关口", "美光大涨10-12%，英伟达等AI龙头大涨", "数据中心需求维持强劲，存储芯片价格预期大涨"),
    ("中东地缘冲突提振避险，黄金与原油齐升", "WTI原油报$83.23/桶，黄金收盘创历史新高", "中东局势未见降温，避险资金支持黄金大涨1.57%"),
    ("美债收益率上升，美联储FOMC决议备受瞩目", "10年期美债收益率升至4.63% (+4bp)", "核心通胀担忧仍存，美联储官员维持高利率鹰派判定")
]

y = 0.73
for title, val, note in events:
    ax.text(0.08, y, title, fontproperties=prop, fontsize=11, color='#334155', fontweight='bold')
    ax.text(0.08, y-0.045, f"{val}  |  {note}", fontproperties=prop, fontsize=9.5, color='#64748b')
    y -= 0.10

# Right Side: Market Indicators & Assets
ax.text(0.56, 0.82, "▌ 核心资产隔夜收盘数据", fontproperties=prop, fontsize=12, fontweight='bold', color='#0f172a')

asset_data = [
    ("道琼斯指数 (Dow Jones)", "52,224.64", "+385.38 (+0.74%)", "#dc2626"),
    ("标普 500 (S&P 500)", "7,509.20", "+65.92 (+0.89%)", "#dc2626"),
    ("纳斯达克 (Nasdaq)", "25,837.21", "+329.13 (+1.29%)", "#dc2626"),
    ("WTI 原油 (Crude Oil)", "$83.23/桶", "+0.91%", "#dc2626"),
    ("COMEX 黄金 (Gold)", "$4,071.10/盎司", "+1.57%", "#dc2626"),
    ("比特币 (Bitcoin)", "$65,199.44", "+0.69%", "#dc2626")
]

y_right = 0.73
for title, price, change, color in asset_data:
    ax.text(0.58, y_right, title, fontproperties=prop, fontsize=10.5, color='#334155', fontweight='bold')
    ax.text(0.58, y_right-0.04, f"{price}  ", fontproperties=prop, fontsize=9.5, color='#475569')
    ax.text(0.82, y_right-0.04, f"{change}", fontproperties=prop, fontsize=9.5, color=color, fontweight='bold')
    y_right -= 0.075

plt.tight_layout()
output_path = "images/charts/2026-07-22-morning.png"
plt.savefig(output_path, dpi=300, bbox_inches='tight', facecolor=fig.get_facecolor())
plt.close()
print(f"Chart saved to {output_path}")
