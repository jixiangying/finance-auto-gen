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
ax.text(0.05, 0.93, "【核心行情信息图】(2026/07/15 周三早报)", fontproperties=prop, fontsize=14, fontweight='bold', color='#1e293b')
ax.axhline(y=0.88, xmin=0.04, xmax=0.96, color='#cbd5e1', linewidth=1.5)

# Left Side: Overnight Key Events
ax.text(0.06, 0.82, "▌ 隔夜全球重磅事件与动态", fontproperties=prop, fontsize=12, fontweight='bold', color='#0f172a')

events = [
    ("美国6月CPI超预期降温", "环比下跌0.4%年率降至3.5%，低于市场预期的3.8%", "能源价格下行是主因，缓解美联储立即加息隐忧"),
    ("大行二季度业绩开门红", "高盛创纪录营收，花旗净利58亿美元并上调股息", "摩根大通、美银等业绩普遍超预期，支撑金融股"),
    ("IBM业绩警报大跌25%创纪录", "Q2营收不及预期，因企业预算向AI硬件倾斜", "成长股受IBM爆冷拖累，但存储/AI硬件需求强劲"),
    ("地缘局势持续紧绷油价上浮", "美伊摩擦继续扰动霍尔木兹海峡，WTI逼近80美元", "地缘溢价支撑油价涨超2.1%，与通胀降温形成博弈")
]

y = 0.72
for title, val, note in events:
    ax.text(0.08, y, title, fontproperties=prop, fontsize=10.5, color='#334155', fontweight='bold')
    ax.text(0.08, y-0.04, f"{val}\n{note}", fontproperties=prop, fontsize=9.0, color='#64748b')
    y -= 0.11

# Right Side: Market Indicators & Assets
ax.text(0.56, 0.82, "▌ 核心资产收盘表现", fontproperties=prop, fontsize=12, fontweight='bold', color='#0f172a')

asset_data = [
    ("纳斯达克 (Nasdaq)", "26,107.01 (+0.90%) 🔴", "CPI降温提振估值，科技龙头重获买盘支撑"),
    ("标普 500 (S&P 500)", "7,543.59 (+0.38%) 🔴", "金融股开门红与CPI利好对冲IBM暴跌冲击"),
    ("WTI原油 (Crude Oil)", "$79.78 (+2.10%) 🔴", "海湾局势仍旧紧张，地缘溢价推高油价"),
    ("伦敦现货黄金 (Spot Gold)", "$4,024.30 (-1.40%) 🟢", "从日内低点3983反弹，受美债收益率下行提振"),
    ("比特币 (Bitcoin)", "$62,242.00 (-2.36%) 🟢", "避险情绪缓和，加密市场表现相对偏弱"),
    ("国际商业机器 (IBM)", "$217.41 (-25.06%) 🟢", "营收暴冷与利润警报引发历史性抛售重挫")
]

y_right = 0.72
for title, val, comment in asset_data:
    ax.text(0.58, y_right, title, fontproperties=prop, fontsize=10.5, color='#334155', fontweight='bold')
    # Use red (#ef4444) for rise 🔴 and green (#10b981) for fall 🟢 in Chinese market convention
    color = '#ef4444' if '🔴' in val else '#10b981'
    clean_val = val.replace('🟢', '').replace('🔴', '')
    
    # Draw value with corresponding color
    ax.text(0.58, y_right-0.035, clean_val, fontproperties=prop, fontsize=9.0, fontweight='bold', color=color)
    # Draw comment next to it
    val_width = len(clean_val) * 0.0075 + 0.02
    ax.text(0.58 + val_width, y_right-0.035, f"|  {comment}", fontproperties=prop, fontsize=9.0, color='#64748b')
    
    y_right -= 0.075

plt.tight_layout()
output_path = "images/charts/2026-07-15-morning.png"
plt.savefig(output_path, dpi=300, bbox_inches='tight', facecolor=fig.get_facecolor())
plt.close()
print(f"Chart saved to {output_path}")
