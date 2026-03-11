import sys
import os
import requests
import random
import time
import urllib.parse

def generate_image(prompt, style, output_path):
    # Combine prompt and style
    full_prompt = f"{style} style, {prompt}"
    encoded_prompt = urllib.parse.quote(full_prompt)
    seed = random.randint(1, 1000000)
    
    # Define primary and backup endpoints with different logic
    # 1. Hercai (Stable backup)
    # 2. Pollinations (Currently down but normally good)
    
    endpoints = [
        # Hercai API (Alternative free provider)
        {
            "url": f"https://hercai.onrender.com/v3/text2image?prompt={encoded_prompt}",
            "type": "json_url" # Returns a JSON with a URL
        },
        # Pollinations (Original)
        {
            "url": f"https://image.pollinations.ai/prompt/{encoded_prompt}?width=1024&height=1024&seed={seed}&nologo=true&model=flux",
            "type": "direct" # Returns image bytes directly
        },
        {
            "url": f"https://pollinations.ai/p/{encoded_prompt}?width=1024&height=1024&seed={seed}",
            "type": "direct"
        }
    ]
    
    for ep in endpoints:
        url = ep["url"]
        print(f"Trying endpoint: {url}")
        
        for attempt in range(2):
            try:
                r = requests.get(url, timeout=60)
                if r.status_code == 200:
                    if ep["type"] == "direct":
                        if 'image' in r.headers.get('content-type', ''):
                            os.makedirs(os.path.dirname(output_path), exist_ok=True)
                            with open(output_path, 'wb') as f:
                                f.write(r.content)
                            print(f"Success! Image saved via direct download.")
                            return True
                    elif ep["type"] == "json_url":
                        data = r.json()
                        img_url = data.get("url")
                        if img_url:
                            img_r = requests.get(img_url, timeout=60)
                            if img_r.status_code == 200:
                                os.makedirs(os.path.dirname(output_path), exist_ok=True)
                                with open(output_path, 'wb') as f:
                                    f.write(img_r.content)
                                print(f"Success! Image saved via JSON URL.")
                                return True
                elif r.status_code == 429:
                    time.sleep(5)
                else:
                    print(f"HTTP Error {r.status_code}")
                    break
            except Exception as e:
                print(f"Error: {str(e)}")
                time.sleep(2)
    
    return False

if __name__ == "__main__":
    if len(sys.argv) < 4:
        print("Usage: python3 gen_manga.py <prompt> <style> <output_path>")
        sys.exit(1)
        
    prompt = sys.argv[1]
    style = sys.argv[2]
    output_path = sys.argv[3]
    
    success = generate_image(prompt, style, output_path)
    if not success:
        sys.exit(1)
