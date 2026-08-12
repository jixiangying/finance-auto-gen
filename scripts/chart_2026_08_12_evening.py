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
ax.text(0.04, 0.94, "【常规交易日：A股震荡反弹半导体算力爆发，两市成交额2.15万亿，港股承压回调】(2026/08/12 周三晚报)", fontproperties=prop, fontsize=14, fontweight='bold', color='#1e293b')
ax.axhline(y=0.90, xmin=0.03, xmax=0.97, color='#cbd5e1', linewidth=1.5)

# Left Side: Key Market Events / Outlook
ax.text(0.05, 0.84, "▌ 核心行情复盘与主力资金流向", fontproperties=prop, fontsize=12, fontweight='bold', color='#0f172a')

events = [
    ("A股三大指数全线收涨，科技成长赛道领涨", 
     "创业板指大涨1.49%，深证成指涨1.09%，沪指涨0.32%。", 
     "全市场超4100只个股飘红，做多情绪显著回暖。"),
    ("算力硬件产业链全线爆发，半导体芯片强势吸金", 
     "CPO、光纤通信、存储芯片、算力租赁等细分领涨。", 
     "上海发布软件与服务“十五五”规划，人工智能核心环节受强支撑。"),
    ("两市成交总额2.15万亿元，呈现温和缩量", 
     "两市合计成交约2.15万亿，较前一交易日缩量。", 
     "目前市场仍呈存量博弈特征，主力资金偏好高弹性科技成长股。"),
    ("主力资金大幅流入超200亿元，科技股龙头获抢筹", 
     "通信、电子、半导体大幅净流入，通信板块超75亿元。", 
     "长鑫科技净流入超22亿元居首，中际旭创、新易盛等吸金居前。"),
    ("港股市场震荡走弱，科网股及原材料走低压制大市", 
     "恒指收跌0.83%报25440.17点，恒生科技指数跌0.99%。", 
     "市场在美联储关键CPI数据发布前保持防御，资金观望情绪较浓。")
]

y = 0.75
for title, val, note in events:
    ax.text(0.06, y, f"• {title}", fontproperties=prop, fontsize=10.5, color='#334155', fontweight='bold')
    ax.text(0.06, y-0.030, f"  焦点: {val}\n  分析: {note}", fontproperties=prop, fontsize=9.0, color='#64748b')
    y -= 0.105

# Right Side: Market Indicators & Assets
ax.text(0.55, 0.84, "▌ 核心资产今日表现", fontproperties=prop, fontsize=12, fontweight='bold', color='#0f172a')

asset_data = [
    ("上证指数 (SSEC)", "3,946.68", "今日: +0.32% 🔴"),
    ("深证成指 (SZCOMP)", "14,414.43", "今日: +1.09% 🔴"),
    ("创业板指 (Chinext)", "3,602.08", "今日: +1.49% 🔴"),
    ("科创50指数 (STAR50)", "1,020.12", "今日: +1.61% 🔴"),
    ("恒生指数 (HSI)", "25,440.17", "今日: -0.83% 🟢"),
    ("恒生科技指数 (HSTECH)", "4,776.44", "今日: -0.99% 🟢"),
    ("长鑫科技 (60xxxx)", "主力净流入", "今日: +22亿元 🔴"),
    ("沪深两市成交额", "2.15万亿元", "今日: 较前一日缩量 🟢"),
    ("通信行业主力资金", "净流入超75亿", "今日: 行业流入居首 🔴")
]

y_right = 0.75
for title, price, perf in asset_data:
    ax.text(0.57, y_right, title, fontproperties=prop, fontsize=10.0, color='#334155', fontweight='bold')
    
    color = '#ef4444' if '🔴' in perf else '#10b981'
    clean_perf = perf.replace('🟢', '').replace('🔴', '')
    
    # Draw price
    ax.text(0.57, y_right-0.026, f"现价/状态: {price}", fontproperties=prop, fontsize=9.0, color='#475569')
    # Draw performance
    ax.text(0.74, y_right-0.026, f"|  {clean_perf}", fontproperties=prop, fontsize=9.0, fontweight='bold', color=color)
    
    y_right -= 0.058

plt.tight_layout()
output_path = "images/charts/2026-08-12-evening.png"
plt.savefig(output_path, dpi=300, bbox_inches='tight', facecolor=fig.get_facecolor())
plt.close()
print(f"Chart saved to {output_path}")
