# %%
import streamlit as st
import requests
import pandas as pd

url = 'https://viacep.com.br/ws/{cep}/json/'

st.title("Busca CEP")

cep = st.text_input('Busque seu cep')

if cep != '':
    try:
        resp = requests.get(url.format(cep=cep))
        data = pd.DataFrame([resp.json()])
        st.dataframe(data)
    except Exception as err:
        st.error('Entre com um CEP válido!')