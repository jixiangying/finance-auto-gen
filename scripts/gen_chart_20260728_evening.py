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
ax.text(0.05, 0.93, "【每日市场收盘与核心资产盘点】(2026/07/28 周二晚报)", fontproperties=prop, fontsize=14, fontweight='bold', color='#1e293b')
ax.axhline(y=0.88, xmin=0.04, xmax=0.96, color='#cbd5e1', linewidth=1.5)

# Left Side: Key Market Events
ax.text(0.06, 0.82, "▌ 今日重磅事件与政策汇总", fontproperties=prop, fontsize=12, fontweight='bold', color='#0f172a')

events = [
    ("全球半导体重挫，日韩股市剧烈回调", "韩国KOSPI指数重挫触发熔断，日经225指数大跌", "外围市场恐慌情绪传导，A股半导体与AI板块大震荡"),
    ("央行开展3055亿逆回购，预告跨月隔夜流动性", "今日逆回购利率1.40%持平，预告开展隔夜逆回购操作", "持续精准平滑资金面跨月波动，维护银行流动性合理充裕"),
    ("金融监管总局召开年中会议，部署重点工作", "强调中小金融机构改革化险，督促实现错位发展", "严监管强监管态势持续，提升金融与实体经济适配性"),
    ("商务部发布产能过剩立场文件，反对保护主义", "中国产业发展靠创新与改革，全球分工是国际分工结果", "中方主张在开放合作中解决分歧，倡导维护自由贸易")
]

y = 0.72
for title, val, note in events:
    ax.text(0.08, y, title, fontproperties=prop, fontsize=10.5, color='#334155', fontweight='bold')
    ax.text(0.08, y-0.035, f"{val}\n{note}", fontproperties=prop, fontsize=9.0, color='#64748b')
    y -= 0.11

# Right Side: Market Indicators & Assets
ax.text(0.56, 0.82, "▌ 核心资产表现与今日收盘", fontproperties=prop, fontsize=12, fontweight='bold', color='#0f172a')

asset_data = [
    ("上证指数 (SSEC)", "3,813.31 (-1.16%) 🟢", "主力资金净流出，盘中失守3800点后拉回"),
    ("深证成指 (SZCOMP)", "13,509.68 (-4.52%) 🟢", "半导体及科技硬件大跌，成长风格显著回调"),
    ("创业板指 (CHINEXT)", "3,327.03 (-7.35%) 🟢", "科技股与新能源重挫，指数创单日较深跌幅"),
    ("恒生指数 (HSI)", "25,310.85 (+0.41%) 🔴", "逆市走强重上25300点，估值优势及配置资金支撑"),
    ("恒生科技 (HSTECH)", "4,730.61 (+0.61%) 🔴", "科网龙头逆势收涨，互联网平台展现抗跌属性"),
    ("主力资金流向 (Flow)", "1,086亿元 (净卖出) 🟢", "内资主力资金流出明显，短线避险情绪浓厚"),
    ("沪深京成交额 (Volume)", "2.03万亿元 (缩量486亿) 🟢", "量能小幅回落，近2700只个股下跌"),
    ("央行流动性投放 (PBOC)", "3,055亿元 (逆回购) 🔴", "平稳跨月资金面表现，公开市场维持合理充裕")
]

y_right = 0.72
for title, val, comment in asset_data:
    ax.text(0.58, y_right, title, fontproperties=prop, fontsize=10.5, color='#334155', fontweight='bold')
    color = '#ef4444' if '🔴' in val else '#10b981'
    clean_val = val.replace('🟢', '').replace('🔴', '')
    
    # Draw value with corresponding color
    ax.text(0.58, y_right-0.030, clean_val, fontproperties=prop, fontsize=9.0, fontweight='bold', color=color)
    # Draw comment next to it
    val_width = len(clean_val) * 0.007 + 0.025
    ax.text(0.58 + val_width, y_right-0.030, f"|  {comment}", fontproperties=prop, fontsize=9.0, color='#64748b')
    
    y_right -= 0.052

plt.tight_layout()
output_path = "images/charts/2026-07-28-evening.png"
plt.savefig(output_path, dpi=300, bbox_inches='tight', facecolor=fig.get_facecolor())
plt.close()
print(f"Chart saved to {output_path}")
