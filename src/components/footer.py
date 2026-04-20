import streamlit as st


def footer_home():
    
    st.markdown(f"""
        <div style="margin-top:2rem; display:flex; gap:6px; justify-content:center; item-align:center;">
            <p style="color:white;"> Created with ❤️ by</p>
            <b style="font-weight:bold; color:white;">@Adityaraj</b>
        </div>

        """, unsafe_allow_html=True)