import matplotlib.pyplot as plt
import matplotlib.font_manager as fm
import os

# Create directory if not exists
output_dir = "/Users/jxy/Documents/Project/finance-auto-gen/images/charts"
os.makedirs(output_dir, exist_ok=True)

# Font setting for macOS
font_path = '/System/Library/Fonts/STHeiti Medium.ttc'
if not os.path.exists(font_path):
    font_path = '/System/Library/Fonts/PingFang.ttc'
prop = fm.FontProperties(fname=font_path)
plt.rcParams['font.family'] = prop.get_name()
plt.rcParams['axes.unicode_minus'] = False

# Data
assets = ['比特币', '现货黄金', '纳指', '标普500', '上证指数', '创业板指', '恒生指数', '道指', 'WTI原油']
weekly_changes = [-18.62, -4.65, -4.68, -2.59, -1.00, -1.98, -0.53, -0.32, 3.64]
prices = ['$59,800.00', '$4,331.00', '25,709.43', '7,383.74', '4,027.74', '3,957.94', '25,047.86', '50,866.78', '$90.54']

# Sort by change (descending or ascending) for better visualization
data_sorted = sorted(zip(assets, weekly_changes, prices), key=lambda x: x[1])
assets_s, changes_s, prices_s = zip(*data_sorted)

colors = ['#ff4d4d' if x > 0 else '#2ecc71' for x in changes_s]

fig, ax = plt.subplots(figsize=(10, 6), dpi=150)
fig.patch.set_facecolor('#f8f9fa')
ax.set_facecolor('#f8f9fa')

bars = ax.barh(assets_s, changes_s, color=colors, height=0.6)

# Add value labels
for i, bar in enumerate(bars):
    width = bar.get_width()
    label_x = width + (0.2 if width > 0 else -0.2)
    ha_align = 'left' if width > 0 else 'right'
    ax.text(label_x, bar.get_y() + bar.get_height()/2, 
            f'{prices_s[i]}\n({"+" if changes_s[i]>0 else ""}{changes_s[i]}%)', 
            va='center', ha=ha_align,
            fontproperties=prop, fontsize=9, fontweight='bold',
            color='#2c3e50')

# Decoration
ax.axvline(0, color='black', linewidth=0.8, linestyle='--')
ax.set_title('本周全球核心资产涨跌幅 (6/01 - 6/05)', fontproperties=prop, fontsize=16, pad=20)
ax.set_xlabel('周涨跌幅 (%)', fontproperties=prop, fontsize=12)
ax.set_xlim(-22, 6)

# Set tick fonts explicitly to prevent box characters
ax.set_yticklabels(assets_s, fontproperties=prop, fontsize=11)
for label in ax.get_xticklabels():
    label.set_fontproperties(prop)

plt.tight_layout()

# Save the plot
output_path = os.path.join(output_dir, '2026-06-06-evening.png')
plt.savefig(output_path, dpi=300, bbox_inches='tight')
print(f"Chart saved to {output_path}")
