import streamlit as st

from streamlit.logger import get_logger

LOGGER = get_logger(__name__)


if "step" not in st.session_state:
      st.session_state["step"] = 0

if "zaal_dict" not in st.session_state:
      st.session_state["zaal_dict"] = {
      1: "Zaal 1",
      2: "Zaal 1",
      3: "Zaal 2",
      4: "Zaal 2",
      5: "Zaal 3",
      6: "Zaal 4",
      7: "Zaal 4",
      8: "Zaal 4",
      9: "Zaal 5",
      10: "Zaal 6",
      11: "Zaal 7",
      12: "Zaal 8",
      13: "Turnzaal",
      14: "Highlights ",
      15: "Landgoed ",
      }


def artwork(i):
    
    if i == 0:
        return
    
    st.divider()

    try:
      st.write(f"#### {st.session_state['zaal_dict'][i]}")
      st.image("images/" + str(i) + ".jpg", use_column_width=True)
      st.write("Artwork " + str(i))
      st.audio("audio/" + str(i) + ".mp3")
    except:
        LOGGER.error("Error loading image or audio")

    st.divider()

    return 


def run():
    st.set_page_config(
        page_title="Jubilee",
        page_icon="💎",
    )

    hide_streamlit_style = """
    <style>
        #root > div:nth-child(1) > div > div > div > div > section > div {padding-top: 1.5rem;}
    </style>

    """
    st.markdown(hide_streamlit_style, unsafe_allow_html=True)

    st.write("## Paul & Mieke")

    artwork(st.session_state["step"])
    
    st.button("Volgende kunstwerk", type='primary', on_click=lambda: st.session_state.update(step=min(st.session_state["step"] + 1, 16)))
    st.button("Vorige", on_click=lambda: st.session_state.update(step=max(st.session_state["step"] - 1, 0)))

if __name__ == "__main__":
    run()