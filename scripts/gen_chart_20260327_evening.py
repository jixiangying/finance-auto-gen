import matplotlib.pyplot as plt
import matplotlib.font_manager as fm

# Define data
asset_names = ['上证指数', '深证成指', '创业板指', '恒生指数', '恒生科技']
current_prices = ['3,889.08', '13,606.44', '2,815.12', '24,856.43', '跌幅超2%']
percent_changes = [-1.09, -1.41, -1.34, -1.89, -2.00]

# Set Chinese font
font_path = '/System/Library/Fonts/STHeiti Medium.ttc'
prop = fm.FontProperties(fname=font_path)
plt.rcParams['axes.unicode_minus'] = False

# Create figure
fig, ax = plt.subplots(figsize=(8, 5))
ax.axis('off')

# Table data
table_data = [['资产名称', '现价', '涨跌幅']]
for i in range(len(asset_names)):
    table_data.append([asset_names[i], current_prices[i], f"{percent_changes[i]:+.2f}%"])

# Table styling
cell_colors = [['#455a64', '#455a64', '#455a64']]
for pc in percent_changes:
    if pc > 0:
        cell_colors.append(['#ffebee', '#ffebee', '#ffebee'])
    else:
        cell_colors.append(['#e8f5e9', '#e8f5e9', '#e8f5e9'])

table = ax.table(cellText=table_data,
                 cellColours=cell_colors,
                 cellLoc='center',
                 loc='center')

table.auto_set_font_size(False)
table.set_fontsize(14)
table.scale(1.2, 2.5)

# Style cells
for (row, col), cell in table.get_celld().items():
    if row == 0:
        cell.set_text_props(fontproperties=prop, weight='bold', color='white')
    else:
        cell.set_text_props(fontproperties=prop)
        if col == 2:
            val = percent_changes[row-1]
            cell.get_text().set_color('green' if val < 0 else 'red')

plt.title('2026年3月27日 国内市场收盘速览', fontproperties=prop, fontsize=18, pad=20)
plt.tight_layout()
plt.savefig('images/charts/2026-03-27-evening.png', dpi=300, bbox_inches='tight')
print("Chart generated successfully at images/charts/2026-03-27-evening.png")
