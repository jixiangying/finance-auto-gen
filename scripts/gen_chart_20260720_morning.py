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
ax.text(0.05, 0.93, "【新周财经焦点与资产关键位置】(2026/07/20 周一早)", fontproperties=prop, fontsize=14, fontweight='bold', color='#1e293b')
ax.axhline(y=0.88, xmin=0.04, xmax=0.96, color='#cbd5e1', linewidth=1.5)

# Left Side: Weekend & Overnight Events
ax.text(0.06, 0.82, "▌ 周末及晨间重磅事件与动态", fontproperties=prop, fontsize=12, fontweight='bold', color='#0f172a')

events = [
    ("“国家队”增持护盘与座谈会召开", "证监会7月20日召开座谈会听取意见", "国新/诚通大举买入数百亿央企股与ETF平抑波动"),
    ("电池消费税政策发布与调整", "财政部自9月起调整税率，免征钠/固/光伏税", "促进行业绿色转型，钠电池与固态电池迎利好"),
    ("中东局势加剧导致原油再度高开", "美伊海湾冲突频发，霍尔木兹航道风险拉满", "WTI原油周一晨间跳涨突破84美元/桶"),
    ("美股超级财报周拉开序幕", "谷歌、特斯拉、英特尔等科技巨头本周放榜", "AI估值挤水分进入深水区，检验商业闭环能力")
]

y = 0.73
for title, val, note in events:
    ax.text(0.08, y, title, fontproperties=prop, fontsize=11, color='#334155', fontweight='bold')
    ax.text(0.08, y-0.045, f"{val}  |  {note}", fontproperties=prop, fontsize=9.5, color='#64748b')
    y -= 0.10

# Right Side: Market Indicators & Assets
ax.text(0.56, 0.82, "▌ 核心资产位置与今日关注", fontproperties=prop, fontsize=12, fontweight='bold', color='#0f172a')

asset_data = [
    ("沪深 300 (CSI 300)", "4,529.10 (上周五:-3.60%)", "证监会座谈会及国家队重磅护盘防范两融风险"),
    ("纳斯达克 (Nasdaq)", "25,520.24 (上周五:-1.41%)", "上周五费半跌入熊市，本周超级财报季开启检验"),
    ("WTI原油 (Crude Oil)", "$84.10 (今日晨:+1.95%)", "中东局势升级影响航运通道，原油持续上攻"),
    ("中国 LPR 利率 (LPR)", "1年期3.00% / 5年期3.50%", "7月20日最新报价出炉，连续第14个月维持不变")
]

y_right = 0.73
for title, val, comment in asset_data:
    ax.text(0.58, y_right, title, fontproperties=prop, fontsize=11, color='#334155', fontweight='bold')
    ax.text(0.58, y_right-0.045, f"{val} ({comment})", fontproperties=prop, fontsize=9.5, color='#64748b')
    y_right -= 0.10

plt.tight_layout()
output_path = "images/charts/2026-07-20-morning.png"
plt.savefig(output_path, dpi=300, bbox_inches='tight', facecolor=fig.get_facecolor())
plt.close()
print(f"Chart saved to {output_path}")
