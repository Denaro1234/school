import streamlit as st

st.title('St.John Paul II Cambrige College ')
countries = ['Information', 'people', 'about', 'Contact']
page_bg_img = '''
<style>
body {
background-image: url("https://jp2college.com/wp-content/uploads/2020/10/How-we-started-3-1.jpg");
background-size: cover;
}
</style>
'''

st.markdown(page_bg_img, unsafe_allow_html=True)

st.sidebar.write('select data type')
country = st.sidebar.selectbox('Select Country', countries)

