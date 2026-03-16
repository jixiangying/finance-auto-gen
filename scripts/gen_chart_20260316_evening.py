
import os
from PIL import Image, ImageDraw, ImageFont

# Ensure directory exists
os.makedirs('images/charts', exist_ok=True)

def create_dashboard(assets, filename):
    # Create a single dashboard image for the report
    width = 800
    card_height = 80
    spacing = 8
    total_height = (card_height + spacing) * len(assets) + 40
    
    img = Image.new('RGB', (width, total_height), color=(255, 255, 255))
    draw = ImageDraw.Draw(img)
    
    # Use system font (macOS)
    font_path = "/System/Library/Fonts/STHeiti Medium.ttc"
    try:
        font_title = ImageFont.truetype(font_path, 20)
        font_value = ImageFont.truetype(font_path, 24)
        font_change = ImageFont.truetype(font_path, 22)
    except:
        font_title = ImageFont.load_default()
        font_value = ImageFont.load_default()
        font_change = ImageFont.load_default()

    y_offset = 20
    for name, value, change in assets:
        is_up = '+' in change
        is_down = '-' in change
        
        if is_up:
            bg_color = (255, 240, 240)
            text_color = (220, 0, 0)
        elif is_down:
            bg_color = (240, 255, 240)
            text_color = (0, 150, 0)
        else:
            bg_color = (245, 245, 245)
            text_color = (100, 100, 100)
            
        # Draw card background
        draw.rectangle([20, y_offset, width - 20, y_offset + card_height], fill=bg_color, outline=(220, 220, 220))
        
        # Draw text
        draw.text((40, y_offset + 15), name, font=font_title, fill=(50, 50, 50))
        draw.text((40, y_offset + 45), value, font=font_value, fill=(0, 0, 0))
        
        # Calculate text width for change to align right
        change_text = change
        draw.text((width - 200, y_offset + 30), change_text, font=font_change, fill=text_color)
        
        y_offset += card_height + spacing
    
    img.save(f'images/charts/{filename}')

# Data from research (March 16, 2026 Evening)
assets = [
    ("上证指数 (SSE)", "4084.79", "-0.26%"),
    ("深证成指 (SZSE)", "14307.58", "+0.19%"),
    ("创业板指 (ChiNext)", "3357.02", "+1.41%"),
    ("恒生指数 (HSI)", "25755", "+1.14%"),
    ("恒生科技指数 (HSTECH)", "5,230", "+2.24%"),
    ("A股成交额 (A-share Vol)", "2.34万亿元", "活跃"),
    ("北向资金 (Northbound)", "净流入26.3亿", "+26.3B"),
    ("比特币 (BTC)", "$73,760", "+2.90%"),
    ("以太坊 (ETH)", "$2,265", "+7.70%"),
    ("现货黄金 (Gold)", "$5,028.90", "-0.14%"),
    ("布伦特原油 (Brent)", "$104.50", "+1.50%")
]

create_dashboard(assets, "2026-03-16-evening-chart.png")
print("Dashboard chart generated successfully.")
