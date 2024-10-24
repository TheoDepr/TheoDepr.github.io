import streamlit as st

from streamlit.logger import get_logger

LOGGER = get_logger(__name__)

def artwork(i):
    
    if i == 0:
        return
    
    st.divider()

    try:
      st.image("images/" + str(i) + ".jpg", use_column_width=True)
      st.write("Artwork " + str(i))
      st.audio("audio/" + str(i) + ".mp3")
    except:
        LOGGER.error("Error loading image or audio")

    st.divider()

    return 

def next():
    st.session_state["step"] += 1
    return

def previous():
    if st.session_state["step"] > 0:
      st.session_state["step"] -= 1
    return

def run():
    st.set_page_config(
        page_title="Jubilee",
        page_icon="💎",
    )

    if "step" not in st.session_state:
      st.session_state["step"] = 0
    
    st.write("## Paul & Mieke")

    artwork(st.session_state["step"])
    
    col1, col2, col3 = st.columns([1, 1, 1])
    with col1:
      st.button("Vorige", on_click=lambda: st.session_state.update(step=max(st.session_state["step"] - 1, 0)))
    with col3:
      st.button("Volgende", type='primary', on_click=lambda: st.session_state.update(step=st.session_state["step"] + 1))


    st.write(f"## {st.session_state['step']}")
  
    #st.write("### Zaal 1")
    #st.write("### Zaal 2")
    #st.write("### Zaal 3")
    #st.write("### Zaal 4")
    #st.write("### Zaal 5")
    #st.write("### Zaal 6")
    #st.write("### Zaal 7")
    #st.write("### Zaal 8")

if __name__ == "__main__":
    run()