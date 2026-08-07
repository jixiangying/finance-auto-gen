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
ax.text(0.05, 0.93, "【成长主线共振爆发：创新药与PCB掀涨停潮，成交额突破2.66万亿】(2026/08/07 周五晚报)", fontproperties=prop, fontsize=14, fontweight='bold', color='#1e293b')
ax.axhline(y=0.88, xmin=0.04, xmax=0.96, color='#cbd5e1', linewidth=1.5)

# Left Side: Key Market Events / Outlook
ax.text(0.06, 0.82, "▌ 今日市场核心动向要闻", fontproperties=prop, fontsize=12, fontweight='bold', color='#0f172a')

events = [
    ("创新药与CRO板块大爆发，龙头业绩回暖提振景气", "多家龙头中报亮眼或上调业绩指引，License-out出海额大幅增长", "基本面底部验证+全球医药并购回暖，CXO产业链出现低配共振修复"),
    ("PCB及覆铜板供应链掀涨停潮，AI算力硬件持续拉动", "8月电子布与CCL价格延续成本传导，高盛上调算力服务器PCB预期", "宝鼎科技、华正新材等封板，英伟达等核心算力需求高企支撑景气度"),
    ("沪深两市放量普涨，成交额创近期新高", "沪深两市全天合计成交2.66万亿元，较前一交易日放量1356亿元", "约2800只个股收涨，成长赛道分流红利资金，多空热度明显提升"),
    ("宽基指数全线飘红，科创50暴涨2.51%", "沪指收涨1.02%逼近3950点，创业板指涨1.35%，深成指涨1.42%", "主力大举增配科技成长与医药股，市场情绪在震荡中转为积极")
]

y = 0.72
for title, val, note in events:
    ax.text(0.08, y, title, fontproperties=prop, fontsize=10.5, color='#334155', fontweight='bold')
    ax.text(0.08, y-0.035, f"{val}\n{note}", fontproperties=prop, fontsize=9.0, color='#64748b')
    y -= 0.11

# Right Side: Market Indicators & Assets
ax.text(0.56, 0.82, "▌ 核心资产最新价格与变化", fontproperties=prop, fontsize=12, fontweight='bold', color='#0f172a')

asset_data = [
    ("上证指数 (SSEC)", "3,940.04 (日: +1.02% / 放量大涨) 🔴", "收复3900点后再度冲高，全天单边走强"),
    ("深证成指 (SZI)", "14,311.01 (日: +1.42% / 题材活跃) 🔴", "成长题材大面积飘红，成分股普遍拉升"),
    ("创业板指 (CHINEXT)", "3,563.12 (日: +1.35% / 强势冲高) 🔴", "CXO医药与科技权重股共振拉升"),
    ("科创50 (STAR50)", "1,744.02 (日: +2.51% / 领涨全场) 🔴", "芯片硬件及前沿科技掀起涨停潮"),
    ("恒生指数 (HSI)", "25,667.62 (日: +0.54% / 温和收涨) 🔴", "医药生物股领涨，红利资产小幅调整"),
    ("北证50 (BSE50)", "1,134.24 (日: +1.01% / 稳健向上) 🔴", "北交所个股轮动活跃，均线系统支撑"),
    ("成交额表现 (Turnover)", "2.66万亿元 (日: +1356亿元 / 显著放量) 🔴", "沪深两市全天大幅放量，市场人气高涨")
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
output_path = "images/charts/2026-08-07-evening.png"
plt.savefig(output_path, dpi=300, bbox_inches='tight', facecolor=fig.get_facecolor())
plt.close()
print(f"Chart saved to {output_path}")
