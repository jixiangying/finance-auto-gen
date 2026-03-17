
import matplotlib.pyplot as plt
from PIL import Image, ImageDraw, ImageFont
import os

# Ensure directory exists
os.makedirs('images/charts', exist_ok=True)

def create_card(name, value, change, filename):
    # Colors: Red for Up, Green for Down (Chinese market standard)
    is_up = '+' in change or (float(change.strip('%')) > 0 if '%' in change and change.strip('%') else False)
    
    # Background and text colors based on trend
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
        font_title = ImageFont.load_default()
        font_value = ImageFont.load_default()
        font_change = ImageFont.load_default()

    draw.text((25, 30), name, font=font_title, fill=(50, 50, 50))
    draw.text((25, 85), value, font=font_value, fill=(0, 0, 0))
    draw.text((25, 150), change, font=font_change, fill=text_color)
    
    # Add a small icon or indicator
    indicator = "▲" if is_up else "▼"
    draw.text((340, 30), indicator, font=font_title, fill=text_color)
    
    save_path = f'images/charts/{filename}'
    img.save(save_path)
    print(f"Generated: {save_path}")

# Data from research (March 17, 2026 Morning)
assets = [
    ("S&P 500 Index", "6,699.38", "+1.00%", "2026-03-17-sp500.png"),
    ("Nasdaq Composite", "22,374.18", "+1.20%", "2026-03-17-nasdaq.png"),
    ("Dow Jones Index", "46,946.41", "+0.80%", "2026-03-17-dow.png"),
    ("Bitcoin (BTC)", "$74,000", "+1.50%", "2026-03-17-btc.png"),
    ("Gold (Spot)", "$5,018", "+0.10%", "2026-03-17-gold.png"),
    ("WTI Crude Oil", "$96.68", "+3.40%", "2026-03-17-oil.png"), # Compared to Monday settle
    ("US 10Y Treasury", "4.22%", "-1.40%", "2026-03-17-treasury.png")
]

for name, val, change, file in assets:
    create_card(name, val, change, file)

print("All morning charts generated successfully.")
