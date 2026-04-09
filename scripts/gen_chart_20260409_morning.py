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

# 数据准备 (2026-04-09 Morning - US Market April 8 Closing)
# 红色代表上涨 #ff0000, 绿色代表下跌 #00ff00
data = [
    ("道琼斯指数", "47,909.92", "+2.90", "2026-04-09-dow.png", "#ff0000"),
    ("标普500", "6,782.81", "+2.50", "2026-04-09-sp500.png", "#ff0000"),
    ("纳斯达克", "22,634.99", "+2.80", "2026-04-09-nasdaq.png", "#ff0000"),
    ("WTI原油", "96.06", "-15.00", "2026-04-09-oil.png", "#00ff00"),
    ("伦敦现货金", "4,731.59", "+0.50", "2026-04-09-gold.png", "#ff0000"),
    ("比特币", "71,339.09", "+2.90", "2026-04-09-btc.png", "#ff0000")
]

os.makedirs('images/charts/', exist_ok=True)

for name, price, change, filename, color in data:
    create_card(name, price, change, filename, color)

# 额外生成一个汇总图 (可选，但为了美观，我们可以做一个大图)
def create_summary_chart(data, output_path):
    names = [d[0] for d in data]
    changes = [float(d[2]) for d in data]
    colors = [d[4] for d in data]
    
    fig, ax = plt.subplots(figsize=(10, 6))
    fig.patch.set_facecolor('#1a1a1a')
    ax.set_facecolor('#1a1a1a')
    
    bars = ax.bar(names, changes, color=colors)
    
    # 设置中文字体和颜色
    ax.set_xticklabels(names, fontproperties=zh_font, color='white', fontsize=12)
    plt.yticks(color='white')
    ax.set_title("隔夜核心资产涨跌幅 (%)", fontproperties=zh_font, color='white', fontsize=16, pad=20)
    
    # 在柱状图上方添加数值
    for bar in bars:
        height = bar.get_height()
        ax.text(bar.get_x() + bar.get_width()/2., height + (0.1 if height > 0 else -0.5),
                f'{height}%', ha='center', va='bottom' if height > 0 else 'top', color='white', fontweight='bold')

    # 隐藏边框
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.spines['bottom'].set_color('#444444')
    ax.spines['left'].set_color('#444444')
    
    plt.tight_layout()
    plt.savefig(output_path, dpi=100, facecolor='#1a1a1a')
    plt.close()

create_summary_chart(data, 'images/charts/2026-04-09-morning-chart.png')

print("行情卡片及汇总图生成完成。")
