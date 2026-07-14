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

fig, ax = plt.subplots(figsize=(10.8, 7.2))
fig.patch.set_facecolor('#f8fafc')
ax.set_facecolor('#ffffff')
ax.set_xlim(0, 1)
ax.set_ylim(0, 1)
ax.axis('off')

# Title
ax.text(0.05, 0.93, "【核心行情信息图】(2026/07/14 周二早报)", fontproperties=prop, fontsize=14, fontweight='bold', color='#1e293b')
ax.axhline(y=0.88, xmin=0.04, xmax=0.96, color='#cbd5e1', linewidth=1.5)

# Left Side: Overnight Key Events
ax.text(0.06, 0.82, "▌ 隔夜全球重磅事件与动态", fontproperties=prop, fontsize=12, fontweight='bold', color='#0f172a')

events = [
    ("海湾局势骤紧美伊冲突升级", "美国重启对伊港口封锁并计划收取20%通道安全费", "伊朗关闭海峡并警告，WTI原油冲高至$74.51"),
    ("SK Hynix纳指常规首秀重挫9%", "常规交易首日收盘大跌8.97%至$152.35", "受韩股暴挫15%与券商调降Q2 HBM4盈利预期打击"),
    ("美股半导体存储板块大面积普跌", "美光科技跌4.30%，西部数据跌4.60%，英伟达跌3.40%", "SKHY大跌触发存储板块重置担忧，SOX跌超4%"),
    ("美债收益率狂飙黄金承压走低", "10年期美债收益率冲高至4.610%，避险推动美元走强", "高利率预期及美元强势，现货黄金大幅下挫至$4,081.43")
]

y = 0.72
for title, val, note in events:
    ax.text(0.08, y, title, fontproperties=prop, fontsize=10.5, color='#334155', fontweight='bold')
    ax.text(0.08, y-0.04, f"{val}\n{note}", fontproperties=prop, fontsize=9.0, color='#64748b')
    y -= 0.11

# Right Side: Market Indicators & Assets
ax.text(0.56, 0.82, "▌ 核心资产收盘表现", fontproperties=prop, fontsize=12, fontweight='bold', color='#0f172a')

asset_data = [
    ("纳斯达克 (Nasdaq)", "25,873.18 (-1.55%) 🟢", "存储芯片首秀暴跌，科技巨头遭遇获利抛售"),
    ("标普 500 (S&P 500)", "7,515.34 (-0.79%) 🟢", "AI芯片及高估值成长股拥挤踩踏"),
    ("道琼斯 (Dow Jones)", "52,498.64 (-0.29%) 🟢", "防御性资产及银行业绩期前提供较强韧性"),
    ("WTI原油 (Crude Oil)", "$74.51 (+3.50%) 🔴", "海峡危机阻断全球50% crossings，能源暴涨"),
    ("美光科技 (Micron)", "$936.50 (-4.30%) 🟢", "存储重置浪潮席卷，美光跟跌"),
    ("比特币 (Bitcoin)", "$61,750.90 (-2.30%) 🟢", "地缘风险升级触发风险资产避险抛盘")
]

y_right = 0.72
for title, val, comment in asset_data:
    ax.text(0.58, y_right, title, fontproperties=prop, fontsize=10.5, color='#334155', fontweight='bold')
    # Use red for increase and green for decrease
    color = '#10b981' if '🟢' in val else '#ef4444'
    clean_val = val.replace('🟢', '').replace('🔴', '')
    ax.text(0.58, y_right-0.035, f"{clean_val}  |  {comment}", fontproperties=prop, fontsize=9.0, color='#64748b')
    y_right -= 0.075

plt.tight_layout()
output_path = "images/charts/2026-07-14-morning.png"
plt.savefig(output_path, dpi=300, bbox_inches='tight', facecolor=fig.get_facecolor())
plt.close()
print(f"Chart saved to {output_path}")
