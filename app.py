import streamlit as st

st.title('St.John Paul II Cambrige College ')
countries = ['Information', 'people', 'about', 'Contact']
st.image(f"https://flagcdn.com/80x60/{country_code[country]}.png")
st.markdown(page_bg_img, unsafe_allow_html=True)

st.sidebar.write('select data type')
country = st.sidebar.selectbox('Select Country', countries)

