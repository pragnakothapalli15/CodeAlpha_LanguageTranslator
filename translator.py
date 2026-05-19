import streamlit as st
from deep_translator import GoogleTranslator
from gtts import gTTS
import tempfile

st.title("Language Translation Tool")

text = st.text_area("Enter Text")

source = st.selectbox(
    "Source Language",
    ["english","telugu","hindi","french"]
)
target = st.selectbox(
    "Target Language",
      ["telugu","english","hindi","french"]
)
if st.button("Translate"):
    translated = GoogleTranslator(
        source=source,
        target=target
    ).translate(text)

    st.success(translated)

    st.code(translated)

    tts = gTTS(translated)

    with tempfile.NamedTemporaryFile(delete=False,suffix=".mp3")as fp:
        tts.save(fp.name)

        audio_file = open(fp.name,"rb")
        audio_bytes = audio_file.read()

        st.audio(audio_bytes,format="audio/mp3")