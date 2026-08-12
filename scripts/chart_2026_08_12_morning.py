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
ax.text(0.04, 0.94, "【常规交易日：美股承压下行，地缘政治冲突推动油价大涨，市场静待CPI数据】(2026/08/12 周三早报)", fontproperties=prop, fontsize=14, fontweight='bold', color='#1e293b')
ax.axhline(y=0.90, xmin=0.03, xmax=0.97, color='#cbd5e1', linewidth=1.5)

# Left Side: Key Market Events / Outlook
ax.text(0.05, 0.84, "▌ 本周全球市场核心博弈逻辑与前瞻", fontproperties=prop, fontsize=12, fontweight='bold', color='#0f172a')

events = [
    ("美股三大股指全面收跌，市场情绪转向谨慎", 
     "道指跌0.34%，标普500跌0.32%，纳指跌0.60%。", 
     "投资者在周三关键CPI通胀报告发布前选择落袋为安，科技股领跌。"),
    ("费城半导体指数（SOX）逆势收涨1.67%", 
     "收盘于12,194.60点，上涨200.74点。", 
     "经历前一交易日大跌后迎来超跌反弹，博通与英伟达等核心股表现稳健。"),
    ("美伊霍尔木兹海峡地缘危机悬而未决，WTI原油飙升6.18%", 
     "WTI原油大涨收于$84.58/桶，盘中因阿曼斡旋传闻略有回落。", 
     "供给端溢价显著上升，红海与波斯湾关键航道关闭隐忧继续主导能源市场。"),
    ("华尔街巨头联手，5000亿美元AI基建财团成形", 
     "高盛、摩根大通、黑石与Nvidia合作，提供巨额资金支持AI算力基建。", 
     "显示出金融巨头对AI芯片与数据中心长期需求的强劲信心，缓解部分泡沫担忧。"),
    ("宏观流动性与政策去前瞻化，美债收益率与比特币整固", 
     "10年期美债收益率收于4.683%，比特币回调1.80%至$63,686点位。", 
     "Goolsbee重申通胀为首要难题；Warsh推动的去前瞻指引政策让市场静待数据。")
]

y = 0.75
for title, val, note in events:
    ax.text(0.06, y, f"• {title}", fontproperties=prop, fontsize=10.5, color='#334155', fontweight='bold')
    ax.text(0.06, y-0.030, f"  焦点: {val}\n  研研: {note}", fontproperties=prop, fontsize=9.0, color='#64748b')
    y -= 0.105

# Right Side: Market Indicators & Assets
ax.text(0.55, 0.84, "▌ 核心资产前一交易日表现", fontproperties=prop, fontsize=12, fontweight='bold', color='#0f172a')

asset_data = [
    ("纳斯达克指数 (NASDAQ)", "26,445.45", "周二: -0.60% 🟢"),
    ("标普 500 指数 (S&P 500)", "7,728.20", "周二: -0.32% 🟢"),
    ("道琼斯工业指数 (DJIA)", "53,791.85", "周二: -0.34% 🟢"),
    ("费城半导体指数 (SOX)", "12,194.60", "周二: +1.67% 🔴"),
    ("上证指数 (SSEC)", "3,934.09", "周二: -0.82% 🟢"),
    ("深圳成指 (SZCOMP)", "14,259.44", "周二: -0.40% 🟢"),
    ("COMEX 黄金期货 (Gold)", "$4,383.00", "周二: -0.46% 🟢"),
    ("WTI 原油期货 (WTI)", "$84.58", "周二: +6.18% 🔴"),
    ("10年期美债收益率 (US10Y)", "4.683%", "周二: -1.4BP 🟢"),
    ("比特币 (BTC)", "$63,686.00", "周二: -1.80% 🟢")
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
output_path = "images/charts/2026-08-12-morning.png"
plt.savefig(output_path, dpi=300, bbox_inches='tight', facecolor=fig.get_facecolor())
plt.close()
print(f"Chart saved to {output_path}")
