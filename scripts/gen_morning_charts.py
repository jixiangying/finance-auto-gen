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

# 数据准备
data = [
    ("道琼斯指数", "47,417.27", "-0.61", "dow_card.png", "#00ff00"), # 绿色代表下跌 (按照中国习惯可能反过来，但指令要求红涨绿跌)
    ("标普500", "6,775.80", "-0.08", "sp500_card.png", "#00ff00"),
    ("纳斯达克", "22,716.13", "+0.08", "nasdaq_card.png", "#ff0000"),
    ("WTI原油", "94.23", "+8.00", "oil_card.png", "#ff0000"),
    ("伦敦现货金", "5,157.37", "-0.43", "gold_card.png", "#00ff00"),
    ("比特币", "70,199.0", "0.00", "btc_card.png", "#ffffff")
]

os.makedirs('images/charts/', exist_ok=True)

for name, price, change, filename, color in data:
    create_card(name, price, change, filename, color)

print("行情卡片生成完成。")
