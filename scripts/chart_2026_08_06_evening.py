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
ax.text(0.05, 0.93, "【沪指站上3900点呈分化行情，两市成交2.53万亿现分歧缩量】(2026/08/06 周四晚报)", fontproperties=prop, fontsize=14, fontweight='bold', color='#1e293b')
ax.axhline(y=0.88, xmin=0.04, xmax=0.96, color='#cbd5e1', linewidth=1.5)

# Left Side: Key Market Events
ax.text(0.06, 0.82, "▌ 今日市场核心动向要闻", fontproperties=prop, fontsize=12, fontweight='bold', color='#0f172a')

events = [
    ("A股三大指数震荡分化，沪指重回3900点收涨0.57%", "上证综指收报3900.35点，深成指跌0.24%报14110.12点，创业板指跌0.55%", "前几日连阳大反弹后迎来分歧整理，个股涨多跌少"),
    ("煤炭资源与周期红利大爆发，多股涨停掀起板块高潮", "煤炭开采加工全天领涨，昊华能源、潞安环能、淮北矿业等封死涨停", "大宗商品金价高位提振贵金属走强，红利资产受防守资金青睐"),
    ("两市成交缩量至2.53万亿，主力资金呈规模净流出", "沪深两市合计成交2.53万亿元，较昨日缩量1309亿，主力净流出380亿", "主力资金偏向CPO、PCB等科技硬件拿筹，高标爱丽家居录得10连板"),
    ("港股受压窄幅震荡下行，恒生指数收跌1.49%失守二万六", "恒生指数收报25530.28点，受海外流动性压力与外围科技回调拖累", "央行开展10亿逆回购操作利率不变，持续引导适度宽松货币预期")
]

y = 0.72
for title, val, note in events:
    ax.text(0.08, y, title, fontproperties=prop, fontsize=10.5, color='#334155', fontweight='bold')
    ax.text(0.08, y-0.035, f"{val}\n{note}", fontproperties=prop, fontsize=9.0, color='#64748b')
    y -= 0.11

# Right Side: Market Indicators & Assets
ax.text(0.56, 0.82, "▌ 核心指数表现与涨跌一览", fontproperties=prop, fontsize=12, fontweight='bold', color='#0f172a')

asset_data = [
    ("上证指数 (SSEC)", "3,900.35 (日: +0.57% / 震荡收红) 🔴", "煤炭及周期权重股护盘拉升，沪指重回3900点"),
    ("深证成指 (SZI)", "14,110.12 (日: -0.24% / 弱势整理) 🟢", "题材股分化，创业板及深成指受部分成长权重压制"),
    ("创业板指 (CHINEXT)", "3,515.56 (日: -0.55% / 震荡收绿) 🟢", "新能源与权重医药走弱，指数午后承压调整"),
    ("科创50 (STAR50)", "1,701.29 (日: +0.45% / 延续活跃) 🔴", "半导体化学品、芯片封装及6G概念发力抗跌"),
    ("北证50 (BSE50)", "1,122.88 (日: +0.31% / 窄幅收红) 🔴", "题材轮动活跃，北交所个股抗跌性较好"),
    ("恒生指数 (HSI)", "25,530.28 (日: -1.49% / 弱势震荡) 🟢", "科技股受外围压制，权重股回调拖累指数收绿"),
    ("沪深两市成交额 (Turnover)", "2.53万亿 (较前一日缩量1309亿) 🟢", "连续大涨后资金观望意愿上升，呈现缩量整理特征")
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
output_path = "images/charts/2026-08-06-evening.png"
plt.savefig(output_path, dpi=300, bbox_inches='tight', facecolor=fig.get_facecolor())
plt.close()
print(f"Chart saved to {output_path}")
