import streamlit as st

tab1, tab2, tab3 = st.tabs(['Cat','Dog','Owl'])

with tab1:
    st.header("A Cat")

    