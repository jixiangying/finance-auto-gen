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

fig, ax = plt.subplots(figsize=(12.0, 8.5))
fig.patch.set_facecolor('#f8fafc')
ax.set_facecolor('#ffffff')
ax.set_xlim(0, 1)
ax.set_ylim(0, 1)
ax.axis('off')

# Title
ax.text(0.05, 0.94, "【全球市场周末复盘：非农爆冷助推科技股，黄金飙升油价大跌】(2026/08/08 周六晚报)", fontproperties=prop, fontsize=14, fontweight='bold', color='#1e293b')
ax.axhline(y=0.89, xmin=0.04, xmax=0.96, color='#cbd5e1', linewidth=1.5)

# Left Side: Key Market Events / Outlook
ax.text(0.06, 0.84, "▌ 本周全球宏观与核心事件复盘", fontproperties=prop, fontsize=12, fontweight='bold', color='#0f172a')

events = [
    ("美国7月非农就业意外爆冷，降息预期大幅重塑", "7月非农就业减少2.3万人(预期增8万)，失业率降至4.1%(主要由于参与率降低)", "美联储9月加息预期瞬间熄火，市场降息呼声高涨，美元走弱，美股标普创历史新高"),
    ("A股在7月调整后迎来大捷，科创50指数单周暴涨12%", "主要宽基指数周内连续反弹，科创50本周大涨12%，创业板涨近8%，沪指涨3.4%", "大资金高低切换，资金流出红利板块回流CXO创新药与AI算力硬件，做多热情激活"),
    ("地缘政治局势暂现缓和，原油价格全周大跌超7%", "伊朗与阿曼达成维持霍尔木兹海峡60天开放的暂定协议框架，原油溢价大幅消退", "布伦特原油收报83.37美元/桶，全周累计下跌超7.0%，原油单周回踩前期平台支撑"),
    ("避险与降息预期共振，黄金白银全周飙涨创新高", "COMEX黄金期货收盘突破4300.7美元/盎司，本周累计涨幅约5%，创近期最大单周涨幅", "美联储货币政策转向确定性增强，叠加中东地缘遗留风险，黄金多头重夺市场主动权")
]

y = 0.74
for title, val, note in events:
    ax.text(0.08, y, title, fontproperties=prop, fontsize=10.5, color='#334155', fontweight='bold')
    ax.text(0.08, y-0.032, f"{val}\n{note}", fontproperties=prop, fontsize=9.0, color='#64748b')
    y -= 0.105

# Right Side: Market Indicators & Assets
ax.text(0.56, 0.84, "▌ 核心资产本周及日度表现 (8月3日 - 8月7日)", fontproperties=prop, fontsize=12, fontweight='bold', color='#0f172a')

asset_data = [
    ("上证指数 (SSEC)", "3,940.04 (周五: +1.02% 🔴 / 全周: +3.40% 🔴)", "连收四阳重返3900上方，成长赛道彻底激活"),
    ("深证成指 (SZI)", "14,311.01 (周五: +1.42% 🔴 / 全周: +6.40% 🔴)", "科技板块本周大举吸筹，均线系统强力向上支撑"),
    ("创业板指 (CHINEXT)", "3,563.12 (周五: +1.35% 🔴 / 全周: +8.00% 🔴)", "CXO龙头与医药权重股全周引领市场爆发式补涨"),
    ("科创50 (STAR50)", "1,744.02 (周五: +2.51% 🔴 / 全周: +12.00% 🔴)", "本周表现冠绝全球，算力及半导体软硬件掀涨停潮"),
    ("恒生指数 (HSI)", "25,668.03 (周五: +0.54% 🔴 / 全周: -0.84% 🟢)", "结束连续五周上涨，全周小幅整理但科技股抗跌"),
    ("标普500指数 (S&P 500)", "7,757.64 (周五: +0.62% 🔴 / 全周: +3.50% 🔴)", "非农爆冷刺激分母端，周五收盘创历史新高"),
    ("纳斯达克 (Nasdaq)", "26,690.62 (周五: +1.30% 🔴 / 全周: +5.00% 🔴)", "分母端定价最敏感的科技权重全周领跑美股市场"),
    ("COMEX黄金 (Gold)", "4,300.70 美元 (周五: 震荡整理 / 全周: +5.00% 🔴)", "避险与美联储降息预期双轨驱动，周线放量长阳"),
    ("布伦特原油 (Brent)", "83.37 美元 (周五: +1.00% 🔴 / 全周: -7.00% 🟢)", "霍尔木兹海峡协议框架缓和局势，油价溢价退潮")
]

y_right = 0.74
for title, val, comment in asset_data:
    ax.text(0.58, y_right, title, fontproperties=prop, fontsize=10.0, color='#334155', fontweight='bold')
    
    # Analyze color based on last character in val
    if '🔴' in val and '🟢' in val:
        # mixed case, let's split or default to color based on weekly
        color = '#ef4444' if val.count('🔴') > val.count('🟢') else '#10b981'
    elif '🔴' in val:
        color = '#ef4444'
    elif '🟢' in val:
        color = '#10b981'
    else:
        color = '#334155'
        
    clean_val = val.replace('🟢', '').replace('🔴', '')
    
    # Draw value with corresponding color
    ax.text(0.58, y_right-0.030, clean_val, fontproperties=prop, fontsize=8.5, fontweight='bold', color=color)
    # Draw comment next to it
    val_width = len(clean_val) * 0.0068 + 0.02
    ax.text(0.58 + val_width, y_right-0.030, f"|  {comment}", fontproperties=prop, fontsize=8.5, color='#64748b')
    
    y_right -= 0.055

plt.tight_layout()
output_path = "images/charts/2026-08-08-evening.png"
plt.savefig(output_path, dpi=300, bbox_inches='tight', facecolor=fig.get_facecolor())
plt.close()
print(f"Chart saved to {output_path}")
