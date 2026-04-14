
import matplotlib.pyplot as plt
from PIL import Image, ImageDraw, ImageFont
import os

# Ensure directory exists
os.makedirs('images/charts', exist_ok=True)

def create_card(name, value, change, filename):
    # Red for Up, Green for Down (Chinese Market Style)
    is_up = '+' in change or (float(change.strip('%')) > 0 if '%' in change else False)
    bg_color = (255, 232, 232) if is_up else (232, 255, 232)
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
        # Fallback for non-macOS or missing font
        font_title = ImageFont.load_default()
        font_value = ImageFont.load_default()
        font_change = ImageFont.load_default()

    draw.text((20, 30), name, font=font_title, fill=(50, 50, 50))
    draw.text((20, 80), value, font=font_value, fill=(0, 0, 0))
    draw.text((20, 140), change, font=font_change, fill=text_color)
    
    img.save(f'images/charts/{filename}')

# Data for 2026-04-14 Evening
assets = [
    ("上证指数", "4026.34", "+1.00%", "2026-04-14-sse.png"),
    ("深证成指", "14639.22", "+1.60%", "2026-04-14-szse.png"),
    ("创业板指", "3558.31", "+2.40%", "2026-04-14-chinext.png"),
    ("恒生指数", "19250.50", "+1.20%", "2026-04-14-hsi.png"),
    ("离岸人民币", "6.81", "+0.45%", "2026-04-14-cnh.png")
]

for name, val, change, file in assets:
    create_card(name, val, change, file)

# Also create a combined chart if needed, but separate cards are fine.
# We will use one of these or a manually combined one in the report.
# For now, let's just make sure they exist.
print("Evening charts generated.")
