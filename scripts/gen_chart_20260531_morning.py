import matplotlib.pyplot as plt
import matplotlib.font_manager as fm
import os

# 显式设置支持中文的字体
font_path = '/System/Library/Fonts/STHeiti Medium.ttc'
if not os.path.exists(font_path):
    font_path = '/System/Library/Fonts/Cache/PingFang.ttc' # Alternative for some macOS versions

prop = fm.FontProperties(fname=font_path)
plt.rcParams['font.sans-serif'] = [prop.get_name()]
plt.rcParams['axes.unicode_minus'] = False

# 数据
assets = ['道琼斯', '标普500', '纳斯达克', 'WTI原油', '现货黄金', '中国PMI']
values = ['51032.46', '7580.06', '26972.62', '$87.93', '$4544.30', '49.6']
changes = [0.90, 1.43, 2.39, -9.35, 0.75, -1.39] # PMI 较前值 50.3 下降约 1.39%

colors = ['#ff4d4f' if c > 0 else '#52c41a' for c in changes]

fig, ax = plt.subplots(figsize=(10, 6))
fig.patch.set_facecolor('#f0f2f5')
ax.set_facecolor('#f0f2f5')

bars = ax.barh(assets, [abs(c) for c in changes], color=colors, height=0.6)

# 添加数值和涨跌幅
for i, (bar, val, change) in enumerate(zip(bars, values, changes)):
    width = bar.get_width()
    label = f"{val} ({'+' if change > 0 else ''}{change}%)"
    ax.text(width + 0.1, bar.get_y() + bar.get_height()/2, label, 
            va='center', fontproperties=prop, fontsize=12, fontweight='bold')

ax.set_title('全球核心资产本周表现 (截至2026-05-31)', fontproperties=prop, fontsize=16, pad=20)
ax.set_xlabel('周涨跌幅 (%)', fontproperties=prop, fontsize=12)
ax.set_xlim(0, max([abs(c) for c in changes]) + 2)

# 隐藏边框
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)

# 设置刻度字体
ax.set_yticklabels(assets, fontproperties=prop, fontsize=12)

plt.tight_layout()
output_path = 'images/charts/2026-05-31-morning.png'
os.makedirs(os.path.dirname(output_path), exist_ok=True)
plt.savefig(output_path, dpi=300, bbox_inches='tight')
print(f"Chart saved to {output_path}")
