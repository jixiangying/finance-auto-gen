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
ax.text(0.05, 0.93, "【非农爆冷大跌2.3万：美股全线上扬，美债收益率应声回落】(2026/08/08 周六早报)", fontproperties=prop, fontsize=14, fontweight='bold', color='#1e293b')
ax.axhline(y=0.88, xmin=0.04, xmax=0.96, color='#cbd5e1', linewidth=1.5)

# Left Side: Key Market Events / Outlook
ax.text(0.06, 0.82, "▌ 今日市场核心动向要闻", fontproperties=prop, fontsize=12, fontweight='bold', color='#0f172a')

events = [
    ("美国7月非农意外大减2.3万，历史数据下修10.3万", "7月就业减少2.3万（预期增8万），May/June遭下修10.3万", "劳动力市场降温显著，前期强韧增长被证伪，引发市场剧震"),
    ("加息预期退潮，美债收益率与美元大幅下调", "10Y收益率下挫4BP至4.64%，9月加息概率骤降至38%", "非农爆冷给美联储更多“观望”理由，降息交易再度重燃"),
    ("标普500创历史新高，纳指领涨大升1.3%", "纳指大涨342点，大科技股回补跌幅，标普收涨0.6%创新高", "坏消息即是好消息，宽松预期升温驱使风险资金积极入场"),
    ("黄金飙升近2%避近4385美元，油价与加密同步上扬", "金价暴涨1.94%至$4384.59，布油至$83.24，BTC站上6.49万", "收益率回落直接刺激无息黄金暴拉，大宗与加密市场温和收涨")
]

y = 0.72
for title, val, note in events:
    ax.text(0.08, y, title, fontproperties=prop, fontsize=10.5, color='#334155', fontweight='bold')
    ax.text(0.08, y-0.035, f"{val}\n{note}", fontproperties=prop, fontsize=9.0, color='#64748b')
    y -= 0.11

# Right Side: Market Indicators & Assets
ax.text(0.56, 0.82, "▌ 核心资产最新价格与变化", fontproperties=prop, fontsize=12, fontweight='bold', color='#0f172a')

asset_data = [
    ("纳斯达克综合指数 (NASDAQ)", "26,690.62 (日: +1.30% / 领涨大市) 🔴", "大科技股收复失地，宽松预期重燃提振风险偏好"),
    ("标普 500 指数 (S&P 500)", "7,757.64 (日: +0.62% / 创历史新高) 🔴", "收盘点位再创历史新高，坏消息变好消息"),
    ("道琼斯工业指数 (DJIA)", "54,036.93 (日: +0.28% / 小幅收涨) 🔴", "传统蓝筹稳步跟涨，大市呈现普涨格局"),
    ("布伦特原油期货 (Brent)", "$83.24 (日: +0.90% / 温和走高) 🔴", "地缘风险仍存，加之加息压力缓解，油价回升"),
    ("COMEX 黄金期货 (Gold)", "$4,384.59 (日: +1.94% / 强劲飙升) 🔴", "美债收益率大跌直接利好黄金，金价长阳暴拉"),
    ("10年期美债收益率 (US10Y)", "4.640% (日: -4.0BP / 止涨回落) 🟢", "非农爆冷引发收益率快速跳水，宽松预期抬头"),
    ("比特币 (BTC)", "$64,905.53 (日: +0.75% / 窄幅走高) 🔴", "伴随美股反弹，加密市场情绪略有回暖")
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
output_path = "images/charts/2026-08-08-morning.png"
plt.savefig(output_path, dpi=300, bbox_inches='tight', facecolor=fig.get_facecolor())
plt.close()
print(f"Chart saved to {output_path}")
