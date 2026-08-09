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
ax.text(0.04, 0.94, "【新周展望：周末重磅要闻汇总与下周核心博弈逻辑】(2026/08/09 周日晚报)", fontproperties=prop, fontsize=14, fontweight='bold', color='#1e293b')
ax.axhline(y=0.90, xmin=0.03, xmax=0.97, color='#cbd5e1', linewidth=1.5)

# Left Side: Key Weekend Events & Outlook
ax.text(0.05, 0.84, "▌ 周末重磅财经要闻与政策风向", fontproperties=prop, fontsize=12, fontweight='bold', color='#0f172a')

events = [
    ("7月经济数据发布：CPI同比上涨0.5%，PPI上涨3.5%", 
     "CPI同比温和回升0.5%（基本符合预期），物价水平总体保持稳定；", 
     "外汇储备上升至3.4188万亿美元，显示国内基本面延续企稳修复。"),
    ("北京限购松绑再落地，降低非京籍家庭购房社保年限", 
     "非京籍购房社保及个税缴纳年限由2年缩短至1年，公积金贷款额度适度提高。", 
     "一线城市政策持续宽松，有助于巩固房地产板块及顺周期的企稳动能。"),
    ("国家卫健委发布2026新版基本药物目录，创新药首次被纳入", 
     "首次明确将创新药纳入基本目录，并直接打通全国公立医院采购的壁垒。", 
     "创新药板块再迎重磅政策支撑，估值迎来历史性低位的强势催化。"),
    ("美国拟禁中国光模块传闻发酵，外交部表示坚决反对", 
     "外交部坚决反对美泛化国安概念的行为，算力板块中报预喜且交易拥拥挤度低。", 
     "核心科技龙头受业绩支撑依然具备吸引力，警惕地缘博弈带来的高波动。"),
    ("宏观“超级周”来临：联储利率决议及通胀数据将定调", 
     "下周将公布美PCE物价指数、零售数据，并召开美联储8月利率决议。", 
     "非农爆冷后市场进入实质性宽松定价期，全球科技成长股望迎流动性红利。")
]

y = 0.75
for title, val, note in events:
    ax.text(0.06, y, f"• {title}", fontproperties=prop, fontsize=10.5, color='#334155', fontweight='bold')
    ax.text(0.06, y-0.030, f"  要闻: {val}\n  研判: {note}", fontproperties=prop, fontsize=9.0, color='#64748b')
    y -= 0.105

# Right Side: Market Indicators & Assets
ax.text(0.55, 0.84, "▌ 核心资产当前状态（上周收盘）", fontproperties=prop, fontsize=12, fontweight='bold', color='#0f172a')

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
output_path = "images/charts/2026-08-09-evening.png"
plt.savefig(output_path, dpi=300, bbox_inches='tight', facecolor=fig.get_facecolor())
plt.close()
print(f"Chart saved to {output_path}")
