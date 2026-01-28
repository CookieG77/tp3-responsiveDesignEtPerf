import streamlit as st
from pathlib import Path

st.set_page_config(page_title="Landing", layout="wide")
html = Path("index.html").read_text(encoding="utf-8")
css = Path("style.css").read_text(encoding="utf-8")
st.components.v1.html(f"<style>{css}</style>{html}", height=1200, scrolling=True)
