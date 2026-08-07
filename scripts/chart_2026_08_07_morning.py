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
ax.text(0.05, 0.93, "【美股回调：企业绩后指引不及预期，美债收益率反弹压制大市】(2026/08/07 周五早报)", fontproperties=prop, fontsize=14, fontweight='bold', color='#1e293b')
ax.axhline(y=0.88, xmin=0.04, xmax=0.96, color='#cbd5e1', linewidth=1.5)

# Left Side: Key Market Events / Outlook
ax.text(0.06, 0.82, "▌ 今日市场核心动向要闻", fontproperties=prop, fontsize=12, fontweight='bold', color='#0f172a')

events = [
    ("The Trade Desk业绩偏弱，大科技板块高位震荡", "TTD二季度营收$715M但指引未达内部标准，强调AI与测量重要性", "科技巨头高投入与估值剪刀差引关注，市场情绪在非农前偏向谨慎"),
    ("ConocoPhillips利润大增，原油价格反弹站上$82", "COP二季度利润达$39亿大超去年，原油与天然气价格大涨带来丰厚回报", "霍尔木兹海峡多边协议处于极限拉扯，地缘局势隐忧仍为原油提供支撑"),
    ("初请失业金人数录得19.9万，劳工市场仍具强韧性", "上周初请失业金微增至19.9万，连续第三周保持在20万下方", "非农就业报告发布在即，美联储前次会议9-3决议暗示加息担忧未消"),
    ("美股大市普遍收跌，美债收益率反弹施压估值", "道指跌0.85%报53,885点；纳指微跌0.06%，标普跌0.18%至7,710点", "10年期美债收益率升至4.68%，结束三连跌，美股非农前选择性调整")
]

y = 0.72
for title, val, note in events:
    ax.text(0.08, y, title, fontproperties=prop, fontsize=10.5, color='#334155', fontweight='bold')
    ax.text(0.08, y-0.035, f"{val}\n{note}", fontproperties=prop, fontsize=9.0, color='#64748b')
    y -= 0.11

# Right Side: Market Indicators & Assets
ax.text(0.56, 0.82, "▌ 核心资产最新价格与变化", fontproperties=prop, fontsize=12, fontweight='bold', color='#0f172a')

asset_data = [
    ("纳斯达克综合指数 (NASDAQ)", "26,348.00 (日: -0.06% / 震荡收跌) 🟢", "大科技股高位盘整，The Trade Desk指引偏弱拖累"),
    ("标普 500 指数 (S&P 500)", "7,710.00 (日: -0.18% / 小幅微调) 🟢", "蓝筹与科技分化，市场静待周五非农就业数据发布"),
    ("道琼斯工业指数 (DJIA)", "53,885.00 (日: -0.85% / 大幅回调) 🟢", "成分股大跌拖累道指回踩，回吐前期连涨涨幅"),
    ("布伦特原油期货 (Brent)", "$82.50 (日: +2.67% / 油价反弹) 🔴", "海峡谈判极限拉扯，地缘变数与业绩利好促油价走高"),
    ("COMEX 黄金期货 (Gold)", "$4,301.00 (日: +1.00% / 高位稳健) 🔴", "避险需求与通胀预期支撑，金价守住4300美元大关"),
    ("10年期美债收益率 (US10Y)", "4.680% (日: +6.4BP / 止跌反弹) 🔴", "降息预期受劳动力数据扰动，收益率结束三连跌"),
    ("比特币 (BTC)", "$64,420.00 (日: -0.80% / 窄幅震荡) 🟢", "缺乏强力催化剂，随美股走弱及风险偏好回落微调")
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
output_path = "images/charts/2026-08-07-morning.png"
plt.savefig(output_path, dpi=300, bbox_inches='tight', facecolor=fig.get_facecolor())
plt.close()
print(f"Chart saved to {output_path}")
