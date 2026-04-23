import matplotlib.pyplot as plt
import matplotlib.font_manager as fm
import os

# Set up the font for Chinese characters
font_path = '/System/Library/Fonts/STHeiti Medium.ttc'
if not os.path.exists(font_path):
    font_path = '/System/Library/Fonts/PingFang.ttc'

prop = fm.FontProperties(fname=font_path)
plt.rcParams['axes.unicode_minus'] = False

def create_market_card(data, output_path):
    fig, ax = plt.subplots(figsize=(8, 6))
    ax.set_facecolor('#f4f4f4')
    fig.patch.set_facecolor('#ffffff')

    # Remove axes
    ax.axis('off')

    # Title
    plt.text(0.5, 0.92, '今日市场核心数据 (2026-04-23 收盘)', 
             horizontalalignment='center', fontsize=20, fontproperties=prop, weight='bold')

    # Table headers
    headers = ['资产名称', '收盘点位', '涨跌幅']
    y_start = 0.82
    plt.axhline(y=y_start+0.03, xmin=0.1, xmax=0.9, color='#333333', linewidth=2)
    for i, h in enumerate(headers):
        plt.text(0.2 + i*0.3, y_start, h, horizontalalignment='center', 
                 fontsize=14, fontproperties=prop, weight='bold', color='#333333')
    plt.axhline(y=y_start-0.03, xmin=0.1, xmax=0.9, color='#333333', linewidth=1)

    # Data rows
    for j, row in enumerate(data):
        y_pos = y_start - (j + 1) * 0.12
        name, value, change = row
        # Red for up (+), Green for down (-)
        color = '#e63946' if '+' in change else '#2a9d8f'
        
        plt.text(0.2, y_pos, name, horizontalalignment='center', fontsize=14, fontproperties=prop)
        plt.text(0.5, y_pos, value, horizontalalignment='center', fontsize=14)
        plt.text(0.8, y_pos, change, horizontalalignment='center', fontsize=14, color=color, weight='bold')
        if j < len(data) - 1:
            plt.axhline(y=y_pos-0.05, xmin=0.1, xmax=0.9, color='#dddddd', linewidth=0.5, linestyle='--')

    plt.tight_layout()
    plt.savefig(output_path, dpi=200, bbox_inches='tight')
    plt.close()

data = [
    ['上证指数', '4093.25', '-0.32%'],
    ['深证成指', '15043.45', '-0.88%'],
    ['创业板指', '3720.25', '-0.87%'],
    ['恒生指数', '25915.20', '-0.95%'],
    ['恒生科技', '4865.52', '-1.98%']
]

output_dir = 'images/charts'
os.makedirs(output_dir, exist_ok=True)
create_market_card(data, os.path.join(output_dir, '2026-04-23-evening.png'))
print("Chart generated successfully.")
