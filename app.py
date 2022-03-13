import streamlit as st

st.title('St.John Paul II Cambrige College ')
countries = ['Information', 'people', 'about', 'Contact']
st.image(f"https://jp2college.com/wp-content/uploads/2020/10/How-we-started-3-1.jpg")
st.markdown(page_bg_img, unsafe_allow_html=True)

st.sidebar.write('select data type')
country = st.sidebar.selectbox('Select Country', countries)

