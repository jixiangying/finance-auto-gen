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
ax.text(0.05, 0.93, "【核心行情复盘与重要要闻】(2026/07/28 周二早报)", fontproperties=prop, fontsize=14, fontweight='bold', color='#1e293b')
ax.axhline(y=0.88, xmin=0.04, xmax=0.96, color='#cbd5e1', linewidth=1.5)

# Left Side: Key Market Events
ax.text(0.06, 0.82, "▌ 核心解读与市场逻辑", fontproperties=prop, fontsize=12, fontweight='bold', color='#0f172a')

events = [
    ("美伊地缘局势降温，原油暴跌", "美伊局势出现缓和停火预期", "布油重挫逾11%回落至$85.87，极大缓解二次通胀忧虑"),
    ("美联储议息会议今日开启", "7月利率决议将于29日公布", "预期维持3.5%-3.75%不变，关注沃什的鹰鸽表态"),
    ("科技巨头财报前夕资金轮动", "纳斯达克微跌0.18%科技股回吐", "Nvidia等AI链回落，资金流入大金融与传统价值板块"),
    ("宏观数据密集出炉临近", "本周将有二季度GDP与6月PCE", "油价大跌缓解前期美债压力，美债收益率回落至4.64%")
]

y = 0.72
for title, val, note in events:
    ax.text(0.08, y, title, fontproperties=prop, fontsize=10.5, color='#334155', fontweight='bold')
    ax.text(0.08, y-0.035, f"{val}\n{note}", fontproperties=prop, fontsize=9.0, color='#64748b')
    y -= 0.11

# Right Side: Market Indicators & Assets
ax.text(0.56, 0.82, "▌ 核心资产最新行情与表现", fontproperties=prop, fontsize=12, fontweight='bold', color='#0f172a')

asset_data = [
    ("纳斯达克综合指数 (NASDAQ)", "24,932.08 (日: -0.18%) 🟢", "科技股财报前谨慎，半导体AI算力板块承压"),
    ("标普 500 指数 (S&P 500)", "7,413.18 (日: +0.02%) 🔴", "大金融与消费股走强抵消科技板块跌幅"),
    ("道琼斯工业指数 (DJIA)", "52,210.08 (日: +0.51%) 🔴", "受益于油价重挫与价值股轮动，指数明显上涨"),
    ("布伦特原油期货 (Brent)", "$85.87 (日: -11.27%) 🟢", "美伊冲突局势缓和，原油多头离场引发重挫"),
    ("COMEX 黄金期货 (Gold)", "$4,074.50 (日: +0.26%) 🔴", "美债收益率回落，黄金价格高位获得买盘支撑"),
    ("10年期美债收益率 (US10Y)", "4.64% (日: -5BP) 🟢", "通胀担忧随油价回落降温，收益率高位缓释"),
    ("比特币 (BTC)", "$65,002.50 (日: +1.06%) 🔴", "加密市场情绪有所复苏，价格收复6.5万美元")
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
output_path = "images/charts/2026-07-28-morning.png"
plt.savefig(output_path, dpi=300, bbox_inches='tight', facecolor=fig.get_facecolor())
plt.close()
print(f"Chart saved to {output_path}")
