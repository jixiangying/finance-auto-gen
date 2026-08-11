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

# 显式设置 rcParams 以防止乱码
plt.rcParams['font.sans-serif'] = ['STHeiti', 'PingFang SC', 'Heiti TC', 'sans-serif']
plt.rcParams['axes.unicode_minus'] = False

fig, ax = plt.subplots(figsize=(12.0, 8.0))
fig.patch.set_facecolor('#f8fafc')
ax.set_facecolor('#ffffff')
ax.set_xlim(0, 1)
ax.set_ylim(0, 1)
ax.axis('off')

# Title
ax.text(0.04, 0.94, "【常规交易日：A股震荡整固半导体分化，央行十五五规划绘就开放新蓝图】(2026/08/11 周二收盘报)", fontproperties=prop, fontsize=14, fontweight='bold', color='#1e293b')
ax.axhline(y=0.90, xmin=0.03, xmax=0.97, color='#cbd5e1', linewidth=1.5)

# Left Side: Key Market Events / Outlook
ax.text(0.05, 0.84, "▌ 本日全球与国内市场核心动态及前瞻", fontproperties=prop, fontsize=12, fontweight='bold', color='#0f172a')

events = [
    ("A股三大指数涨跌互现，全市场成交额收窄至2.34万亿元", 
     "沪指收盘跌0.82%报3934.09点，创业板指逆势上涨0.34%报3549.16点。", 
     "成交额对比前一日缩量7.99%。全盘呈震荡偏弱走势，上涨个股1615只，下跌3777只。"),
    ("板块热点分化，MLCC概念、机器人及影视院线逆势走强", 
     "MLCC受涨价预期驱动大涨；宇树科技IPO定价带动人形机器人板块活跃。", 
     "前期强势的贵金属、有色金属、商业航天以及军工装备等板块则迎来获利回吐。"),
    ("央行印发“十五五”改革规划，描绘金融强国与高水平开放", 
     "健全现代货币政策框架与宏观审慎，稳步推进人民币全球使用与高水平开放。", 
     "同时，央行今日公开市场开展零逆回购操作，净回笼资金465亿元，维稳流动性。"),
    ("港股市场集体回调，恒指收盘下跌1.10%跌破25700点", 
     "恒指报25652.82点，恒生科技指数跌1.93%报4824.42点。", 
     "大市整体受科技股走弱和金属原材料板块回落拖累，市场交投情绪有所退潮。"),
    ("大宗商品显著拉升，WTI原油重回$83关口，黄金逼近4500", 
     "美伊谈判陷入僵局及红海运输紧张，WTI油价涨至$83.77；黄金涨至$4469.50。", 
     "海外期指盘前微跌，市场进入观望期，静待今晚美零售数据与明晚CPI发布。")
]

y = 0.75
for title, val, note in events:
    ax.text(0.06, y, f"• {title}", fontproperties=prop, fontsize=10.5, color='#334155', fontweight='bold')
    ax.text(0.06, y-0.030, f"  焦点: {val}\n  研判: {note}", fontproperties=prop, fontsize=9.0, color='#64748b')
    y -= 0.105

# Right Side: Market Indicators & Assets
ax.text(0.55, 0.84, "▌ 核心资产今日/日内最新表现", fontproperties=prop, fontsize=12, fontweight='bold', color='#0f172a')

asset_data = [
    ("上证指数 (SSEC)", "3,934.09", "收盘: -0.82% 🟢"),
    ("深证成指 (SZCOMP)", "14,259.44", "收盘: -0.40% 🟢"),
    ("创业板指 (CHINEXT)", "3,549.16", "收盘: +0.34% 🔴"),
    ("恒生指数 (HSI)", "25,652.82", "收盘: -1.10% 🟢"),
    ("恒生科技指数 (HSTECH)", "4,824.42", "收盘: -1.93% 🟢"),
    ("COMEX 黄金期货 (Gold)", "$4,469.50", "日内: +1.50% 🔴"),
    ("WTI 原油期货 (WTI)", "$83.77", "日内: +5.16% 🔴"),
    ("比特币 (BTC)", "$64,000.00", "日内: -1.32% 🟢"),
    ("10年期美债收益率 (US10Y)", "4.690%", "日内: -0.7BP 🟢"),
    ("纳指100期货 (NQ Futures)", "26,550.00", "日内: -0.21% 🟢")
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
output_path = "images/charts/2026-08-11-evening.png"
plt.savefig(output_path, dpi=300, bbox_inches='tight', facecolor=fig.get_facecolor())
plt.close()
print(f"Chart saved to {output_path}")
