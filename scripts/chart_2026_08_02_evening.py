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
ax.text(0.05, 0.93, "【周末财经要闻与新周开盘展望】(2026/08/02 周日晚报)", fontproperties=prop, fontsize=14, fontweight='bold', color='#1e293b')
ax.axhline(y=0.88, xmin=0.04, xmax=0.96, color='#cbd5e1', linewidth=1.5)

# Left Side: Key Market Events
ax.text(0.06, 0.82, "▌ 周末重磅财经要闻汇总", fontproperties=prop, fontsize=12, fontweight='bold', color='#0f172a')

events = [
    ("央行下半年工作会议：实施适度宽松货币政策", "强调保持流动性合理充裕，强化逆周期和跨周期调节", "稳步深化金融改革，提升服务实体质效，做实五篇大文章"),
    ("港交所实施最低上落价位下调第二阶段", "于8月3日正式生效，旨在降低交易摩擦成本，提升流动性", "缩窄买卖差价，有助于在高波动市场中降低投资者开损"),
    ("中东局势加剧担忧，WTI原油重回84美元上方", "WTI原油收涨1.29%报84.67美元，黄金高位偏强震荡在4043美元", "避险资金流向商品，宏观及地缘风险溢价短期对油金构成强支撑"),
    ("欧盟《人工智能法》执行，合规细则8月2日生效", "首个针对AI的全面跨国监管法规，新增严格的透明度规则", "限制高风险AI应用，对大模型出海和合规披露带来新挑战")
]

y = 0.72
for title, val, note in events:
    ax.text(0.08, y, title, fontproperties=prop, fontsize=10.5, color='#334155', fontweight='bold')
    ax.text(0.08, y-0.035, f"{val}\n{note}", fontproperties=prop, fontsize=9.0, color='#64748b')
    y -= 0.11

# Right Side: Market Indicators & Assets
ax.text(0.56, 0.82, "▌ 核心资产表现与新周开盘前瞻", fontproperties=prop, fontsize=12, fontweight='bold', color='#0f172a')

asset_data = [
    ("上证指数 (SSEC)", "3,832.26 (日: +0.72% / 周五收盘) 🔴", "7月31日定调宽松，中报期注重防御与业绩"),
    ("恒生指数 (HSI)", "25,884.43 (日: +0.10% / 周五收盘) 🔴", "港交所降费降价差政策落地，市场韧性增强"),
    ("纳斯达克指数 (NASDAQ)", "25,373.85 (日: +1.00% / 周五收盘) 🔴", "科技股分化整理，亚马逊及英伟达多空博弈"),
    ("富时A50期指 (FTSE A50)", "14,806.00 (日: +0.09% / 全周走稳) 🔴", "大盘蓝筹筑底迹象明显，静待A股开盘方向"),
    ("WTI原油期货 (Crude Oil)", "$84.67 (日: +1.29% / 地缘支撑) 🔴", "中东冲突升级忧虑，油价震荡反弹至高位"),
    ("COMEX黄金期货 (Gold)", "$4,043.00 (日: +0.14% / 偏强防守) 🔴", "4040美元关口稳固，全球央行与地缘避险买盘"),
    ("比特币 (BTC)", "$63,500.00 (周末: +1.28% / 止跌反弹) 🔴", "特朗普通胀与避险情绪，一度下探6.2万后回升")
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
output_path = "images/charts/2026-08-02-evening.png"
plt.savefig(output_path, dpi=300, bbox_inches='tight', facecolor=fig.get_facecolor())
plt.close()
print(f"Chart saved to {output_path}")
