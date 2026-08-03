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
ax.text(0.05, 0.93, "【A股震荡缩量科创深回调，港股迎开门红突破26000】(2026/08/03 周一晚报)", fontproperties=prop, fontsize=14, fontweight='bold', color='#1e293b')
ax.axhline(y=0.88, xmin=0.04, xmax=0.96, color='#cbd5e1', linewidth=1.5)

# Left Side: Key Market Events
ax.text(0.06, 0.82, "▌ 今日市场核心动向要闻", fontproperties=prop, fontsize=12, fontweight='bold', color='#0f172a')

events = [
    ("A股三大指数震荡走弱，沪指收报3809.66点", "沪指收跌0.59%，深成指跌0.96%，创业板指跌1.24%", "全天呈现缩量震荡格局，多头追高意愿受限"),
    ("科创50指数暴跌5.08%，半导体及存储概念重挫", "芯片半导体板块显著回调，领跌两市，资金流出明显", "前期累积获利盘集中回吐，多只权重半导体股跌幅居前"),
    ("核电及人形机器人逆势走强，个股呈现普涨", "全市场超4000只个股上涨，中国核建、合锻智能等多股涨停", "中小微盘股表现活跃，与大盘股及科技权重形成跷跷板"),
    ("港股迎8月开门红站上26000，科网股领涨", "恒指涨0.48%收26009.4点，恒生科技指数大涨0.96%", "阿里巴巴-W大涨超7%，港交所下调股票最低上落价位刺激成交")
]

y = 0.72
for title, val, note in events:
    ax.text(0.08, y, title, fontproperties=prop, fontsize=10.5, color='#334155', fontweight='bold')
    ax.text(0.08, y-0.035, f"{val}\n{note}", fontproperties=prop, fontsize=9.0, color='#64748b')
    y -= 0.11

# Right Side: Market Indicators & Assets
ax.text(0.56, 0.82, "▌ 核心指数表现与涨跌一览", fontproperties=prop, fontsize=12, fontweight='bold', color='#0f172a')

asset_data = [
    ("上证指数 (SSEC)", "3,809.66 (日: -0.59% / 震荡回调) 🟢", "主力防守，量能不足下回踩支撑位"),
    ("深证成指 (SZI)", "13,448.29 (日: -0.96% / 偏弱调整) 🟢", "深市股指震荡下行，白马股资金流出"),
    ("创业板指 (CHINEXT)", "3,302.55 (日: -1.24% / 弱势整理) 🟢", "新能源等权重股疲软，创业板承压明显"),
    ("科创50 (STAR50)", "1,552.89 (日: -5.08% / 泥沙俱下) 🟢", "半导体存储板块回调，回吐近期全部涨幅"),
    ("恒生指数 (HSI)", "26,009.40 (日: +0.48% / 突破新高) 🔴", "港交所价差新规首日，买盘情绪活跃"),
    ("恒生科技 (HSTECH)", "4,875.61 (日: +0.96% / 科网领涨) 🔴", "阿里大涨超7%领衔拉升，恒科指反弹"),
    ("沪深两市成交额 (Turnover)", "2.01万亿 (较前一日缩量超5000亿) 🟢", "量能回落，资金趋于谨慎观望")
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
output_path = "images/charts/2026-08-03-evening.png"
plt.savefig(output_path, dpi=300, bbox_inches='tight', facecolor=fig.get_facecolor())
plt.close()
print(f"Chart saved to {output_path}")
