import streamlit as st # to streamlit web
from gtts import gTTS # for text to speech using google
import tempfile # to store audio data for temporary
import time # for animation purpose


st.set_page_config(page_title="စာမှ အသံပြောင်းသူ", page_icon=":speech_balloon:") # page title
#Resource Link : https://streamlit-emoji-shortcodes-streamlit-app-gwckff.streamlit.app/



# style customization (header bar , footer bar and audio)
st.markdown("""
<style>
.css-18ni7ap , .css-h5rgaw{ visibility: hidden;}
audio {width:100%;border-radius:5em;background-color:white;}
</style>
""",unsafe_allow_html=True)

# Define your button emoji shortcode
title_emoji_shortcode = ":speech_balloon:"
speaker_emoji_shortcode = ":speaker:"
#Resource Link : https://streamlit-emoji-shortcodes-streamlit-app-gwckff.streamlit.app/

with st.container(): 


    time.sleep(0.3) #For animations
    st.title(f"{title_emoji_shortcode} စာမှ အသံ ပြောင်းသူ") # program title

    time.sleep(0.3)
    text_input = st.text_area("ပြောင်းလိုသောစာသားတိကိုရွီးထည့်ပါ:", "Hello, world!")  # to insert text for speech
    time.sleep(0.3)

    

    if st.button(f"စာမှ အသံသိုပြောင်းပါ{speaker_emoji_shortcode}"): # button to generate text to speech
        try:
        # Create a temporary file to store the speech audio
            with tempfile.NamedTemporaryFile(delete=False, suffix=".mp3") as temp_audio_file:
            # Generate the speech audio from the input text
                tts = gTTS(text_input, lang="en")
                tts.save(temp_audio_file.name)

            # Display the audio player for playback
                with st.spinner("စာမှ အသံသို့ပြောင်းနိန်ပါရေ..."):
                    time.sleep(1)
                audio_file = open(temp_audio_file.name, "rb")
                st.audio(audio_file.read(), format="audio/mp3", start_time=0)
            
            
        except Exception as e:
            st.error("မရပါ၊ ပြန်လို့လုပ်ကြည့်ပါနန်း") # to show error if there is no text on text area
            st.error(str(e))
        
with st.sidebar: # This is side bar
    
    st.write("Written By")

  
    st.success("Kyaw Tun Linn")   
