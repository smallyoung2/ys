# -*- coding: utf-8 -*-
"""
Created on Fri May 17 15:13:13 2024

@author: soyoung
"""

import streamlit as st
import pandas as pd
import folium
import geopandas as gpd
from streamlit_folium import folium_static

# 수원시 법정경계(읍면동) GeoJSON 파일 경로
geojson_path = "D:\Workspace\Python\mini\수원시_법정경계(읍면동).geojson"

# Streamlit 앱 제목
st.title("수원시 지도")

# GeoJSON 파일을 GeoDataFrame으로 읽어옴
gdf = gpd.read_file(geojson_path)

# Folium 지도 객체 생성
m = folium.Map(location=[37.2636, 127.0286], zoom_start=11)

# GeoDataFrame의 geometry 데이터를 Folium GeoJson으로 추가
folium.GeoJson(gdf).add_to(m)

# Folium 지도를 Streamlit에 표시
folium_static(m)


#streamlit run d:\workspace\python\mini\example.phttps://github.com/ADERGRAM/2024_Accident_Project/blob/main/BumCheol/%EB%85%B8%EC%9D%B8%20%EB%A9%B4%ED%97%88%20%EC%9E%90%EC%A7%84%20%EB%B0%98%EB%82%A9%EC%9E%90%20%EC%88%98(2019~2023)(%EC%A7%84%ED%96%89%20%EC%A4%91)/65%EC%84%B8%20%EC%9D%B4%EC%83%81%20%EB%A9%B4%ED%97%88%20%EB%B0%98%EB%82%A9%EC%9E%90%20%EC%88%98(2019~2023).pyy