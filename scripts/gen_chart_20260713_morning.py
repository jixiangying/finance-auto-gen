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
ax.text(0.05, 0.93, "【新周财经焦点与资产关键位置】(2026/07/13 周一早)", fontproperties=prop, fontsize=14, fontweight='bold', color='#1e293b')
ax.axhline(y=0.88, xmin=0.04, xmax=0.96, color='#cbd5e1', linewidth=1.5)

# Left Side: Weekend & Overnight Events
ax.text(0.06, 0.82, "▌ 周末及晨间重磅事件与动态", fontproperties=prop, fontsize=12, fontweight='bold', color='#0f172a')

events = [
    ("中东局势突发恶化油价飙涨", "美伊突发新一轮空中打击冲突，避险情绪升温", "WTI原油周一晨间跳涨超3%，地缘溢价重燃"),
    ("SK Hynix常规交易今日启动", "历史级IPO募资265亿，今日起以代码“SKHY”交易", "芯片算力巨头正式挂牌，引爆全球半导体预期"),
    ("我国氦气出口临时管制生效", "限制本国战略性稀缺气体氦气出口，强化资源保障", "半导体制造、超导、航天军工特种气体溢价"),
    ("英国强化金融云服务巨头监管", "7月13日起，英监管部门对AWS、谷歌云等实施直管", "提高关键第三方(CTP)的系统性金融韧性与合规")
]

y = 0.73
for title, val, note in events:
    ax.text(0.08, y, title, fontproperties=prop, fontsize=11, color='#334155', fontweight='bold')
    ax.text(0.08, y-0.045, f"{val}  |  {note}", fontproperties=prop, fontsize=9.5, color='#64748b')
    y -= 0.10

# Right Side: Market Indicators & Assets
ax.text(0.56, 0.82, "▌ 核心资产位置与今日关注", fontproperties=prop, fontsize=12, fontweight='bold', color='#0f172a')

asset_data = [
    ("沪深 300 (CSI 300)", "4,780.79 (周五:-2.00%)", "天量换手静待本周二季度GDP及中报预告大考"),
    ("纳斯达克 (Nasdaq)", "26,281.61 (周五:+0.29%)", "SKHY今日挂牌常规交易，芯片算力风向标"),
    ("WTI原油 (Crude Oil)", "$73.55 (今日晨:+3.00%)", "中东地缘摩擦突发恶化，推动能源短线暴涨"),
    ("比特币 (BTC)", "$63,220.69 (周五:+1.56%)", "高位震荡等待宏观指引，降息预期温和修复")
]

y_right = 0.73
for title, val, comment in asset_data:
    ax.text(0.58, y_right, title, fontproperties=prop, fontsize=11, color='#334155', fontweight='bold')
    ax.text(0.58, y_right-0.045, f"{val} ({comment})", fontproperties=prop, fontsize=9.5, color='#64748b')
    y_right -= 0.10

plt.tight_layout()
output_path = "images/charts/2026-07-13-morning.png"
plt.savefig(output_path, dpi=300, bbox_inches='tight', facecolor=fig.get_facecolor())
plt.close()
print(f"Chart saved to {output_path}")
