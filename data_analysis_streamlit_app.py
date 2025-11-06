import os
from dotenv import load_dotenv
import streamlit as st

# Load environment variables from .env file
load_dotenv()

# Retrieve the OpenAI API key safely
openai_api_key = os.getenv("OPENAI_API_KEY")

# DEBUG: Print to verify (remove after debugging)
if openai_api_key:
    print(f"✓ API Key loaded successfully (first 10 chars): {openai_api_key[:10]}")
    os.environ["OPENAI_API_KEY"] = openai_api_key
else:
    print("✗ ERROR: API Key not found!")
    raise ValueError("OPENAI_API_KEY not found in .env file!")

# Set Streamlit configuration
os.environ["STREAMLIT_SERVER_MAX_UPLOAD_SIZE"] = "2000"

# Set Streamlit to wide mode
st.set_page_config(layout="wide", page_title="Main Dashboard", page_icon="📊")


data_visualisation_page = st.Page(
    "./Pages/python_visualisation_agent.py", title="Data Visualisation", icon="📈"
)

pg = st.navigation(
    {
        "Visualisation Agent": [data_visualisation_page]
    }
)

pg.run()