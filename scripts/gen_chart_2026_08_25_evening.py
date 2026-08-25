#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
生成 2026-08-25 晚报核心行情数据卡片
"""
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm
import os

# 中文字体支持 (macOS)
font_candidates = [
    '/System/Library/Fonts/STHeiti Medium.ttc',
    '/System/Library/Fonts/PingFang.ttc',
    '/System/Library/Fonts/Supplemental/Arial Unicode MS.ttf',
]
font_path = None
for fp in font_candidates:
    if os.path.exists(fp):
        font_path = fp
        break

if font_path:
    prop = fm.FontProperties(fname=font_path)
    plt.rcParams['font.family'] = prop.get_name()
else:
    prop = fm.FontProperties()

plt.rcParams['axes.unicode_minus'] = False

# 数据
assets = [
    ("上证指数", "3,889.44", "+0.19%", True),
    ("深证成指", "13,745.87", "-0.35%", False),
    ("创业板指", "3,397.52", "-1.00%", False),
    ("沪深300", "4,552.03", "-0.24%", False),
    ("科创50", "1,604.59", "+0.14%", True),
    ("恒生指数", "25,511.10", "-0.02%", False),
    ("恒生科技", "4,588.54", "-0.12%", False),
    ("人民币中间价", "6.7852", "-", None),
]

fig, ax = plt.subplots(figsize=(12, 6))
ax.set_xlim(0, 1)
ax.set_ylim(0, 1)
ax.axis('off')

# 背景
fig.patch.set_facecolor('#0d1117')
ax.set_facecolor('#0d1117')

# 标题
title_text = "2026年08月25日 · 国内市场收盘行情"
ax.text(0.5, 0.94, title_text,
        fontproperties=prop,
        fontsize=16, fontweight='bold',
        color='#e6edf3', ha='center', va='top', transform=ax.transAxes)

subtitle_text = "晚报 | 常规交易日"
ax.text(0.5, 0.86, subtitle_text,
        fontproperties=prop,
        fontsize=11, color='#8b949e', ha='center', va='top', transform=ax.transAxes)

# 绘制卡片
n = len(assets)
cols = 4
rows = (n + cols - 1) // cols
card_w = 0.22
card_h = 0.26
x_start = 0.03
y_start = 0.72

for i, (name, price, change, is_up) in enumerate(assets):
    col = i % cols
    row = i // cols
    x = x_start + col * (card_w + 0.035)
    y = y_start - row * (card_h + 0.04)

    # 卡片背景
    if is_up is True:
        bg_color = '#1a2e1a'
        border_color = '#2ea043'
        price_color = '#3fb950'
        change_color = '#3fb950'
    elif is_up is False:
        bg_color = '#2e1a1a'
        border_color = '#da3633'
        price_color = '#f85149'
        change_color = '#f85149'
    else:
        bg_color = '#1c2128'
        border_color = '#30363d'
        price_color = '#8b949e'
        change_color = '#8b949e'

    rect = plt.Rectangle((x, y - card_h), card_w, card_h,
                          facecolor=bg_color, edgecolor=border_color,
                          linewidth=1.5, transform=ax.transAxes, clip_on=False)
    ax.add_patch(rect)

    # 资产名称
    ax.text(x + card_w / 2, y - 0.045, name,
            fontproperties=prop, fontsize=10, fontweight='bold',
            color='#c9d1d9', ha='center', va='top', transform=ax.transAxes)
    # 点位
    ax.text(x + card_w / 2, y - 0.12, price,
            fontproperties=prop, fontsize=12, fontweight='bold',
            color=price_color, ha='center', va='top', transform=ax.transAxes)
    # 涨跌幅
    ax.text(x + card_w / 2, y - 0.195, change,
            fontproperties=prop, fontsize=11,
            color=change_color, ha='center', va='top', transform=ax.transAxes)

# 底部成交额
ax.text(0.5, 0.04,
        "沪深京三市成交额：1.84万亿元  |  较前日缩量约1769亿元",
        fontproperties=prop,
        fontsize=10, color='#8b949e', ha='center', va='bottom', transform=ax.transAxes)

# 保存
output_dir = '/Users/jxy/Documents/Project/finance-auto-gen/images/charts'
os.makedirs(output_dir, exist_ok=True)
output_path = os.path.join(output_dir, '2026-08-25-evening-chart.png')
plt.savefig(output_path, dpi=150, bbox_inches='tight',
            facecolor='#0d1117', edgecolor='none')
plt.close()
print(f"✅ 图表已保存至：{output_path}")
