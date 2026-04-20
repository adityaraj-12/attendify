import streamlit as st
from src.components.header import header_home
from src.components.footer import footer_home
from src.ui.base_layout import style_base_layout, style_background_home


def home_screen():

    header_home()
    style_background_home()
    style_base_layout()

    col1, col2 = st.columns(2, gap="large")

    with col1:
        st.header("I'm Student")
        st.image("https://res.cloudinary.com/dqygwpst9/image/upload/v1776657999/ChatGPT_Image_Apr_20_2026_09_31_15_AM_f7v5yv.png", width=120)
        if st.button('Student Portal', type='primary', icon=':material/arrow_outward:', icon_position="right"):
            st.session_state['login_type'] = 'student'
            st.rerun()
            
    with col2:
        st.header("I'm Teacher")
        st.image("https://res.cloudinary.com/dqygwpst9/image/upload/v1776658011/ChatGPT_Image_Apr_20_2026_09_35_55_AM_iwt0fj.png", width=132)
        if st.button('Teacher Portal', type='primary', icon=':material/arrow_outward:', icon_position="right"):
            st.session_state['login_type'] = 'teacher'
            st.rerun()
    
    footer_home()
        