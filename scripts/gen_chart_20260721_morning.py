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
ax.text(0.05, 0.93, "【美股隔夜收盘与全球核心资产分化】(2026/07/21 周二早)", fontproperties=prop, fontsize=14, fontweight='bold', color='#1e293b')
ax.axhline(y=0.88, xmin=0.04, xmax=0.96, color='#cbd5e1', linewidth=1.5)

# Left Side: Macro & News
ax.text(0.06, 0.82, "▌ 隔夜宏观要闻与政策动态", fontproperties=prop, fontsize=12, fontweight='bold', color='#0f172a')

events = [
    ("美股小幅收跌，财报周前夕交投谨慎", "道指跌0.6%，标普跌0.2%，纳指微跌0.1%", "科技巨头二季报放榜前夕市场重拾观望情绪"),
    ("中东局势提振油价，地缘避险升温", "美伊海湾对峙风险攀升，中东溢价持续", "WTI原油攀升至82.48-83.00美元/桶高位"),
    ("美联储通胀立场偏鹰，美债收益率反弹", "10年期美债收益率回升至 4.59%", "维持Higher-for-Longer判定，降息节点预期推迟"),
    ("机构二季报强劲，看好长期AI资本开支", "高盛/摩根士丹利发布财报", "强调定价权与自给资金增长，坚定看好AI主线")
]

y = 0.73
for title, val, note in events:
    ax.text(0.08, y, title, fontproperties=prop, fontsize=11, color='#334155', fontweight='bold')
    ax.text(0.08, y-0.045, f"{val}  |  {note}", fontproperties=prop, fontsize=9.5, color='#64748b')
    y -= 0.10

# Right Side: Market Indicators & Assets
ax.text(0.56, 0.82, "▌ 核心资产隔夜收盘数据", fontproperties=prop, fontsize=12, fontweight='bold', color='#0f172a')

asset_data = [
    ("道琼斯指数 (Dow Jones)", "51,839.26", "-307.16 (-0.60%)", "#16a34a"),
    ("标普 500 (S&P 500)", "7,443.28", "-14.41 (-0.20%)", "#16a34a"),
    ("纳斯达克 (Nasdaq)", "25,508.07", "-12.17 (-0.10%)", "#16a34a"),
    ("WTI 原油 (Crude Oil)", "$82.48/桶", "+1.20%", "#dc2626"),
    ("COMEX 黄金 (Gold)", "$4,008.00/盎司", "+0.30%", "#dc2626"),
    ("比特币 (Bitcoin)", "$64,750.00", "-1.50%", "#16a34a")
]

y_right = 0.73
for title, price, change, color in asset_data:
    ax.text(0.58, y_right, title, fontproperties=prop, fontsize=10.5, color='#334155', fontweight='bold')
    ax.text(0.58, y_right-0.04, f"{price}  ", fontproperties=prop, fontsize=9.5, color='#475569')
    ax.text(0.82, y_right-0.04, f"{change}", fontproperties=prop, fontsize=9.5, color=color, fontweight='bold')
    y_right -= 0.075

plt.tight_layout()
output_path = "images/charts/2026-07-21-morning.png"
plt.savefig(output_path, dpi=300, bbox_inches='tight', facecolor=fig.get_facecolor())
plt.close()
print(f"Chart saved to {output_path}")
