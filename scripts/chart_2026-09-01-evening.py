import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm
import numpy as np
import os

# --- 字体设置（macOS 中文支持）---
font_path = '/System/Library/Fonts/STHeiti Medium.ttc'
if not os.path.exists(font_path):
    font_path = '/System/Library/Fonts/Supplemental/Songti.ttc'
prop = fm.FontProperties(fname=font_path)
plt.rcParams['axes.unicode_minus'] = False

# --- 数据 ---
assets = [
    '上证指数', '深证成指', '沪深300',
    '创业板指', '科创50', '恒生指数'
]
prices = [3979.89, 13872.38, 4611.44, 3393.43, 2050.12, 25329.73]
changes = [-0.16, -1.02, -0.30, -1.32, -2.19, -0.93]

# --- 颜色 (红涨绿跌，中国惯例) ---
colors = ['#D94F4F' if c > 0 else '#2ECC71' for c in changes]

fig, ax = plt.subplots(figsize=(13, 6))
fig.patch.set_facecolor('#0D1117')
ax.set_facecolor('#0D1117')

x = np.arange(len(assets))
bars = ax.bar(x, [abs(c) for c in changes], color=colors, width=0.55, zorder=3)

# --- 价格和涨跌幅标注 ---
for i, (bar, price, chg) in enumerate(zip(bars, prices, changes)):
    sign = '+' if chg > 0 else ''
    ax.text(
        bar.get_x() + bar.get_width() / 2,
        bar.get_height() + 0.05,
        f'{sign}{chg:.2f}%',
        ha='center', va='bottom',
        fontproperties=prop, fontsize=11,
        color=colors[i], fontweight='bold'
    )
    ax.text(
        bar.get_x() + bar.get_width() / 2,
        -0.25,
        f'{price:,.2f}',
        ha='center', va='top',
        fontproperties=prop, fontsize=9.5,
        color='#AAAAAA'
    )

# --- 标题与装饰 ---
ax.set_title(
    '2026年9月1日（周二）· 收盘行情快照',
    fontproperties=prop, fontsize=15, color='#FFFFFF',
    pad=16, fontweight='bold'
)
ax.set_xticks(x)
ax.set_xticklabels(assets, fontproperties=prop, fontsize=12, color='#CCCCCC')
ax.set_yticks([])
ax.spines[:].set_visible(False)
ax.tick_params(colors='#CCCCCC', length=0)
ax.set_ylim(-0.5, max(abs(c) for c in changes) + 0.6)
ax.yaxis.set_visible(False)

# 添加水印说明
fig.text(0.5, 0.01, '数据来源：东方财富 / 新浪财经 | 仅供参考，不构成投资建议',
         ha='center', fontproperties=prop, fontsize=8, color='#555555')

plt.tight_layout()
out_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'images', 'charts')
os.makedirs(out_dir, exist_ok=True)
out_path = os.path.join(out_dir, 'chart_2026-09-01-evening.png')
plt.savefig(out_path, dpi=150, bbox_inches='tight', facecolor=fig.get_facecolor())
print(f"图表已保存至：{out_path}")
