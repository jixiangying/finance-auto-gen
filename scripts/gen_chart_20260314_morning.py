import matplotlib.pyplot as plt
import matplotlib.patches as patches

# 设置中文字体 (macOS)
plt.rcParams['font.sans-serif'] = ['STHeiti', 'PingFang SC', 'Arial Unicode MS']
plt.rcParams['axes.unicode_minus'] = False

def create_card(title, value, change_pct, filename):
    fig, ax = plt.subplots(figsize=(4, 2))
    
    # 颜色判断：红涨绿跌 (国际习惯通常是绿涨红跌，但指令要求红色代表上涨，绿色代表下跌)
    is_up = change_pct >= 0
    color = '#e63946' if is_up else '#2a9d8f' # 红色 vs 绿色
    bg_color = '#f1f1f1'
    
    # 背景
    fig.patch.set_facecolor('white')
    ax.set_facecolor(bg_color)
    
    # 隐藏坐标轴
    ax.set_xticks([])
    ax.set_yticks([])
    for spine in ax.spines.values():
        spine.set_visible(False)
    
    # 文字
    plt.text(0.5, 0.75, title, fontsize=16, ha='center', va='center', fontweight='bold', color='#333')
    plt.text(0.5, 0.45, f"{value}", fontsize=24, ha='center', va='center', fontweight='bold', color='black')
    
    change_text = f"{'+' if is_up else ''}{change_pct:.2f}%"
    plt.text(0.5, 0.15, change_text, fontsize=18, ha='center', va='center', fontweight='bold', color=color)
    
    # 边框
    rect = patches.Rectangle((0.01, 0.01), 0.98, 0.98, linewidth=2, edgecolor=color, facecolor='none', transform=ax.transAxes)
    ax.add_patch(rect)
    
    plt.tight_layout()
    plt.savefig(f"images/charts/{filename}", dpi=100)
    plt.close()

# 数据
data = [
    ("道琼斯工业指数", "46,558.47", -0.26, "2026-03-14-dow.png"),
    ("标普 500 指数", "6,632.19", -0.61, "2026-03-14-sp500.png"),
    ("纳斯达克指数", "22,105.36", -0.93, "2026-03-14-nasdaq.png"),
    ("布伦特原油", "$103.14", 2.70, "2026-03-14-oil.png"),
    ("比特币", "$73,000", 1.20, "2026-03-14-btc.png")
]

for title, val, change, fname in data:
    create_card(title, val, change, fname)

print("Charts generated successfully.")
