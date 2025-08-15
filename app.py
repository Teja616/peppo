import streamlit as st
from huggingface_hub import InferenceClient

# -------------------------------
# Page Config
# -------------------------------
st.set_page_config(
    page_title="AI Video Creator",
    page_icon="🎥",
    layout="centered"
)

# -------------------------------
# Title & Description
# -------------------------------
st.markdown("<h1 style='text-align: center;'>🎬 AI Video Creator</h1>", unsafe_allow_html=True)
st.markdown(
    """
    <p style="text-align: center; font-size:16px;">
    Turn your imagination into short, stunning AI-generated videos. 
    Just describe what you want to see — the AI will do the rest.
    </p>
    """,
    unsafe_allow_html=True
)
st.markdown("---")

# -------------------------------
# Hugging Face API Client
# -------------------------------
HF_TOKEN = st.secrets["HF_TOKEN"]
client = InferenceClient(
    provider="fal-ai",
    api_key=HF_TOKEN,
)

# -------------------------------
# Prompt Input
# -------------------------------
st.subheader("✨ Describe Your Scene")
st.markdown(
    "<small>Be as creative as you want — the more detailed, the better.</small>",
    unsafe_allow_html=True
)
prompt = st.text_area(
    "Your video description:",
    height=100,
    placeholder="Example: A breathtaking aerial view of a tropical island at sunset"
)

# -------------------------------
# Generate Button
# -------------------------------
if st.button("🎥 Generate My Video"):
    if not prompt.strip():
        st.warning("Please enter a description to generate your video.")
    else:
        with st.spinner("⏳ Creating your video... please wait."):
            try:
                video_bytes = client.text_to_video(
                    prompt,
                    model="tencent/HunyuanVideo",
                )
                st.success("✅ Your video is ready!")
                st.video(video_bytes)
            except Exception as e:
                st.error(f"Something went wrong: {e}")

# -------------------------------
# Footer
# -------------------------------
st.markdown("---")
st.markdown(
    "<p style='text-align:center; font-size:14px; color:gray;'>Powered by AI • Made for creators</p>",
    unsafe_allow_html=True
)
