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

# 数据准备 (2026-04-29 Evening - Domestic Market Closing)
# 红色代表上涨 #ff0000, 绿色代表下跌 #00ff00
data = [
    ("上证指数", "4107.51", "+0.71", "2026-04-29-sse.png", "#ff0000"),
    ("深证成指", "15120.92", "+1.96", "2026-04-29-szse.png", "#ff0000"),
    ("创业板指", "3687.17", "+2.52", "2026-04-29-chinext.png", "#ff0000"),
    ("恒生指数", "26050.00", "+1.68", "2026-04-29-hsi.png", "#ff0000"),
    ("离岸人民币", "6.8340", "-0.15", "2026-04-29-cnh.png", "#00ff00"), # 汇率跌代表升值，这里用绿色表示升值压力或变动
    ("比特币", "77024.00", "+0.89", "2026-04-29-btc.png", "#ff0000")
]

os.makedirs('images/charts/', exist_ok=True)

for name, price, change, filename, color in data:
    create_card(name, price, change, filename, color)

def create_summary_chart(data, output_path):
    names = [d[0] for d in data]
    changes = [float(d[2]) for d in data]
    colors = [d[4] for d in data]
    
    fig, ax = plt.subplots(figsize=(10, 6))
    fig.patch.set_facecolor('#1a1a1a')
    ax.set_facecolor('#1a1a1a')
    
    bars = ax.bar(names, changes, color=colors)
    
    # 设置中文字体和颜色
    ax.set_xticks(range(len(names)))
    ax.set_xticklabels(names, fontproperties=zh_font, color='white', fontsize=12)
    plt.yticks(color='white')
    ax.set_title("今日核心资产涨跌幅 (%)", fontproperties=zh_font, color='white', fontsize=16, pad=20)
    
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

create_summary_chart(data, 'images/charts/2026-04-29-evening-chart.png')

print("行情卡片及汇总图生成完成。")
