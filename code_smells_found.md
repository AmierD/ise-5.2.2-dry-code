# Code Smells Found
* repeating the same sidebar logic in each page
    * ex:
        ```python
        if st.session_state.get("logged_in") == None:
            st.session_state["logged_in"] = False

        def login():
            st.session_state.logged_in = True


        def logout():
            st.session_state.logged_in = False


        st.set_page_config(page_title="About")

        st.markdown("# About")
        st.sidebar.header("About")

        if st.session_state.logged_in:
            st.sidebar.success("Logged in")
            st.sidebar.button("Log out", key="logout", on_click=logout)
        else:
            st.sidebar.warning("Not logged in")
            st.sidebar.button("Log in", key="login", on_click=login)
        ```
* the same company info and links footer in each page
    * ex:
        ```python
        with st.expander("Company Info"):
            st.write(
                """
                Fake Company LLC Inc. is located at 1600 Amphitheatre Parkway Mountain View, CA 94043
            """
            )

        with st.expander("Links"):
            st.markdown(
                """
                [Google](https://google.com)

                [Gemini](https://gemini.google.com)

                [Streamlit Docs](https://docs.streamlit.io/)
            """
            )
        ```
* hard-coded image name in about.py
    * ex:
        ```python
        st.image("./assets/fake_company.png")
        ```
* hard-coded data in report.py
    * ex:
        ```python
        st.bar_chart({"data": [1, 5, 2, 6, 2, 1]})
        ```