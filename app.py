import streamlit as st

st.title('St.John Paul II Cambrige College ')

st.sidebar.write('select data type')
country = st.sidebar.selectbox('Select Country', countries)

