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
ax.text(0.05, 0.93, "【周末市场复盘与核心资产表现】(2026/07/25 周六晚报)", fontproperties=prop, fontsize=14, fontweight='bold', color='#1e293b')
ax.axhline(y=0.88, xmin=0.04, xmax=0.96, color='#cbd5e1', linewidth=1.5)

# Left Side: Key Market Events
ax.text(0.06, 0.82, "▌ 过去48小时及全周重磅事件", fontproperties=prop, fontsize=12, fontweight='bold', color='#0f172a')

events = [
    ("央行加量续作，5000亿MLF护航流动性", "央行7月24日净投放1000亿元，连续3个月加量续作", "显示监管层逆周期调节力度，呵护季末流动性充裕"),
    ("美联储议息前瞻，超级周科技巨头报捷", "FOMC会议定于7月28-29日召开，沃什保持静默", "主流预期维持3.50%-3.75%利率不变，关注下周财报密集期"),
    ("关税与地缘共振，商品外汇市场剧烈波动", "美加征关税生效，黄金下挫近2%，原油冲高后回撤", "布油盘中逼近96美元后回落收跌，避险资金高位了结"),
    ("成交跌破2万亿，国家队600亿重金筑底", "两市缩量至1.94万亿元，A股港股周五跟跌美股", "存量博弈特征显著，证监会部署防风险，国家队护盘明显")
]

y = 0.72
for title, val, note in events:
    ax.text(0.08, y, title, fontproperties=prop, fontsize=10.5, color='#334155', fontweight='bold')
    ax.text(0.08, y-0.035, f"{val}\n{note}", fontproperties=prop, fontsize=9.0, color='#64748b')
    y -= 0.11

# Right Side: Market Indicators & Assets
ax.text(0.56, 0.82, "▌ 核心资产本周及周五表现", fontproperties=prop, fontsize=12, fontweight='bold', color='#0f172a')

asset_data = [
    ("上证指数 (SSEC)", "3,814.20 (周: +1.33% / 日: -1.61%) 🔴", "成交缩量失守2万亿，周内反弹趋势未改"),
    ("深证成指 (SDEC)", "13,774.68 (周: +0.49% / 日: -2.47%) 🔴", "科技股高位整固，主力资金流出成长板块"),
    ("创业板指 (CHINEXT)", "3,480.87 (周: +1.52% / 日: -2.65%) 🔴", "赛道股获利回吐明显，周度累计涨幅收窄"),
    ("恒生指数 (HSI)", "24,963.23 (周: +1.63% / 日: -0.98%) 🔴", "周五冲高回落失守25000点，周线翻红"),
    ("恒生科技指数 (HSTECH)", "4,629.51 (周: +0.14% / 日: -1.47%) 🔴", "科网股受美股波动传导，本周微幅收涨"),
    ("WTI原油期货 (WTI)", "$91.27 (周: 震荡上行 / 日: -1.00%) 🔴", "中东地缘局势仍紧，避险溢价与多头回吐交织")
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
output_path = "images/charts/2026-07-25-evening.png"
plt.savefig(output_path, dpi=300, bbox_inches='tight', facecolor=fig.get_facecolor())
plt.close()
print(f"Chart saved to {output_path}")
