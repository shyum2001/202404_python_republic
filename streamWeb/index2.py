import streamlit as st
col1, col2= st.columns([1,1]) #(3,1)前面就是3/4，後面就是1/4的欄位配置

with col1:
    st.title("這是欄位1")
    st.header("欄位1header")
    st.subheader("欄位1subHeader")

with col2:
    st.title("這是欄位2")
    st.header("欄位2header")
    st.subheader("欄位2subHeader")