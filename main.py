from data.trends import fetch_trends
from data.research import research_topic
from ai.writer import create_content
from ai.director import generate_video_script # New Import
from utils.saver import save_all

def main():
    print("🚀 Starting TrendBot Pro 2.0...")
    topics = fetch_trends()
    
    for topic in topics:
        info = research_topic(topic)
        from analysis.sentiment import analyze_vibe
        vibe = analyze_vibe(info)
        
        # Generate Blog & Social
        blog, social = create_content(topic, info, vibe)
        
        # Generate Video Script (New Feature!)
        video_script = generate_video_script(topic, info)
        
        # Save everything combined
        combined_content = f"{blog}\n\n{video_script}\n\n--- SOCIAL ---\n{social}"
        save_all(topic, combined_content, "Combined Output")

if __name__ == "__main__":
    main()