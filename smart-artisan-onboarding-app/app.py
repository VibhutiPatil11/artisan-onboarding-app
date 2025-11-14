import sys, os
import streamlit as st

# -------- Fix Streamlit Import Path --------
CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.join(CURRENT_DIR, "models"))
sys.path.append(os.path.join(CURRENT_DIR, "utils"))
# -------------------------------------------

from models.image_model import classify_image
from utils.translate import translate_to_english
from utils.whisper_stt import speech_to_text
from utils.gpt_metadata import generate_listing

st.title("🛍️ Smart Artisan Onboarding App")

# Step 1: Voice Input
audio_file = st.audio_input("🎤 Speak your product details")

if audio_file:
    st.info("Processing speech...")
    text = speech_to_text(audio_file.getvalue())
    st.write("🗣️ Recognized Speech:", text)

    translated = translate_to_english(text)
    st.write("🌐 Translated to English:", translated)

# Step 2: Image Upload
image = st.file_uploader("📸 Upload product image")

if image:
    st
