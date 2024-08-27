import streamlit as st

st.title("🎈 My new app")
st.write(
    "Let's start building! For help and inspiration, head over to [docs.streamlit.io](https://docs.streamlit.io/)."
)

#=================================================

import streamlit as st
from streamlit_webrtc import webrtc_streamer

st.title("OpenCV Filters on Video Stream")

webrtc_streamer(key="streamer", sendback_audio=False)
