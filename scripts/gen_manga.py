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
    
    # Official SiliconFlow Images Generation Endpoint
    url = "https://api.siliconflow.cn/v1/images/generations"
    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json"
    }
    payload = {
        "model": "Kwai-Kolors/Kolors", # Free model on SiliconFlow
        "prompt": prompt,
        "n": 1,
        "size": "1024x1024"
    }
    
    print(f"Calling SiliconFlow (Kwai-Kolors/Kolors) for prompt: {prompt}")
    try:
        r = requests.post(url, headers=headers, json=payload, timeout=60)
        if r.status_code == 200:
            data = r.json()
            # Extract image URL from SiliconFlow response (standard OpenAI format)
            img_url = data.get("data", [{}])[0].get("url")
            if img_url:
                print(f"Downloading from SiliconFlow source: {img_url}")
                img_r = requests.get(img_url, timeout=60)
                if img_r.status_code == 200 and is_valid_image(img_r.content):
                    os.makedirs(os.path.dirname(output_path), exist_ok=True)
                    with open(output_path, 'wb') as f:
                        f.write(img_r.content)
                    print("Success! Image generated via SiliconFlow.")
                    return True
        else:
            print(f"SiliconFlow error {r.status_code}: {r.text}")
    except Exception as e:
        print(f"SiliconFlow connection error: {str(e)}")
    return False

def generate_image(prompt, style, output_path):
    full_prompt = f"{style} style, {prompt}"
    encoded_prompt = urllib.parse.quote(full_prompt)
    
    # Tier 1: Pollinations (Best Quality / Free-no-key)
    pollinations_models = ["flux", "turbo"]
    for model in pollinations_models:
        seed = random.randint(1, 1000000)
        url = f"https://image.pollinations.ai/prompt/{encoded_prompt}?width=1024&height=1024&seed={seed}&nologo=true&model={model}"
        print(f"Trying Pollinations ({model})...")
        for attempt in range(2):
            try:
                r = requests.get(url, timeout=45)
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

    # Tier 3: Hercai (Public Aggregate)
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

    return False

if __name__ == "__main__":
    if len(sys.argv) < 4:
        sys.exit(1)
    if generate_image(sys.argv[1], sys.argv[2], sys.argv[3]):
        sys.exit(0)
    else:
        sys.exit(1)
