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
ax.text(0.04, 0.94, "【常规交易日：A股高开午后跳水，医药逆势领涨，成交额放量至2.55万亿，央行发布货币政策报告】(2026/08/13 周四晚报)", fontproperties=prop, fontsize=14, fontweight='bold', color='#1e293b')
ax.axhline(y=0.90, xmin=0.03, xmax=0.97, color='#cbd5e1', linewidth=1.5)

# Left Side: Key Market Events / Outlook
ax.text(0.05, 0.84, "▌ 核心行情复盘与政策面动向", fontproperties=prop, fontsize=12, fontweight='bold', color='#0f172a')

events = [
    ("A股三大指数冲高回落，尾盘遭遇快速跳水", 
     "上证指数收跌0.50%报3926.96点，深成指跌0.87%，创业板指跌0.45%。", 
     "全市场超4300只个股飘绿，早盘高开后午后抛压加剧，赚钱效应减弱。"),
    ("医药生物板块逆势领涨，创新药与CXO表现亮眼", 
     "博济医药、万邦医药、陇神戎发20CM涨停，医疗服务大涨。", 
     "业绩改善、出海授权逻辑和政策见底红利，促使医药成为避险主阵地。"),
    ("全市场成交额突破2.55万亿元，较昨日放量约4000亿", 
     "两市合计成交约2.55万亿，放量冲高显示资金在尾盘高位套现离场。", 
     "资金博弈激烈，跷跷板效应明显，程序化交易主导成长与红利的轮动。"),
    ("央行发布二季度货币政策报告，释放适度宽松信号", 
     "明确强调加大逆周期调节力度，淡化对贷款单一通道关注。", 
     "预告月中新增隔夜逆回购工具（日限额6000亿），管理短端流动性。"),
    ("港股维持窄幅震荡，恒生科技指数微涨0.33%", 
     "恒指微跌0.17%报25396.51点，恒生科技收涨0.33%报4792.39点。", 
     "在全球央行决策及关键宏观数据前，港股整体呈现防守特征。")
]

y = 0.75
for title, val, note in events:
    ax.text(0.06, y, f"• {title}", fontproperties=prop, fontsize=10.5, color='#334155', fontweight='bold')
    ax.text(0.06, y-0.030, f"  焦点: {val}\n  分析: {note}", fontproperties=prop, fontsize=9.0, color='#64748b')
    y -= 0.105

# Right Side: Market Indicators & Assets
ax.text(0.55, 0.84, "▌ 核心资产今日表现", fontproperties=prop, fontsize=12, fontweight='bold', color='#0f172a')

asset_data = [
    ("上证指数 (SSEC)", "3,926.96", "今日: -0.50% 🟢"),
    ("深证成指 (SZCOMP)", "14,289.44", "今日: -0.87% 🟢"),
    ("创业板指 (Chinext)", "3,586.04", "今日: -0.45% 🟢"),
    ("科创50指数 (STAR50)", "1,717.75", "今日: -1.11% 🟢"),
    ("恒生指数 (HSI)", "25,396.51", "今日: -0.17% 🟢"),
    ("恒生科技指数 (HSTECH)", "4,792.39", "今日: +0.33% 🔴"),
    ("医药生物 (行业主题)", "博济/万邦等大涨", "今日: 逆势飘红领涨 🔴"),
    ("沪深两市成交额", "2.55万亿元", "今日: 较昨日大放量 🔴"),
    ("央行隔夜回购预告", "额度单日6000亿", "今日: 宽松流动性引导 🔴")
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
output_path = "images/charts/2026-08-13-evening.png"
plt.savefig(output_path, dpi=300, bbox_inches='tight', facecolor=fig.get_facecolor())
plt.close()
print(f"Chart saved to {output_path}")
