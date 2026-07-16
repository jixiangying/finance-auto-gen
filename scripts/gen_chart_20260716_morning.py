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
ax.text(0.05, 0.93, "【核心行情信息图】(2026/07/16 周四早报)", fontproperties=prop, fontsize=14, fontweight='bold', color='#1e293b')
ax.axhline(y=0.88, xmin=0.04, xmax=0.96, color='#cbd5e1', linewidth=1.5)

# Left Side: Overnight Key Events
ax.text(0.06, 0.82, "▌ 隔夜全球重磅事件与动态", fontproperties=prop, fontsize=12, fontweight='bold', color='#0f172a')

events = [
    ("美6月PPI降温超预期", "批发物价同比放缓至5.5%（前值6%），低于市场预期", "继CPI后通胀压力再度释放，缓解了美联储加息隐忧"),
    ("贝莱德Q2营收狂飙31%", "营收达70.8亿美元，EPS $13.91，AUM达15.3万亿美元", "运营利润率达45.9%创五年新高，ETF与Aladdin系统表现亮眼"),
    ("Lucid暴涨29%辟谣破产", "Lucid辟谣破产传言，股价应声大涨提振新能源车板块", "澄清破产质疑极大地缓解了做空情绪，带动EV概念走高"),
    ("中国二季度GDP增4.3%", "较一季度的5.0%放缓，因消费和房地产投资拖累", "市场对刺激政策期望升温，恒生指数大涨1.5%")
]

y = 0.72
for title, val, note in events:
    ax.text(0.08, y, title, fontproperties=prop, fontsize=10.5, color='#334155', fontweight='bold')
    ax.text(0.08, y-0.04, f"{val}\n{note}", fontproperties=prop, fontsize=9.0, color='#64748b')
    y -= 0.11

# Right Side: Market Indicators & Assets
ax.text(0.56, 0.82, "▌ 核心资产收盘表现", fontproperties=prop, fontsize=12, fontweight='bold', color='#0f172a')

asset_data = [
    ("纳斯达克 (Nasdaq)", "26,269.23 (+0.62%) 🔴", "PPI放缓提振估值，科技板块多头回归"),
    ("标普 500 (S&P 500)", "7,572.40 (+0.38%) 🔴", "贝莱德等财报超预期支撑大盘，逼近历史高点"),
    ("道琼斯 (Dow Jones)", "52,658.64 (+0.29%) 🔴", "传统蓝筹股大面积修复，市场人气回升"),
    ("WTI原油 (Crude Oil)", "$79.60 (-0.23%) 🟢", "油价在海峡紧张局势下略有回落，高位维持震荡"),
    ("伦敦现货黄金 (Spot Gold)", "$4,028.13 (+0.09%) 🔴", "美债收益率小幅下行，黄金止跌筑底企稳"),
    ("比特币 (Bitcoin)", "$64,750.00 (+4.03%) 🔴", "风险偏好显著回升，突破6.4万美元阻力区间")
]

y_right = 0.72
for title, val, comment in asset_data:
    ax.text(0.58, y_right, title, fontproperties=prop, fontsize=10.5, color='#334155', fontweight='bold')
    # Use red (#ef4444) for rise 🔴 and green (#10b981) for fall 🟢 in Chinese market convention
    color = '#ef4444' if '🔴' in val else '#10b981'
    clean_val = val.replace('🟢', '').replace('🔴', '')
    
    # Draw value with corresponding color
    ax.text(0.58, y_right-0.035, clean_val, fontproperties=prop, fontsize=9.0, fontweight='bold', color=color)
    # Draw comment next to it
    val_width = len(clean_val) * 0.0075 + 0.02
    ax.text(0.58 + val_width, y_right-0.035, f"|  {comment}", fontproperties=prop, fontsize=9.0, color='#64748b')
    
    y_right -= 0.075

plt.tight_layout()
output_path = "images/charts/2026-07-16-morning.png"
plt.savefig(output_path, dpi=300, bbox_inches='tight', facecolor=fig.get_facecolor())
plt.close()
print(f"Chart saved to {output_path}")
