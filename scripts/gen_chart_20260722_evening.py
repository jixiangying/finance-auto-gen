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

fig, ax = plt.subplots(figsize=(10.5, 6.8))
fig.patch.set_facecolor('#f8fafc')
ax.set_facecolor('#ffffff')
ax.set_xlim(0, 1)
ax.set_ylim(0, 1)
ax.axis('off')

# Title
ax.text(0.05, 0.93, "【A股冲高回落震荡分化与港股走低】(2026/07/22 周三晚)", fontproperties=prop, fontsize=14, fontweight='bold', color='#1e293b')
ax.axhline(y=0.88, xmin=0.04, xmax=0.96, color='#cbd5e1', linewidth=1.5)

# Left Side: Macro & News
ax.text(0.06, 0.82, "▌ 核心解读与政策要闻", fontproperties=prop, fontsize=12, fontweight='bold', color='#0f172a')

events = [
    ("获利筹码兑现，科技板块分化回落", "半导体、存储芯片及通信等全天走弱", "科创50收跌3.82%，呈现高低切换"),
    ("避险板块强劲，贵金属与电力领涨", "金价反弹，立新能源5连板/华银电力4连板", "避险资金流向公用事业及大宗资源"),
    ("证监会密集座谈，吴清推进合作", "强调防风险强监管，会见加拿大养老基金", "一体推进资本市场稳定，引导中长期资金"),
    ("发改委聚焦两重两新，央行逆回购", "郑栅洁召开民企座谈会，逆回购操作760亿", "政策协同宏观保障，维系流动性合理充裕")
]

y = 0.73
for title, val, note in events:
    ax.text(0.08, y, title, fontproperties=prop, fontsize=11, color='#334155', fontweight='bold')
    ax.text(0.08, y-0.045, f"{val}  |  {note}", fontproperties=prop, fontsize=9.5, color='#64748b')
    y -= 0.10

# Right Side: Market Indicators & Assets
ax.text(0.56, 0.82, "▌ 核心资产收盘数据 (A/港股)", fontproperties=prop, fontsize=12, fontweight='bold', color='#0f172a')

asset_data = [
    ("上证指数 (Shanghai)", "3,867.03", "+0.07%", "#dc2626"),
    ("深证成指 (Shenzhen)", "14,061.44", "-1.42%", "#16a34a"),
    ("创业板指 (ChiNext)", "3,566.73", "-3.23%", "#16a34a"),
    ("科创50 (STAR 50)", "1,085.39", "-3.82%", "#16a34a"),
    ("恒生指数 (Hang Seng)", "24,892.66", "-0.95%", "#16a34a"),
    ("恒生科技 (HS Tech)", "4,668.23", "-3.04%", "#16a34a")
]

y_right = 0.73
for title, price, change, color in asset_data:
    ax.text(0.58, y_right, title, fontproperties=prop, fontsize=10.5, color='#334155', fontweight='bold')
    ax.text(0.58, y_right-0.04, f"{price}  ", fontproperties=prop, fontsize=9.5, color='#475569')
    ax.text(0.82, y_right-0.04, f"{change}", fontproperties=prop, fontsize=9.5, color=color, fontweight='bold')
    y_right -= 0.075

plt.tight_layout()
output_path = "images/charts/2026-07-22-evening.png"
plt.savefig(output_path, dpi=300, bbox_inches='tight', facecolor=fig.get_facecolor())
plt.close()
print(f"Chart saved to {output_path}")
