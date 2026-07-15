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
ax.text(0.05, 0.93, "【核心行情信息图】(2026/07/15 周三晚)", fontproperties=prop, fontsize=14, fontweight='bold', color='#1e293b')
ax.axhline(y=0.88, xmin=0.04, xmax=0.96, color='#cbd5e1', linewidth=1.5)

# Left Side: Key Market Events
ax.text(0.06, 0.82, "▌ 核心事件与市场逻辑", fontproperties=prop, fontsize=12, fontweight='bold', color='#0f172a')

events = [
    ("央行货政会稳健宽松定调", "继续实施适度宽松货政，引导融资成本低位运行", "邹澜副行长介绍上半年数据，强调加大逆周期调节"),
    ("买断式逆回购大额净投放", "开展14000亿6个月期操作，实现净投放5000亿", "流动性“及时雨”平滑税期与政府债发行流动性缺口"),
    ("长鑫科技IPO申购在即", "科创板发行价定为8.66元，定于7月16日申购", "中报窗口密集预喜，券商业绩弹性提供风格切换基础"),
    ("创新药CRO爆发科技回调", "昭衍新药中报预告亮眼，半导体产业链高位回吐", "A股缩量宽幅震荡，港股生物医药与AI概念强势领涨")
]

y = 0.73
for title, val, note in events:
    ax.text(0.08, y, title, fontproperties=prop, fontsize=11, color='#334155', fontweight='bold')
    ax.text(0.08, y-0.045, f"{val}  |  {note}", fontproperties=prop, fontsize=9.5, color='#64748b')
    y -= 0.10

# Right Side: Asset Indicators
ax.text(0.56, 0.82, "▌ 核心资产收盘表现", fontproperties=prop, fontsize=12, fontweight='bold', color='#0f172a')

asset_data = [
    ("上证指数 (SSEC)", "3,955.58 (-0.29%)", "A股宽幅整理，医药消费逆市活跃"),
    ("深证成指 (SDEC)", "14,779.40 (-0.97%)", "深证震荡回调，市场风格呈现高低切换"),
    ("创业板指 (CHINEXT)", "3,804.70 (-1.21%)", "科技赛道承压，半导体板块明显回吐"),
    ("恒生指数 (HSI)", "24,681.10 (+1.40%)", "港股逆市走强，生物医药与AI概念领涨")
]

y_right = 0.73
for title, val, comment in asset_data:
    ax.text(0.58, y_right, title, fontproperties=prop, fontsize=11, color='#334155', fontweight='bold')
    ax.text(0.58, y_right-0.045, f"{val} ({comment})", fontproperties=prop, fontsize=9.5, color='#64748b')
    y_right -= 0.10

plt.tight_layout()
output_path = "images/charts/2026-07-15-evening.png"
plt.savefig(output_path, dpi=300, bbox_inches='tight', facecolor=fig.get_facecolor())
plt.close()
print(f"Chart saved to {output_path}")
