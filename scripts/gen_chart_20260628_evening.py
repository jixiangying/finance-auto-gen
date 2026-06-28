import matplotlib.pyplot as plt
import matplotlib.font_manager as fm
import os

output_dir = "images/charts/"
os.makedirs(output_dir, exist_ok=True)

font_path = "/System/Library/Fonts/STHeiti Medium.ttc"
if not os.path.exists(font_path):
    font_path = "/System/Library/Fonts/PingFang.ttc"
prop = fm.FontProperties(fname=font_path)

fig, ax = plt.subplots(figsize=(10, 6.5))
fig.patch.set_facecolor('#f8fafc')
ax.set_facecolor('#ffffff')
ax.set_xlim(0, 1)
ax.set_ylim(0, 1)
ax.axis('off')

# Title
ax.text(0.05, 0.93, "【新周财经焦点与资产关键位置】(2026/06/28 周日晚)", fontproperties=prop, fontsize=14, fontweight='bold', color='#1e293b')
ax.axhline(y=0.88, xmin=0.04, xmax=0.96, color='#cbd5e1', linewidth=1.5)

# Left Side: Weekend Events
ax.text(0.06, 0.82, "▌ 周末重磅事件与产业动态", fontproperties=prop, fontsize=12, fontweight='bold', color='#0f172a')

weekend_events = [
    ("5月工业企业利润", "同比 +21.1% (AI/电子利润飙升103.9%)", "显示科技制造业强劲"),
    ("三星十年半导体规划", "拟投入 1000 万亿韩元 (约7200亿美元)", "重点布局代工与先进制程"),
    ("核聚变关键装置国产化", "实现100%自主可控，多项指标创世界纪录", "硬科技及能源赛道新风口"),
    ("地缘与贸易新动向", "美空袭伊朗目标；日启动与南方共同市场谈判", "关注中东卢塞恩谈判签署")
]

y = 0.74
for title, val, note in weekend_events:
    ax.text(0.08, y, title, fontproperties=prop, fontsize=11, color='#334155', fontweight='bold')
    ax.text(0.08, y-0.045, f"{val}  |  {note}", fontproperties=prop, fontsize=10, color='#64748b')
    y -= 0.10

# Right Side: Market Indicators & Assets
ax.text(0.56, 0.82, "▌ 核心资产收盘与关键位置", fontproperties=prop, fontsize=12, fontweight='bold', color='#0f172a')

asset_data = [
    ("伦敦金现", "$4,032.00 / 盎司", "短线承压，考验4000支撑"),
    ("WTI原油期货", "$69.23 / 桶", "跌破70关口，静待地缘溢价退潮"),
    ("比特币 (BTC)", "$59,893.00", "跌破60k防线，测试买方支撑"),
    ("美元指数 (DXY)", "101.36", "探底回升，仍处13个月高位附近")
]

y_right = 0.74
for title, val, comment in asset_data:
    ax.text(0.58, y_right, title, fontproperties=prop, fontsize=11, color='#334155', fontweight='bold')
    ax.text(0.58, y_right-0.045, f"{val} ({comment})", fontproperties=prop, fontsize=10, color='#64748b')
    y_right -= 0.10

plt.tight_layout()
output_path = os.path.join(output_dir, "2026-06-28-evening.png")
plt.savefig(output_path, dpi=300, bbox_inches='tight')
plt.close()
print(f"Chart saved to {output_path}")
