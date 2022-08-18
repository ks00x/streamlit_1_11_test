import streamlit as st



def function_in_main():
    st.write('function_in_main called')

st.header('main landing page (multipage app)')

st.write(
    '''
    testing some of the more recent features in Streamlit 1.11    
    checkout the side bar for the menu of subpages!   

    
    https://docs.streamlit.io/library/get-started/multipage-apps

    see also the [changelog](https://docs.streamlit.io/library/changelog)
    ''')


st.sidebar.write(
    """
    pages are collect from the pages subfolder!
    add numeric prefixes (0.1_,02_,..) to 
    manually change sorting of page items   
    """
    )


