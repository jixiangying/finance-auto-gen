import matplotlib.pyplot as plt
import matplotlib.font_manager as fm
import os

# Create directory if it doesn't exist
os.makedirs('images/charts', exist_ok=True)

# Function to create a data card
def create_card(title, price, change_pct, filename):
    # Setup font - macOS specific
    font_path = '/System/Library/Fonts/STHeiti Medium.ttc'
    if not os.path.exists(font_path):
        font_path = '/System/Library/Fonts/Supplemental/Arial.ttf' # Fallback
    
    prop = fm.FontProperties(fname=font_path)
    
    fig, ax = plt.subplots(figsize=(6, 3), dpi=100)
    fig.patch.set_facecolor('#f4f4f4')
    ax.axis('off')
    
    # Color based on change
    color = '#e15b5b' if change_pct >= 0 else '#5bb15b' # Red for up, Green for down
    trend = '▲' if change_pct >= 0 else '▼'
    
    # Draw card background
    rect = plt.Rectangle((0, 0), 1, 1, transform=ax.transAxes, color='white', ec='#dddddd', lw=2, zorder=1)
    ax.add_patch(rect)
    
    # Add text
    plt.text(0.1, 0.7, title, fontsize=20, weight='bold', fontproperties=prop, zorder=2)
    plt.text(0.1, 0.35, f"{price}", fontsize=36, weight='bold', color='#333333', zorder=2)
    plt.text(0.65, 0.35, f"{trend} {abs(change_pct):.2f}%", fontsize=24, weight='bold', color=color, zorder=2)
    
    plt.tight_layout()
    plt.savefig(f'images/charts/{filename}', bbox_inches='tight', facecolor='#f4f4f4')
    plt.close()

# Data for 2026-03-19 evening
data = [
    ("上证指数", "4006.55", -1.39, "2026-03-19-shanghai.png"),
    ("深证成指", "13901.57", -2.02, "2026-03-19-shenzhen.png"),
    ("创业板指", "2843.12", -1.83, "2026-03-19-chinext.png"),
    ("恒生指数", "19342.38", 0.61, "2026-03-19-hangseng.png"),
    ("恒生科技", "4218.45", 0.01, "2026-03-19-hstech.png")
]

for title, price, change, filename in data:
    create_card(title, price, change, filename)

print("Charts generated successfully.")
