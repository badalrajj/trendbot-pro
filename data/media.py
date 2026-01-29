def get_image_url(topic):
    print(f"🖼️ Finding visual for: {topic}...")
    # This creates a dynamic link to an image based on your topic
    safe_topic = topic.replace(" ", "").lower()
    return f"https://images.unsplash.com/photo-1507146426996-ef05306b995a?q=80&w=1000&auto=format&fit=crop"