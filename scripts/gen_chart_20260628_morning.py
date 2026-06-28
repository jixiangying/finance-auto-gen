import matplotlib.pyplot as plt
import matplotlib.font_manager as fm
import os

output_dir = "/Users/jxy/Documents/Project/finance-auto-gen/images/charts/"
os.makedirs(output_dir, exist_ok=True)

font_path = "/System/Library/Fonts/STHeiti Medium.ttc"
if not os.path.exists(font_path):
    font_path = "/System/Library/Fonts/PingFang.ttc"
prop = fm.FontProperties(fname=font_path)

fig, ax = plt.subplots(figsize=(10, 6.5))
fig.patch.set_facecolor('#f8fafc')
ax.set_facecolor('#ffffff')
ax.set_xlim(0, 1)
ax.set_ylim(0, 1)
ax.axis('off')

# Title
ax.text(0.05, 0.93, "【新周宏观前瞻与大宗关键数据】(2026/06/28 周日)", fontproperties=prop, fontsize=14, fontweight='bold', color='#1e293b')
ax.axhline(y=0.88, xmin=0.04, xmax=0.96, color='#cbd5e1', linewidth=1.5)

# Left Side: Macro Indicators Preview
ax.text(0.06, 0.82, "▌ 核心经济数据预测与前瞻", fontproperties=prop, fontsize=12, fontweight='bold', color='#0f172a')

macro_data = [
    ("中国6月官方制造业PMI", "预测: 49.6 - 50.1", "关注荣枯线"),
    ("美国6月新增非农就业人数", "预测: 11.3 - 11.4 万", "提前至周四发布"),
    ("美国6月失业率", "预测: 4.3%", "关注就业放缓"),
    ("下周特殊假期提示", "7月1日港股休市", "7月3日美股独立日休市")
]

y = 0.74
for title, val, note in macro_data:
    ax.text(0.08, y, title, fontproperties=prop, fontsize=11, color='#334155', fontweight='bold')
    ax.text(0.08, y-0.045, f"{val}  |  {note}", fontproperties=prop, fontsize=10, color='#64748b')
    y -= 0.10

# Right Side: Commodity and Cryptos
ax.text(0.56, 0.82, "▌ 大宗商品及加密关键点位", fontproperties=prop, fontsize=12, fontweight='bold', color='#0f172a')

market_data = [
    ("伦敦现货黄金", "$4,032.00 / 盎司", "关注4000支撑"),
    ("WTI原油期货", "$69.23 / 桶", "三年来首破70"),
    ("比特币 (BTC)", "$59,893.00", "考验60k关口"),
    ("美元指数 (DXY)", "101.36", "全周小幅走弱")
]

y_right = 0.74
for title, val, trend in market_data:
    ax.text(0.58, y_right, title, fontproperties=prop, fontsize=11, color='#334155', fontweight='bold')
    ax.text(0.58, y_right-0.045, f"{val} ({trend})", fontproperties=prop, fontsize=10, color='#64748b')
    y_right -= 0.10

plt.tight_layout()
output_path = os.path.join(output_dir, "2026-06-28-morning.png")
plt.savefig(output_path, dpi=300, bbox_inches='tight')
plt.close()
print(f"Chart saved to {output_path}")
