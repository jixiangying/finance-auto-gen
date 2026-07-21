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
ax.text(0.05, 0.93, "【A股科技股V型狂飙攻防与港股分化】(2026/07/21 周二晚)", fontproperties=prop, fontsize=14, fontweight='bold', color='#1e293b')
ax.axhline(y=0.88, xmin=0.04, xmax=0.96, color='#cbd5e1', linewidth=1.5)

# Left Side: Macro & News
ax.text(0.06, 0.82, "▌ 核心解读与政策要闻", fontproperties=prop, fontsize=12, fontweight='bold', color='#0f172a')

events = [
    ("半导体产业链狂飙，创业板暴涨超7%", "存储芯片、CPO、先进封装掀起涨停潮", "科创50飙升10.73%，市场交投极其火爆"),
    ("两市成交放量至2.96万亿元", "较前一交易日大幅增量放量", "场外与超跌资金猛烈回流，个股普涨"),
    ("证监会密集座谈，国资增持托底信心", "听取市场建议，诚通国新大额增持", "政策组合拳落地，市场底部共识进一步夯实"),
    ("央行保持7月LPR不变，资金流动性充裕", "1年期3.0%，5年期以上3.5%", "维护银行息差与定力，跨两地债券合作深化")
]

y = 0.73
for title, val, note in events:
    ax.text(0.08, y, title, fontproperties=prop, fontsize=11, color='#334155', fontweight='bold')
    ax.text(0.08, y-0.045, f"{val}  |  {note}", fontproperties=prop, fontsize=9.5, color='#64748b')
    y -= 0.10

# Right Side: Market Indicators & Assets
ax.text(0.56, 0.82, "▌ 核心资产收盘数据 (A/港股)", fontproperties=prop, fontsize=12, fontweight='bold', color='#0f172a')

asset_data = [
    ("上证指数 (Shanghai)", "3,864.37", "+1.79%", "#dc2626"),
    ("深证成指 (Shenzhen)", "14,264.29", "+4.81%", "#dc2626"),
    ("创业板指 (ChiNext)", "3,685.97", "+7.05%", "#dc2626"),
    ("科创50 (STAR 50)", "1,128.50", "+10.73%", "#dc2626"),
    ("恒生指数 (Hang Seng)", "25,132.29", "-0.04%", "#16a34a"),
    ("恒生科技 (HS Tech)", "4,814.83", "+1.32%", "#dc2626")
]

y_right = 0.73
for title, price, change, color in asset_data:
    ax.text(0.58, y_right, title, fontproperties=prop, fontsize=10.5, color='#334155', fontweight='bold')
    ax.text(0.58, y_right-0.04, f"{price}  ", fontproperties=prop, fontsize=9.5, color='#475569')
    ax.text(0.82, y_right-0.04, f"{change}", fontproperties=prop, fontsize=9.5, color=color, fontweight='bold')
    y_right -= 0.075

plt.tight_layout()
output_path = "images/charts/2026-07-21-evening.png"
plt.savefig(output_path, dpi=300, bbox_inches='tight', facecolor=fig.get_facecolor())
plt.close()
print(f"Chart saved to {output_path}")
