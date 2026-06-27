import matplotlib.pyplot as plt
import matplotlib.font_manager as fm
import os

output_dir = "/Users/jxy/Documents/Project/finance-auto-gen/images/charts/"
os.makedirs(output_dir, exist_ok=True)

font_path = "/System/Library/Fonts/STHeiti Medium.ttc"
if not os.path.exists(font_path):
    font_path = "/System/Library/Fonts/PingFang.ttc"
prop = fm.FontProperties(fname=font_path)

assets = [
    "道琼斯指数", "标普500", "纳斯达克", "上证指数", "深证成指", 
    "创业板指", "恒生指数", "恒生科技", "WTI原油", "伦敦金"
]
weekly_changes = [
    "🔴 +0.60%", "🟢 -1.90%", "🟢 -4.60%", "🟢 -1.55%", "🟢 -1.55%",
    "🟢 -1.37%", "🟢 -5.24%", "🟢 -7.57%", "🟢 -10.0%+", "🟢 -5.20%"
]
colors = [
    "red", "green", "green", "green", "green",
    "green", "green", "green", "green", "green"
]

fig, ax = plt.subplots(figsize=(10, 6.5))
fig.patch.set_facecolor('#f7f9fc')
ax.set_facecolor('#ffffff')
ax.set_xlim(0, 1)
ax.set_ylim(0, 1)
ax.axis('off')

y = 0.94
ax.text(0.05, y, "核心资产", fontproperties=prop, fontsize=12, fontweight='bold', color='#1e293b')
ax.text(0.60, y, "本周累计涨跌幅", fontproperties=prop, fontsize=12, fontweight='bold', color='#1e293b')
ax.axhline(y=0.91, xmin=0.04, xmax=0.96, color='#cbd5e1', linewidth=1.2)
y -= 0.08

for i, (asset, change, color) in enumerate(zip(assets, weekly_changes, colors)):
    ax.text(0.06, y, asset, fontproperties=prop, fontsize=11, color='#334155')
    text_color = '#e24c3c' if color == "red" else '#27ae60'
    ax.text(0.62, y, change, fontproperties=prop, fontsize=11, color=text_color, fontweight='bold')
    ax.axhline(y=y-0.025, xmin=0.04, xmax=0.96, color='#f1f5f9', linewidth=0.8)
    y -= 0.075

plt.title("全球核心资产本周累计表现 (2026/06/22 - 2026/06/26)", fontsize=14, fontproperties=prop, pad=15, color='#0f172a', fontweight='bold')
plt.tight_layout()

output_path = os.path.join(output_dir, "2026-06-27-evening.png")
plt.savefig(output_path, dpi=300, bbox_inches='tight')
plt.close()
print(f"Chart saved to {output_path}")
