import wikipediaapi

def research_topic(topic):
    print(f"📖 Researching facts for: {topic}...")
    # Wikipedia requires a User-Agent to know who is requesting data
    wiki = wikipediaapi.Wikipedia(
        language='en', 
        user_agent='TrendBotPro/1.0 (contact@example.com)'
    )
    
    try:
        page = wiki.page(topic)
        if page.exists():
            return page.summary[:1000]
        return f"Trending topic detected, but no detailed encyclopedia entry is available for {topic} yet."
    except Exception as e:
        return f"Research temporarily unavailable for {topic}."
