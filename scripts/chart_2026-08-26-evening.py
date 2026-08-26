#!/usr/bin/env python3
"""
行情数据卡片生成脚本 - 2026-08-26 晚报（常规交易日）
数据基于 2026年8月26日（周三）A股及港股收盘数据
"""
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.font_manager import FontProperties
import os

# ── 中文字体配置 ──────────────────────────────────────────────────────────────
FONT_PATHS = [
    "/System/Library/Fonts/STHeiti Medium.ttc",
    "/System/Library/Fonts/PingFang.ttc",
    "/System/Library/Fonts/Supplemental/Arial Unicode MS.ttf",
    "/Library/Fonts/Arial Unicode MS.ttf",
]
font_path = None
for fp in FONT_PATHS:
    if os.path.exists(fp):
        font_path = fp
        break

if font_path:
    prop = FontProperties(fname=font_path)
    prop_bold = FontProperties(fname=font_path, weight="bold")
else:
    prop = FontProperties()
    prop_bold = FontProperties(weight="bold")

# ── 数据定义（周三收盘） ──────────────────────────────────────────
assets = [
    # (名称, 收盘点位/价格, 涨跌额, 涨跌幅%, 单位)
    ("上证综合指数", " 3,912.52", " +23.08", +0.59, "点"),
    ("深证成分指数", "13,841.33", " +95.46", +0.69, "点"),
    ("创业板指数",   " 3,414.88", " +17.36", +0.51, "点"),
    ("科创50指数",   " 1,632.02", " +27.43", +1.71, "点"),
    ("沪深300指数",  " 4,579.35", " +27.32", +0.60, "点"),
    ("恒生指数",     "25,652.97", "+141.87", +0.56, "点"),
    ("恒生科技指数", " 4,626.15", " +37.61", +0.82, "点"),
    ("中国10年国债", "    1.687", " +0.005", +0.30, "% (收益率)"),
    ("美元/人民币中间价", " 6.7829", " -0.0023", -0.03, "元"),
]

def get_color(pct):
    if pct is None:
        return "#888888"
    return "#E84040" if pct >= 0 else "#28A745"

fig, ax = plt.subplots(figsize=(12, 5.8))
ax.set_xlim(0, 12)
ax.set_ylim(0, len(assets) + 1.2)
ax.axis("off")
fig.patch.set_facecolor("#12161E")
ax.set_facecolor("#12161E")

headers = ["资产名称", "收盘价 / 点位", "涨跌变动", "日涨跌幅"]
col_x   = [0.4, 3.8, 7.2, 9.8]
for i, (hdr, cx) in enumerate(zip(headers, col_x)):
    ax.text(cx, len(assets) + 0.6, hdr,
            fontproperties=prop_bold, fontsize=11,
            color="#AAAAAA", va="center", ha="left")

ax.axhline(y=len(assets) + 0.25, xmin=0.02, xmax=0.98,
           color="#444444", linewidth=0.8)

for row_i, (name, price, change, pct, unit) in enumerate(assets):
    y = len(assets) - row_i - 0.45
    bg_color = "#1A1F2B" if row_i % 2 == 0 else "#141820"
    bg = mpatches.FancyBboxPatch((0.1, y - 0.4), 11.8, 0.8,
                                  boxstyle="round,pad=0.02",
                                  facecolor=bg_color, edgecolor="none",
                                  zorder=0)
    ax.add_patch(bg)

    ax.text(col_x[0], y, name,
            fontproperties=prop_bold, fontsize=11.5, color="#FFFFFF",
            va="center", ha="left", zorder=1)

    price_label = f"{price}" + (f"  {unit}" if unit else "")
    ax.text(col_x[1], y, price_label,
            fontproperties=prop, fontsize=11, color="#E0E0E0",
            va="center", ha="left", zorder=1)

    c_color = get_color(pct)
    ax.text(col_x[2], y, change,
            fontproperties=prop, fontsize=11, color=c_color,
            va="center", ha="left", zorder=1)

    prefix = "+" if pct > 0 else ""
    pct_str = f"{prefix}{pct:.2f}%"
    ax.text(col_x[3], y, pct_str,
            fontproperties=prop_bold, fontsize=11.5, color=c_color,
            va="center", ha="left", zorder=1)

ax.text(6, -0.3,
        "数据截至 2026.08.26 收盘 | 涨跌：红色=上涨  绿色=下跌 | 仅供参考",
        fontproperties=prop, fontsize=8.5, color="#777777",
        va="center", ha="center")

fig.text(0.5, 0.96,
         "2026-08-26 晚报  |  国内核心资产收盘行情（8/26收盘）",
         fontproperties=prop_bold, fontsize=13.5, color="#FFFFFF",
         ha="center", va="top")

plt.tight_layout(rect=[0, 0.04, 1, 0.95])
out_path = "images/charts/2026-08-26-evening-chart.png"
os.makedirs(os.path.dirname(out_path), exist_ok=True)
plt.savefig(out_path, dpi=150, bbox_inches="tight", facecolor=fig.get_facecolor())
plt.close()
print(f"Chart successfully saved to: {out_path}")
