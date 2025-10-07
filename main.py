import streamlit as st

# Page configuration
st.set_page_config(page_title="My ML Portfolio", layout="wide")

# Initialize session_state for navigation
if "project" not in st.session_state:
    st.session_state.project = "Home"

# Sidebar for navigation
st.session_state.project = st.sidebar.radio(
    "Go to Project",
    ["Home", "Salary Prediction", "iris", "fake"],
    index=["Home", "Salary Prediction", "iris", "fake"].index(st.session_state.project)
)

# Title and intro
st.title("Welcome to My ML Portfolio")
st.markdown("""
This website showcases my machine learning projects.
Use the sidebar to navigate between different projects.
""")

# About Me section
st.title("About Me")

# Create two columns: left for image, right for text + buttons
col1, col2 = st.columns([1, 2])

with col1:
    st.image(r"WhatsApp Image 2025-09-18 at 15.36.51_1aaf220c.jpg", width=300)

with col2:
    st.write("""
        Hi! I am Anandha Krishnan, a data scientist and machine learning enthusiast.
        Below are some of my projects.
    """)

    # Home page buttons inside column 2
    if st.session_state.project == "Home":
        st.write("### Navigate to Projects:")
        col_button1, col_button2, col_button3 = st.columns(3)
        
        with col_button1:
            if st.button("Salary Prediction"):
                st.session_state.project = "Salary Prediction"
        
        with col_button2:
            if st.button("iris"):
                st.session_state.project = "iris"
        
        with col_button3:
            if st.button("fake"):
                st.session_state.project = "fake"

# Load project pages based on selection
if st.session_state.project == "Salary Prediction":
    from apps.Salary import run_app
    run_app()

elif st.session_state.project == "iris":
    from apps.iris import run_app
    run_app()

elif st.session_state.project == "fake":
    from apps.fake import run_app
    run_app()
