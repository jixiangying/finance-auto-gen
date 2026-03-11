import sys
import os
import requests
import random
import time
import urllib.parse

def is_valid_image(content):
    if len(content) < 1000: return False
    if content.startswith(b'\xff\xd8\xff'): return True # JPEG
    if content.startswith(b'\x89PNG\r\n\x1a\n'): return True # PNG
    if content.startswith(b'GIF87a') or content.startswith(b'GIF89a'): return True # GIF
    if content.startswith(b'RIFF') and content[8:12] == b'WEBP': return True # WEBP
    return False

def generate_image(prompt, style, output_path):
    full_prompt = f"{style} style, {prompt}"
    encoded_prompt = urllib.parse.quote(full_prompt)
    
    # Priority List: Pollinations Models first
    pollinations_models = ["flux", "turbo", "standard"]
    
    print(f"Targeting Pollinations for prompt: {full_prompt}")
    
    for model in pollinations_models:
        seed = random.randint(1, 1000000)
        url = f"https://image.pollinations.ai/prompt/{encoded_prompt}?width=1024&height=1024&seed={seed}&nologo=true"
        if model != "standard":
            url += f"&model={model}"
            
        print(f"Trying Pollinations ({model}): {url}")
        
        for attempt in range(2): # 2 attempts per model
            try:
                r = requests.get(url, timeout=45)
                if r.status_code == 200:
                    if is_valid_image(r.content):
                        os.makedirs(os.path.dirname(output_path), exist_ok=True)
                        with open(output_path, 'wb') as f:
                            f.write(r.content)
                        print(f"Success! High-quality image generated via Pollinations ({model}).")
                        return True
                elif r.status_code == 429:
                    print(f"Rate limited. Waiting 10s before retry...")
                    time.sleep(10)
                else:
                    print(f"HTTP {r.status_code} from Pollinations.")
            except Exception as e:
                print(f"Network error: {str(e)}")
            time.sleep(1)

    # Ultimate fallback ONLY if Pollinations fails completely
    print("Pollinations failed after multiple attempts. Using fallback.")
    fallback_seed = random.randint(1, 1000000)
    fallback_url = f"https://picsum.photos/seed/{fallback_seed}/1024/1024"
    try:
        r = requests.get(fallback_url, timeout=20)
        if r.status_code == 200 and is_valid_image(r.content):
            os.makedirs(os.path.dirname(output_path), exist_ok=True)
            with open(output_path, 'wb') as f:
                f.write(r.content)
            print("Saved fallback placeholder image.")
            return True
    except:
        pass

    return False

if __name__ == "__main__":
    if len(sys.argv) < 4:
        sys.exit(1)
    if generate_image(sys.argv[1], sys.argv[2], sys.argv[3]):
        sys.exit(0)
    else:
        sys.exit(1)
