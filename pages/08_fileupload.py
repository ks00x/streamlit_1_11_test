import streamlit as st

st.write('#### file_uploader now accepts multiple files!')
st.write('https://docs.streamlit.io/library/api-reference/widgets/st.file_uploader')

uploaded_files = st.file_uploader("Choose a CSV file", accept_multiple_files=True,key='upload')

st.write(st.session_state.upload)

# for uploaded_file in uploaded_files:
#      bytes_data = uploaded_file.read()
#      st.write("filename:", uploaded_file.name)
#      #st.write(bytes_data)