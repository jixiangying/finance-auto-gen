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
ax.text(0.05, 0.93, "【周末市场复盘与核心资产表现】(2026/07/18 周六晚报)", fontproperties=prop, fontsize=14, fontweight='bold', color='#1e293b')
ax.axhline(y=0.88, xmin=0.04, xmax=0.96, color='#cbd5e1', linewidth=1.5)

# Left Side: Key Market Events
ax.text(0.06, 0.82, "▌ 过去48小时及全周重磅事件", fontproperties=prop, fontsize=12, fontweight='bold', color='#0f172a')

events = [
    ("A股科技重挫与创业板周跌超10%", "高位AI及芯片股估值清洗与融资盘踩踏共振", "创业板指周五跌7.15%，全周累计重挫10.78%"),
    ("并购重组放宽与电池税制改革", "特殊税务持股降至50%，电池消费税分级引导升级", "政策组合拳助力企业转型升级，激活并购重组活力"),
    ("中东局势紧绷，原油暴涨超4%", "美伊局势升级威胁航道，WTI原油收于82.49美元", "地缘溢价推升避险，全球商品及股指承受流动性压力"),
    ("国家队ETF托底，电力银行逆市红", "多只宽基ETF午后放量拉升，红利防御资产逆市飘红", "大资金托底维稳流动性，电力、银行表现出防御韧性")
]

y = 0.72
for title, val, note in events:
    ax.text(0.08, y, title, fontproperties=prop, fontsize=10.5, color='#334155', fontweight='bold')
    ax.text(0.08, y-0.035, f"{val}\n{note}", fontproperties=prop, fontsize=9.0, color='#64748b')
    y -= 0.11

# Right Side: Market Indicators & Assets
ax.text(0.56, 0.82, "▌ 核心资产本周及周五表现", fontproperties=prop, fontsize=12, fontweight='bold', color='#0f172a')

asset_data = [
    ("上证指数 (SSEC)", "3,764.15 (周: -5.81% / 日: -3.05%) 🟢", "跌破3800点，主要大资金通过ETF托底护航"),
    ("深证成指 (SDEC)", "13,706.88 (周: -5.91% / 日: -5.40%) 🟢", "题材股大面积调整，两市放量成交2.65万亿元"),
    ("创业板指 (CHINEXT)", "3,428.63 (周: -10.78% / 日: -7.15%) 🟢", "高位科技拥挤度极高，遭获利盘与融资盘双重打压"),
    ("恒生指数 (HSI)", "24,562.24 (周: +1.60% / 日: -1.78%) 🔴", "虽然周五重挫，但全周仍录得上涨，周线三连阳"),
    ("恒生科技指数 (HSTECH)", "4,623.17 (周: -2.09% / 日: -4.37%) 🟢", "中概科网股与芯片股走低，创三周最大单周跌幅"),
    ("WTI原油期货 (WTI)", "82.49 (周: 上涨 / 日: +4.48%) 🔴", "中东地缘局势恶化推动油价大涨，避险溢价骤增")
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
    
    y_right -= 0.065

plt.tight_layout()
output_path = "images/charts/2026-07-18-evening.png"
plt.savefig(output_path, dpi=300, bbox_inches='tight', facecolor=fig.get_facecolor())
plt.close()
print(f"Chart saved to {output_path}")
