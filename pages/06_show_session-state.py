import streamlit as st

header = '''
#### session_state is not really preserved accross pages!
there is a confusing behavior with respect to multipage apps and session_state (Streamlit V 1.11.1). 
See here for the details:
- https://github.com/streamlit/streamlit/issues/4989
- https://github.com/streamlit/streamlit/issues/4338   
- https://github.com/streamlit/streamlit/issues/4458 

A workaround:   
https://gist.github.com/okld/0aba4869ba6fdc8d49132e6974e2e662   


check the official notes on widgets here:   
https://docs.streamlit.io/library/advanced-features/widget-semantics#advanced-notes-on-widget-behavior

'''
st.write(header)

st.write(st.session_state)