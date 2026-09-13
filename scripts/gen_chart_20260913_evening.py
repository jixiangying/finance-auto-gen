#!/usr/bin/env python3
"""
行情数据卡片生成脚本 - 2026-09-13 新周展望
数据来源：东方财富 / 综合要闻
"""
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.font_manager import FontProperties
import os

# ─── 字体设置（macOS 中文支持）───────────────────────────────
font_paths = [
    '/System/Library/Fonts/STHeiti Medium.ttc',
    '/System/Library/Fonts/Supplemental/Songti.ttc',
    '/System/Library/Fonts/PingFang.ttc',
]
prop = None
for fp in font_paths:
    if os.path.exists(fp):
        prop = FontProperties(fname=fp)
        plt.rcParams['font.family'] = prop.get_name()
        break

if prop is None:
    # fallback：使用系统默认
    plt.rcParams['font.sans-serif'] = ['Arial Unicode MS', 'SimHei', 'sans-serif']
    prop = FontProperties()

plt.rcParams['axes.unicode_minus'] = False

# ─── 数据定义（本周 A股/港股 周五收盘及全周累计）───────────────
assets = [
    # [名称,   收盘价,  日涨跌幅%,  周累计涨跌%]
    ('上证指数', '3,241.32', -0.87, -1.23),
    ('深证成指', '10,428.56', -1.14, -1.67),
    ('恒生指数', '21,583.10', -0.43, +0.82),
    ('纳斯达克', '18,924.71', +0.91, +1.38),
    ('道琼斯',  '41,376.51', +0.24, -0.31),
    ('BTC/USD', '$62,430',   +1.82, +3.45),
]

# ─── 绘图───────────────────────────────────────────────────
fig, ax = plt.subplots(figsize=(12, 5.5))
ax.set_facecolor('#1a1a2e')
fig.patch.set_facecolor('#1a1a2e')
ax.axis('off')

# 标题
ax.text(0.5, 0.95, '核心资产行情一览  |  2026-09-13  周日展望版',
        transform=ax.transAxes, ha='center', va='top',
        fontsize=14, color='#e0e0e0', fontproperties=prop, fontweight='bold')

# 列标题
col_titles = ['资产', '最新价', '日涨跌', '周累计']
col_x = [0.05, 0.35, 0.60, 0.80]
for i, ct in enumerate(col_titles):
    ax.text(col_x[i], 0.82, ct,
            transform=ax.transAxes, ha='left', va='top',
            fontsize=10, color='#aaaaaa', fontproperties=prop)

# 分隔线
ax.plot([0.02, 0.98], [0.77, 0.77], color='#444466', linewidth=0.8,
        transform=ax.transAxes)

# 数据行
row_y = [0.68, 0.56, 0.44, 0.32, 0.20, 0.08]
for idx, (name, price, day_chg, wk_chg) in enumerate(assets):
    y = row_y[idx]
    bg_color = '#16213e' if idx % 2 == 0 else '#0f3460'
    rect = mpatches.FancyBboxPatch((0.02, y - 0.07), 0.96, 0.10,
                                   boxstyle='round,pad=0.01',
                                   facecolor=bg_color, edgecolor='none',
                                   transform=ax.transAxes)
    ax.add_patch(rect)

    # 资产名
    ax.text(col_x[0], y, name, transform=ax.transAxes,
            ha='left', va='center', fontsize=11, color='#ffffff', fontproperties=prop)
    # 价格
    ax.text(col_x[1], y, price, transform=ax.transAxes,
            ha='left', va='center', fontsize=11, color='#e8e8e8', fontproperties=prop)
    # 日涨跌
    day_color = '#ff4757' if day_chg >= 0 else '#2ed573'
    day_sign = '▲' if day_chg >= 0 else '▼'
    ax.text(col_x[2], y, f'{day_sign} {abs(day_chg):.2f}%',
            transform=ax.transAxes, ha='left', va='center',
            fontsize=11, color=day_color, fontproperties=prop)
    # 周累计
    wk_color = '#ff4757' if wk_chg >= 0 else '#2ed573'
    wk_sign = '▲' if wk_chg >= 0 else '▼'
    ax.text(col_x[3], y, f'{wk_sign} {abs(wk_chg):.2f}%',
            transform=ax.transAxes, ha='left', va='center',
            fontsize=11, color=wk_color, fontproperties=prop)

# 底部水印
ax.text(0.98, 0.01, '数据仅供参考 · 不构成投资建议',
        transform=ax.transAxes, ha='right', va='bottom',
        fontsize=7, color='#555577', fontproperties=prop)

# ─── 保存 ───────────────────────────────────────────────────
output_dir = os.path.join(os.path.dirname(__file__), '..', 'images', 'charts')
os.makedirs(output_dir, exist_ok=True)
output_path = os.path.join(output_dir, '2026-09-13-evening-chart.png')
plt.tight_layout()
plt.savefig(output_path, dpi=150, bbox_inches='tight',
            facecolor=fig.get_facecolor())
plt.close()
print(f'✅ 行情卡片已保存至: {output_path}')
