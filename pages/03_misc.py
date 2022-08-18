import streamlit as st
import my_module


st.write('#### import works for modules on the main level')
my_module.module_function()


st.write('#### st.metric')
st.write('https://docs.streamlit.io/library/api-reference/data/st.metric')
cols = st.columns(3)

cols[0].metric(label="Gas price", value=4, delta=-0.5,
    delta_color="inverse")

cols[1].metric(label="Active developers", value=123, delta=123,
    delta_color="off")

st.write('#### st.radio - horizontal layout')
st.write('https://docs.streamlit.io/library/api-reference/widgets/st.radio')
st.radio('radio buttons',[1,2,3],horizontal=True)


st.write('#### disable parameter for input widgets')
st.button('normal')
st.button('disabled',disabled=True)


st.write('#### still no way to disable the increment buttons...')
st.number_input('number',value=1.234e-9,step=None,format="%g")


st.write('#### st.download_button()')
st.write('https://docs.streamlit.io/library/api-reference/widgets/st.download_button')
text_contents = '''This is some text'''
st.download_button('Download some text', text_contents)


st.write('#### text area box is resizeable')
st.text_area('text area box',placeholder='placeholder text')
