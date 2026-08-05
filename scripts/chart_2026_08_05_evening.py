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
ax.text(0.05, 0.93, "【沪指大涨1.47%放量收复失地，全市场成交额达2.66万亿】(2026/08/05 周三晚报)", fontproperties=prop, fontsize=14, fontweight='bold', color='#1e293b')
ax.axhline(y=0.88, xmin=0.04, xmax=0.96, color='#cbd5e1', linewidth=1.5)

# Left Side: Key Market Events
ax.text(0.06, 0.82, "▌ 今日市场核心动向要闻", fontproperties=prop, fontsize=12, fontweight='bold', color='#0f172a')

events = [
    ("A股三大指数共振收涨，上证指数大涨1.47%收复失地", "上证指数报3878.43点，深成指涨1.86%报14144.20点，创业板指涨1.32%", "全市场超4000只个股收涨，多头氛围极其强烈"),
    ("科创50指数强势狂飙4.78%，存储芯片与光刻机板块领涨", "科创50报1693.67点涨幅居首，存储芯片、光刻机、电子化学品大面积爆发", "国家自动驾驶系统安全标准发布、半导体国产替代高潮刺激硬科技反弹"),
    ("央行开展5000亿买断式逆回购，实现净投放2000亿元", "3个月期限操作维持流动性充裕，平稳跨月并对冲到期3000亿存量逆回购", "延续适度宽松的货币政策基调，支持实体经济并强化逆周期调节"),
    ("港股冲高回落集体收涨，恒生科技指数收涨0.97%", "恒指收涨0.24%报25915.82点，黄金及贵金属、PCB概念股走势活跃", "证监会深化与香港资本市场合作，提升两地协同发展和资金吸引力")
]

y = 0.72
for title, val, note in events:
    ax.text(0.08, y, title, fontproperties=prop, fontsize=10.5, color='#334155', fontweight='bold')
    ax.text(0.08, y-0.035, f"{val}\n{note}", fontproperties=prop, fontsize=9.0, color='#64748b')
    y -= 0.11

# Right Side: Market Indicators & Assets
ax.text(0.56, 0.82, "▌ 核心指数表现与涨跌一览", fontproperties=prop, fontsize=12, fontweight='bold', color='#0f172a')

asset_data = [
    ("上证指数 (SSEC)", "3,878.43 (日: +1.47% / 强劲大涨) 🔴", "收复失地，小盘成长与大盘蓝筹共振收红"),
    ("深证成指 (SZI)", "14,144.20 (日: +1.86% / 大幅拉升) 🔴", "成长白马及题材股全线走强，多头均线发散"),
    ("创业板指 (CHINEXT)", "3,535.14 (日: +1.32% / 延续涨势) 🔴", "医疗及科技板块领跑，权重成长股持续走强"),
    ("科创50 (STAR50)", "1,693.67 (日: +4.78% / 狂飙突进) 🔴", "半导体硬科技及光刻机概念爆发，领涨宽基指数"),
    ("恒生指数 (HSI)", "25,915.82 (日: +0.24% / 窄幅收涨) 🔴", "黄金股活跃，金融权重反弹拉动恒指收红"),
    ("恒生科技 (HSTECH)", "4,933.07 (日: +0.97% / 稳步上行) 🔴", "半导体与消费电子走强，互联网龙头小幅回暖"),
    ("沪深两市成交额 (Turnover)", "2.66万亿 (较前一日放量超4300亿) 🔴", "成交额创近期新高，场外资金呈现规模性回流")
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
output_path = "images/charts/2026-08-05-evening.png"
plt.savefig(output_path, dpi=300, bbox_inches='tight', facecolor=fig.get_facecolor())
plt.close()
print(f"Chart saved to {output_path}")
