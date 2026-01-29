import streamlit as st
from data.trends import fetch_trends
from data.research import research_topic
from ai.writer import create_content
from ai.director import generate_video_script
from utils.saver import save_all

# --- UI SETUP ---
st.set_page_config(page_title="TrendBot Pro: Automation", layout="wide")
st.title("🤖 TrendBot Content Engine")

# --- SIDEBAR CONTROLS ---
st.sidebar.header("Step 1: Choose Your Source")
mode = st.sidebar.radio("Input Method", ["Google Trends (Auto)", "Manual Topic"])

topic_to_research = None

if mode == "Google Trends (Auto)":
    if st.sidebar.button("Fetch Latest Trends"):
        topics = fetch_trends()
        if topics:
            topic_to_research = st.sidebar.selectbox("Select a Trending Topic", topics)
        else:
            st.error("Could not fetch trends. Try manual mode.")

else:
    topic_to_research = st.sidebar.text_input("Enter your topic manually", placeholder="e.g. Future of AI in 2026")

# --- MAIN EXECUTION ---
if topic_to_research:
    st.header(f"🎯 Current Focus: {topic_to_research}")
    
    if st.button("Generate Complete Research & Blog"):
        with st.status("Processing...", expanded=True) as status:
            
            # 1. Researching Phase
            st.write("🔍 Gathering reference materials and latest news...")
            research_data = research_topic(topic_to_research)
            
            # 2. Vibe Analysis
            from analysis.sentiment import analyze_vibe
            vibe = analyze_vibe(research_data)
            
            # 3. Content Creation
            st.write("✍️ Drafting your unique blog post...")
            blog, social = create_content(topic_to_research, research_data, vibe)
            video_script = generate_video_script(topic_to_research, research_data)
            
            status.update(label="Content Generated!", state="complete", expanded=False)

        # --- DISPLAY RESULTS ---
        col1, col2 = st.columns(2)

        with col1:
            st.subheader("📚 Reference Research")
            st.info("Based on the latest web data:")
            st.write(research_data[:1000] + "...") # Show snippet of research

        with col2:
            st.subheader("📝 New Generated Blog")
            st.success("Here is your original content:")
            st.markdown(blog)

        # --- ADDITIONAL OUTPUTS ---
        with st.expander("📱 View Social Media Posts & Video Script"):
            st.write("**Social Media Snippets:**")
            st.write(social)
            st.divider()
            st.write("**Video Script:**")
            st.code(video_script)

        # --- SAVE ---
        save_all(topic_to_research, blog, "Web_Deployment")
        st.toast(f"Saved to local storage!", icon="💾")

else:
    st.info("👈 Use the sidebar to select a trending topic or type your own to start.")