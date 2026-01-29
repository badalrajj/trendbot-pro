def generate_video_script(topic, facts):
    # This creates a 'Hook-Body-CTA' structure common in viral videos
    script = f"""--- 🎥 60-SECOND VIDEO SCRIPT ---
[00-05s HOOK]: Did you hear about {topic}? It’s literally blowing up right now.
[05-45s THE TEA]: Here's the breakdown: {facts[:200]}... 
[45-60s OUTRO]: What do you think? Is this a game changer or just hype? Let me know in the comments!
---"""
    return script