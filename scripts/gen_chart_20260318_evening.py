
import matplotlib.pyplot as plt
from PIL import Image, ImageDraw, ImageFont
import os

# Ensure directory exists
os.makedirs('images/charts', exist_ok=True)

def create_card(name, value, change, filename):
    # Determine trend: Chinese standard (Red=Up, Green=Down)
    # The 'change' string might start with '+' or '-'
    is_up = '+' in change or (float(change.strip('%')) > 0 if '%' in change and change.strip('%') else False)
    
    # Colors (Chinese Market Standard)
    if is_up:
        bg_color = (255, 235, 235)  # Light Red
        text_color = (220, 20, 60)   # Crimson/Red
    else:
        bg_color = (235, 255, 235)  # Light Green
        text_color = (34, 139, 34)   # Forest Green/Green
    
    # Create image
    img = Image.new('RGB', (400, 220), color=bg_color)
    draw = ImageDraw.Draw(img)
    
    # Use system font (macOS)
    font_path = "/System/Library/Fonts/STHeiti Medium.ttc"
    try:
        font_title = ImageFont.truetype(font_path, 32)
        font_value = ImageFont.truetype(font_path, 52)
        font_change = ImageFont.truetype(font_path, 38)
    except:
        # Fallback for non-macOS or missing font
        font_title = ImageFont.load_default()
        font_value = ImageFont.load_default()
        font_change = ImageFont.load_default()

    draw.text((25, 30), name, font=font_title, fill=(50, 50, 50))
    draw.text((25, 85), value, font=font_value, fill=(0, 0, 0))
    draw.text((25, 150), change, font=font_change, fill=text_color)
    
    # Add trend indicator
    indicator = "▲" if is_up else "▼"
    draw.text((340, 30), indicator, font=font_title, fill=text_color)
    
    save_path = f'images/charts/{filename}'
    img.save(save_path)
    print(f"Generated: {save_path}")

# Data from research (March 18, 2026 Evening)
# Format: (Name, Value, Change, Filename)
assets = [
    ("上证指数", "4062.98", "+0.32%", "2026-03-18-shanghai.png"),
    ("深证成指", "14187.80", "+1.05%", "2026-03-18-shenzhen.png"),
    ("创业板指", "3346.37", "+2.02%", "2026-03-18-chinext.png"),
    ("恒生指数", "26000.00", "+0.50%", "2026-03-18-hangseng.png")
]

for name, val, change, file in assets:
    create_card(name, val, change, file)

print("All evening charts for 2026-03-18 generated successfully.")
