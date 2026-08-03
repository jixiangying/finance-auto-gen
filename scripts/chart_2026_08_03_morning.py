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
ax.text(0.05, 0.93, "【新一周市场博弈与重磅前瞻】(2026/08/03 周一早报)", fontproperties=prop, fontsize=14, fontweight='bold', color='#1e293b')
ax.axhline(y=0.88, xmin=0.04, xmax=0.96, color='#cbd5e1', linewidth=1.5)

# Left Side: Key Market Events / Outlook
ax.text(0.06, 0.82, "▌ 新一周宏观博弈与重磅前瞻", fontproperties=prop, fontsize=12, fontweight='bold', color='#0f172a')

events = [
    ("利率预期生变，美债收益率攀升至4.75%", "10年期美债收益率升至4.75%高水位，受油价大涨与通胀担忧推动", "美联储未来紧缩预期抬头，9月加息概率飙升至80%以上"),
    ("日元干预疑云，外汇市场波动显著加剧", "日元汇率急剧震荡至157区间，传美日当局联手干预以遏制贬值", "跨境利差交易及流动性再分配对全球资本流向产生外溢效应"),
    ("超级非农周重磅来袭，考验美联储政策路径", "周五公布美国7月非农就业数据，市场静待薪资与失业率指引", "ADP小非农及制造业PMI先行公布，数据强弱将重塑货币政策定价"),
    ("中报季考验来临，聚焦硬科技与高股息主线", "A股与港股行情步入业绩验证期，AMD、伯克希尔等将公布中报", "市场逐步从情绪驱动转向基本面驱动，关注AI硬件及红利防御资产")
]

y = 0.72
for title, val, note in events:
    ax.text(0.08, y, title, fontproperties=prop, fontsize=10.5, color='#334155', fontweight='bold')
    ax.text(0.08, y-0.035, f"{val}\n{note}", fontproperties=prop, fontsize=9.0, color='#64748b')
    y -= 0.11

# Right Side: Market Indicators & Assets
ax.text(0.56, 0.82, "▌ 核心资产最新价格与变化", fontproperties=prop, fontsize=12, fontweight='bold', color='#0f172a')

asset_data = [
    ("纳斯达克综合指数 (NASDAQ)", "25,373.85 (日: +1.00% / 周五收盘) 🔴", "亚马逊云计算财报提振AI信心，科技板块企稳反弹"),
    ("标普 500 指数 (S&P 500)", "7,489.72 (日: +0.70% / 周五收盘) 🔴", "科技巨头盈余好转托底大盘，市场震荡中收涨"),
    ("道琼斯工业指数 (DJIA)", "52,485.03 (日: +0.53% / 周五收盘) 🔴", "大金融及工业蓝筹表现稳健，防守板块表现活跃"),
    ("布伦特原油期货 (Brent)", "$90.12 (日: +2.41% / 周五收盘) 🔴", "地缘局势恶化引发供给忧虑，油价大涨刷新近期高点"),
    ("COMEX 黄金期货 (Gold)", "$4,096.29 (日: +1.32% / 周五收盘) 🔴", "中东局势升级激发避险买盘，金价克服强势美元拉升"),
    ("10年期美债收益率 (US10Y)", "4.75% (日: +1BP / 周五收盘) 🔴", "能源暴涨加剧粘性通胀担忧，收益率攀升至高点"),
    ("比特币 (BTC)", "$61,250.00 (周末变动: -2.32%) 🟢", "避险情绪压制风险资产，缩量回调寻求支撑")
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
output_path = "images/charts/2026-08-03-morning.png"
plt.savefig(output_path, dpi=300, bbox_inches='tight', facecolor=fig.get_facecolor())
plt.close()
print(f"Chart saved to {output_path}")
