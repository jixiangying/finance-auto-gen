import sys
import os
import requests
import random
import time
import urllib.parse
from dotenv import load_dotenv

# Load environment variables from .env
load_dotenv()

def is_valid_image(content):
    if len(content) < 5000: return False
    if content.startswith(b'\xff\xd8\xff'): return True # JPEG
    if content.startswith(b'\x89PNG\r\n\x1a\n'): return True # PNG
    if content.startswith(b'RIFF') and content[8:12] == b'WEBP': return True # WEBP
    return False

def generate_with_siliconflow(prompt, output_path):
    api_key = os.getenv("SILICONFLOW_API_KEY")
    if not api_key:
        print("SILICONFLOW_API_KEY not found. Skipping SiliconFlow.")
        return False
    
    url = "https://api.siliconflow.cn/v1/images/generations"
    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json"
    }
    
    # Try two models on SiliconFlow
    models = ["Kwai-Kolors/Kolors", "black-forest-labs/FLUX.1-schnell"]
    
    for model in models:
        payload = {
            "model": model,
            "prompt": prompt,
            "n": 1,
            "size": "1024x1024"
        }
        
        print(f"Calling SiliconFlow ({model}) for prompt: {prompt}")
        try:
            # Increased timeout to 120s for generation
            r = requests.post(url, headers=headers, json=payload, timeout=120)
            if r.status_code == 200:
                data = r.json()
                img_url = data.get("data", [{}])[0].get("url")
                if img_url:
                    print(f"Downloading from SiliconFlow source: {img_url}")
                    img_r = requests.get(img_url, timeout=120)
                    if img_r.status_code == 200 and is_valid_image(img_r.content):
                        os.makedirs(os.path.dirname(output_path), exist_ok=True)
                        with open(output_path, 'wb') as f:
                            f.write(img_r.content)
                        print(f"Success! Image generated via SiliconFlow ({model}).")
                        return True
            else:
                print(f"SiliconFlow ({model}) error {r.status_code}: {r.text}")
        except Exception as e:
            print(f"SiliconFlow ({model}) connection error: {str(e)}")
        time.sleep(2)
    return False

def generate_image(prompt, style, output_path):
    # Dynamic prompt enrichment to avoid homogenization
    quality_boosters = "masterpiece, high detail, intricate composition, cinematic lighting, 8k resolution"
    full_prompt = f"{style} style, {prompt}, {quality_boosters}"
    
    # Tier 1: Pollinations
    pollinations_models = ["flux", "turbo"]
    for model in pollinations_models:
        encoded_prompt = urllib.parse.quote(full_prompt)
        seed = random.randint(1, 1000000)
        url = f"https://image.pollinations.ai/prompt/{encoded_prompt}?width=1024&height=1024&seed={seed}&nologo=true&model={model}"
        print(f"Trying Pollinations ({model})...")
        for attempt in range(2):
            try:
                r = requests.get(url, timeout=60)
                if r.status_code == 200 and is_valid_image(r.content):
                    os.makedirs(os.path.dirname(output_path), exist_ok=True)
                    with open(output_path, 'wb') as f:
                        f.write(r.content)
                    print(f"Success! Image generated via Pollinations ({model}).")
                    return True
                elif r.status_code == 429:
                    print(f"Rate limited. Waiting 10s...")
                    time.sleep(10)
            except: pass
            time.sleep(1)

    # Tier 2: SiliconFlow (Stable Key-based Backup)
    if generate_with_siliconflow(full_prompt, output_path):
        return True

    # Tier 3: Hercai
    encoded_prompt = urllib.parse.quote(full_prompt)
    hercai_url = f"https://hercai.onrender.com/v3/text2image?prompt={encoded_prompt}"
    print(f"Trying Hercai fallback...")
    try:
        r = requests.get(hercai_url, timeout=60)
        if r.status_code == 200:
            data = r.json()
            img_url = data.get("url")
            if img_url:
                img_r = requests.get(img_url, timeout=60)
                if img_r.status_code == 200 and is_valid_image(img_r.content):
                    os.makedirs(os.path.dirname(output_path), exist_ok=True)
                    with open(output_path, 'wb') as f:
                        f.write(img_r.content)
                    print("Success! Image generated via Hercai.")
                    return True
    except: pass

    # Last resort: Try a very short prompt if long one caused timeouts
    if len(prompt) > 20:
        print("Everything failed. Retrying with a very short prompt...")
        short_prompt = prompt.split(',')[0][:50]
        return generate_image(short_prompt, style, output_path)

    return False

if __name__ == "__main__":
    if len(sys.argv) < 4:
        sys.exit(1)
    if generate_image(sys.argv[1], sys.argv[2], sys.argv[3]):
        sys.exit(0)
    else:
        sys.exit(1)
