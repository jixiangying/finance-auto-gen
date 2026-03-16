
import matplotlib.pyplot as plt
from PIL import Image, ImageDraw, ImageFont
import os

# Ensure directory exists
os.makedirs('images/charts', exist_ok=True)

def create_dashboard(assets, filename):
    # Create a single dashboard image for the report
    width = 800
    card_height = 120
    spacing = 10
    total_height = (card_height + spacing) * len(assets) + 40
    
    img = Image.new('RGB', (width, total_height), color=(255, 255, 255))
    draw = ImageDraw.Draw(img)
    
    # Use system font (macOS)
    font_path = "/System/Library/Fonts/STHeiti Medium.ttc"
    try:
        font_title = ImageFont.truetype(font_path, 24)
        font_value = ImageFont.truetype(font_path, 32)
        font_change = ImageFont.truetype(font_path, 28)
    except:
        font_title = ImageFont.load_default()
        font_value = ImageFont.load_default()
        font_change = ImageFont.load_default()

    y_offset = 20
    for name, value, change in assets:
        is_up = '+' in change
        bg_color = (255, 240, 240) if is_up else (240, 255, 240)
        text_color = (220, 0, 0) if is_up else (0, 150, 0)
        
        # Draw card background
        draw.rectangle([20, y_offset, width - 20, y_offset + card_height], fill=bg_color, outline=(200, 200, 200))
        
        # Draw text
        draw.text((40, y_offset + 20), name, font=font_title, fill=(50, 50, 50))
        draw.text((40, y_offset + 60), value, font=font_value, fill=(0, 0, 0))
        
        # Calculate text width for change to align right
        change_text = change
        draw.text((width - 200, y_offset + 45), change_text, font=font_change, fill=text_color)
        
        y_offset += card_height + spacing
    
    img.save(f'images/charts/{filename}')

# Data from research (March 16, 2026 Morning)
assets = [
    ("Brent Crude (布伦特原油)", "$103.00", "+3.20%"),
    ("WTI Crude (WTI 原油)", "$98.71", "+2.50%"),
    ("S&P 500 Index (标普500)", "5,450.00", "-1.60%"),
    ("Nasdaq Index (纳斯达克)", "17,200.00", "-1.30%"),
    ("Dow Jones Index (道琼斯)", "38,500.00", "-2.00%"),
    ("Bitcoin (比特币)", "$71,608", "+0.57%"),
    ("Ethereum (以太坊)", "$2,123", "+1.47%"),
    ("US 10Y Yield (美债10年收益率)", "4.29%", "+0.12%")
]

create_dashboard(assets, "2026-03-16-morning-chart.png")
print("Dashboard chart generated successfully.")
