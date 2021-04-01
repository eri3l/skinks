import streamlit as st

def app():
    st.title('Home')

    st.markdown(""" 
    	Please select a search method from the options in the navigation page. 
    	- The **Toes** option is for searching by missing toes only.
    	- The **`Search`** option is for searching by SVL, Trap Location and Toes (intact and missing)
	""")
    
    image = '/data/P1060519.jpg'
    st.image(image, caption='El pretty skinko',
         use_column_width = True)
         
    st.sidebar.subheader("About")
    st.sidebar.info("Copyright © 2021 Polina Stucke  \n  \n This app is open source. You can find it on GitHub")

