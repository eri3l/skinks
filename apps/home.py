import streamlit as st

def app():
    st.write("## Welcome to the Skink Search Tool app")

    st.write(""" 
                The app filters existing skink data by multiple criteria in order to help with the identification of skinks. \n
                Use the navigation bar to select the type of search you would like to perform.
	""")
    
    
    st.markdown("### Toes")
    st.write("Use this option to search by missing toes only")
    with st.beta_expander("More information"):
        st.markdown("""
            - This search filters by all possible combinations of  **`missing toes`** and excludes other missing toes.  \n
            Example:
                
            > `selected toes` = [LF1, LF2]   \n
            > Results:   \n
            > The search returns all skinks where [LF1], [LF2], [LF1, LF2] or [none] toes are missing. 
            """)
    
    
    st.markdown("### Search")
    st.write("Use this option to search by multiple criteria:")
    st.markdown("""
            - SVL (snout to vent length) (mm)  \n
            Existing skinks above 70mm are classified as adults and labelled with `projected_SVL`=100
                    """)
    with st.beta_expander("More information"):
        st.markdown("""
            The search considers matches within 5 mm of the selected length. All skinks above 70 mm (`@adult`) are classified as adults. 
In finding matches, it is assumed that skinks grow by  **10** mm per year (`@delta`) and reach adult size at **70** mm (`@adult`). 
Search is performed on a calculated variable, `projected_SVL`:
```python
projected_SVL= skink_SVL + delta*(current_year – skink_Year) 
```
                    """)
    st.markdown("""
                - Paddock/traplist  \n
                Each paddock contains multiple traps, click below to view the full list of traps
                """)
    with st.beta_expander("See traps"):
            st.markdown("""
                        | Paddock | Traps |
                        | ------ | ------ |
                        | pdk_R66 | ['R66', 'board', 'R67', 'M14', 'R68', 'R69', 'R70', 'M11', 'PR1'] |
                        | pdk_R71 | ['R71', 'PR2', 'R72', 'M9', 'P3', 'PR3', 'R73', 'M8', 'PR4', 'R74', 'M7', 'PR5', 'R75', 'PR6', 'R76', 'M5', 'PR7'] |
                        | pdk_R77 | ['R2', 'PR13', 'R3', 'PR14', 'R4', 'PR15', 'P16', 'PR16', 'R6', 'PR17'] |
                        | pdk_R02 | ['W1', 'W2', 'W3', 'W4', 'W5', 'W6', 'W7', 'W8', 'W9', 'W10', 'W11', 'W12', 'W13'] |
                        | ... | ... |
                        """)
    st.markdown("""
                - Toes  \n
                Search by intact or missing toes.
                """)
                    
    image = 'data/P1060519.jpg'
    st.image(image, caption='El pretty skinko', use_column_width = True)
    

    with st.sidebar.beta_expander("About"):   
        st.markdown(''' Copyright © 2021 Polina Stucke.    
               This app is open source. You can find it on [GitHub](https://github.com/eri3l/skinks) ''')

