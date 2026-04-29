import streamlit as st


def style_background_home():

    st.markdown("""
        <style>
            .stApp{
                background: #061340 !important
            }
            
            .stApp div[data-testid="stColumn"]{
                background-color: #6a77a3 !important;
                padding: 2.5rem !important;
                border-radius: 5rem !important;
                }
                
        </style>
    """, unsafe_allow_html=True)

def style_background_deshboard():

    st.markdown("""
        <style>
            .stApp{
                background: #061340 !important
            }
            
        </style>
    """, unsafe_allow_html=True)


def style_base_layout():

    st.markdown("""
                
        <style>
            @import url('https://fonts.googleapis.com/css2?family=Climate+Crisis:YEAR@1979&display=swap');
            @import url('https://fonts.googleapis.com/css2?family=Climate+Crisis:YEAR@1979&family=Outfit:wght@100..900&display=swap');
                
            /*  Hide Top Bar of streamlit */
            #MainMenu, footer, header{
                visibility: hidden;
            }
            .block-container {
                padding-top:1.5rem !important
            }
                  
            h1{
                font-family: 'Climate Crisis', sans-serif !important;
                color: #72fcde !important;
                font-size: 3.5rem !important
                line-height: 1.1 !important;
                margin-bottom: 0rem !important;
            }

            h2{
                font-family: 'Climate Crisis', sans-serif !important;
                color: #b0f5e6  !important;
                font-size: 2rem !important;
                line-height: 0.9 !important;
                margin-bottom: 0rem !important;
            }
                
            h3, h4, p{
                font-family: 'Outfit', sans-serif;
            }
            
            
            button{
                border-radius: 1.5rem !important;
                background-color: #03134a !important;
                color: #bacaff !important;
                pedding: 10px 20px !important;
                border: none !important; 
                transition: transform 0.25s ease-in-out !importatn;
            }
                
            button[kind="secondary"]{
                border-radius: 1.5rem !important;
                background-color: #b5364e !important;
                color: white !important;
                pedding: 10px 20px !important;
                border: none !important; 
                transition: transform 0.25s ease-in-out !importatn;
            }
            
            button[kind="tertiary"]{
                border-radius: 1.5rem !important;
                background-color: #b5364e !important;
                color: white !important;
                pedding: 10px 20px !important;
                border: none !important; 
                transition: transform 0.25s ease-in-out !importatn;
            }
            
            button[kind="primary"]{
                border-radius: 1.5rem !important;
                background-color: #1df083 !important;
                color: white !important;
                pedding: 10px 20px !important;
                border: none !important; 
                transition: transform 0.25s ease-in-out !importatn;
            }
                
            button:hover{
                transform: scale(1.05)}
                
        </style>
    """, unsafe_allow_html=True)