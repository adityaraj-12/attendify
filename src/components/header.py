import streamlit as st


def header_home():

    logo_url = "https://res.cloudinary.com/dqygwpst9/image/upload/v1776657259/ChatGPT_Image_Apr_20_2026_08_52_40_AM_typu6z.png"
    
    st.markdown(f"""
        <div style="display: flex; flex-direction:column; align-items:center; justify-content:center; margin-bottom:30px; margin-top:30px">
            <img src="{logo_url}" style='height:100px;'>
            <h1 style='text-align:center; color:#E0E3FF'>Attendify</h1>
        </div>

        """, unsafe_allow_html=True)