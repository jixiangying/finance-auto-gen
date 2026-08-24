#!/usr/bin/env python3
"""
行情数据卡片生成脚本 - 2026-08-24 早报（新周展望）
数据基于2026年8月21日（周五）收盘及本周累计表现
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

# ── 数据定义（周五收盘 + 周度累计） ──────────────────────────────────────────
assets = [
    # (名称, 收盘点位/价格, 单日涨跌%, 周度累计%, 单位)
    ("道琼斯",    "53,277.01", +0.98, -0.85, "点"),
    ("标普500",   " 7,674.37", +0.43, -1.43, "点"),
    ("纳斯达克",  "26,180.45", +0.43, -2.05, "点"),
    ("美债10Y",   "    4.738", +0.00,  None, "%"),
    ("黄金现货",  " 4,516.58", +0.00,  None, "美元/盎司"),
    ("WTI原油",   "   87.06",  +0.26,  None, "美元/桶"),
    ("布伦特原油","   94.39",  +0.65,  None, "美元/桶"),
    ("美元指数",  "   98.80",  -0.09,  None, ""),
    ("BTC",       "~77,000",   +9.00, +22.0, "美元"),
]

def get_color(pct):
    if pct is None:
        return "#888888"
    return "#E84040" if pct >= 0 else "#28A745"

fig, ax = plt.subplots(figsize=(12, 5.5))
ax.set_xlim(0, 12)
ax.set_ylim(0, len(assets) + 1)
ax.axis("off")
fig.patch.set_facecolor("#12161E")
ax.set_facecolor("#12161E")

headers = ["资产", "收盘价 / 指数", "单日涨跌", "周度累计"]
col_x   = [0.3, 3.5, 7.2, 9.8]
for i, (hdr, cx) in enumerate(zip(headers, col_x)):
    ax.text(cx, len(assets) + 0.55, hdr,
            fontproperties=prop_bold, fontsize=10,
            color="#AAAAAA", va="center", ha="left")

ax.axhline(y=len(assets) + 0.2, xmin=0.02, xmax=0.98,
           color="#444444", linewidth=0.8)

for row_i, (name, price, day_pct, week_pct, unit) in enumerate(assets):
    y = len(assets) - row_i - 0.5
    bg_color = "#1A1F2B" if row_i % 2 == 0 else "#141820"
    bg = mpatches.FancyBboxPatch((0.05, y - 0.42), 11.9, 0.84,
                                  boxstyle="round,pad=0.02",
                                  facecolor=bg_color, edgecolor="none",
                                  zorder=0)
    ax.add_patch(bg)

    ax.text(col_x[0], y, name,
            fontproperties=prop_bold, fontsize=11, color="#FFFFFF",
            va="center", ha="left", zorder=1)

    price_label = f"{price}" + (f"  {unit}" if unit else "")
    ax.text(col_x[1], y, price_label,
            fontproperties=prop, fontsize=10.5, color="#E0E0E0",
            va="center", ha="left", zorder=1)

    day_color = get_color(day_pct)
    day_prefix = "+" if day_pct > 0 else ""
    day_str = f"──" if day_pct == 0 else f"{day_prefix}{day_pct:.2f}%"
    ax.text(col_x[2], y, day_str,
            fontproperties=prop_bold, fontsize=10.5, color=day_color,
            va="center", ha="left", zorder=1)

    if week_pct is not None:
        w_color = get_color(week_pct)
        w_prefix = "+" if week_pct > 0 else ""
        week_str = f"{w_prefix}{week_pct:.2f}%"
    else:
        w_color = "#888888"
        week_str = "——"
    ax.text(col_x[3], y, week_str,
            fontproperties=prop_bold, fontsize=10.5, color=w_color,
            va="center", ha="left", zorder=1)

ax.text(6, -0.3,
        "数据截至 2026.08.21 收盘 | 涨跌：红色=上涨  绿色=下跌 | 仅供参考",
        fontproperties=prop, fontsize=8, color="#666666",
        va="center", ha="center")

fig.text(0.5, 0.97,
         "2026-08-24 早报  |  核心资产周度表现回顾（截至8/21收盘）",
         fontproperties=prop_bold, fontsize=13, color="#FFFFFF",
         ha="center", va="top")

plt.tight_layout(rect=[0, 0.03, 1, 0.95])
out_path = "images/charts/2026-08-24-morning-chart.png"
os.makedirs(os.path.dirname(out_path), exist_ok=True)
plt.savefig(out_path, dpi=150, bbox_inches="tight", facecolor=fig.get_facecolor())
plt.close()
print(f"Chart saved: {out_path}")
