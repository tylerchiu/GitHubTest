import streamlit as st

st.markdown("# Welcome to my Website!")
st.sidebar.markdown("# Main Page")

st.write("Click on a page to see racer or kart stats")

link = '[To My GitHub Pages Site](https://tylerchiu.github.io/GitHubTest/)'
st.markdown(link, unsafe_allow_html=True)