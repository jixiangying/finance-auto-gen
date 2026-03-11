import matplotlib.pyplot as plt
import matplotlib.font_manager as fm
import os

# Set font for macOS
font_path = '/System/Library/Fonts/STHeiti Medium.ttc'
if not os.path.exists(font_path):
    font_path = '/System/Library/Fonts/PingFang.ttc'

prop = fm.FontProperties(fname=font_path)
plt.rcParams['axes.unicode_minus'] = False

def create_card(data, filename):
    fig, ax = plt.subplots(figsize=(10, 6), dpi=100)
    ax.axis('off')
    fig.patch.set_facecolor('#f4f4f4')
    
    y_pos = 0.9
    ax.text(0.5, 0.95, "今日核心行情数据 (2026-03-11 收盘)", fontproperties=prop, fontsize=20, ha='center', fontweight='bold')
    
    headers = ["资产名称", "现价/点位", "涨跌幅"]
    cols = [0.15, 0.5, 0.8]
    for i, h in enumerate(headers):
        ax.text(cols[i], 0.85, h, fontproperties=prop, fontsize=14, fontweight='bold')
    
    y = 0.78
    for item in data:
        name, price, change = item
        color = 'red' if '+' in change else 'green'
        if change == '0.00%': color = 'black'
        
        ax.text(cols[0], y, name, fontproperties=prop, fontsize=14)
        ax.text(cols[1], y, price, fontproperties=prop, fontsize=14)
        ax.text(cols[2], y, change, fontproperties=prop, fontsize=14, color=color, fontweight='bold')
        y -= 0.08
    
    plt.tight_layout()
    plt.savefig(filename, bbox_inches='tight', facecolor=fig.get_facecolor())
    plt.close()

market_data = [
    ("上证指数", "4133.00", "+0.25%"),
    ("深证成指", "-", "+0.78%"),
    ("创业板指", "3349.00", "+1.31%"),
    ("恒生指数", "-", "+0.08%"),
    ("恒生科技", "-", "+0.26%"),
    ("全市场成交额", "2.53万亿", "+1115亿"),
    ("BTC (比特币)", "$69,958", "-0.41%"),
    ("现货黄金", "$5,202.19", "+0.10%"),
    ("布伦特原油", "$87.50", "-0.34%")
]

output_dir = 'images/charts/'
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

create_card(market_data, os.path.join(output_dir, '2026-03-11-evening.png'))
print("Chart generated: images/charts/2026-03-11-evening.png")
