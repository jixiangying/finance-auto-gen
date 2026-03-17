
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

# Data from research (March 17, 2026 Evening)
# Format: (Name, Value, Change, Filename)
assets = [
    ("上证指数", "4049.91", "-0.85%", "2026-03-17-shanghai.png"),
    ("深证成指", "14039.73", "-1.87%", "2026-03-17-shenzhen.png"),
    ("创业板指", "3280.06", "-2.29%", "2026-03-17-chinext.png"),
    ("科创50", "1354.15", "-2.23%", "2026-03-17-star50.png"),
    ("恒生指数", "26088.03", "+0.98%", "2026-03-17-hangseng.png"),
    ("恒生科技", "5222.09", "+1.34%", "2026-03-17-hstech.png")
]

for name, val, change, file in assets:
    create_card(name, val, change, file)

print("All evening charts generated successfully.")
