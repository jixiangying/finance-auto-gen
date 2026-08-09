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

fig, ax = plt.subplots(figsize=(12.0, 8.0))
fig.patch.set_facecolor('#f8fafc')
ax.set_facecolor('#ffffff')
ax.set_xlim(0, 1)
ax.set_ylim(0, 1)
ax.axis('off')

# Title
ax.text(0.04, 0.94, "【全球市场周度收官：宽松交易重燃引爆股债金，大宗商品大幅回踩】(2026/08/09 周末特刊)", fontproperties=prop, fontsize=14, fontweight='bold', color='#1e293b')
ax.axhline(y=0.90, xmin=0.03, xmax=0.97, color='#cbd5e1', linewidth=1.5)

# Left Side: Key Market Events / Outlook
ax.text(0.05, 0.84, "▌ 本周全球市场核心逻辑与动态", fontproperties=prop, fontsize=12, fontweight='bold', color='#0f172a')

events = [
    ("美国7月非农惨淡大跌2.3万，加息阴霾彻底消散", 
     "7月新增非农大跌至-2.3万（预期增8万），历史数据合计下修10.3万。", 
     "劳动力市场超预期冷落，降温迹象确认，彻底扭转了此前偏鹰的政策担忧。"),
    ("美股创 4 月中旬以来最强周涨幅，标普/纳指均创历史新高", 
     "纳斯达克周涨5.2%，标普500周涨3.6%创新高，道琼斯指数全周累计上涨3.0%。", 
     "坏消息变好消息，降息逻辑重归市场主导，大科技板块迎流动性回补。"),
    ("避险情绪与降息预期双轨共振，黄金周暴涨超7%", 
     "COMEX黄金大幅拉升，收报$4,384.59/盎司，单周累涨7.2%创半年最佳。", 
     "美债收益率与美元双下挫，去中心化及避险配置资金疯狂涌入黄金等核心资产。"),
    ("地缘博弈现松动迹象，布油全周深跌7.5%", 
     "布伦特原油收报$83.24/桶，周五温和反弹0.9%，但全周累计下跌超7.5%。", 
     "伊朗与美欧等谈判传出降温预期，市场对霍尔木兹海峡阻断的溢价大幅挤出。"),
    ("中港两地市场稳步企稳，A股沪指单周反弹2.81%", 
     "上证指数周五收涨1.02%至3940.04，周涨2.81%；恒指收报25668.03，周跌0.84%。", 
     "人民币汇率跟随美元回调走强，A股成长股全线反弹，港股科技亦小幅企稳。")
]

y = 0.75
for title, val, note in events:
    ax.text(0.06, y, f"• {title}", fontproperties=prop, fontsize=10.5, color='#334155', fontweight='bold')
    ax.text(0.06, y-0.030, f"  数据: {val}\n  逻辑: {note}", fontproperties=prop, fontsize=9.0, color='#64748b')
    y -= 0.105

# Right Side: Market Indicators & Assets
ax.text(0.55, 0.84, "▌ 核心资产周度/日度表现回顾", fontproperties=prop, fontsize=12, fontweight='bold', color='#0f172a')

asset_data = [
    ("纳斯达克指数 (NASDAQ)", "26,690.62", "周五: +1.30%  |  全周: +5.20% 🔴"),
    ("标普 500 指数 (S&P 500)", "7,757.64", "周五: +0.62%  |  全周: +3.60% 🔴"),
    ("道琼斯工业指数 (DJIA)", "54,036.93", "周五: +0.28%  |  全周: +3.00% 🔴"),
    ("上证指数 (SSEC)", "3,940.04", "周五: +1.02%  |  全周: +2.81% 🔴"),
    ("沪深 300 指数 (CSI300)", "4,694.44", "周五: +0.93%  |  全周: +1.28% 🔴"),
    ("恒生指数 (HSI)", "25,668.03", "周五: +0.54%  |  全周: -0.84% 🟢"),
    ("COMEX 黄金期货 (Gold)", "$4,384.59", "周五: +1.94%  |  全周: +7.20% 🔴"),
    ("布伦特原油期货 (Brent)", "$83.24", "周五: +0.90%  |  全周: -7.50% 🟢"),
    ("10年期美债收益率 (US10Y)", "4.640%", "周五: -4.0BP   |  全周: -8.6BP 🟢"),
    ("比特币 (BTC)", "$64,905.53", "周五: +0.75%  |  全周: +3.10% 🔴")
]

y_right = 0.75
for title, price, perf in asset_data:
    ax.text(0.57, y_right, title, fontproperties=prop, fontsize=10.0, color='#334155', fontweight='bold')
    
    color = '#ef4444' if '🔴' in perf else '#10b981'
    clean_perf = perf.replace('🟢', '').replace('🔴', '')
    
    # Draw price
    ax.text(0.57, y_right-0.026, f"现价: {price}", fontproperties=prop, fontsize=9.0, color='#475569')
    # Draw performance
    ax.text(0.71, y_right-0.026, f"|  {clean_perf}", fontproperties=prop, fontsize=9.0, fontweight='bold', color=color)
    
    y_right -= 0.054

plt.tight_layout()
output_path = "images/charts/2026-08-09-morning.png"
plt.savefig(output_path, dpi=300, bbox_inches='tight', facecolor=fig.get_facecolor())
plt.close()
print(f"Chart saved to {output_path}")
