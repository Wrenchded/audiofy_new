import streamlit as st
import subprocess

st.set_page_config(page_title="YouTube MP3 Downloader", layout="centered")

# Inject CSS for styling globally
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@400;600&display=swap');

    /* Page container style */
    .css-1d391kg {  /* Streamlit's default container class, may change, but works currently */
        background-color: #1e1e1e;
        padding: 2rem 3rem;
        border-radius: 12px;
        max-width: 480px;
        margin-top: 1rem;
        font-family: 'Poppins', sans-serif;
        color: #eee;
        box-shadow: 0 8px 24px rgba(0,0,0,0.8);
    }

    /* Logo centered and sized */
    .logo {
        display: block;
        margin-left: auto;
        margin-right: auto;
        max-width: 60px;
        margin-bottom: 0.1rem;
    }

    /* Title style */
    h1 {
        text-align: center;
        margin-top: -0.1rem;
        margin-bottom: 0.2rem;
        font-weight: 600;
        font-size: 2rem;
        color: #fff;
    }

    /* Subtitle */
    p.subtitle {
        text-align: center;
        color: #aaa;
        margin-top: 0;
        margin-bottom: 2rem;
        font-weight: 400;
        font-size: 1rem;
    }

    /* Input box */
    .stTextInput>div>div>input {
        background-color: #2a2a2a !important;
        color: #eee !important;
        border-radius: 8px !important;
        border: 1.8px solid #444 !important;
        padding: 12px !important;
        font-size: 1rem !important;
    }

    /* Button styling */
    .stButton>button {
        background: linear-gradient(45deg, #3a8ee6, #2c6ecc);
        color: white;
        font-weight: 600;
        font-size: 1.1rem;
        border-radius: 8px;
        padding: 0.75rem 0;
        box-shadow: 0 6px 14px rgba(58, 142, 230, 0.7);
        border: none;
        cursor: pointer;
        transition: background-color 0.3s ease;
        width: 100%;
    }

    .stButton>button:hover {
        background-color: #1f4f99 !important;
    }

    /* Messages */
    .message-success {
        background-color: #155724;
        color: #d4edda;
        padding: 0.75rem 1rem;
        border-radius: 6px;
        font-weight: 600;
        margin-top: 1.5rem;
        user-select: none;
    }
    .message-error {
        background-color: #721c24;
        color: #f8d7da;
        padding: 0.75rem 1rem;
        border-radius: 6px;
        font-weight: 600;
        margin-top: 1.5rem;
        user-select: none;
    }
    .message-info {
        background-color: #004085;
        color: #cce5ff;
        padding: 0.75rem 1rem;
        border-radius: 6px;
        font-weight: 600;
        margin-top: 1.5rem;
        user-select: none;
    }
    .message-warning {
        background-color: #856404;
        color: #fff3cd;
        padding: 0.75rem 1rem;
        border-radius: 6px;
        font-weight: 600;
        margin-top: 1.5rem;
        user-select: none;
    }
</style>
""", unsafe_allow_html=True)

# Logo centered using Streamlit native layout
st.image("static/audiofy_1.png", width=50, use_container_width=True)

# Title and subtitle using Streamlit native components with markdown styling
st.markdown("<h1 style='text-align: center; margin-top: -0.1rem; margin-bottom: 0.1rem; color: #fff; font-weight: 600;'>YouTube Audio Downloads</h1>", unsafe_allow_html=True)
st.markdown("<p class='subtitle'>Smooth MP3 conversions — anytime, anywhere.</p>", unsafe_allow_html=True)

url = st.text_input("Paste YouTube URL")

if st.button("Download MP3"):
    if url:
        st.markdown('<div class="message-info">⏳ Downloading... Please wait.</div>', unsafe_allow_html=True)

        command = f'yt-dlp -f bestaudio -x --audio-format mp3 "{url}"'
        result = subprocess.run(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

        if result.returncode == 0:
            st.markdown('<div class="message-success">✅ Audio downloaded and converted to MP3 successfully!</div>', unsafe_allow_html=True)
        else:
            err_msg = result.stderr.decode()
            st.markdown(f'<div class="message-error">❌ Download failed. Please check the URL.<br><pre>{err_msg}</pre></div>', unsafe_allow_html=True)
    else:
        st.markdown('<div class="message-warning">⚠️ Please enter a valid YouTube URL.</div>', unsafe_allow_html=True)