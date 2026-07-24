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
ax.text(0.05, 0.93, "【外部波动与估值回吐引发A股大调整，两市首破2万亿关口】(2026/07/24 周五晚)", fontproperties=prop, fontsize=14, fontweight='bold', color='#1e293b')
ax.axhline(y=0.88, xmin=0.04, xmax=0.96, color='#cbd5e1', linewidth=1.5)

# Left Side: Macro & News
ax.text(0.06, 0.82, "▌ 市场核心要闻与政策动态", fontproperties=prop, fontsize=12, fontweight='bold', color='#0f172a')

events = [
    ("外部输入性风险外溢，全球科技股普跌共振", "美债收益率攀升及海外大跌，部分资金周末前流出", "受美日韩半导体板块回撤影响，北向资金阶段性流出压制估值"),
    ("两市成交额跌破2万亿，存量博弈观望情绪浓厚", "沪深两市全天成交1.94万亿元，创4月以来新低", "资金追逐真实业绩兑现，盘面呈缩量震荡且分化加剧态势"),
    ("政策面逆周期调节发力，国家队资金大举申购护航", "证监会加强政策储备防传导，国新、诚通投入超600亿", "监管释放稳预期信号，国家队及地方国资表态增持核心资产"),
    ("下周长鑫科技上市，市场短线筹码面临考验", "半导体国产链表现分化，多空博弈静待巨头落地", "重磅IP首发在即，半导体设备及国产替代链展现局部韧性")
]

y = 0.73
for title, val, note in events:
    ax.text(0.08, y, title, fontproperties=prop, fontsize=11, color='#334155', fontweight='bold')
    ax.text(0.08, y-0.045, f"{val}  |  {note}", fontproperties=prop, fontsize=9.5, color='#64748b')
    y -= 0.10

# Right Side: Market Indicators & Assets
ax.text(0.56, 0.82, "▌ 核心指数今日收盘数据", fontproperties=prop, fontsize=12, fontweight='bold', color='#0f172a')

asset_data = [
    ("上证指数 (Shanghai Composite)", "3,814.20", "-62.58 (-1.61%)", "#16a34a"),
    ("深证成指 (Shenzhen Component)", "13,774.68", "-348.63 (-2.47%)", "#16a34a"),
    ("创业板指 (Chinext)", "3,480.87", "-94.65 (-2.65%)", "#16a34a"),
    ("科创50指数 (STAR 50)", "1,042.90", "-1.46 (-0.14%)", "#16a34a"),
    ("恒生指数 (Hang Seng)", "24,963.23", "-178.41 (-0.98%)", "#16a34a"),
    ("恒生科技指数 (Hang Seng Tech)", "4,629.51", "-69.06 (-1.47%)", "#16a34a")
]

y_right = 0.73
for title, price, change, color in asset_data:
    ax.text(0.58, y_right, title, fontproperties=prop, fontsize=10.5, color='#334155', fontweight='bold')
    ax.text(0.58, y_right-0.04, f"{price}  ", fontproperties=prop, fontsize=9.5, color='#475569')
    ax.text(0.82, y_right-0.04, f"{change}", fontproperties=prop, fontsize=9.5, color=color, fontweight='bold')
    y_right -= 0.075

plt.tight_layout()
output_path = "images/charts/2026-07-24-evening.png"
plt.savefig(output_path, dpi=300, bbox_inches='tight', facecolor=fig.get_facecolor())
plt.close()
print(f"Chart saved to {output_path}")
