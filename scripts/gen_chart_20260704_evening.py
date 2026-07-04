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
    "创业板指", "科创50", "恒生指数", "恒生科技", "WTI原油", "伦敦金", "比特币 (BTC)"
]
weekly_changes = [
    "+1.97%", "+1.75%", "+2.12%", "+0.41%", "-1.17%",
    "-4.16%", "-2.79%", "+2.99%", "+5.72%", "-0.65%", "+2.00%", "+4.26%"
]
colors = [
    "red", "red", "red", "red", "green",
    "green", "green", "red", "red", "green", "red", "red"
]

fig, ax = plt.subplots(figsize=(10, 7.5))
fig.patch.set_facecolor('#f7f9fc')
ax.set_facecolor('#ffffff')
ax.set_xlim(0, 1)
ax.set_ylim(0, 1)
ax.axis('off')

y = 0.94
ax.text(0.05, y, "核心资产", fontproperties=prop, fontsize=12, fontweight='bold', color='#1e293b')
ax.text(0.60, y, "本周累计涨跌幅", fontproperties=prop, fontsize=12, fontweight='bold', color='#1e293b')
ax.axhline(y=0.91, xmin=0.04, xmax=0.96, color='#cbd5e1', linewidth=1.2)
y -= 0.07

for i, (asset, change, color) in enumerate(zip(assets, weekly_changes, colors)):
    ax.text(0.06, y, asset, fontproperties=prop, fontsize=11, color='#334155')
    text_color = '#e24c3c' if color == "red" else '#27ae60'
    
    # Draw a colored circle marker next to the percentage
    ax.plot(0.61, y + 0.015, marker='o', color=text_color, markersize=7)
    
    ax.text(0.63, y, change, fontproperties=prop, fontsize=11, color=text_color, fontweight='bold')
    ax.axhline(y=y-0.02, xmin=0.04, xmax=0.96, color='#f1f5f9', linewidth=0.8)
    y -= 0.065

plt.title("全球核心资产本周累计表现 (2026/06/29 - 2026/07/03)", fontsize=14, fontproperties=prop, pad=15, color='#0f172a', fontweight='bold')
plt.tight_layout()

output_path = os.path.join(output_dir, "2026-07-04-evening.png")
plt.savefig(output_path, dpi=300, bbox_inches='tight')
plt.close()
print(f"Chart saved to {output_path}")
