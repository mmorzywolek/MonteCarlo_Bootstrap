import streamlit as st
import functions
from simulations import monte_carlo, show_random_walk, show_author

st.set_page_config(page_title="Symulator - Monte Carlo", layout="wide",initial_sidebar_state="expanded")

def main():

    selection = st.sidebar.selectbox('Idź do ...', functions.OPTIONS)

    if selection == 'Marketing Simulator':
        monte_carlo()

    elif selection == 'Random Walk Simulator':
        show_random_walk()

    else:
        st.markdown("Coś poszło nie tak :(")

    st.markdown("Autor: Maciej Morzywołek ")



hide_streamlit_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            </style>
            """
st.markdown(hide_streamlit_style, unsafe_allow_html=True)
if __name__ == '__main__':
    main()

