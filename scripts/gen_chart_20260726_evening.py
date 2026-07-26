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
ax.text(0.05, 0.93, "【新周宏观展望与核心资产盘点】(2026/07/26 周日晚报)", fontproperties=prop, fontsize=14, fontweight='bold', color='#1e293b')
ax.axhline(y=0.88, xmin=0.04, xmax=0.96, color='#cbd5e1', linewidth=1.5)

# Left Side: Key Market Events
ax.text(0.06, 0.82, "▌ 周末重磅事件与政策汇总", fontproperties=prop, fontsize=12, fontweight='bold', color='#0f172a')

events = [
    ("央行保持政策宽松，加强实体流动性注入", "7月24日大额净投放5000亿MLF，保持流动性充裕", "强调金融稳健性并定向加大对文旅等产业支持力度"),
    ("多国央行将决议，新周进入“超级议息周”", "美联储、日本央行、英国央行等下周将密集议息", "市场关注下半年降息节奏与汇率波动边际扰动"),
    ("美股超级财报周来临，科技巨头估值待检", "苹果、微软、亚马逊及Meta等多家科技龙头披露财报", "高额资本开支（CapEx）回报率是多空博弈的核心关键"),
    ("国内中报披露进入密集期，资金偏向防御", "A股与港股周五调整，多板块缩量，市场静待方向", "随着7月政治局会议将至，市场博弈政策定调与业绩兑现")
]

y = 0.72
for title, val, note in events:
    ax.text(0.08, y, title, fontproperties=prop, fontsize=10.5, color='#334155', fontweight='bold')
    ax.text(0.08, y-0.035, f"{val}\n{note}", fontproperties=prop, fontsize=9.0, color='#64748b')
    y -= 0.11

# Right Side: Market Indicators & Assets
ax.text(0.56, 0.82, "▌ 核心资产表现与周末行情", fontproperties=prop, fontsize=12, fontweight='bold', color='#0f172a')

asset_data = [
    ("上证指数 (SSEC)", "3,814.20 (周五: -1.61%) 🟢", "两市大幅震荡回调，市场防守情绪升温"),
    ("创业板指 (CHINEXT)", "3,480.87 (周五: -2.65%) 🟢", "高位成长股获利回吐，估值结构性修正"),
    ("恒生指数 (HSI)", "24,963.23 (周五: -0.98%) 🟢", "跌破二万五千点关口，受外围科技拖累"),
    ("富时中国 A50 期货", "15,033.00 (周五: -1.31%) 🟢", "期指全周偏弱，受外部政策风险溢价抑制"),
    ("纳斯达克指数 (NASDAQ)", "24,975.82 (周五: -0.64%) 🟢", "科技龙头继续承压，CapEx周期忧虑发酵"),
    ("现货黄金 (Spot Gold)", "$4,052.98 (周五: +0.08%) 🔴", "金价在4050美元关口企稳，避险需求仍存"),
    ("比特币 (BTC)", "$64,450.00 (周末: +0.35%) 🔴", "展现出加密资产的避险轮动，小幅回暖"),
    ("WTI 原油期货 (WTI Oil)", "$90.47 (周五: -1.87%) 🟢", "地缘局势盘整，油价跌破91美元关口")
]

y_right = 0.72
for title, val, comment in asset_data:
    ax.text(0.58, y_right, title, fontproperties=prop, fontsize=10.5, color='#334155', fontweight='bold')
    color = '#ef4444' if '🔴' in val else '#10b981'
    clean_val = val.replace('🟢', '').replace('🔴', '')
    
    # Draw value with corresponding color
    ax.text(0.58, y_right-0.030, clean_val, fontproperties=prop, fontsize=9.0, fontweight='bold', color=color)
    # Draw comment next to it
    val_width = len(clean_val) * 0.007 + 0.025
    ax.text(0.58 + val_width, y_right-0.030, f"|  {comment}", fontproperties=prop, fontsize=9.0, color='#64748b')
    
    y_right -= 0.052

plt.tight_layout()
output_path = "images/charts/2026-07-26-evening.png"
plt.savefig(output_path, dpi=300, bbox_inches='tight', facecolor=fig.get_facecolor())
plt.close()
print(f"Chart saved to {output_path}")
