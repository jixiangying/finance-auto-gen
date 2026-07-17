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
ax.text(0.05, 0.93, "【核心行情信息图】(2026/07/17 周五早报)", fontproperties=prop, fontsize=14, fontweight='bold', color='#1e293b')
ax.axhline(y=0.88, xmin=0.04, xmax=0.96, color='#cbd5e1', linewidth=1.5)

# Left Side: Overnight Key Events
ax.text(0.06, 0.82, "▌ 隔夜全球重磅事件与动态", fontproperties=prop, fontsize=12, fontweight='bold', color='#0f172a')

events = [
    ("美6月PPI环比意外下降0.3%", "受能源成本走低推动，通胀压力进一步退潮", "紧随CPI降温之后，强化了降息预期的中长期合理性"),
    ("台积电Q2业绩大超预期但股价回调", "净利润大增77.4%，但受板块估值调整与地缘风险影响", "半导体板块普遍承受回吐压力，拖累纳斯达克表现"),
    ("联合健康二季报超预期并调高指引", "医疗巨头业绩亮眼，调高2026全年EPS预测", "作为权重蓝筹表现强劲，为道琼斯指数提供了核心支撑"),
    ("美联储高官发声保持耐心", "副主席Jefferson等重申当前限制性利率的必要性", "强调通胀降温持续性仍待观察，对降息决策维持审慎")
]

y = 0.72
for title, val, note in events:
    ax.text(0.08, y, title, fontproperties=prop, fontsize=10.5, color='#334155', fontweight='bold')
    ax.text(0.08, y-0.04, f"{val}\n{note}", fontproperties=prop, fontsize=9.0, color='#64748b')
    y -= 0.11

# Right Side: Market Indicators & Assets
ax.text(0.56, 0.82, "▌ 核心资产收盘表现", fontproperties=prop, fontsize=12, fontweight='bold', color='#0f172a')

asset_data = [
    ("纳斯达克 (Nasdaq)", "25,885.47 (-1.47%) 🟢", "半导体及AI主线大跌，拖累科技板块普跌"),
    ("标普 500 (S&P 500)", "7,534.62 (-0.50%) 🟢", "科技股失血拖累大盘，避险情绪小幅升温"),
    ("道琼斯 (Dow Jones)", "52,549.51 (-0.21%) 🟢", "联合健康等蓝筹强势护盘，跌幅相对有限"),
    ("WTI原油 (Crude Oil)", "$79.60 (0.00%) 🔴", "多空拉锯，在供需博弈下原油价格保持平盘"),
    ("伦敦现货黄金 (Spot Gold)", "$3,976.18 (-1.29%) 🟢", "避险资金流向美债，黄金价格承压回落"),
    ("比特币 (Bitcoin)", "$64,495.00 (-0.39%) 🟢", "风险偏好退潮，高位面临小幅调整回调"),
    ("10年期美债收益率", "4.568% (+2.3 BP) 🔴", "降息预期的博弈拉锯，美债收益率小幅上扬")
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
output_path = "images/charts/2026-07-17-morning.png"
plt.savefig(output_path, dpi=300, bbox_inches='tight', facecolor=fig.get_facecolor())
plt.close()
print(f"Chart saved to {output_path}")
