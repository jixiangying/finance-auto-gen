
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm
import os

# Set font for macOS to support Chinese
prop = fm.FontProperties(fname='/System/Library/Fonts/STHeiti Medium.ttc')
plt.rcParams['font.sans-serif'] = ['PingFang SC']
plt.rcParams['axes.unicode_minus'] = False

def generate_chart():
    # Data
    labels = ['S&P 500', 'Nasdaq', 'Dow Jones', 'China A50', 'Bitcoin']
    values = [7209.01, 24892.31, 49652.14, 15508.00, 77300]
    pct_changes = [1.02, 0.89, 1.62, 0.36, 1.28]
    
    # Colors: Red for Up (Chinese Market Style)
    colors = ['#ff4d4d' if v > 0 else '#2ecc71' for v in pct_changes]
    
    fig, ax = plt.subplots(figsize=(10, 6))
    fig.patch.set_facecolor('#f8f9fa')
    ax.set_facecolor('#f8f9fa')
    
    y_pos = range(len(labels))
    bars = ax.barh(y_pos, pct_changes, color=colors, height=0.6)
    
    # Add labels and values
    for i, (bar, val, pct) in enumerate(zip(bars, values, pct_changes)):
        label_text = f"{val:,.2f} ({'+' if pct > 0 else ''}{pct:.2f}%)"
        ax.text(pct + (0.1 if pct > 0 else -0.1), i, label_text, 
                va='center', ha='left' if pct > 0 else 'right',
                fontproperties=prop, fontsize=12, fontweight='bold')
    
    ax.set_yticks(y_pos)
    ax.set_yticklabels(labels, fontproperties=prop, fontsize=14)
    ax.set_xlabel('涨跌幅 (%)', fontproperties=prop, fontsize=12)
    ax.set_title('全球核心资产表现 (2026-05-01 上午)', fontproperties=prop, fontsize=18, pad=20)
    
    # Grid and spines
    ax.xaxis.grid(True, linestyle='--', alpha=0.7)
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.axvline(0, color='black', linewidth=0.8)
    
    plt.tight_layout()
    
    # Save path
    output_path = 'images/charts/20260501_morning.png'
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    plt.savefig(output_path, dpi=300, bbox_inches='tight')
    print(f"Chart saved to {output_path}")

if __name__ == "__main__":
    generate_chart()
