import streamlit as st
import requests

moon2024_json_url = "https://svs.gsfc.nasa.gov/vis/a000000/a005100/a005187/mooninfo_2024.json"
response = requests.get(moon2024_json_url)

if response.status_code == 200:
    data = response.json()
    st.dataframe(data)