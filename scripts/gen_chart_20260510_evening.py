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
    plt.text(0.5, 0.92, '新一周市场核心博弈前瞻 (2026-05-10)', 
             horizontalalignment='center', fontsize=20, fontproperties=prop, weight='bold')

    # Table headers
    headers = ['指标名称', '当前/预期数值', '趋势/影响']
    y_start = 0.8
    for i, h in enumerate(headers):
        plt.text(0.15 + i*0.35, y_start, h, horizontalalignment='center', 
                 fontsize=14, fontproperties=prop, weight='bold', color='#333333')

    # Data rows
    for j, row in enumerate(data):
        y_pos = y_start - (j + 1) * 0.12
        name, value, change = row
        color = '#e63946' if '利好' in change or '+' in value or '回升' in change else ('#2a9d8f' if '承压' in change or '-' in value else '#333333')
        
        plt.text(0.15, y_pos, name, horizontalalignment='center', fontsize=14, fontproperties=prop)
        plt.text(0.5, y_pos, value, horizontalalignment='center', fontsize=14)
        plt.text(0.85, y_pos, change, horizontalalignment='center', fontsize=14, fontproperties=prop, color=color, weight='bold')

    plt.tight_layout()
    plt.savefig(output_path, dpi=200, bbox_inches='tight')
    plt.close()

data = [
    ['中国 4月 CPI', '+0.3%', '消费温和回升'],
    ['中国 4月 PPI', '-2.1%', '工业端降幅收窄'],
    ['比特币 (BTC)', '$81,245', '+1.3% (周末表现)'],
    ['A50 指数期货', '+0.45%', '预示开盘乐观'],
    ['离岸人民币', '7.2250', '汇率维持稳定']
]

output_dir = 'images/charts'
os.makedirs(output_dir, exist_ok=True)
create_market_card(data, os.path.join(output_dir, '2026-05-10-evening.png'))
