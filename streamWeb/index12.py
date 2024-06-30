import streamlit as st

st.title("計數器範例")
count = 0

increment = st.button("Increment")
if increment:
    count += 1

st.write("Count=", count)
#這個只會計一次，沒有迴圈的概念
