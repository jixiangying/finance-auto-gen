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
    
    # Define reliable endpoints
    endpoints = [
        # 1. Airforce API (Very fast and stable currently)
        {
            "url": f"https://api.airforce/v1/desktop/generation?prompt={encoded_prompt}&model=flux&width=1024&height=1024&seed={seed}",
            "type": "direct"
        },
        # 2. Pollinations Flux Model
        {
            "url": f"https://image.pollinations.ai/prompt/{encoded_prompt}?width=1024&height=1024&seed={seed}&nologo=true&model=flux",
            "type": "direct"
        },
        # 3. Pollinations Turbo
        {
            "url": f"https://image.pollinations.ai/prompt/{encoded_prompt}?width=1024&height=1024&seed={seed}&nologo=true&model=turbo",
            "type": "direct"
        }
    ]
    
    for ep in endpoints:
        url = ep["url"]
        print(f"Trying endpoint: {url}")
        
        for attempt in range(2):
            try:
                # Use a generous timeout for image generation
                r = requests.get(url, timeout=45)
                if r.status_code == 200:
                    # Check if we got an image or at least a decent amount of data
                    content_type = r.headers.get('content-type', '')
                    if 'image' in content_type or len(r.content) > 10000:
                        os.makedirs(os.path.dirname(output_path), exist_ok=True)
                        with open(output_path, 'wb') as f:
                            f.write(r.content)
                        print(f"Success! Image saved from {url}")
                        return True
                print(f"Attempt {attempt+1} failed with status {r.status_code}")
                time.sleep(2)
            except Exception as e:
                print(f"Error on attempt {attempt+1}: {str(e)}")
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
