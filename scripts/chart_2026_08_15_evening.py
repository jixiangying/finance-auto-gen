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

fig, ax = plt.subplots(figsize=(14.0, 9.0))
fig.patch.set_facecolor('#f8fafc')
ax.set_facecolor('#ffffff')
ax.set_xlim(0, 1)
ax.set_ylim(0, 1)
ax.axis('off')

# Title
ax.text(0.04, 0.95, "【全球市场周末复盘：标普500创历史新高，存储股爆发，霍尔木兹海峡突发】(2026/08/15 周六晚报)", fontproperties=prop, fontsize=13, fontweight='bold', color='#1e293b')
ax.axhline(y=0.90, xmin=0.03, xmax=0.97, color='#cbd5e1', linewidth=1.5)

# Left Side: Key Market Events
ax.text(0.05, 0.86, "▌ 本周全球宏观与核心事件复盘", fontproperties=prop, fontsize=12, fontweight='bold', color='#0f172a')

events = [
    ("标普500指数周四创历史新高，美股本周小幅收涨",
     "道指本周跌0.56%；纳指涨0.14%；标普500涨0.36%；周四收盘创历史新高",
     "周五三大指数小幅收跌修正，存储、光通信超强，半导体设备股普跌"),
    ("DeepSeek正式涨价，AI平台从价格战转向智能竞争",
     "DeepSeek API最高涨11倍，DeepSeek V4 Pro正式版同步发布",
     "国产AI芯片迎价值重估预期，信创与AI应用主线逻辑持续强化"),
    ("霍尔木兹海峡突发事故，特朗普宣称主权引发市场震荡",
     "周六盘中加密市场9万人爆仓，油价短线波动；特朗普称将宣布霍尔木兹为美国领土",
     "伊朗回应\"完全掌控\"海峡，地缘风险溢价重燃，大宗商品市场高度警惕"),
    ("央行放大招：万亿元买断式逆回购注入6月期流动性",
     "8月14日，PBOC以固定数量、利率招标方式开展10000亿元买断式逆回购，期限185天",
     "7月金融数据：M2增速7.7%，社融余额463.27万亿，货币政策保持支持性立场")
]

y = 0.77
for title, val, note in events:
    ax.text(0.06, y, title, fontproperties=prop, fontsize=10.5, color='#334155', fontweight='bold')
    ax.text(0.06, y-0.030, val, fontproperties=prop, fontsize=9.0, color='#64748b')
    ax.text(0.06, y-0.054, note, fontproperties=prop, fontsize=8.5, color='#94a3b8')
    y -= 0.115

# Right Side: Market Indicators & Assets
ax.text(0.54, 0.86, "▌ 核心资产本周及日度表现 (8月11日 - 8月14日)", fontproperties=prop, fontsize=12, fontweight='bold', color='#0f172a')

asset_data = [
    ("上证指数 (SSEC)", "周五: 震荡调整 🟢 / 全周: 小幅收窄 🟢", "A股7月以来'夏日寒风'进入尾声，底部确认"),
    ("深证成指 (SZI)", "周五: 弱势整理 🟢 / 全周: AI应用驱动局部活跃", "AI应用下游板块蓄力，CRO/医药8月超跑CPO"),
    ("科创50 (STAR50)", "周五: 小幅震荡 / 全周: 关注A股新股次新股机会", "张忆东：8月耐心布局秋季行情，不追高赌反弹"),
    ("恒生指数 (HSI)", "周四: +0.54% 🔴 / 全周: 小幅整理", "布局时机已成熟，内外资共振可期，黄金股/铜值得关注"),
    ("标普500 (S&P 500)", "周五: -0.17% 🟢 / 全周: +0.36% 🔴 创历史新高", "分母端降息预期再定价，标普500周内刷新历史高点"),
    ("纳斯达克 (Nasdaq)", "周五: -0.28% 🟢 / 全周: +0.14% 🔴", "存储股闪迪+13%(周四)、应用光电+15%，半导体设备承压"),
    ("道琼斯 (DJIA)", "周五: -0.20% 🟢 / 全周: -0.56% 🟢", "防御性蓝筹跑输，市场风险偏好短期边际下降"),
    ("COMEX黄金 (Gold)", "全周: 地缘溢价重燃，避险需求上升 🔴", "霍尔木兹海峡风险叠加降息预期，黄金多头重获驱动"),
    ("布伦特原油 (Brent)", "周四: -2.00% 🟢 / 周五: 受地缘扰动波动", "中东突发事故令油价脱离前期低位，溢价不确定性上升"),
]

y_right = 0.77
for title, val, comment in asset_data:
    ax.text(0.56, y_right, title, fontproperties=prop, fontsize=10.0, color='#334155', fontweight='bold')
    if '🔴' in val and '🟢' in val:
        color = '#ef4444' if val.count('🔴') > val.count('🟢') else '#10b981'
    elif '🔴' in val:
        color = '#ef4444'
    elif '🟢' in val:
        color = '#10b981'
    else:
        color = '#334155'
    clean_val = val.replace('🟢', '').replace('🔴', '')
    ax.text(0.56, y_right-0.028, clean_val, fontproperties=prop, fontsize=8.5, fontweight='bold', color=color)
    ax.text(0.56, y_right-0.050, comment, fontproperties=prop, fontsize=8.0, color='#64748b')
    y_right -= 0.078

# Footer
ax.axhline(y=0.04, xmin=0.03, xmax=0.97, color='#e2e8f0', linewidth=1.0)
ax.text(0.05, 0.02, "数据来源：东方财富、海通国际 | 本报告仅供参考，不构成投资建议", fontproperties=prop, fontsize=8.5, color='#94a3b8')

plt.tight_layout()
output_path = "images/charts/2026-08-15-evening.png"
plt.savefig(output_path, dpi=300, bbox_inches='tight', facecolor=fig.get_facecolor())
plt.close()
print(f"Chart saved to {output_path}")
