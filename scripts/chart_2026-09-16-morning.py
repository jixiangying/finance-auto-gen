import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm
import matplotlib.patches as mpatches
import os

# --- 字体设置（macOS 中文支持）---
font_paths = [
    '/System/Library/Fonts/STHeiti Medium.ttc',
    '/System/Library/Fonts/PingFang.ttc',
    '/Library/Fonts/Arial Unicode MS.ttf',
]
prop = None
for fp in font_paths:
    if os.path.exists(fp):
        prop = fm.FontProperties(fname=fp)
        plt.rcParams['font.family'] = prop.get_name()
        break
if prop is None:
    prop = fm.FontProperties()

# --- 数据 ---
assets = [
    {"name": "标普500\nS&P 500", "value": "7,585.73", "change": "-0.45%", "up": False},
    {"name": "纳斯达克\nNasdaq", "value": "25,981.57", "change": "-0.78%", "up": False},
    {"name": "道琼斯\nDow Jones", "value": "52,093.11", "change": "-0.63%", "up": False},
    {"name": "美债10Y\nUS 10Y Yield", "value": "4.996%", "change": "+1bp", "up": True},
    {"name": "WTI原油\nWTI Crude", "value": "$105.70", "change": "+4.2%", "up": True},
    {"name": "黄金\nGold", "value": "$4,335", "change": "-0.4%", "up": False},
    {"name": "比特币\nBTC/USD", "value": "$75,900", "change": "-0.7%", "up": False},
    {"name": "美元指数\nDXY", "value": "99.65", "change": "+0.26%", "up": True},
]

# --- 绘图 ---
n = len(assets)
cols = 4
rows = 2
fig, axes = plt.subplots(rows, cols, figsize=(16, 6))
fig.patch.set_facecolor('#1a1a2e')

for i, ax in enumerate(axes.flat):
    if i >= n:
        ax.set_visible(False)
        continue
    a = assets[i]
    bg_color = '#16213e'
    border_color = '#e74c3c' if a["up"] else '#27ae60'
    arrow = '▲' if a["up"] else '▼'
    text_color = '#e74c3c' if a["up"] else '#2ecc71'

    ax.set_facecolor(bg_color)
    for spine in ax.spines.values():
        spine.set_edgecolor(border_color)
        spine.set_linewidth(2)
    ax.set_xticks([])
    ax.set_yticks([])

    # 资产名称
    ax.text(0.5, 0.80, a["name"], transform=ax.transAxes,
            ha='center', va='center', fontsize=10, color='#ecf0f1',
            fontproperties=prop, fontweight='bold')
    # 价格
    ax.text(0.5, 0.50, a["value"], transform=ax.transAxes,
            ha='center', va='center', fontsize=16, color='#f0f0f0',
            fontproperties=prop, fontweight='bold')
    # 涨跌幅
    ax.text(0.5, 0.18, f"{arrow} {a['change']}", transform=ax.transAxes,
            ha='center', va='center', fontsize=13, color=text_color,
            fontproperties=prop, fontweight='bold')

plt.suptitle('2026-09-16 国际市场早报行情卡片', fontsize=14, color='white',
             fontproperties=prop, fontweight='bold', y=1.02)
plt.tight_layout()

out_path = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))),
                        'images', 'charts', 'chart_2026-09-16-morning.png')
os.makedirs(os.path.dirname(out_path), exist_ok=True)
plt.savefig(out_path, dpi=150, bbox_inches='tight', facecolor=fig.get_facecolor())
plt.close()
print(f"[OK] Chart saved to: {out_path}")
