import matplotlib.pyplot as plt
from matplotlib.font_manager import FontProperties
import os

# Ensure directory exists
os.makedirs('images/charts', exist_ok=True)

# Font setup for macOS Chinese support
font_path = "/System/Library/Fonts/STHeiti Medium.ttc"
try:
    prop_large = FontProperties(fname=font_path, size=22)
    prop_medium = FontProperties(fname=font_path, size=15)
except Exception:
    prop_large = prop_medium = FontProperties()

try:
    prop_title = FontProperties(fname=font_path, size=16)
except Exception:
    prop_title = FontProperties()

# 2026-08-27 US market closing data
assets = [
    ("标普500",    "7,730.99", "+0.72%", True),
    ("纳斯达克",   "26,541.35", "+1.57%", True),
    ("道琼斯",    "53,569.44", "+0.20%", True),
    ("美国10Y债",  "4.671%",   "+1.1bps", True),
    ("美元指数",   "99.07",    "+0.22%", True),
    ("WTI原油",    "$82.23",   "+2.41%", True),
    ("现货黄金",   "$4,602",   "+0.23%", True),
    ("比特币",     "$79,000",  "+2.2%",  True),
]

fig, axes = plt.subplots(2, 4, figsize=(18, 7))
fig.patch.set_facecolor('#0d1117')

for idx, (name, value, change, is_up) in enumerate(assets):
    ax = axes[idx // 4][idx % 4]
    bg = '#1a0505' if is_up else '#051a05'
    ax.set_facecolor(bg)
    for spine in ax.spines.values():
        spine.set_edgecolor('#ff4444' if is_up else '#00cc44')
        spine.set_linewidth(2)
    ax.set_xticks([])
    ax.set_yticks([])
    ax.text(0.5, 0.78, name, ha='center', va='center',
            fontproperties=prop_medium, color='#cccccc', transform=ax.transAxes)
    ax.text(0.5, 0.50, value, ha='center', va='center',
            fontproperties=prop_large, color='white', transform=ax.transAxes, fontweight='bold')
    color = '#ff4444' if is_up else '#00cc44'
    ax.text(0.5, 0.22, change, ha='center', va='center',
            fontproperties=prop_medium, color=color, transform=ax.transAxes, fontweight='bold')

plt.suptitle('2026-08-27 国际市场收盘数据卡片（英伟达财报驱动全线飘红）',
             fontproperties=prop_title, color='white', fontsize=14, y=1.01)
plt.tight_layout()
plt.savefig('images/charts/2026-08-28-morning-chart.png',
            dpi=150, bbox_inches='tight', facecolor='#0d1117')
plt.close()
print("Chart saved: images/charts/2026-08-28-morning-chart.png")
