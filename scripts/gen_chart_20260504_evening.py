import matplotlib.pyplot as plt
import matplotlib.font_manager as fm
import os

# Set font for Chinese characters (macOS)
font_path = '/System/Library/Fonts/STHeiti Medium.ttc'
if not os.path.exists(font_path):
    font_path = '/System/Library/Fonts/PingFang.ttc'

prop = fm.FontProperties(fname=font_path)
plt.rcParams['font.family'] = prop.get_name()
plt.rcParams['axes.unicode_minus'] = False

def draw_card(data, output_path):
    fig, ax = plt.subplots(figsize=(10, 4))
    ax.set_facecolor('#f4f4f4')
    fig.patch.set_facecolor('#f4f4f4')

    # Remove axes
    ax.xaxis.set_visible(False)
    ax.yaxis.set_visible(False)
    for spine in ax.spines.values():
        spine.set_visible(False)

    x_start = 0.05
    y_start = 0.7
    col_width = 0.3

    for i, item in enumerate(data):
        name = item['name']
        value = item['value']
        change = item['change']
        color = 'red' if '+' in change else 'green'
        
        x = x_start + i * col_width
        
        # Name
        ax.text(x, y_start, name, fontproperties=prop, fontsize=18, fontweight='bold', color='#333333')
        # Value
        ax.text(x, y_start - 0.25, value, fontproperties=prop, fontsize=24, fontweight='bold', color=color)
        # Change
        ax.text(x, y_start - 0.45, change, fontproperties=prop, fontsize=16, color=color)

    plt.title('核心资产休市/假期行情表现 (2026-05-04)', fontproperties=prop, fontsize=22, pad=20)
    plt.tight_layout()
    plt.savefig(output_path, dpi=200, bbox_inches='tight')
    plt.close()

if __name__ == '__main__':
    data = [
        {'name': '富时中国A50期货', 'value': '15,670', 'change': '+0.15%'},
        {'name': '离岸人民币(CNH)', 'value': '6.8239', 'change': '+0.12% (升值)'},
        {'name': '比特币 (BTC)', 'value': '80,594', 'change': '+2.50%'}
    ]
    
    output_dir = 'images/charts'
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    
    draw_card(data, os.path.join(output_dir, '20260504_evening.png'))
    print(f"Chart saved to {output_dir}/20260504_evening.png")
