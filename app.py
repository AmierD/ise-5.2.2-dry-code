import streamlit as st
from utils import common_page_config, render_sidebar, render_footer

common_page_config(page_title="Hello", page_icon="👋")
st.markdown("# Welcome to Streamlit!")

render_sidebar()

st.markdown(
    """
    This website has a lot of redundant code. Can you find it and create a utility file which contains the redundancies?
    """
)

render_footer()
