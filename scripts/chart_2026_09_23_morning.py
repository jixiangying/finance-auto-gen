"""
国际市场早报行情卡片 — 2026-09-23 早报
基于美东 9月22日（周二）核心资产收盘数据
"""
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.font_manager import FontProperties
import os

# ── 中文字体设置 ──────────────────────────────────────────────────
font_path = '/System/Library/Fonts/STHeiti Medium.ttc'
if not os.path.exists(font_path):
    font_path = '/System/Library/Fonts/Supplemental/Arial Unicode MS.ttf'
prop = FontProperties(fname=font_path)
prop_bold = FontProperties(fname=font_path, weight='bold')

# ── 数据定义 ──────────────────────────────────────────────────────
assets = [
    # (名称, 收盘/现值, 涨跌幅%, 备注)
    ("道琼斯指数",   "51,863.69", -0.36, None),
    ("标普500",      "7,764.64",   0.00, "基本平收"),
    ("纳斯达克",     "27,244.28", +0.45, "收盘新高"),
    ("美10年债收益率", "4.968%",   None, "+1.3bp"),
    ("WTI原油",      "$94.59",    -1.24, "五连跌"),
    ("布伦特原油",    "$99.25",    -1.09, "五连跌"),
    ("现货黄金",     "$4,361",    +0.40, None),
    ("比特币(BTC)",  "$86,143",   -0.55, None),
    ("美元指数",     "100.43",    +0.31, None),
    ("VIX恐慌指数",   "14.87",     None, "基本持平"),
]

# ── 布局 ──────────────────────────────────────────────────────────
n = len(assets)
cols = 3
rows = (n + cols - 1) // cols

fig, axes = plt.subplots(rows, cols, figsize=(14, rows * 2.6))
fig.patch.set_facecolor('#0d1117')

axs = axes.flatten() if hasattr(axes, 'flatten') else [axes]

for i, ax in enumerate(axs):
    ax.set_axis_off()
    if i >= n:
        continue
    name, price, chg, note = assets[i]

    # 背景颜色（红涨绿跌）
    if chg is None:
        bg_color = '#1e2a3a'
        txt_color = '#c9d1d9'
        badge_color = '#30363d'
        badge_txt = note if note else '—'
    elif abs(chg) < 0.005:
        bg_color = '#1e2a3a'
        txt_color = '#c9d1d9'
        badge_color = '#30363d'
        badge_txt = '±0.00%'
    elif chg > 0:
        bg_color = '#1a0000'
        txt_color = '#ff4444'
        badge_color = '#cc0000'
        badge_txt = f"▲ {chg:+.2f}%"
    else:
        bg_color = '#001a00'
        txt_color = '#33cc33'
        badge_color = '#006600'
        badge_txt = f"▼ {chg:.2f}%"

    rect = mpatches.FancyBboxPatch(
        (0.03, 0.05), 0.94, 0.90,
        boxstyle="round,pad=0.04",
        linewidth=0,
        facecolor=bg_color,
        transform=ax.transAxes,
        clip_on=False
    )
    ax.add_patch(rect)

    # 资产名称
    ax.text(0.5, 0.80, name, transform=ax.transAxes,
            ha='center', va='center', fontsize=13,
            color='#e6edf3', fontproperties=prop_bold)

    # 价格
    ax.text(0.5, 0.52, price, transform=ax.transAxes,
            ha='center', va='center', fontsize=16,
            color=txt_color, fontproperties=prop_bold)

    # 涨跌幅徽章
    badge_rect = mpatches.FancyBboxPatch(
        (0.18, 0.12), 0.64, 0.24,
        boxstyle="round,pad=0.02",
        linewidth=0,
        facecolor=badge_color,
        transform=ax.transAxes,
        clip_on=False,
        zorder=5
    )
    ax.add_patch(badge_rect)
    ax.text(0.5, 0.24, badge_txt, transform=ax.transAxes,
            ha='center', va='center', fontsize=11,
            color='white', fontproperties=prop, zorder=6)

# ── 标题 ──────────────────────────────────────────────────────────
fig.suptitle('国际市场早报 · 隔夜核心资产行情卡片', fontsize=16,
             color='#e6edf3', fontproperties=prop_bold, y=0.98)
fig.text(0.5, 0.01, '数据基准：2026-09-22（美东周二）收盘  |  仅供参考，不构成投资建议',
         ha='center', va='bottom', fontsize=9, color='#6e7681', fontproperties=prop)

plt.tight_layout(rect=[0, 0.03, 1, 0.96])

# ── 保存 ──────────────────────────────────────────────────────────
out_path = 'images/charts/chart_20260923_morning.png'
os.makedirs(os.path.dirname(out_path), exist_ok=True)
plt.savefig(out_path, dpi=150, bbox_inches='tight', facecolor=fig.get_facecolor())
plt.close()
print(f"✅ 行情卡片已保存至：{out_path}")
