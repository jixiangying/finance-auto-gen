import matplotlib.pyplot as plt
import matplotlib.font_manager as fm
import os

# Set up font for Chinese support (macOS)
font_path = '/System/Library/Fonts/STHeiti Medium.ttc'
if not os.path.exists(font_path):
    font_path = '/System/Library/Fonts/Supplemental/Songti.ttc' # Fallback
    
prop = fm.FontProperties(fname=font_path)
plt.rcParams['font.family'] = prop.get_name()
plt.rcParams['axes.unicode_minus'] = False

# Data
labels = ['S&P 500', 'Nasdaq', 'Dow Jones', 'US 10Y Yield', 'Gold', 'WTI Oil', 'Bitcoin']
values = [0.38, 0.34, 0.27, 1.15, -1.00, 3.00, 0.66] # Change percentages
prices = ['7,427.07', '26,336.86', '49,743.44', '4.41%', '$4,667', '$98.07', '$81,951']

# Note: US 10Y Yield rose 5bps from ~4.36% to 4.41%, which is approx 1.15% relative change.

colors = ['red' if v > 0 else 'green' for v in values]

fig, ax = plt.subplots(figsize=(10, 6))
bars = ax.barh(labels, values, color=colors)

# Add price labels
for bar, price, val in zip(bars, prices, values):
    width = bar.get_width()
    label_x_pos = width if width > 0 else width - 0.1
    ax.text(label_x_pos, bar.get_y() + bar.get_height()/2, f'{price} ({val:+.2f}%)', 
            va='center', ha='left' if width > 0 else 'right', fontproperties=prop, fontsize=12)

ax.set_title('核心行情快报 (2026-05-12 Morning)', fontproperties=prop, fontsize=16)
ax.set_xlabel('涨跌幅 (%)', fontproperties=prop)
ax.axvline(0, color='black', linewidth=0.8)

# Set tick fonts
ax.set_yticklabels(labels, fontproperties=prop)

plt.tight_layout()
output_path = 'images/charts/2026-05-12-morning.png'
os.makedirs(os.path.dirname(output_path), exist_ok=True)
plt.savefig(output_path, dpi=300)
print(f"Chart saved to {output_path}")
