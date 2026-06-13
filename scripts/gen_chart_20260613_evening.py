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

# Data for 2026-06-08 to 2026-06-12
assets = ['比特币', '上证指数', '标普500', '道指', '纳指', '恒生指数', '现货黄金', '创业板指', 'WTI原油']
weekly_changes = [6.27, 0.09, 0.65, 0.66, 0.70, -0.98, -2.66, -3.22, -6.90]
prices = ['$63,552.30', '4,031.51', '7,431.46', '51,202.26', '25,888.84', '24,718.10', '$4,216.00', '3,830.35', '$84.29']

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
ax.set_title('本周全球核心资产涨跌幅 (6/08 - 6/12)', fontproperties=prop, fontsize=16, pad=20)
ax.set_xlabel('周涨跌幅 (%)', fontproperties=prop, fontsize=12)
ax.set_xlim(-10, 10)

# Set tick fonts explicitly to prevent box characters
ax.set_yticklabels(assets_s, fontproperties=prop, fontsize=11)
for label in ax.get_xticklabels():
    label.set_fontproperties(prop)

plt.tight_layout()

# Save the plot
output_path = os.path.join(output_dir, '2026-06-13-evening.png')
plt.savefig(output_path, dpi=300, bbox_inches='tight')
print(f"Chart saved to {output_path}")
