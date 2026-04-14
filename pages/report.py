import streamlit as st
from utils import common_page_config, render_sidebar, render_footer, get_report_data

common_page_config(page_title="Report")

st.markdown("# Report")
st.markdown("Here is a page with a report on it.")

st.bar_chart(get_report_data())

st.markdown("Look at those numbers. Amazing.")

st.sidebar.header("Report")
render_sidebar()
render_footer()
