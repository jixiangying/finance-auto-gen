"""
新周展望行情卡片 — 2026-09-20 晚报
基于上周五（9月18日）核心资产收盘数据
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
    # (名称, 收盘/现值, 涨跌幅%)
    ("上证指数",    "3,911.87",  +0.94),
    ("深证成指",   "13,640.87",  +1.72),
    ("创业板指",    "3,372.68",  +2.25),
    ("恒生指数",   "24,750.78",  +0.60),
    ("道琼斯指数", "51,682.64",  -0.18),
    ("标普500",    "7,650.50",   +0.17),
    ("纳斯达克",   "26,522.55",  +0.39),
    ("美10年债",       "5.00%",   None),
    ("比特币(BTC)","$80,000+",   None),
]

# ── 布局 ──────────────────────────────────────────────────────────
n = len(assets)
cols = 3
rows = (n + cols - 1) // cols

fig, axes = plt.subplots(rows, cols, figsize=(14, rows * 2.6))
fig.patch.set_facecolor('#0d1117')

# 扁平化 axes
axs = axes.flatten() if hasattr(axes, 'flatten') else [axes]

for i, ax in enumerate(axs):
    ax.set_axis_off()
    if i >= n:
        continue
    name, price, chg = assets[i]

    # 背景颜色
    if chg is None:
        bg_color = '#1e2a3a'
        txt_color = '#c9d1d9'
        badge_color = '#30363d'
        badge_txt = '—'
    elif chg >= 0:
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
fig.suptitle('新周展望 · 核心资产上周收盘行情', fontsize=16,
             color='#e6edf3', fontproperties=prop_bold, y=0.98)
fig.text(0.5, 0.01, '数据基准：2026-09-18（上周五）收盘  |  仅供参考，不构成投资建议',
         ha='center', va='bottom', fontsize=9, color='#6e7681', fontproperties=prop)

plt.tight_layout(rect=[0, 0.03, 1, 0.96])

# ── 保存 ──────────────────────────────────────────────────────────
out_path = '/Users/jxy/Documents/Project/finance-auto-gen/images/charts/chart_2026_09_20_evening.png'
os.makedirs(os.path.dirname(out_path), exist_ok=True)
plt.savefig(out_path, dpi=150, bbox_inches='tight', facecolor=fig.get_facecolor())
plt.close()
print(f"✅ 行情卡片已保存至：{out_path}")
