
import matplotlib.pyplot as plt
from PIL import Image, ImageDraw, ImageFont
import os

# Ensure directory exists
os.makedirs('images/charts', exist_ok=True)

def create_combined_chart(assets, output_filename):
    # Image dimensions
    card_width = 300
    card_height = 180
    padding = 20
    cols = 3
    rows = (len(assets) + cols - 1) // cols
    
    img_width = cols * card_width + (cols + 1) * padding
    img_height = rows * card_height + (rows + 1) * padding
    
    # White background for the whole sheet
    img = Image.new('RGB', (img_width, img_height), color=(245, 245, 245))
    draw = ImageDraw.Draw(img)
    
    # Use system font (macOS)
    font_path = "/System/Library/Fonts/STHeiti Medium.ttc"
    try:
        font_title = ImageFont.truetype(font_path, 24)
        font_value = ImageFont.truetype(font_path, 36)
        font_change = ImageFont.truetype(font_path, 28)
    except:
        font_title = ImageFont.load_default()
        font_value = ImageFont.load_default()
        font_change = ImageFont.load_default()

    for i, (name, value, change) in enumerate(assets):
        row = i // cols
        col = i % cols
        
        x = padding + col * (card_width + padding)
        y = padding + row * (card_height + padding)
        
        # Determine trend
        is_up = '+' in change or (float(change.strip('%')) > 0 if '%' in change and change.strip('%') else False)
        
        # Card background
        if is_up:
            bg_color = (255, 235, 235)  # Light Red
            text_color = (220, 20, 60)   # Crimson/Red
        else:
            bg_color = (235, 255, 235)  # Light Green
            text_color = (34, 139, 34)   # Forest Green/Green
            
        # Draw card rounded rect (simulated with rectangle)
        draw.rectangle([x, y, x + card_width, y + card_height], fill=bg_color, outline=(200, 200, 200))
        
        # Draw text
        draw.text((x + 20, y + 20), name, font=font_title, fill=(50, 50, 50))
        draw.text((x + 20, y + 60), value, font=font_value, fill=(0, 0, 0))
        draw.text((x + 20, y + 115), change, font=font_change, fill=text_color)
        
        # Indicator
        indicator = "▲" if is_up else "▼"
        draw.text((x + card_width - 40, y + 20), indicator, font=font_title, fill=text_color)
    
    save_path = f'images/charts/{output_filename}'
    img.save(save_path)
    print(f"Generated: {save_path}")

# Data for 2026-05-22 Morning
assets = [
    ("道琼斯工业指数", "50,285.66", "+0.55%"),
    ("标普 500 指数", "7,445.72", "+0.17%"),
    ("纳斯达克指数", "26,293.10", "+0.09%"),
    ("布伦特原油", "102.58", "-2.30%"),
    ("现货黄金", "4,545.00", "+0.20%"),
    ("比特币 (BTC)", "78,000", "+1.01%")
]

create_combined_chart(assets, "2026-05-22-morning.png")
