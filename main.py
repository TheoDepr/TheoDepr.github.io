import streamlit as st

from streamlit.logger import get_logger

LOGGER = get_logger(__name__)

def artwork(i):
    st.divider()
    st.image("images/" + str(i) + ".jpg")
    st.write("Artwork " + str(i))
    st.audio("audio/" + str(i) + ".mp3")
    st.divider()
    return 

def run():
    st.set_page_config(
        page_title="Jubilee",
        page_icon="💎",
    )
 
    st.write("# Jubilee ")
    st.write("## Ron Mueck")

    st.write("### Zaal 1")
    artwork(1)
    st.write("### Zaal 2")
    st.write("### Zaal 3")
    st.write("### Zaal 4")
    st.write("### Zaal 5")
    st.write("### Zaal 6")
    st.write("### Zaal 7")
    st.write("### Zaal 8")

if __name__ == "__main__":
    run()