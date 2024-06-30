import streamlit as st

if 'robert' not in st.session_state:
    st.session_state['robert'] = 30

st.session_state    #確認robert是否有在值裡，沒有的話加入