
from PIL import Image, ImageDraw, ImageFont
import os

# Ensure directory exists
os.makedirs('images/charts', exist_ok=True)

def create_card(name, value, change, filename):
    # Determine direction
    is_up = '+' in change or (float(change.replace('%', '')) > 0 if '%' in change else False)
    
    # Chinese Style: Red for Up, Green for Down (as per skill instructions)
    bg_color = (255, 235, 235) if is_up else (235, 255, 235)
    text_color = (200, 0, 0) if is_up else (0, 150, 0)
    
    # Create image
    img = Image.new('RGB', (400, 200), color=bg_color)
    draw = ImageDraw.Draw(img)
    
    # Use system font (macOS)
    font_path = "/System/Library/Fonts/STHeiti Medium.ttc"
    try:
        font_title = ImageFont.truetype(font_path, 30)
        font_value = ImageFont.truetype(font_path, 50)
        font_change = ImageFont.truetype(font_path, 35)
    except:
        font_title = ImageFont.load_default()
        font_value = ImageFont.load_default()
        font_change = ImageFont.load_default()

    draw.text((20, 30), name, font=font_title, fill=(50, 50, 50))
    draw.text((20, 80), value, font=font_value, fill=(0, 0, 0))
    draw.text((20, 140), change, font=font_change, fill=text_color)
    
    img.save(f'images/charts/{filename}')

# Data from research (March 20, 2026 Close)
assets = [
    ("上证指数", "3957.05", "-1.24%", "2026-03-22-shanghai.png"),
    ("深证成指", "13866.20", "-0.25%", "2026-03-22-shenzhen.png"),
    ("创业板指", "3352.10", "+1.30%", "2026-03-22-chinext.png"),
    ("沪深300", "4567.02", "-0.35%", "2026-03-22-sp300.png"),
    ("恒生指数", "25277.32", "-0.88%", "2026-03-22-hangseng.png"),
    ("恒生科技", "4872.38", "-2.48%", "2026-03-22-hstech.png")
]

for name, val, change, file in assets:
    create_card(name, val, change, file)

print("Domestic market charts generated successfully.")
