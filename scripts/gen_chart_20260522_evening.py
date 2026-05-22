
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

# Data for 2026-05-22 Evening
assets = [
    ("上证指数", "4,112.90", "+0.87%"),
    ("深证成指", "15,597.30", "+2.30%"),
    ("创业板指", "3,938.50", "+2.84%"),
    ("恒生指数", "25,606.03", "+0.86%"),
    ("恒生科技指数", "4,872.67", "+2.11%"),
    ("联想集团 (HK)", "11.58", "+19.00%")
]

create_combined_chart(assets, "2026-05-22-evening.png")
