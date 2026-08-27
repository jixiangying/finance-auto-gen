#!/usr/bin/env python3
"""
行情数据卡片生成脚本 - 2026-08-27 早报（常规交易日）
数据基于 2026年8月26日（周三）北美及全球市场收盘数据
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

# ── 数据定义（美东时间 8月26日收盘）──────────────────────────────
assets = [
    # (名称, 收盘点位/价格, 涨跌额, 涨跌幅%, 单位)
    ("标普 500",           " 7,675.70", "  -1.58",  -0.02, "点"),
    ("纳斯达克综合",       "26,130.20", " -21.10",  -0.08, "点"),
    ("道琼斯工业",         "53,463.88", "-113.52",  -0.21, "点"),
    ("英伟达 盘后(NVDA)",  "  盘后+4%", "  盘后",   +4.00, "财报大超预期"),
    ("美10年期国债收益",   "    4.660", "  +0.022", +0.47, "% (收益率)"),
    ("WTI 原油",           "   $81.87", "  +0.41",  +0.50, "美元/桶"),
    ("现货黄金",           " $4,610",   " -30",     -0.65, "美元/盎司"),
    ("比特币 BTC",         "  $78,250", "  -650",   -0.82, "美元"),
]

def get_color(pct):
    if pct is None:
        return "#888888"
    return "#E84040" if pct >= 0 else "#28A745"

fig, ax = plt.subplots(figsize=(13, 5.6))
ax.set_xlim(0, 13)
ax.set_ylim(0, len(assets) + 1.2)
ax.axis("off")
fig.patch.set_facecolor("#12161E")
ax.set_facecolor("#12161E")

headers = ["资产名称", "收盘价 / 点位", "涨跌变动", "日涨跌幅"]
col_x   = [0.4, 4.2, 7.8, 10.5]
for i, (hdr, cx) in enumerate(zip(headers, col_x)):
    ax.text(cx, len(assets) + 0.6, hdr,
            fontproperties=prop_bold, fontsize=11,
            color="#AAAAAA", va="center", ha="left")

ax.axhline(y=len(assets) + 0.25, xmin=0.02, xmax=0.98,
           color="#444444", linewidth=0.8)

for row_i, (name, price, change, pct, unit) in enumerate(assets):
    y = len(assets) - row_i - 0.45
    bg_color = "#1A1F2B" if row_i % 2 == 0 else "#141820"
    bg = mpatches.FancyBboxPatch((0.1, y - 0.4), 12.8, 0.8,
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

    if pct is not None:
        prefix = "+" if pct > 0 else ""
        pct_str = f"{prefix}{pct:.2f}%"
    else:
        pct_str = "—"
    ax.text(col_x[3], y, pct_str,
            fontproperties=prop_bold, fontsize=11.5, color=c_color,
            va="center", ha="left", zorder=1)

ax.text(6.5, -0.3,
        "数据截至 2026.08.26 美股收盘 | 涨跌：红色=上涨  绿色=下跌 | 仅供参考",
        fontproperties=prop, fontsize=8.5, color="#777777",
        va="center", ha="center")

fig.text(0.5, 0.96,
         "2026-08-27 早报  |  北美及全球核心资产隔夜收盘行情（8/26收盘）",
         fontproperties=prop_bold, fontsize=13.5, color="#FFFFFF",
         ha="center", va="top")

plt.tight_layout(rect=[0, 0.04, 1, 0.95])
out_path = "images/charts/2026-08-27-morning-chart.png"
os.makedirs(os.path.dirname(out_path), exist_ok=True)
plt.savefig(out_path, dpi=150, bbox_inches="tight", facecolor=fig.get_facecolor())
plt.close()
print(f"Chart successfully saved to: {out_path}")
