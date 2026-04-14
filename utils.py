import streamlit as st

def init_session_state():
    """Initialize session state variables."""
    if st.session_state.get("logged_in") is None:
        st.session_state["logged_in"] = False

def login():
    st.session_state.logged_in = True

def logout():
    st.session_state.logged_in = False

def render_sidebar():
    """Centralized sidebar for login/logout logic."""
    if st.session_state.logged_in:
        st.sidebar.success("Logged in")
        st.sidebar.button("Log out", key="logout", on_click=logout)
    else:
        st.sidebar.warning("Not logged in")
        st.sidebar.button("Log in", key="login", on_click=login)
    
    st.sidebar.write("This site is copyright Fake Company LLC Inc., 2024")

def render_footer():
    """Centralized footer for company info and links."""
    with st.expander("Company Info"):
        st.markdown("Fake Company LLC Inc. is located at 1600 Amphitheatre Parkway Mountain View, CA 94043")

    with st.expander("Links"):
        st.markdown("[Google](https://google.com)\n\n[Gemini](https://gemini.google.com)\n\n[Streamlit Docs](https://docs.streamlit.io/)")

# Constants to fix hard-coding smells
COMPANY_LOGO = "./assets/fake_company.png"

def get_report_data():
    """Returns data for charts, avoiding hard-coding in page files."""
    return {"data": [1, 5, 2, 6, 2, 1]}

def common_page_config(page_title, page_icon=None):
    """Standardize page configuration and common UI elements."""
    st.set_page_config(page_title=page_title, page_icon=page_icon)
    init_session_state()