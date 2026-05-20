from PIL import Image, ImageDraw, ImageFont
import os

# Ensure directory exists
os.makedirs('images/charts', exist_ok=True)

def create_card(name, value, change, filename):
    # Determine direction
    try:
        if '+' in change:
            is_up = True
        elif '-' in change:
            is_up = False
        else:
            is_up = float(change.replace('%', '')) > 0
    except:
        is_up = True 
    
    # Chinese Style: Red for Up, Green for Down
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

# Data from research (May 20, 2026 Close)
assets = [
    ("上证指数", "4162.18", "-0.18%", "2026-05-20-shanghai.png"),
    ("深证成指", "15569.98", "+0.00%", "2026-05-20-shenzhen.png"),
    ("创业板指", "3921.79", "+0.34%", "2026-05-20-chinext.png"),
    ("科创50", "1832.02", "+3.20%", "2026-05-20-star50.png"),
    ("恒生指数", "25651.12", "-0.57%", "2026-05-20-hangseng.png"),
    ("恒生科技", "4873.82", "+0.34%", "2026-05-20-hstech.png")
]

for name, val, change, file in assets:
    create_card(name, val, change, file)

print("Domestic market charts for 2026-05-20 generated successfully.")
