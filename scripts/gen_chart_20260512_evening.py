import matplotlib.pyplot as plt
import matplotlib.font_manager as fm
import os

# Set font for Chinese characters (macOS specific)
font_path = '/System/Library/Fonts/STHeiti Medium.ttc'
prop = fm.FontProperties(fname=font_path)
plt.rcParams['font.sans-serif'] = ['STHeiti']
plt.rcParams['axes.unicode_minus'] = False

def draw_chart():
    data = [
        ("上证指数", 4214.49, -0.25),
        ("深证成指", 15824.58, -0.47),
        ("创业板指", 3934.86, 0.15),
        ("恒生指数", 26347.91, -0.22),
        ("恒生科技", 5070.61, -0.70)
    ]

    fig, ax = plt.subplots(figsize=(10, 6))
    ax.set_facecolor('#f9f9f9')
    
    indices = [item[0] for item in data]
    values = [item[1] for item in data]
    changes = [item[2] for item in data]
    colors = ['#00ba50' if c < 0 else '#ff4d4d' for c in changes]

    bars = ax.bar(indices, [1]*len(indices), color=colors, alpha=0.1) # Background bars for style
    
    for i, (name, val, change) in enumerate(data):
        color = '#00ba50' if change < 0 else '#ff4d4d'
        symbol = "▼" if change < 0 else "▲"
        
        ax.text(i, 0.6, f"{val:.2f}", ha='center', va='center', fontsize=24, fontweight='bold', color=color, fontproperties=prop)
        ax.text(i, 0.4, f"{symbol} {abs(change):.2f}%", ha='center', va='center', fontsize=18, color=color, fontproperties=prop)
        ax.text(i, 0.8, name, ha='center', va='center', fontsize=16, color='#333333', fontproperties=prop)

    ax.set_ylim(0, 1)
    ax.axis('off')
    
    plt.title("核心行情快报 (2026-05-12 收盘)", fontproperties=prop, fontsize=20, pad=20)
    
    output_path = 'images/charts/2026-05-12-evening.png'
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    plt.savefig(output_path, bbox_inches='tight', dpi=150)
    print(f"Chart saved to {output_path}")

if __name__ == "__main__":
    draw_chart()
