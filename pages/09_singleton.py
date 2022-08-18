import streamlit as st
import random


header='''
#### @st.experimental_singleton modifier

https://docs.streamlit.io/library/api-reference/performance/st.experimental_singleton   

- global_init() should only run once for each streamlit server start independent on session...
- could be a good use to init devices etc
- st.experimental_singleton.clear() to reset the singleton state
'''
st.write(header)

@st.experimental_singleton
def global_init():
    x = random.random()
    print('global_init() :', x)
    return(x)

ret = global_init()
st.write('init value: ',ret)

st.button('press to reset global init',on_click=st.experimental_singleton.clear)