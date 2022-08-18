import streamlit as st

st.write('## camera input')
st.write('https://docs.streamlit.io/library/api-reference/widgets/st.camera_input')

picture = st.camera_input("Take a picture")

if picture:
     st.image(picture)