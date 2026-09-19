#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
行情数据卡片生成脚本 - 2026-09-19 早报（国际市场）
"""
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm
import os

# ---------- 数据 ----------
assets = [
    ("道琼斯\nDJIA",      51682.64, -0.18),
    ("标普500\nS&P 500",  7650.50,  +0.17),
    ("纳斯达克\nNasdaq",  26522.55, +0.39),
    ("黄金\nGold($/oz)",  4377.80,  +0.30),
    ("WTI原油\n($/bbl)",  100.30,   +0.80),
    ("比特币\nBTC($)",    80911.70, +1.20),
    ("10Y美债\nYield(%)", 5.00,     +0.05),
]

# ---------- 字体 ----------
font_paths = [
    "/System/Library/Fonts/STHeiti Medium.ttc",
    "/System/Library/Fonts/PingFang.ttc",
    "/System/Library/Fonts/Supplemental/Arial Unicode MS.ttf",
]
prop = None
for fp in font_paths:
    if os.path.exists(fp):
        prop = fm.FontProperties(fname=fp)
        plt.rcParams["font.family"] = prop.get_name()
        break

# ---------- 绘图 ----------
fig, axes = plt.subplots(1, len(assets), figsize=(20, 4.5))
fig.patch.set_facecolor("#0d1117")

for ax, (name, price, pct) in zip(axes, assets):
    color = "#ff4d4d" if pct >= 0 else "#00c853"
    ax.set_facecolor("#161b22")
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    ax.axis("off")

    # 资产名
    fp_kwargs = {"fontproperties": prop} if prop else {}
    ax.text(0.5, 0.80, name, ha="center", va="center",
            color="#c9d1d9", fontsize=10, **fp_kwargs)

    # 价格
    price_str = f"{price:,.2f}" if price < 10000 else f"{price:,.2f}"
    ax.text(0.5, 0.50, price_str, ha="center", va="center",
            color="white", fontsize=13, fontweight="bold", **fp_kwargs)

    # 涨跌幅
    sign = "▲" if pct >= 0 else "▼"
    ax.text(0.5, 0.22, f"{sign} {abs(pct):.2f}%", ha="center", va="center",
            color=color, fontsize=11, fontweight="bold", **fp_kwargs)

    # 边框
    for spine in ax.spines.values():
        spine.set_visible(False)
    rect = plt.Rectangle((0.03, 0.03), 0.94, 0.94,
                          linewidth=1.5, edgecolor=color,
                          facecolor="none", transform=ax.transAxes)
    ax.add_patch(rect)

plt.suptitle("2026-09-18 国际市场收盘行情", color="#58a6ff",
             fontsize=14, fontweight="bold",
             **({"fontproperties": prop} if prop else {}))
plt.tight_layout(rect=[0, 0, 1, 0.92])

out = "images/charts/20260919-morning-markets.png"
os.makedirs(os.path.dirname(out), exist_ok=True)
plt.savefig(out, dpi=150, bbox_inches="tight", facecolor=fig.get_facecolor())
print(f"Chart saved → {out}")
