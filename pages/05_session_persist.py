import streamlit as st
import datetime
import random

intro = '''
#### persistent widget values between page switching!
- using an extra dict 'store' to hold the values between page switches
- check the show_session page and notice the 'store' variable

'''
st.write(intro)

if 'reset'  not in st.session_state: # also a first run init!
    st.session_state.reset = True # not related to any widget. Thats why it is preserved!
    st.session_state.store = {} # not related to a widget -> preserved!
    st.session_state.store['my_number2'] = st.session_state.my_number2 = 1
    st.session_state.store['my_slider2'] = st.session_state.my_slider2 = 0

if st.session_state.reset : # this works - action is shifted to next run of the script!
    st.session_state.store['my_number2'] = st.session_state.my_number2 = 1
    st.session_state.store['my_slider2'] = st.session_state.my_slider2 = 0
    st.session_state.reset = False

st.session_state.my_number2 = st.session_state.store['my_number2']
st.session_state.my_slider2 = st.session_state.store['my_slider2']


def form_reset():
    st.session_state.reset = True


def form_callback():
    st.session_state.my_number2 += 1*(0.5-random.random())
    st.session_state.my_slider2 += 1
    st.session_state.store['my_number2'] = st.session_state.my_number2
    st.session_state.store['my_slider2'] = st.session_state.my_slider2



with st.form(key='my_form'):
    # do not give default/init values to the controls if they are modfified by session_state also!
    st.slider('My slider', 0, 10, key='my_slider2')
    st.number_input('number',key='my_number2')
    submit_button = st.form_submit_button(label='modify values!', on_click=form_callback)


st.button('reset',on_click=form_reset)

