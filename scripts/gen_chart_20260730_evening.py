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
ax.text(0.05, 0.93, "【每日市场收盘与核心资产盘点】(2026/07/30 周四晚报)", fontproperties=prop, fontsize=14, fontweight='bold', color='#1e293b')
ax.axhline(y=0.88, xmin=0.04, xmax=0.96, color='#cbd5e1', linewidth=1.5)

# Left Side: Key Market Events
ax.text(0.06, 0.82, "▌ 今日重磅事件与政策汇总", fontproperties=prop, fontsize=12, fontweight='bold', color='#0f172a')

events = [
    ("A股三大指数放量调整，科技成长板块集体走弱", "创业板指跌3.97%，科创50跌5.38%，深成指跌2.73%", "半导体与CPO板块大跌，大消费与大金融板块逆势护盘"),
    ("主力资金高低切换明显，科技股遭大举减持", "中际旭创、寒武纪、新易盛等AI核心硬件主力出逃居前", "资金流向低估值的食品饮料、白酒及防御性银行股"),
    ("央行继续组合工具投放流动性，力保月末平稳", "开展2705亿元7天期逆回购与6000亿元隔夜逆回购投放", "7天逆回购利率维持1.40%持平，有效对冲月末资金面波动"),
    ("港股市场探底回稳，恒生指数逆势小幅微涨", "恒生指数涨0.20%报25858点，港股成交额超1620亿港元", "恒生科技受成长股走弱拖累跌1.25%，市场分化格局延续")
]

y = 0.72
for title, val, note in events:
    ax.text(0.08, y, title, fontproperties=prop, fontsize=10.5, color='#334155', fontweight='bold')
    ax.text(0.08, y-0.035, f"{val}\n{note}", fontproperties=prop, fontsize=9.0, color='#64748b')
    y -= 0.11

# Right Side: Market Indicators & Assets
ax.text(0.56, 0.82, "▌ 核心资产表现与今日收盘", fontproperties=prop, fontsize=12, fontweight='bold', color='#0f172a')

asset_data = [
    ("上证指数 (SSEC)", "3,804.69 (-0.62%) 🟢", "大消费及银行护盘，沪指表现相对抗跌"),
    ("深证成指 (SZCOMP)", "13,285.80 (-2.73%) 🟢", "科技及成长股拖累，深成指放量回调较深"),
    ("创业板指 (CHINEXT)", "3,244.62 (-3.97%) 🟢", "高位权重股遭到抛售，创业板指大跌近4%"),
    ("科创50 (STAR50)", "1,588.41 (-5.38%) 🟢", "半导体及算力硬件重挫，指数跌超5%"),
    ("恒生指数 (HSI)", "25,858.88 (+0.20%) 🔴", "微涨超50点，红筹及价值蓝筹提供关键支撑"),
    ("恒生科技 (HSTECH)", "4,803.77 (-1.25%) 🟢", "网联及科网龙头分化，科技指数跑输大盘"),
    ("沪深两市成交 (Volume)", "2.34万亿元 (放量462亿) 🔴", "市场大举换手放量，连续多日维持两万亿上方"),
    ("央行流动性投放 (PBOC)", "组合投放稳定跨月 🔴", "2705亿7天+6000亿隔夜，利率走廊调控平稳")
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
output_path = "images/charts/2026-07-30-evening.png"
plt.savefig(output_path, dpi=300, bbox_inches='tight', facecolor=fig.get_facecolor())
plt.close()
print(f"Chart saved to {output_path}")
