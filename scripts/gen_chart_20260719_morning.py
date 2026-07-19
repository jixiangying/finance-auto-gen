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

fig, ax = plt.subplots(figsize=(11.5, 7.8))
fig.patch.set_facecolor('#f8fafc')
ax.set_facecolor('#ffffff')
ax.set_xlim(0, 1)
ax.set_ylim(0, 1)
ax.axis('off')

# Title
ax.text(0.05, 0.94, "【核心行情周度复盘】(2026/07/19 周日早报)", fontproperties=prop, fontsize=15, fontweight='bold', color='#1e293b')
ax.axhline(y=0.90, xmin=0.04, xmax=0.96, color='#cbd5e1', linewidth=1.5)

# Left Side: Weekly Key Events
ax.text(0.06, 0.84, "▌ 本周全球市场核心要闻复盘", fontproperties=prop, fontsize=12, fontweight='bold', color='#0f172a')

events = [
    ("美伊冲突急剧升级，地缘避险引爆商品", "地缘风险急剧上升推动能源和黄金买盘", "美军连续打击伊朗，WTI原油周暴涨15.52%突破82美元"),
    ("科技股/AI板块面临高估值挤水分压力", "芯片巨头与AI软硬件核心资产轮动调整", "TSMC调高资本支出引发担忧，纳指全周大跌2.90%"),
    ("龙头业绩与前瞻指引共振施压大盘", "奈飞三季度指引不及预期促使科技股回调", "避险情绪与成长板块抛压共振，标普500全周跌1.60%"),
    ("宏观通胀数据与美联储态度交织博弈", "官员在静默期前偏鹰，美债受避险资金支撑", "10年期美债收益率收至4.550%，黄金跌破4000点后企稳"),
    ("中国A股深度回调，港股展现结构韧性", "沪深300周跌3.54%，恒生指数周逆势涨1.44%", "A股面临获利回吐与外围共振，港股受益于估值防线")
]

y = 0.75
for title, val, note in events:
    ax.text(0.08, y, title, fontproperties=prop, fontsize=10.5, color='#334155', fontweight='bold')
    ax.text(0.08, y-0.035, f"{val}\n{note}", fontproperties=prop, fontsize=9.0, color='#64748b')
    y -= 0.11

# Right Side: Market Indicators & Assets
ax.text(0.56, 0.84, "▌ 核心资产周五及全周表现", fontproperties=prop, fontsize=12, fontweight='bold', color='#0f172a')

asset_data = [
    ("纳斯达克 (Nasdaq)", "25,520.24", "周五: -1.41% 🟢", "全周: -2.90% 🟢", "半导体 bear market 轮动抛压"),
    ("标普 500 (S&P 500)", "7,457.69", "周五: -1.02% 🟢", "全周: -1.60% 🟢", "避险情绪蔓延，大盘普跌"),
    ("道琼斯 (Dow Jones)", "52,146.42", "周五: -0.77% 🟢", "全周: -0.83% 🟢", "传统蓝筹表现相对抗跌"),
    ("沪深 300 (CSI 300)", "4,529.10", "周五: -3.60% 🟢", "全周: -3.54% 🟢", "板块普遍回落，周五大跌"),
    ("恒生指数 (HSI)", "24,562.24", "周五: -1.80% 🟢", "全周: +1.44% 🔴", "全周逆势收涨，周五受累外盘"),
    ("WTI原油 (Crude Oil)", "$82.49", "周五: +3.77% 🔴", "全周: +15.52% 🔴", "中东局势骤紧，原油单周暴涨"),
    ("伦敦现货黄金 (Gold)", "$4,016.95", "周五: +1.03% 🔴", "全周: -2.35% 🟢", "避险重燃，金价自低位收复"),
    ("比特币 (Bitcoin)", "$63,485.49", "周五: -1.57% 🟢", "全周: +0.42% 🔴", "震荡加剧，整体高位盘整")
]

y_right = 0.75
for title, val, fri_chg, wk_chg, comment in asset_data:
    ax.text(0.58, y_right, title, fontproperties=prop, fontsize=10.5, color='#334155', fontweight='bold')
    
    # Value
    ax.text(0.58, y_right-0.03, val, fontproperties=prop, fontsize=9.0, fontweight='bold', color='#1e293b')
    
    # Friday Change
    fri_color = '#ef4444' if '🔴' in fri_chg else '#10b981'
    fri_clean = fri_chg.replace('🔴', '').replace('🟢', '')
    ax.text(0.68, y_right-0.03, fri_clean, fontproperties=prop, fontsize=9.0, fontweight='bold', color=fri_color)
    
    # Weekly Change
    wk_color = '#ef4444' if '🔴' in wk_chg else '#10b981'
    wk_clean = wk_chg.replace('🔴', '').replace('🟢', '')
    ax.text(0.77, y_right-0.03, wk_clean, fontproperties=prop, fontsize=9.0, fontweight='bold', color=wk_color)
    
    # Comment
    ax.text(0.85, y_right-0.03, f"| {comment}", fontproperties=prop, fontsize=8.5, color='#64748b')
    
    y_right -= 0.075

plt.tight_layout()
output_path = "images/charts/2026-07-19-morning.png"
plt.savefig(output_path, dpi=300, bbox_inches='tight', facecolor=fig.get_facecolor())
plt.close()
print(f"Chart saved to {output_path}")
