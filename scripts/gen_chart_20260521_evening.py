import matplotlib.pyplot as plt
import matplotlib.font_manager as fm
import os

# Data
indices = [
    {"name": "上证指数", "value": "4077.28", "change": "-2.04%"},
    {"name": "深证成指", "value": "15247.27", "change": "-2.07%"},
    {"name": "创业板指", "value": "3829.78", "change": "-2.35%"},
    {"name": "恒生指数", "value": "25386.52", "change": "-1.03%"},
    {"name": "恒生科技", "value": "4768.90", "change": "-2.15%"}
]

# Style settings
# In China: Red is up, Green is down.
# All are down today.
bg_color = "#1a1a1a"
text_color = "#ffffff"
down_color = "#00ff00"  # Green for down
up_color = "#ff4d4d"    # Red for up

fig, ax = plt.subplots(figsize=(10, 6), facecolor=bg_color)
ax.set_facecolor(bg_color)
ax.axis('off')

# Font setup for macOS
font_path = "/System/Library/Fonts/STHeiti Medium.ttc"
if not os.path.exists(font_path):
    font_path = "/System/Library/Fonts/PingFang.ttc"
prop = fm.FontProperties(fname=font_path)

# Draw Title
plt.text(0.5, 0.9, "核心行情数据卡片 (2026-05-21 晚间)", 
         color=text_color, fontsize=24, fontweight='bold', 
         ha='center', fontproperties=prop)

# Draw Cards
start_y = 0.7
for i, item in enumerate(indices):
    y = start_y - i * 0.15
    color = down_color if "-" in item["change"] else up_color
    
    # Index Name
    plt.text(0.2, y, item["name"], color=text_color, fontsize=20, ha='left', fontproperties=prop)
    
    # Value
    plt.text(0.5, y, item["value"], color=text_color, fontsize=20, ha='center', fontproperties=prop)
    
    # Change
    plt.text(0.8, y, item["change"], color=color, fontsize=20, ha='right', fontproperties=prop)

# Save
output_path = "images/charts/2026-05-21-evening.png"
os.makedirs(os.path.dirname(output_path), exist_ok=True)
plt.savefig(output_path, dpi=300, bbox_inches='tight', facecolor=bg_color)
print(f"Chart saved to {output_path}")
