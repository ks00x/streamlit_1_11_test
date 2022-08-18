import streamlit as st
import datetime
import random

intro = '''

#### the case of programtically updating controls
- widget control key values can only be changed inside 'their' callback function
- ... or before the widget is created (next run) see reset logic here!
- a form can be used to group several controls together
'''
st.write(intro)


if 'reset'  not in st.session_state:
    st.session_state.reset = True

if st.session_state.reset : # this works - action is shifted to next run of the script!
    st.session_state.my_number = 1
    st.session_state.my_slider = 0
    st.session_state.reset = False

def form_reset(): # does not work...
    st.session_state.my_number = 1
    st.session_state.my_slider = 0

def form_reset2():
    st.session_state.reset = True


def form_callback():
    st.session_state.my_number += 1*(0.5-random.random())
    st.session_state.my_slider += 1


with st.form(key='my_form'):
    # do not give default/init values to the controls if they are modfified by session_state also!
    st.slider('My slider', 0, 10, key='my_slider')
    st.number_input('number',key='my_number',format='%f')
    submit_button = st.form_submit_button(label='modify values!', on_click=form_callback)


st.button('reset',on_click=form_reset2)

# exception - does not work!!!
# st.session_state.my_number = 0

# this does also not work:
#st.button('reset form',on_click=form_reset())

