import requests
import xml.etree.ElementTree as ET

def fetch_trends(country='US', limit=3):
    print(f"🌐 Fetching live data via Google News RSS ({country})...")
    # Google News RSS is currently more stable than the Trends RSS in 2026
    url = f"https://news.google.com/rss?hl=en-{country}&gl={country}&ceid={country}:en"
    
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
    }
    
    try:
        response = requests.get(url, headers=headers, timeout=10)
        if response.status_code != 200:
            raise Exception(f"Google News blocked access: {response.status_code}")
            
        root = ET.fromstring(response.content)
        # Extract titles from the News Feed
        topics = []
        for item in root.findall('./channel/item'):
            # We strip out the source name (e.g., "Topic - CNN") to get just the topic
            full_title = item.find('title').text
            topic = full_title.split(' - ')[0] 
            topics.append(topic)
            
        return list(set(topics))[:limit] # Set removes duplicates
        
    except Exception as e:
        print(f"⚠️ RSS Method failed: {e}. Using fallback topics...")
        return ["Generative AI", "Quantum Computing", "Space Exploration"]