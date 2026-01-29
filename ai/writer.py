def create_content(topic, facts, vibe):
    blog = f"""# Trend Alert: {topic}
    
**Current Vibe:** {vibe}

## The Latest Development
{facts}

## Why This Matters
As {topic} continues to trend, it's clear that the landscape is shifting. 
Whether you're an enthusiast or a professional, staying ahead of this 
curve is vital.
"""
    social = f"🚨 TRENDING: {topic}\n\nOur analysis shows a {vibe} sentiment. What's your take? #Trends2026 #Innovation"
    return blog, social