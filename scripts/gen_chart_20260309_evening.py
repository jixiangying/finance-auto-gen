import matplotlib.pyplot as plt
from matplotlib.font_manager import FontProperties
import os

# Set up directories
os.makedirs('images/charts', exist_ok=True)

# Font configuration for Chinese support on macOS
# Try to find a system font that supports Chinese
font_path = '/System/Library/Fonts/STHeiti Medium.ttc'
if os.path.exists(font_path):
    prop = FontProperties(fname=font_path)
    plt.rcParams['font.family'] = prop.get_name()
    # Explicitly set the font for Chinese text if needed
else:
    # Fallback to general settings
    plt.rcParams['font.sans-serif'] = ['STHeiti', 'Heiti TC', 'Arial Unicode MS', 'sans-serif']
plt.rcParams['axes.unicode_minus'] = False # Fix minus sign display issues
data = [
    {"name": "上证指数", "value": "4096.60", "change": "-0.67%"},
    {"name": "恒生指数", "value": "25757.29", "change": "-1.35%"},
    {"name": "两市成交额", "value": "2.65万亿", "change": "+4474亿"},
    {"name": "南向资金", "value": "372.1亿", "change": "净买入(新高)"},
    {"name": "中国海油", "value": "创历史新高", "change": "+3.31%"}
]

# Create figure
fig, ax = plt.subplots(figsize=(8, 4), facecolor='#1a1a1a')
ax.set_xlim(0, 100)
ax.set_ylim(0, len(data) * 20 + 20)
ax.axis('off')

# Title
plt.text(50, len(data) * 20 + 5, "2026-03-09 收盘行情快报", color='white', ha='center', fontsize=18, weight='bold')

# Draw headers
plt.text(10, len(data) * 20 - 5, "资产名称", color='#aaaaaa', ha='left', fontsize=12)
plt.text(50, len(data) * 20 - 5, "现价/数值", color='#aaaaaa', ha='center', fontsize=12)
plt.text(90, len(data) * 20 - 5, "涨跌/动向", color='#aaaaaa', ha='right', fontsize=12)

# Draw data rows
for i, item in enumerate(data):
    y = (len(data) - 1 - i) * 20 + 10
    color = '#ff4444' if '-' in item['change'] else '#44ff44'
    if '净买入' in item['change']: color = '#44ff44'
    
    plt.text(10, y, item['name'], color='white', ha='left', fontsize=14)
    plt.text(50, y, item['value'], color='white', ha='center', fontsize=14)
    plt.text(90, y, item['change'], color=color, ha='right', fontsize=14, weight='bold')
    
    # Separator
    ax.plot([10, 90], [y - 8, y - 8], color='#333333', lw=0.5)

plt.tight_layout()
plt.savefig('images/charts/2026-03-09-evening.png', dpi=100, bbox_inches='tight')
plt.close()
print("Market info card saved to images/charts/2026-03-09-evening.png")
