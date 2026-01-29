import streamlit as st
from data.trends import fetch_trends
from data.research import research_topic
from ai.writer import create_content
from ai.director import generate_video_script
from utils.saver import save_all

# --- STREAMLIT UI SETUP ---
st.set_page_config(page_title="TrendBot Pro 2.0", page_icon="🚀")
st.title("🚀 TrendBot Pro 2.0")
st.sidebar.header("Controls")

if st.sidebar.button("Start Researching Trends"):
    st.info("Searching for the latest trends...")
    
    topics = fetch_trends()
    
    if not topics:
        st.warning("No trends found at the moment.")
    
    for topic in topics:
        with st.expander(f"Topic: {topic}", expanded=True):
            st.write("🔍 Researching...")
            info = research_topic(topic)
            
            from analysis.sentiment import analyze_vibe
            vibe = analyze_vibe(info)
            st.write(f"🎭 Vibe Check: **{vibe}**")
            
            # Generate Content
            st.write("✍️ Writing Blog, Social, and Scripts...")
            blog, social = create_content(topic, info, vibe)
            video_script = generate_video_script(topic, info)
            
            # DISPLAY TO WEB
            st.subheader("📝 Blog Post")
            st.write(blog)
            
            st.subheader("🎥 Video Script")
            st.code(video_script)
            
            st.subheader("📱 Social Media")
            st.info(social)
            
            # Save everything
            combined_content = f"{blog}\n\n{video_script}\n\n--- SOCIAL ---\n{social}"
            save_all(topic, combined_content, "Combined Output")
            st.success(f"Done! Saved {topic} to folder.")

else:
    st.write("Click the button in the sidebar to begin.")