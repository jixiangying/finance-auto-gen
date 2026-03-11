import matplotlib.pyplot as plt
import matplotlib.patches as patches
from PIL import Image, ImageDraw, ImageFont
import os

# Set font for macOS
plt.rcParams['font.sans-serif'] = ['Arial Unicode MS'] # Common on macOS
plt.rcParams['axes.unicode_minus'] = False

def create_card(name, value, change_pct, filename):
    color = '#e74c3c' if change_pct >= 0 else '#2ecc71' # Red for up, Green for down (standard in some contexts, but skill says Red up 🔴, Green down 🟢)
    # Re-reading skill: "红色代表上涨 🔴，绿色代表下跌 🟢" -> Red for up, Green for down.
    
    fig, ax = plt.subplots(figsize=(4, 2))
    fig.patch.set_facecolor('#f8f9fa')
    ax.set_facecolor('#f8f9fa')
    
    # Draw background
    ax.add_patch(patches.Rectangle((0, 0), 1, 1, transform=ax.transAxes, color='#ffffff', ec='#dee2e6', lw=2))
    
    # Text
    plt.text(0.1, 0.7, name, fontsize=16, fontweight='bold', transform=ax.transAxes)
    plt.text(0.1, 0.4, f"{value}", fontsize=24, fontweight='bold', color='#2c3e50', transform=ax.transAxes)
    
    prefix = "+" if change_pct >= 0 else ""
    plt.text(0.1, 0.15, f"{prefix}{change_pct:.2f}%", fontsize=18, fontweight='bold', color=color, transform=ax.transAxes)
    
    plt.axis('off')
    plt.tight_layout()
    
    output_path = f"images/charts/{filename}"
    plt.savefig(output_path, dpi=100, bbox_inches='tight', facecolor='#f8f9fa')
    plt.close()
    print(f"Saved {output_path}")

# Ensure directory exists
os.makedirs('images/charts', exist_ok=True)

data = [
    ("S&P 500", "6,781.48", -0.21, "sp500_card.png"),
    ("Nasdaq", "22,697.10", 0.01, "nasdaq_card.png"),
    ("Dow Jones", "47,706.51", -0.07, "dow_card.png"),
    ("Gold", "$5,231.79", 1.9, "gold_card.png"),
    ("Oil (WTI)", "$83.45", -10.0, "oil_card.png"),
    ("Bitcoin", "$70,665", 2.1, "btc_card.png")
]

for item in data:
    create_card(*item)
