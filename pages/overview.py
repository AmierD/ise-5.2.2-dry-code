import streamlit as st
from utils import common_page_config, render_sidebar, render_footer

common_page_config(page_title="Overview")

st.markdown("# Overview")
st.markdown(
    """
    Here is a page with a site overview.
    This site has one main page (app) and three pages (about, overview, and report).
    All of them have some redundant code that can be abstracted out to make changes easier in the future.
    """
)

st.sidebar.header("Overview")
render_sidebar()
render_footer()
