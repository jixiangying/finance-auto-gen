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
    fig, ax = plt.subplots(figsize=(8, 5))
    ax.set_facecolor('#f4f4f4')
    fig.patch.set_facecolor('#ffffff')

    # Remove axes
    ax.axis('off')

    # Title
    plt.text(0.5, 0.9, '今日市场核心数据 (2026-03-10 收盘)', 
             horizontalalignment='center', fontsize=20, fontproperties=prop, weight='bold')

    # Table headers
    headers = ['资产名称', '点位/指数', '涨跌幅']
    y_start = 0.75
    for i, h in enumerate(headers):
        plt.text(0.2 + i*0.3, y_start, h, horizontalalignment='center', 
                 fontsize=14, fontproperties=prop, weight='bold', color='#333333')

    # Data rows
    for j, row in enumerate(data):
        y_pos = y_start - (j + 1) * 0.12
        name, value, change = row
        color = '#e63946' if '+' in change else '#2a9d8f' # Red for up, Green for down
        
        plt.text(0.2, y_pos, name, horizontalalignment='center', fontsize=14, fontproperties=prop)
        plt.text(0.5, y_pos, value, horizontalalignment='center', fontsize=14)
        plt.text(0.8, y_pos, change, horizontalalignment='center', fontsize=14, color=color, weight='bold')

    plt.tight_layout()
    plt.savefig(output_path, dpi=200, bbox_inches='tight')
    plt.close()

data = [
    ['上证指数', '4123', '+0.65%'],
    ['深证成指', '-', '+2.04%'],
    ['创业板指', '-', '+3.04%'],
    ['恒生指数', '-', '+2.17%'],
    ['恒生科技', '-', '+2.40%']
]

output_dir = 'images/charts'
os.makedirs(output_dir, exist_ok=True)
create_market_card(data, os.path.join(output_dir, '2026-03-10-evening.png'))
