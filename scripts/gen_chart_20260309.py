import matplotlib.pyplot as plt
import matplotlib.patches as patches

def create_market_card(data, filename):
    fig, ax = plt.subplots(figsize=(10, 6), dpi=100)
    ax.set_facecolor('#0f172a')
    fig.patch.set_facecolor('#0f172a')
    
    # Draw Title
    plt.text(0.5, 0.9, 'Market Data Overview - March 09, 2026', 
             color='white', fontsize=20, ha='center', fontweight='bold')
    
    y_pos = 0.7
    for item in data:
        name, price, change, is_up = item
        color = '#ef4444' if not is_up else '#22c55e'
        icon = '🔴' if not is_up else '🟢'
        
        # Rect backdrop for each row
        rect = patches.FancyBboxPatch((0.1, y_pos - 0.05), 0.8, 0.12, 
                                     boxstyle="round,pad=0.02", 
                                     linewidth=0, edgecolor='none', facecolor='#1e293b')
        ax.add_patch(rect)
        
        plt.text(0.15, y_pos, f"{icon} {name}", color='white', fontsize=16, va='center')
        plt.text(0.5, y_pos, f"{price}", color='white', fontsize=16, va='center', ha='center')
        plt.text(0.85, y_pos, f"{change}", color=color, fontsize=16, va='center', ha='right', fontweight='bold')
        
        y_pos -= 0.15

    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    ax.axis('off')
    
    plt.savefig(filename, bbox_inches='tight', facecolor=fig.get_facecolor())
    plt.close()

# Monday Morning Data
market_data = [
    ("Bitcoin (BTC)", "$67,245", "-1.45%", False),
    ("Ethereum (ETH)", "$1,969", "-0.47%", False),
    ("Brent Crude Oil", "$90.85", "+3.20%", True),
    ("Gold (XAU)", "$2,245", "+1.10%", True),
    ("US 10Y Yield", "4.12%", "-2.50%", False)
]

create_market_card(market_data, 'images/charts/2026-03-09-morning-chart.png')
