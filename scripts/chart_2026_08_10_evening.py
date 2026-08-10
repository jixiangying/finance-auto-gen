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
ax.text(0.05, 0.93, "【分化震荡两市缩量：医疗资源类大涨，科技硬件回调，成交超2.5万亿】(2026/08/10 周一晚报)", fontproperties=prop, fontsize=13, fontweight='bold', color='#1e293b')
ax.axhline(y=0.88, xmin=0.04, xmax=0.96, color='#cbd5e1', linewidth=1.5)

# Left Side: Key Market Events / Outlook
ax.text(0.06, 0.82, "▌ 今日市场核心动向要闻", fontproperties=prop, fontsize=12, fontweight='bold', color='#0f172a')

events = [
    ("医药生物医疗大涨，主力资金流入首位", "药明康德诉讼获进展（部分限制解除），医疗服务、免疫治疗板块暴涨", "基本面反弹与政策宽松共振，创新药及医疗板块情绪迎来全面重构"),
    ("有色金属与资源类板块强势拉升", "美非农爆冷助推降息预期，黄金及能源金属（钴、镍、锂）表现强劲", "海外流动性预期宽松与避险需求双重加持，顺周期及大宗板块活跃"),
    ("科技硬件与AI概念回调，交易拥挤度修正", "通信设备、半导体、CPO、电子元器件等前期大涨板块今日领跌", "高位筹码出清回调，AI板块热度正从基础设施向商业应用端整固"),
    ("宏观平稳与北京楼市优化政策落地", "7月CPI温和上涨0.5%，北京调减五环内非京籍购房社保要求至1年", "北京购房限制再度降门槛，宏观政策持续释放流动性与维稳暖意")
]

y = 0.72
for title, val, note in events:
    ax.text(0.08, y, title, fontproperties=prop, fontsize=10.0, color='#334155', fontweight='bold')
    ax.text(0.08, y-0.035, f"{val}\n{note}", fontproperties=prop, fontsize=8.5, color='#64748b')
    y -= 0.11

# Right Side: Market Indicators & Assets
ax.text(0.56, 0.82, "▌ 核心资产最新价格与变化", fontproperties=prop, fontsize=12, fontweight='bold', color='#0f172a')

asset_data = [
    ("上证指数 (SSEC)", "3,966.59 (日: +0.67% / 震荡飘红) 🔴", "收复今日低点震荡上行，有色等板块支撑"),
    ("深证成指 (SZI)", "14,316.96 (日: +0.04% / 题材分化) 🔴", "盘中受科技回调压制，收盘勉强收红"),
    ("创业板指 (CHINEXT)", "3,537.21 (日: -0.73% / 医疗撑盘) 🟢", "宁德等权重弱势拖累，医疗服务板块拉升"),
    ("科创50 (STAR50)", "1,737.77 (日: -0.36% / 硬件回调) 🟢", "半导体及服务器硬件高位筹码震荡调整"),
    ("恒生指数 (HSI)", "25,937.49 (日: +1.05% / 收涨超1%) 🔴", "海外资金修复，科网股及创新药全线飘红"),
    ("北证50 (BSE50)", "1,122.88 (日: -1.00% / 板块轮动) 🟢", "经历上周冲高后，今日缩量震荡小幅回落"),
    ("成交额表现 (Turnover)", "2.54万亿元 (日: -1200亿元 / 缩量整固) 🟢", "相比上周五2.66万亿有所缩量，主力高低切换")
]

y_right = 0.72
for title, val, comment in asset_data:
    ax.text(0.58, y_right, title, fontproperties=prop, fontsize=10.0, color='#334155', fontweight='bold')
    color = '#ef4444' if '🔴' in val else '#10b981'
    clean_val = val.replace('🟢', '').replace('🔴', '')
    
    # Draw value with corresponding color
    ax.text(0.58, y_right-0.032, clean_val, fontproperties=prop, fontsize=8.5, fontweight='bold', color=color)
    
    # Set labels font properties explicitly for the axes tick labels prevention of garbled text (per skill requirement)
    # Here it's a text-based plot, so we ensure text has correct font properties.
    
    # Draw comment next to it
    val_width = len(clean_val) * 0.007 + 0.02
    ax.text(0.58 + val_width, y_right-0.032, f"|  {comment}", fontproperties=prop, fontsize=8.5, color='#64748b')
    
    y_right -= 0.058

plt.tight_layout()
output_path = "images/charts/2026-08-10-evening.png"
plt.savefig(output_path, dpi=300, bbox_inches='tight', facecolor=fig.get_facecolor())
plt.close()
print(f"Chart saved to {output_path}")
