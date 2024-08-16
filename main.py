import streamlit as st
import backend_guide_using_py, js_fundamentals, node_js_core, Express_js, database, Authentication, API, error_handling, deployment

st.title("AJ\'s Guide to Backend using js")

st.sidebar.title("Sequential Topics: ")
page = st.sidebar.radio("Go to", ["Home", "Js Fundamentals", "Node js core", "Express", "Database in backend", "Authentication", "API", "Testing", "Deployment"])

if page == "Home":
    backend_guide_using_py.show()
elif page == "Js Fundamentals":
    js_fundamentals.show()
elif page == "Node js core":
    node_js_core.show()
elif page == "Express":
    Express_js.show()
elif page == "Database in backend":
    database.show()
elif page == "Authentication":
    Authentication.show()
elif page == "API":
    API.show()
elif page == "Testing":
    error_handling.show()
elif page == "Deployment":
    deployment.show()