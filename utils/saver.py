import os
from datetime import datetime

def save_all(topic, blog, social):
    # 1. Ensure the output folder exists
    os.makedirs("output", exist_ok=True)
    
    # 2. Create a clean filename
    date_str = datetime.now().strftime("%Y-%m-%d")
    safe_name = topic.replace(" ", "_").lower()
    filename = f"output/{date_str}_{safe_name}.txt"
    
    # 3. Write both formats to the file
    with open(filename, "w", encoding="utf-8") as f:
        f.write(f"--- FULL BLOG POST ---\n\n{blog}\n\n")
        f.write(f"--- SOCIAL MEDIA CAPTION ---\n\n{social}")
    
    print(f"✅ Successfully saved: {filename}")
