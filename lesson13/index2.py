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

    def ijk(value):
        return value['行政區']

    areas:list[str] = list(set(map(ijk,data)))

    option = st.selectbox("請選擇行政區",areas)
    st.write("您選擇:", option)

