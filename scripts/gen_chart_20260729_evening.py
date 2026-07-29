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
ax.text(0.05, 0.93, "【每日市场收盘与核心资产盘点】(2026/07/29 周三晚报)", fontproperties=prop, fontsize=14, fontweight='bold', color='#1e293b')
ax.axhline(y=0.88, xmin=0.04, xmax=0.96, color='#cbd5e1', linewidth=1.5)

# Left Side: Key Market Events
ax.text(0.06, 0.82, "▌ 今日重磅事件与政策汇总", fontproperties=prop, fontsize=12, fontweight='bold', color='#0f172a')

events = [
    ("A股三大指数放量反弹，两市成交达2.30万亿", "创业板指领涨1.55%，个股超4200只上涨", "大消费、大金融与新能源车活跃，半导体与AI硬件分化"),
    ("央行开展6000亿大额逆回购，平滑跨月跨季", "7月29日至31日每日隔夜逆回购投放6000亿元", "精准呵护跨月流动性平稳，维护银行间流动性合理充裕"),
    ("证监会实施精准逆周期调节，中长期资金稳步入市", "加强应对全球市场波动，防范跨境传导与输入性风险", "精准调节机制持续发力，上市公司股东终止减持提振信心"),
    ("港股市场全线大涨，恒指大涨近2%", "科技与汽车股表现强势，恒生科技指数收涨2.84%", "港股估值洼地优势显现，空头回补与外资低吸意愿增强")
]

y = 0.72
for title, val, note in events:
    ax.text(0.08, y, title, fontproperties=prop, fontsize=10.5, color='#334155', fontweight='bold')
    ax.text(0.08, y-0.035, f"{val}\n{note}", fontproperties=prop, fontsize=9.0, color='#64748b')
    y -= 0.11

# Right Side: Market Indicators & Assets
ax.text(0.56, 0.82, "▌ 核心资产表现与今日收盘", fontproperties=prop, fontsize=12, fontweight='bold', color='#0f172a')

asset_data = [
    ("上证指数 (SSEC)", "3,828.47 (+0.40%) 🔴", "大消费及证券拉升，沪指放量企稳反弹"),
    ("深证成指 (SZCOMP)", "13,658.44 (+1.10%) 🔴", "成长资产偏好修复，核心蓝筹股提振成指"),
    ("创业板指 (CHINEXT)", "3,378.70 (+1.55%) 🔴", "锂电与智能网联活跃，指数领涨市场"),
    ("恒生指数 (HSI)", "25,807.92 (+1.96%) 🔴", "大涨超490点重上2.58万点，资金大幅回流"),
    ("恒生科技 (HSTECH)", "4,864.73 (+2.84%) 🔴", "汽车与互联网龙头强劲，恒科指反弹近3%"),
    ("主力资金分化 (Flow)", "部分核心龙头获增仓 🟢", "长鑫茅台等个股吸金，紫光股份净流出居前"),
    ("沪深两市成交 (Volume)", "2.30万亿元 (放量2700亿) 🔴", "量能明显放大，重回2.3万亿元上方"),
    ("央行流动性投放 (PBOC)", "6,000亿元 (逆回购) 🔴", "启动超常规隔夜流动性投放，平稳跨月跨季")
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
output_path = "images/charts/2026-07-29-evening.png"
plt.savefig(output_path, dpi=300, bbox_inches='tight', facecolor=fig.get_facecolor())
plt.close()
print(f"Chart saved to {output_path}")
