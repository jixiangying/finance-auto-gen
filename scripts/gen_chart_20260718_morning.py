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
ax.text(0.05, 0.93, "【核心行情信息图】(2026/07/18 周六早报)", fontproperties=prop, fontsize=14, fontweight='bold', color='#1e293b')
ax.axhline(y=0.88, xmin=0.04, xmax=0.96, color='#cbd5e1', linewidth=1.5)

# Left Side: Overnight Key Events
ax.text(0.06, 0.82, "▌ 隔夜全球重磅事件与动态", fontproperties=prop, fontsize=12, fontweight='bold', color='#0f172a')

events = [
    ("美伊局势骤然紧张引发避险", "地缘政治局势升级推高油价", "WTI原油大涨3.77%突破81.9美元，黄金避险买盘重燃"),
    ("AI与半导体股深化回调行情", "资金持续流出前期高估值主线", "英伟达、AMD等巨头普遍收跌，拖累纳指下行1.40%"),
    ("奈飞业绩指引放缓遭抛售", "三季度增长预测不及市场预期", "绩后大跌冲击科技及互联网服务板块人气"),
    ("美联储官员静默期前发声", "Hammack与Logan暗示若通胀难降或需加息", "在下周政策静默期前维持审慎，市场宽松预期博弈加剧")
]

y = 0.72
for title, val, note in events:
    ax.text(0.08, y, title, fontproperties=prop, fontsize=10.5, color='#334155', fontweight='bold')
    ax.text(0.08, y-0.04, f"{val}\n{note}", fontproperties=prop, fontsize=9.0, color='#64748b')
    y -= 0.11

# Right Side: Market Indicators & Assets
ax.text(0.56, 0.82, "▌ 核心资产收盘表现", fontproperties=prop, fontsize=12, fontweight='bold', color='#0f172a')

asset_data = [
    ("纳斯达克 (Nasdaq)", "25,520.24 (-1.41%) 🟢", "半导体及AI主线深化回调，大盘承压"),
    ("标普 500 (S&P 500)", "7,457.69 (-1.02%) 🟢", "科技股回调叠加避险情绪，大盘全线走低"),
    ("道琼斯 (Dow Jones)", "52,146.42 (-0.77%) 🟢", "防御性板块难支大局，蓝筹指数集体飘绿"),
    ("WTI原油 (Crude Oil)", "$81.93 (+3.77%) 🔴", "中东局势升级威胁航道，原油暴涨近4%"),
    ("伦敦现货黄金 (Spot Gold)", "$4,016.95 (+1.03%) 🔴", "避险黄金重获青睐，金价收复4000点大关"),
    ("比特币 (Bitcoin)", "$63,485.49 (-1.57%) 🟢", "风险资产遭抛售，加密市场高位整理回撤"),
    ("10年期美债收益率", "4.550% (-1.8 BP) 🟢", "避险资金买入美债，美债收益率小幅下行")
]

y_right = 0.72
for title, val, comment in asset_data:
    ax.text(0.58, y_right, title, fontproperties=prop, fontsize=10.5, color='#334155', fontweight='bold')
    color = '#ef4444' if '🔴' in val else '#10b981'
    clean_val = val.replace('🟢', '').replace('🔴', '')
    
    ax.text(0.58, y_right-0.035, clean_val, fontproperties=prop, fontsize=9.0, fontweight='bold', color=color)
    val_width = len(clean_val) * 0.0075 + 0.02
    ax.text(0.58 + val_width, y_right-0.035, f"|  {comment}", fontproperties=prop, fontsize=9.0, color='#64748b')
    
    y_right -= 0.062

plt.tight_layout()
output_path = "images/charts/2026-07-18-morning.png"
plt.savefig(output_path, dpi=300, bbox_inches='tight', facecolor=fig.get_facecolor())
plt.close()
print(f"Chart saved to {output_path}")
