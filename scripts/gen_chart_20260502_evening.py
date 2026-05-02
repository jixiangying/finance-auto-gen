import matplotlib.pyplot as plt
import matplotlib.font_manager as fm
import os

# 设置中文字体
font_path = '/System/Library/Fonts/STHeiti Medium.ttc'
prop = fm.FontProperties(fname=font_path)

# 数据
assets = ['Nasdaq', 'S&P 500', 'Dow', 'SSE', 'A50', 'BTC', 'WTI', 'Gold']
daily_changes = [0.89, 0.29, -0.31, 0, -0.75, 1.46, -2.83, -0.15]
weekly_changes = [0.2, 0.12, -0.13, 0.81, 1.4, 1.5, 5.5, 2.1]

fig, ax = plt.subplots(figsize=(10, 6))
x = range(len(assets))
width = 0.35

rects1 = ax.bar([i - width/2 for i in x], daily_changes, width, label='Friday Change %', color=['red' if v > 0 else 'green' for v in daily_changes])
rects2 = ax.bar([i + width/2 for i in x], weekly_changes, width, label='Weekly Change %', color=['#ff9999' if v > 0 else '#99ff99' for v in weekly_changes])

ax.set_ylabel('Change %', fontproperties=prop)
ax.set_title('Global Assets Weekend Review (2026-05-02)', fontproperties=prop)
ax.set_xticks(x)
ax.set_xticklabels(assets, fontproperties=prop)
ax.legend(prop=prop)

# 辅助线
ax.axhline(0, color='black', linewidth=0.8)

# 自动标注数值
def autolabel(rects):
    for rect in rects:
        height = rect.get_height()
        ax.annotate(f'{height}%',
                    xy=(rect.get_x() + rect.get_width() / 2, height),
                    xytext=(0, 3 if height > 0 else -12),
                    textcoords="offset points",
                    ha='center', va='bottom', fontproperties=prop)

autolabel(rects1)
autolabel(rects2)

plt.tight_layout()

# 确保目录存在
os.makedirs('images/charts', exist_ok=True)
plt.savefig('images/charts/2026-05-02-evening-chart.png')
print("Chart saved to images/charts/2026-05-02-evening-chart.png")
