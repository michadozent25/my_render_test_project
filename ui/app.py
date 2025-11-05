import os
import requests
import streamlit as st
# primär aus Env (Render/UI-Service), sonst Fallback lokal
API_BASE = os.getenv("API_BASE", "http://localhost:8000")
#API_BASE = "https://my-render-test-project.onrender.com"

st.set_page_config(page_title="Streamlit + FastAPI + Neon", layout="centered")
st.title("Streamlit UI")

with st.sidebar:
    st.caption("Backend:")
    st.code(API_BASE, language="bash")

col1, col2 = st.columns(2)

with col1:
    if st.button("Ping /health", use_container_width=True):
        try:
            r = requests.get(f"{API_BASE}/health", timeout=10)
            st.success(r.json())
        except Exception as e:
            st.error(e)

with col2:
    if st.button("Ping /health/db", use_container_width=True):
        try:
            r = requests.get(f"{API_BASE}/health/db", timeout=15)
            st.success(r.json())
        except Exception as e:
            st.error(e)

st.subheader("Users")
name = st.text_input("Name", "")
if st.button("Add User"):
    try:
        r = requests.post(f"{API_BASE}/users", params={"name": name}, timeout=10)
        r.raise_for_status()
        st.success(r.json())
    except Exception as e:
        st.error(e)

if st.button("List Users"):
    try:
        r = requests.get(f"{API_BASE}/users", timeout=10)
        r.raise_for_status()
        st.table(r.json())
    except Exception as e:
        st.error(e)
