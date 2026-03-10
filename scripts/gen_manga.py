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
    
    # Try multiple endpoints for reliability
    endpoints = [
        f"https://image.pollinations.ai/prompt/{encoded_prompt}?width=1024&height=1024&seed={random.randint(1,1000)}&nologo=true",
        f"https://pollinations.ai/p/{encoded_prompt}?width=1024&height=1024&seed={random.randint(1,1000)}",
    ]
    
    for url in endpoints:
        print(f"Generating image for: {full_prompt}")
        print(f"Requesting URL: {url}")
        
        for attempt in range(3): # Try 3 times per endpoint
            try:
                with requests.get(url, stream=True, timeout=120) as r:
                    if r.status_code == 200:
                        content_type = r.headers.get('content-type', '')
                        if 'image' in content_type:
                            os.makedirs(os.path.dirname(output_path), exist_ok=True)
                            with open(output_path, 'wb') as f:
                                for chunk in r.iter_content(chunk_size=8192):
                                    f.write(chunk)
                            print(f"Success! Image saved to: {output_path}")
                            return True
                    elif r.status_code == 429:
                        print(f"Rate limited (429). Waiting {10 * (attempt + 1)}s...")
                        time.sleep(10 * (attempt + 1))
                    else:
                        print(f"HTTP Error: {r.status_code}")
                        break # Try next endpoint
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
