import streamlit as st
import base64

def show_gif(num):
    """### gif from local file"""
    file_ = open(f"bnimation{num}.gif", "rb")
    contents = file_.read()
    data_url = base64.b64encode(contents).decode("utf-8")
    file_.close()

    st.markdown(
        f'<img src="data:image/gif;base64,{data_url}" alt="cat gif">',
        unsafe_allow_html=True,
    )