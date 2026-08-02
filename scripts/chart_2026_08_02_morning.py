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
ax.text(0.05, 0.93, "【周末全球市场与核心资产表现盘点】(2026/08/02 周日早报)", fontproperties=prop, fontsize=14, fontweight='bold', color='#1e293b')
ax.axhline(y=0.88, xmin=0.04, xmax=0.96, color='#cbd5e1', linewidth=1.5)

# Left Side: Key Market Events
ax.text(0.06, 0.82, "▌ 过去48小时及全周重磅事件", fontproperties=prop, fontsize=12, fontweight='bold', color='#0f172a')

events = [
    ("科技大厂盈利见效提振，纳指大涨复苏", "纳指周五飙升2.78%挽回失地，全周累计微涨0.59%", "亚马逊云业务高增打消ROI顾虑，苹果指引平淡限制硬件表现"),
    ("政治局会议定调偏暖，A股放量大涨迎周末", "两市周五爆发2.56万亿大成交，恒生指数全周大涨3.69%", "历史性首次提出提升资本市场“韧性与信心”，风险偏好大提振"),
    ("地缘危机与通胀忧虑并存，美债收益率走高", "10年美债收益率冲高至4.74%，布油震荡回落收于$88", "特朗普新关税引发通胀担忧，霍尔木兹及红海风险推升油市溢价"),
    ("宏观大事下周接力，超级非农重磅来袭", "下周公布美国7月非农就业，AMD及伯克希尔将公布业绩", "薪资增速与失业率将检验降息可能，中报披露进入最密集阶段")
]

y = 0.72
for title, val, note in events:
    ax.text(0.08, y, title, fontproperties=prop, fontsize=10.5, color='#334155', fontweight='bold')
    ax.text(0.08, y-0.035, f"{val}\n{note}", fontproperties=prop, fontsize=9.0, color='#64748b')
    y -= 0.11

# Right Side: Market Indicators & Assets
ax.text(0.56, 0.82, "▌ 核心资产全周及隔夜表现", fontproperties=prop, fontsize=12, fontweight='bold', color='#0f172a')

asset_data = [
    ("纳斯达克综合指数 (NASDAQ)", "25,122.18 (周: +0.59% / 日: +2.78%) 🔴", "亚马逊云计算提振，科技巨头盈利修复反弹"),
    ("标普 500 指数 (S&P 500)", "7,476.00 (周: +0.86% / 日: +0.52%) 🔴", "权重股科技反弹推动大盘，周期板块走势稳健"),
    ("道琼斯工业指数 (DJIA)", "52,485.03 (周: +1.04% / 日: +0.53%) 🔴", "大金融与工业蓝筹拉升，防守与成长轮动"),
    ("布伦特原油期货 (Brent)", "$88.00 (周: -9.07% / 日: -1.62%) 🟢", "周中油价冲高回落，红海溢价退潮，多头了结"),
    ("COMEX 黄金期货 (Gold)", "$4,042.97 (周: -0.52% / 日: -1.46%) 🟢", "受美元强势及债收益率冲高压制，高位震荡整理"),
    ("10年期美债收益率 (US10Y)", "4.74% (周: +5BP / 日: +8BP) 🔴", "关税生效重燃通胀预期，收益率触及高点"),
    ("比特币 (BTC)", "$62,702.00 (周: -3.61% / 日: -2.33%) 🟢", "市场避险情绪有所缓和，缩量回调至关键水位")
]

y_right = 0.72
for title, val, comment in asset_data:
    ax.text(0.58, y_right, title, fontproperties=prop, fontsize=10.5, color='#334155', fontweight='bold')
    color = '#ef4444' if '🔴' in val else '#10b981'
    clean_val = val.replace('🟢', '').replace('🔴', '')
    
    # Draw value with corresponding color
    ax.text(0.58, y_right-0.032, clean_val, fontproperties=prop, fontsize=9.0, fontweight='bold', color=color)
    # Draw comment next to it
    val_width = len(clean_val) * 0.007 + 0.02
    ax.text(0.58 + val_width, y_right-0.032, f"|  {comment}", fontproperties=prop, fontsize=9.0, color='#64748b')
    
    y_right -= 0.058

plt.tight_layout()
output_path = "images/charts/2026-08-02-morning.png"
plt.savefig(output_path, dpi=300, bbox_inches='tight', facecolor=fig.get_facecolor())
plt.close()
print(f"Chart saved to {output_path}")
