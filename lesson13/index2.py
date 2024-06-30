import requests
from pydantic import BaseModel,Field,RootModel,field_validator,field_serializer
import streamlit as st
import source
from source import Root
import pandas as pd


try:
    data_str = source.download_youbike()
except Exception as e:
    st.error(e)
else:
    root = Root.model_validate_json(data_str)
    data = root.model_dump()
    areas:list[str] = list(set(map(lambda value:value['行政區'],data)))

    st.title("新北市youbike各行政區站點資料")

    col1, col2 = st.columns([1, 6])
    with col2:
        df1 = pd.DataFrame(display_data,
                        columns=['站點名稱','總數','可借','可還'])
        st.dataframe(data=df1)

        with col1:
            st.subheader(sarea_name)

        tableContainer = st.container(border=False)
        with tableContainer:  
                        
        dfo =pd.DataFrame(display_data,
                          columns=['站點名稱','總數'])
        st.scatter_chart(df0,
                         x='站點名稱',
                         y='總數',
                         color='#0000',
                         size='總數')
    

            df2 = pd.DataFrame(display_data,
                               columns=['站點名稱','總數','可借'])
            
            st.scatter_chart(df2,
                             x='站點名稱',
                             y='總數',
                             color='#f0f',
                             size='可借')
            
            df3 = pd.DataFrame(display_data,
                                    columns=['站點名稱','總數','可還'])

            st.scatter_chart(df3,
                                 x='站點名稱',
                                y='總數',
                                color='#fd0',
                                size='可還')



    with st.sidebar:
        st.selectbox(":orange[請選擇行政區域:]",options=areas,on_change=area_change,key='sarea')