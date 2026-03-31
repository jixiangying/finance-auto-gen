import matplotlib.pyplot as plt
import matplotlib.patches as patches
from matplotlib.font_manager import FontProperties
import os

# 设置中文字体 (macOS 路径)
font_path = '/System/Library/Fonts/STHeiti Medium.ttc'
if not os.path.exists(font_path):
    font_path = '/System/Library/Fonts/PingFang.ttc'
zh_font = FontProperties(fname=font_path)
plt.rcParams['axes.unicode_minus'] = False

def create_card(name, price, change_pct, filename, color):
    fig, ax = plt.subplots(figsize=(4, 2))
    fig.patch.set_facecolor('#1a1a1a')
    ax.set_facecolor('#1a1a1a')
    
    # 绘制圆角矩形背景 (模拟卡片)
    rect = patches.FancyBboxPatch((0.05, 0.05), 0.9, 0.9, boxstyle="round,pad=0.02", 
                                  linewidth=2, edgecolor=color, facecolor='#2d2d2d', transform=ax.transAxes)
    ax.add_patch(rect)
    
    # 资产名称
    ax.text(0.5, 0.75, name, color='white', fontsize=18, fontweight='bold', 
            ha='center', va='center', fontproperties=zh_font, transform=ax.transAxes)
    
    # 价格
    ax.text(0.5, 0.45, price, color='white', fontsize=22, fontweight='bold', 
            ha='center', va='center', transform=ax.transAxes)
    
    # 涨跌幅
    ax.text(0.5, 0.2, f"{change_pct}%", color=color, fontsize=16, fontweight='bold', 
            ha='center', va='center', transform=ax.transAxes)
    
    ax.set_axis_off()
    plt.tight_layout()
    plt.savefig(f'images/charts/{filename}', dpi=100, facecolor='#1a1a1a')
    plt.close()

# 数据准备 (2026-03-31 早报数据，基于 3月30日收盘)
data = [
    ("道琼斯指数", "45,166.64", "+0.11", "2026-03-31-dow.png", "#ff0000"),
    ("标普500", "6,368.85", "-0.39", "2026-03-31-sp500.png", "#00ff00"),
    ("纳斯达克", "20,948.36", "-0.73", "2026-03-31-nasdaq.png", "#00ff00"),
    ("WTI原油", "105.18", "+5.56", "2026-03-31-oil.png", "#ff0000"),
    ("伦敦现货金", "4,533.92", "+0.21", "2026-03-31-gold.png", "#ff0000"),
    ("比特币", "67,747", "+2.71", "2026-03-31-btc.png", "#ff0000")
]

os.makedirs('images/charts/', exist_ok=True)

for name, price, change, filename, color in data:
    create_card(name, price, change, filename, color)

print("2026-03-31 行情卡片生成完成。")
