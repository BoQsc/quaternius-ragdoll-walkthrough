import os
import re
import requests
from bs4 import BeautifulSoup
from urllib.parse import urlparse

# --- CONFIGURATION ---
THREAD_URL = "https://forum.godotengine.org/t/quaternius-humanoid-ragdoll-setup-walkthrough/133301"
OUTPUT_DIR = "media"
OUTPUT_FILENAME = "README_GITHUB.md"

def download_file(url, folder):
    if not os.path.exists(folder):
        os.makedirs(folder)
    
    path = urlparse(url).path
    filename = os.path.basename(path)
    
    # Clean Discourse resizing suffixes (e.g. _2_690x388.jpeg -> .jpeg)
    filename = re.sub(r'_\d+_\d+x\d+(\.[a-zA-Z0-9]+)$', r'\1', filename)
    
    local_path = os.path.join(folder, filename)
    
    if os.path.exists(local_path):
        print(f"Skipping (exists): {filename}")
        return local_path

    print(f"Downloading: {filename}...")
    try:
        headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'}
        response = requests.get(url, headers=headers, stream=True)
        response.raise_for_status()
        with open(local_path, 'wb') as f:
            for chunk in response.iter_content(chunk_size=8192):
                f.write(chunk)
        return local_path
    except Exception as e:
        print(f"Failed to download {url}: {e}")
        return None

def main():
    # 1. Fetch JSON
    json_url = THREAD_URL.rstrip('/') + ".json"
    print(f"Fetching thread data from: {json_url}")
    
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'}
    try:
        resp = requests.get(json_url, headers=headers)
        resp.raise_for_status()
        data = resp.json()
    except Exception as e:
        print(f"Error fetching data: {e}")
        return

    op_post = data['post_stream']['posts'][0]
    
    # 2. Fetch RAW Markdown
    if 'raw' in op_post:
        raw_text = op_post['raw']
    else:
        print("Fetching RAW markdown...")
        raw_endpoint = f"https://forum.godotengine.org/raw/{data['id']}/{op_post['post_number']}"
        raw_text = requests.get(raw_endpoint, headers=headers).text

    cooked_html = op_post['cooked']
    print("Parsing media links...")

    # 3. Create Map [upload://hash] -> [Real URL]
    soup = BeautifulSoup(cooked_html, 'html.parser')
    media_map = {} 
    
    def clean_url(url):
        if not url: return None
        if url.startswith("//"): return "https:" + url
        if url.startswith("/"): return "https://" + urlparse(THREAD_URL).netloc + url
        return url

    # SCAN 1: Standard Images
    for tag in soup.find_all(True):
        # Check for standard image hash
        short_hash = tag.get('data-base62-sha1')
        real_url = tag.get('src') or tag.get('href')

        # Fallback for images inside links
        if short_hash and not real_url:
            child = tag.find(src=True)
            if child: real_url = child['src']
            
        if short_hash and real_url:
            media_map[short_hash] = clean_url(real_url)

        # SCAN 2: Video Placeholders (The specific fix for your issue)
        # Videos use 'data-video-base62-sha1' and 'data-video-src'
        video_hash = tag.get('data-video-base62-sha1')
        video_src = tag.get('data-video-src')
        
        if video_hash and video_src:
            # IMPORTANT: Video hashes in HTML often have the extension (e.g. "hash.mp4")
            # But the markdown parser provides just the "hash".
            # We strip the extension from the key so they match.
            clean_hash_key = video_hash.rsplit('.', 1)[0]
            media_map[clean_hash_key] = clean_url(video_src)
            # Add exact match too just in case
            media_map[video_hash] = clean_url(video_src)

    # 4. Replace Links
    def replacement(match):
        full_str = match.group(0)
        alt_text = match.group(1) if match.lastindex >= 1 else ""
        file_hash = match.group(2) # This is usually just the alphanumeric hash
        
        real_url = media_map.get(file_hash)
        
        if not real_url:
            print(f"Warning: Could not resolve URL for hash {file_hash}")
            return full_str

        local_path = download_file(real_url, OUTPUT_DIR)
        
        if local_path:
            rel_path = f"{OUTPUT_DIR}/{os.path.basename(local_path)}"
            if alt_text:
                return f"![{alt_text}]({rel_path})"
            else:
                return f"![]({rel_path})"
        return full_str

    # Matches: ![alt](upload://HASH.ext)
    pattern = re.compile(r'!\[(.*?)\]\(upload://([a-zA-Z0-9]+)\.[a-zA-Z0-9]+\)')
    new_text = pattern.sub(replacement, raw_text)
    
    with open(OUTPUT_FILENAME, 'w', encoding='utf-8') as f:
        f.write(new_text)
        
    print(f"\nSuccess! Processed markdown saved to: {OUTPUT_FILENAME}")

if __name__ == "__main__":
    main()