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

fig, ax = plt.subplots(figsize=(10.8, 7.2))
fig.patch.set_facecolor('#f8fafc')
ax.set_facecolor('#ffffff')
ax.set_xlim(0, 1)
ax.set_ylim(0, 1)
ax.axis('off')

# Title
ax.text(0.05, 0.93, "【核心行情信息图】(2026/07/17 周五晚报)", fontproperties=prop, fontsize=14, fontweight='bold', color='#1e293b')
ax.axhline(y=0.88, xmin=0.04, xmax=0.96, color='#cbd5e1', linewidth=1.5)

# Left Side: Key Market Events
ax.text(0.06, 0.82, "▌ 核心事件与市场逻辑", fontproperties=prop, fontsize=12, fontweight='bold', color='#0f172a')

events = [
    ("科技股重挫与融资盘出清", "半导体、存储、算力等前期高位题材集体重挫，创业板指跌逾7.1%", "市场现普跌踩踏特征，全场超5000股下跌，部分资金获利利好出逃"),
    ("全球市场共振与外部扰动", "亚太股市集体走弱，美日科技股持续调整，叠加密切关注的中东地缘", "外部风险偏好急剧降温，导致场内资金避险与防守情绪显著升温"),
    ("发改委AI行动计划与氦气出口管制", "发改委发布AI全球算力连通合作计划；商务部对氦气实施临时出口管制", "顶层设计强化AI中长期建设，限制关键原料以保障国内科技链条安全"),
    ("ETF巨量托底与防御板块飘红", "电力、银行、石油等红利资产逆向飘红；创业板与科创ETF显著放量", "红利红字吸纳避险资金，长线大资金（国家队）疑似借道宽基托底")
]

y = 0.72
for title, val, note in events:
    ax.text(0.08, y, title, fontproperties=prop, fontsize=10.5, color='#334155', fontweight='bold')
    ax.text(0.08, y-0.04, f"{val}\n{note}", fontproperties=prop, fontsize=9.0, color='#64748b')
    y -= 0.11

# Right Side: Market Indicators & Assets
ax.text(0.56, 0.82, "▌ 核心资产收盘表现", fontproperties=prop, fontsize=12, fontweight='bold', color='#0f172a')

asset_data = [
    ("上证指数 (SSEC)", "3,764.15 (-3.05%) 🟢", "跌破3800点，主要技术支撑位面临考验"),
    ("深证成指 (SDEC)", "13,706.88 (-5.40%) 🟢", "深指重挫超5%，全天两市放量成交达2.67万亿"),
    ("创业板指 (CHINEXT)", "3,428.63 (-7.15%) 🟢", "前期热门科技题材大幅踩踏，录得近年单日最大跌幅"),
    ("恒生指数 (HSI)", "24,562.24 (-1.78%) 🟢", "港股随大市走弱，直接失守昨日收复的两万五关口"),
    ("恒生科技指数 (HSTECH)", "4,623.17 (-4.37%) 🟢", "科网巨头及芯片股悉数飘绿，昨日涨幅全部回吐")
]

y_right = 0.72
for title, val, comment in asset_data:
    ax.text(0.58, y_right, title, fontproperties=prop, fontsize=10.5, color='#334155', fontweight='bold')
    color = '#ef4444' if '🔴' in val else '#10b981'
    clean_val = val.replace('🟢', '').replace('🔴', '')
    
    # Draw value with corresponding color
    ax.text(0.58, y_right-0.035, clean_val, fontproperties=prop, fontsize=9.0, fontweight='bold', color=color)
    # Draw comment next to it
    val_width = len(clean_val) * 0.0075 + 0.02
    ax.text(0.58 + val_width, y_right-0.035, f"|  {comment}", fontproperties=prop, fontsize=9.0, color='#64748b')
    
    y_right -= 0.075

plt.tight_layout()
output_path = "images/charts/2026-07-17-evening.png"
plt.savefig(output_path, dpi=300, bbox_inches='tight', facecolor=fig.get_facecolor())
plt.close()
print(f"Chart saved to {output_path}")
