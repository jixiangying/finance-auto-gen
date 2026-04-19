import matplotlib.pyplot as plt
import matplotlib.font_manager as fm
import os

# Data for the chart
indices = ['S&P 500', 'Nasdaq', 'Dow Jones', 'CSI 300', 'Hang Seng']
values = [7126.06, 24468.48, 49447.43, 4728.67, 26160.33]
changes = [4.54, 6.84, 3.0, 0.7, 1.7]
colors = ['#e63946' if c > 0 else '#2a9d8f' for c in changes] # Red for up, Green for down

# Set font for macOS
font_path = '/System/Library/Fonts/STHeiti Medium.ttc'
if not os.path.exists(font_path):
    font_path = '/System/Library/Fonts/Supplemental/Arial.ttf' # Fallback
prop = fm.FontProperties(fname=font_path)

fig, ax = plt.subplots(figsize=(10, 6))
fig.patch.set_facecolor('#f8f9fa')
ax.set_facecolor('#f8f9fa')

# Create horizontal bars
bars = ax.barh(indices, changes, color=colors, height=0.6)

# Add labels and formatting
ax.set_title('Global Market Weekly Performance (Ending April 17, 2026)', fontproperties=prop, fontsize=18, fontweight='bold', pad=20)
ax.set_xlabel('Weekly Change (%)', fontproperties=prop, fontsize=12)
ax.invert_yaxis()  # Labels read top-to-bottom

# Add value labels to the bars
for i, bar in enumerate(bars):
    width = bar.get_width()
    label_x_pos = width + (0.1 if width > 0 else -0.5)
    ax.text(label_x_pos, bar.get_y() + bar.get_height()/2, f'{values[i]:,.2f} ({changes[i]:+g}%)', 
            va='center', fontproperties=prop, fontsize=12, fontweight='bold', color=colors[i])

# Customizing spines and grid
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
ax.spines['left'].set_linewidth(1.5)
ax.spines['bottom'].set_linewidth(1.5)
ax.grid(axis='x', linestyle='--', alpha=0.7)

# Set tick labels font
ax.set_yticklabels(indices, fontproperties=prop, fontsize=12)
ax.tick_params(axis='x', labelsize=10)

plt.tight_layout()

# Save the plot
output_dir = 'images/charts'
os.makedirs(output_dir, exist_ok=True)
output_path = os.path.join(output_dir, '20260419_morning.png')
plt.savefig(output_path, dpi=300, bbox_inches='tight')
print(f"Chart saved to {output_path}")
