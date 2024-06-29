import requests
from pydantic import BaseModel,Field,RootModel,field_validator,field_serializer
import streamlit as st
import source  #增加的地方
from source import Root  #增加的地方


try:
    data_str = source.download_youbike()
except Exception as e:
    st.error(e)
else:
    root = Root.model_validate_json(data_str)
    data = root.model_dump()
    areas: list[str] = list(set(map(lambda value: value['行政區'],data)))

    def area_change():
        print("Hello")

    with st.sidebar:
        st.selectbox(":orange[請選擇行政區域:]",options =areas,on_change=area_change,Key='sarea')
        st.session_state





