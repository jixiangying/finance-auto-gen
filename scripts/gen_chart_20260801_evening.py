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
ax.text(0.05, 0.93, "【周末市场复盘与核心资产表现】(2026/08/01 周六晚报)", fontproperties=prop, fontsize=14, fontweight='bold', color='#1e293b')
ax.axhline(y=0.88, xmin=0.04, xmax=0.96, color='#cbd5e1', linewidth=1.5)

# Left Side: Key Market Events
ax.text(0.06, 0.82, "▌ 过去48小时及全周重磅事件", fontproperties=prop, fontsize=12, fontweight='bold', color='#0f172a')

events = [
    ("政治局会议强力定调，首次提出提升资本市场“韧性与信心”", "7月30日政治局会议指引下半年工作，要求加大逆周期调节力度", "深化投融资综合改革，扫除观望情绪，扫清长期耐心资本入市障碍"),
    ("美股巨头二季报大分化，科技股周五暴力反弹平稳收周", "亚马逊二季报超预期大涨，苹果四财季业绩指引平平但股价收窄跌幅", "微软等强劲财报和芯片板块暴力反弹，纳指全周累计上涨1.59%"),
    ("中东及海湾地缘局势升级，美债收益率与原油避险走高", "美伊局势升级加剧通胀担忧，10年期美债收益率升至4.74%", "布油盘中避险溢价走高后高位整理，全球资产处于敏感博弈期"),
    ("月末红盘放量大涨收官，A股两市成交额飙升至2.56万亿", "科技赛道显著回流，创业板及科创50分别暴涨3.06%及2.99%", "单日放量超2000亿确立底部蓄势，半导体、通信等AI硬件成多头主力")
]

y = 0.72
for title, val, note in events:
    ax.text(0.08, y, title, fontproperties=prop, fontsize=10.5, color='#334155', fontweight='bold')
    ax.text(0.08, y-0.035, f"{val}\n{note}", fontproperties=prop, fontsize=9.0, color='#64748b')
    y -= 0.11

# Right Side: Market Indicators & Assets
ax.text(0.56, 0.82, "▌ 全球核心资产周度及周五收盘表现", fontproperties=prop, fontsize=12, fontweight='bold', color='#0f172a')

asset_data = [
    ("上证指数 (SSEC)", "3,832.26 (周: +0.47% / 日: +0.72%) 🔴", "月末放量修复，周线成功收阳稳固底部"),
    ("深证成指 (SZCOMP)", "13,578.93 (周: -1.42% / 日: +2.21%) 🟢", "科技股周五绝地反扑，收复本周部分失地"),
    ("创业板指 (CHINEXT)", "3,343.96 (周: -3.93% / 日: +3.06%) 🟢", "AI硬件重获热烈追捧，单日暴涨平抑周度跌幅"),
    ("恒生指数 (HSI)", "25,884.43 (周: +3.69% / 日: +0.10%) 🔴", "红盘收官七月，全月大涨13.13%领跑全球"),
    ("恒生科技 (HSTECH)", "4,829.22 (周: +4.31% / 日: +0.53%) 🔴", "科网龙头走势坚挺，周线重回上行通道"),
    ("纳斯达克 (IXIC)", "25,373.85 (周: +1.59% / 日: +1.00%) 🔴", "受科技大厂财报提振，周五大涨扭转下行势头"),
    ("标普500 (SPX)", "7,489.72 (周: +1.05% / 日: +0.70%) 🔴", "科技权重大涨共振，终结连续两周的回调"),
    ("道琼斯 (DJI)", "52,485.03 (周: +1.04% / 日: +0.50%) 🔴", "平稳度过美联戏前夕的剧烈波动期")
]

y_right = 0.72
for title, val, comment in asset_data:
    ax.text(0.58, y_right, title, fontproperties=prop, fontsize=10.5, color='#334155', fontweight='bold')
    
    # Red for overall positive week, Green for overall negative week
    color = '#ef4444' if '🔴' in val else '#10b981'
    clean_val = val.replace('🟢', '').replace('🔴', '')
    
    # Draw value with corresponding color
    ax.text(0.58, y_right-0.026, clean_val, fontproperties=prop, fontsize=9.0, fontweight='bold', color=color)
    # Draw comment next to it
    val_width = len(clean_val) * 0.0068 + 0.025
    ax.text(0.58 + val_width, y_right-0.026, f"|  {comment}", fontproperties=prop, fontsize=9.0, color='#64748b')
    
    y_right -= 0.052

plt.tight_layout()
output_path = "images/charts/2026-08-01-evening.png"
plt.savefig(output_path, dpi=300, bbox_inches='tight', facecolor=fig.get_facecolor())
plt.close()
print(f"Chart saved to {output_path}")
