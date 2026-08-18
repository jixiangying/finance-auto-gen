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
ax.text(0.05, 0.93, "【每日市场复盘与核心资产表现】(2026/08/18 周二晚报)", fontproperties=prop, fontsize=14, fontweight='bold', color='#1e293b')
ax.axhline(y=0.88, xmin=0.04, xmax=0.96, color='#cbd5e1', linewidth=1.5)

# Left Side: Key Market Events
ax.text(0.06, 0.82, "▌ 今日核心热点与政策脉动", fontproperties=prop, fontsize=12, fontweight='bold', color='#0f172a')

events = [
    ("A股探底回升走势分化，两市成交额达2.42万亿元", "上证指数微涨0.19%报3990.30点，创业板指回调0.93%", "全市场超3900只个股调整，北证50放量领涨+2.67%"),
    ("农业与信创午后爆发，机器人大会在即概念活跃", "受全球粮食危机预警驱动种植业、猪肉及渔业多股涨停", "世界机器人大会明日开幕人形机器人催化，算力与芯片调整"),
    ("统计局定调前7月经济大盘，产业政策赋能下沉市场", "高技术制造与服务消费保持韧性，财政协同促内需呼声渐高", "商务部等9部门促县域消费，上海出台软件服务业十五五规划"),
    ("机构看好中报业绩确定性，关注AI硬件与电网出海", "中金/华泰认为A股向上趋势基础未变，关注中观景气扩散", "中信证券强调银行基本面与科技融资红利，红利与成长均衡")
]

y = 0.72
for title, val, note in events:
    ax.text(0.08, y, title, fontproperties=prop, fontsize=10.5, color='#334155', fontweight='bold')
    ax.text(0.08, y-0.035, f"{val}\n{note}", fontproperties=prop, fontsize=9.0, color='#64748b')
    y -= 0.11

# Right Side: Market Indicators & Assets
ax.text(0.56, 0.82, "▌ 全球及国内核心资产今日表现", fontproperties=prop, fontsize=12, fontweight='bold', color='#0f172a')

asset_data = [
    ("上证指数 (SSEC)", "3,990.30 (+0.19%) 🔴", "探底回升逼近4000点，红利权重托底"),
    ("深证成指 (SZI)", "14,622.50 (-0.56%) 🟢", "成长板块分化回调，个股跌多涨少"),
    ("创业板指 (CHINEXT)", "3,705.56 (-0.93%) 🟢", "算力与芯片回调压制指数，均线整固"),
    ("科创50 (STAR50)", "1,790.82 (+0.11%) 🔴", "硬科技高位窄幅震荡，软件信创接力"),
    ("北证50 (BSE50)", "1,428.65 (+2.67%) 🔴", "专精特新概念受资金热炒，放量大涨"),
    ("恒生指数 (HSI)", "25,471.15 (+0.07%) 🔴", "维持25,000点上方窄幅震荡整固"),
    ("恒生科技 (HSTECH)", "4,739.18 (-0.90%) 🟢", "港股科技股分化调整，交投维持活跃"),
    ("沪深两市成交额", "2.42万亿元 🔴", "交投活跃度保持高位，结构性轮动")
]

y_right = 0.72
for title, val, comment in asset_data:
    ax.text(0.58, y_right, title, fontproperties=prop, fontsize=10.5, color='#334155', fontweight='bold')
    
    color = '#ef4444' if '🔴' in val else '#10b981'
    clean_val = val.replace('🟢', '').replace('🔴', '')
    
    ax.text(0.58, y_right-0.026, clean_val, fontproperties=prop, fontsize=9.0, fontweight='bold', color=color)
    val_width = len(clean_val) * 0.0068 + 0.025
    ax.text(0.58 + val_width, y_right-0.026, f"|  {comment}", fontproperties=prop, fontsize=9.0, color='#64748b')
    
    y_right -= 0.052

plt.tight_layout()
output_path = "images/charts/2026-08-18-evening.png"
plt.savefig(output_path, dpi=300, bbox_inches='tight', facecolor=fig.get_facecolor())
plt.close()
print(f"Chart saved to {output_path}")
