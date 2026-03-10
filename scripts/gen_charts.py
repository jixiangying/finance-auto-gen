
import matplotlib.pyplot as plt
from PIL import Image, ImageDraw, ImageFont
import os

# Ensure directory exists
os.makedirs('images/charts', exist_ok=True)

def create_card(name, value, change, filename):
    # Colors: Red for Up, Green for Down (as per skill instructions)
    is_up = '+' in change or float(change.strip('%')) > 0 if '%' in change else False
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

# Data from research
assets = [
    ("S&P 500", "6,795.99", "+0.83%", "sp500_card.png"),
    ("Nasdaq", "22,695.95", "+1.38%", "nasdaq_card.png"),
    ("Dow Jones", "47,740.80", "+0.50%", "dow_card.png"),
    ("Bitcoin", "$69,250", "+1.2%", "btc_card.png"),
    ("Gold", "$5,133", "-0.15%", "gold_card.png"),
    ("WTI Oil", "$86.24", "-8.5%", "oil_card.png"), # From peak
    ("US 10Y Yield", "4.15%", "+2.1%", "treasury_card.png")
]

for name, val, change, file in assets:
    create_card(name, val, change, file)

print("Charts generated successfully.")
