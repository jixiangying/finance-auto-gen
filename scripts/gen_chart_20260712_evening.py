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
ax.text(0.05, 0.93, "【新周财经焦点与资产关键位置】(2026/07/12 周日晚)", fontproperties=prop, fontsize=14, fontweight='bold', color='#1e293b')
ax.axhline(y=0.88, xmin=0.04, xmax=0.96, color='#cbd5e1', linewidth=1.5)

# Left Side: Weekend Events
ax.text(0.06, 0.82, "▌ 周末重磅事件与产业动态", fontproperties=prop, fontsize=12, fontweight='bold', color='#0f172a')

weekend_events = [
    ("国常会部署加快算力网", "系统推进数字中国建设，加快通信网与算力网建设", "攻关关键软硬件，全链条推动产业化规模发展"),
    ("中医药“十五五”规划获批", "国务院原则同意振兴规划，完善传承创新机制", "传承与产业化双轮驱动，推动中医药走向世界"),
    ("两部门对氦气临时禁止出口", "商务部、海关总署公告，对氦气实施临时管制", "强化关键稀有资源安全管控，自7月起施行"),
    ("全国电力用电负荷创新高", "7月10日负荷达15.18亿千瓦，今年首创历史新高", "高温天气与数字算力新兴产业用电需求共振")
]

y = 0.73
for title, val, note in weekend_events:
    ax.text(0.08, y, title, fontproperties=prop, fontsize=11, color='#334155', fontweight='bold')
    ax.text(0.08, y-0.045, f"{val}  |  {note}", fontproperties=prop, fontsize=9.5, color='#64748b')
    y -= 0.10

# Right Side: Market Indicators & Assets
ax.text(0.56, 0.82, "▌ 核心资产收盘与关键位置", fontproperties=prop, fontsize=12, fontweight='bold', color='#0f172a')

asset_data = [
    ("沪深 300 (CSI 300)", "4,780.79 (-1.27% / -2.00%)", "天量筹码换手重组，业绩期关注真龙头"),
    ("纳斯达克 (Nasdaq)", "26,281.61 (+1.74% / +0.29%)", "SK Hynix首日大涨13%提振AI算力链"),
    ("比特币 (BTC)", "$63,220.69 (+2.82% / +1.56%)", "震荡收复关口，降息流动性预期回暖"),
    ("现货黄金 (Gold)", "$4,119.56 (-0.12% / -0.06%)", "高位蓄势震荡，静待下周美国CPI决战")
]

y_right = 0.73
for title, val, comment in asset_data:
    ax.text(0.58, y_right, title, fontproperties=prop, fontsize=11, color='#334155', fontweight='bold')
    ax.text(0.58, y_right-0.045, f"{val} ({comment})", fontproperties=prop, fontsize=9.5, color='#64748b')
    y_right -= 0.10

plt.tight_layout()
output_path = "images/charts/2026-07-12-evening.png"
plt.savefig(output_path, dpi=300, bbox_inches='tight', facecolor=fig.get_facecolor())
plt.close()
print(f"Chart saved to {output_path}")
