import matplotlib.pyplot as plt
import matplotlib.font_manager as fm
import os

output_dir = "images/charts/"
os.makedirs(output_dir, exist_ok=True)

font_path = "/System/Library/Fonts/STHeiti Medium.ttc"
if not os.path.exists(font_path):
    font_path = "/System/Library/Fonts/PingFang.ttc"
prop = fm.FontProperties(fname=font_path)

fig, ax = plt.subplots(figsize=(10, 6.5))
fig.patch.set_facecolor('#f8fafc')
ax.set_facecolor('#ffffff')
ax.set_xlim(0, 1)
ax.set_ylim(0, 1)
ax.axis('off')

# Title
ax.text(0.05, 0.93, "【新周财经焦点与资产关键位置】(2026/07/05 周日晚)", fontproperties=prop, fontsize=14, fontweight='bold', color='#1e293b')
ax.axhline(y=0.88, xmin=0.04, xmax=0.96, color='#cbd5e1', linewidth=1.5)

# Left Side: Weekend Events
ax.text(0.06, 0.82, "▌ 周末重磅事件与产业动态", fontproperties=prop, fontsize=12, fontweight='bold', color='#0f172a')

weekend_events = [
    ("A股交易新规正式施行", "7月6日启用 (放宽ST涨幅限制、优化基金尾盘竞价)", "盘后扩容至全市场A股/ETF"),
    ("央行重磅提供流动性", "7月6日开展 10000 亿元买断式逆回购操作", "结束缩量，强力呵护与托底市场"),
    ("存储芯片业绩大爆发", "江波龙中报预增最高超740倍，涨价潮持续", "下游复苏及产能吃紧推动景气度"),
    ("“十五五”规划出台", "美丽中国与循环经济规划出台，控制煤电装机", "聚焦降碳减污及资源循环利用")
]

y = 0.74
for title, val, note in weekend_events:
    ax.text(0.08, y, title, fontproperties=prop, fontsize=11, color='#334155', fontweight='bold')
    ax.text(0.08, y-0.045, f"{val}  |  {note}", fontproperties=prop, fontsize=10, color='#64748b')
    y -= 0.10

# Right Side: Market Indicators & Assets
ax.text(0.56, 0.82, "▌ 核心资产收盘与关键位置", fontproperties=prop, fontsize=12, fontweight='bold', color='#0f172a')

asset_data = [
    ("伦敦金现", "$4,174.21 / 盎司", "非农爆冷提振降息预期，强力撑盘"),
    ("WTI原油期货", "$68.08 / 桶", "跌穿70关口，地缘溢价退潮，供需角力"),
    ("比特币 (BTC)", "$63,094.00", "回升站上63k关口，降息流动性回暖"),
    ("美元指数 (DXY)", "100.86", "跌破101大关，创近期新低，汇率压力减")
]

y_right = 0.74
for title, val, comment in asset_data:
    ax.text(0.58, y_right, title, fontproperties=prop, fontsize=11, color='#334155', fontweight='bold')
    ax.text(0.58, y_right-0.045, f"{val} ({comment})", fontproperties=prop, fontsize=10, color='#64748b')
    y_right -= 0.10

plt.tight_layout()
output_path = os.path.join(output_dir, "2026-07-05-evening.png")
plt.savefig(output_path, dpi=300, bbox_inches='tight')
plt.close()
print(f"Chart saved to {output_path}")
