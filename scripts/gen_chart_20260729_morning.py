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
ax.text(0.05, 0.93, "【核心行情复盘与重要要闻】(2026/07/29 周三早报)", fontproperties=prop, fontsize=14, fontweight='bold', color='#1e293b')
ax.axhline(y=0.88, xmin=0.04, xmax=0.96, color='#cbd5e1', linewidth=1.5)

# Left Side: Key Market Events
ax.text(0.06, 0.82, "▌ 核心解读与市场逻辑", fontproperties=prop, fontsize=12, fontweight='bold', color='#0f172a')

events = [
    ("半导体板块跌势蔓延，纳指收跌", "美/亚半导体及AI链出现持续回调", "担忧高Capex支出及获利回吐，英伟达等硬科技股走低"),
    ("原油价格延续跌势，避险情绪升温", "美伊外交和谈预期继续打压溢价", "布油收跌2.47%至$83.75，大幅缓和二次通胀担忧"),
    ("美联储议息会议今日将公布决议", "市场预计维持3.5%-3.75%利率不变", "将关注沃什新闻发布会，对后续降息指引成为关键"),
    ("道指大涨逾500点，防御股受捧", "强劲财报（如可口可乐）支撑传统板块", "美债收益率回落至4.60%，资金由成长股轮动至价值股")
]

y = 0.72
for title, val, note in events:
    ax.text(0.08, y, title, fontproperties=prop, fontsize=10.5, color='#334155', fontweight='bold')
    ax.text(0.08, y-0.035, f"{val}\n{note}", fontproperties=prop, fontsize=9.0, color='#64748b')
    y -= 0.11

# Right Side: Market Indicators & Assets
ax.text(0.56, 0.82, "▌ 核心资产最新行情与表现", fontproperties=prop, fontsize=12, fontweight='bold', color='#0f172a')

asset_data = [
    ("纳斯达克综合指数 (NASDAQ)", "24,876.91 (日: -0.22%) 🟢", "半导体板块承压拖累，AI科技股延续弱势"),
    ("标普 500 指数 (S&P 500)", "7,428.78 (日: +0.21%) 🔴", "传统防御板块上扬，对冲了部分科技股跌幅"),
    ("道琼斯工业指数 (DJIA)", "52,747.32 (日: +1.03%) 🔴", "蓝筹股财报稳健，避险与防守资金大量流入"),
    ("布伦特原油期货 (Brent)", "$83.75 (日: -2.47%) 🟢", "美伊外交谈判预期升温，地缘溢价快速回吐"),
    ("COMEX 黄金期货 (Gold)", "$4,028.70 (日: -1.12%) 🟢", "美联储决议前夕，短线多头抛售打压金价"),
    ("10年期美债收益率 (US10Y)", "4.60% (日: -4BP) 🟢", "通胀预期随油价回落，美债收益率实现三连跌"),
    ("比特币 (BTC)", "$63,550.00 (日: -2.23%) 🟢", "遭遇Pre-FOMC去风险抛盘，多头爆仓情绪受挫")
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
output_path = "images/charts/2026-07-29-morning.png"
plt.savefig(output_path, dpi=300, bbox_inches='tight', facecolor=fig.get_facecolor())
plt.close()
print(f"Chart saved to {output_path}")
