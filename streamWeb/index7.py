import streamlit as st


st.write("Inside the form")
slider_val = st.slider("Form slider")
checkbox_val = st.checkbox("Form checkbox")

    
st.write("slider", slider_val, "checkbox", checkbox_val)
#可以不用submit就可以把圖表撥動的值顯示在下方
