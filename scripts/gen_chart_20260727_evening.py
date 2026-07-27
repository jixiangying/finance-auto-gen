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
ax.text(0.05, 0.93, "【每日市场收盘与核心资产盘点】(2026/07/27 周一晚报)", fontproperties=prop, fontsize=14, fontweight='bold', color='#1e293b')
ax.axhline(y=0.88, xmin=0.04, xmax=0.96, color='#cbd5e1', linewidth=1.5)

# Left Side: Key Market Events
ax.text(0.06, 0.82, "▌ 今日重磅事件与政策汇总", fontproperties=prop, fontsize=12, fontweight='bold', color='#0f172a')

events = [
    ("长鑫科技科创板挂牌上市，天量成交创历史", "首日大涨465.82%报49.00元，单日成交额达1411.87亿元", "总市值登顶A股首位(3.28万亿元)，半导体板块掀普涨狂潮"),
    ("央行流动性精准呵护，预告隔夜逆回购安排", "今日开展3255亿逆回购，预告跨月隔夜逆回购精准调控", "稳定跨月资金面表现，合理匹配银行短期流动性需求"),
    ("证监会多场座谈会，强化逆周期稳市部署", "部署重点工作维护平稳运行，推动中长期资金稳步入市", "加强防范全球市场风险跨境传导，强调从严惩治财务造假"),
    ("两高内幕交易刑事司法新规自今日起实施", "新内幕交易司法解释正式施行，加大资本市场执法威慑", "促进资本市场高质量发展，为健康交易筑牢法治底线")
]

y = 0.72
for title, val, note in events:
    ax.text(0.08, y, title, fontproperties=prop, fontsize=10.5, color='#334155', fontweight='bold')
    ax.text(0.08, y-0.035, f"{val}\n{note}", fontproperties=prop, fontsize=9.0, color='#64748b')
    y -= 0.11

# Right Side: Market Indicators & Assets
ax.text(0.56, 0.82, "▌ 核心资产表现与今日收盘", fontproperties=prop, fontsize=12, fontweight='bold', color='#0f172a')

asset_data = [
    ("上证指数 (SSEC)", "3,858.25 (+1.15%) 🔴", "收复失地站稳3800点，多头力量占优"),
    ("深证成指 (SZCOMP)", "14,148.73 (+2.72%) 🔴", "科技成长股领涨，市场呈现普涨行情"),
    ("创业板指 (CHINEXT)", "3,590.79 (+3.16%) 🔴", "风格偏向高弹性板块，人气彻底激活"),
    ("恒生指数 (HSI)", "25,217.49 (+0.98%) 🔴", "重上25000点整数关口，大型科网股领涨"),
    ("恒生科技 (HSTECH)", "4,704.30 (+1.57%) 🔴", "小米/腾讯等权重普涨，科网股反弹明确"),
    ("长鑫科技 (688825.SH)", "49.00 (+465.82%) 🔴", "上市首日登顶A股市值榜首，提振科技信心"),
    ("沪深京成交额 (Volume)", "2.09万亿元 (大幅放量) 🔴", "两市成交显著放大，近5200只个股飘红"),
    ("央行流动性投放 (PBOC)", "3,255亿元 (逆回购) 🔴", "精准呵护跨月需求，稳定短期资金预期")
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
output_path = "images/charts/2026-07-27-evening.png"
plt.savefig(output_path, dpi=300, bbox_inches='tight', facecolor=fig.get_facecolor())
plt.close()
print(f"Chart saved to {output_path}")
