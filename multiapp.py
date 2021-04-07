"""Frameworks for running multiple Streamlit applications as a single app.
"""
import streamlit as st

class MultiApp:
    """Framework for combining multiple streamlit applications.
    Usage:
        def foo():
            st.title("Hello Foo")
        def bar():
            st.title("Hello Bar")
        app = MultiApp()
        app.add_app("Foo", foo)
        app.add_app("Bar", bar)
        app.run()
    It is also possible keep each application in a separate file.
        import foo
        import bar
        app = MultiApp()
        app.add_app("Foo", foo.app)
        app.add_app("Bar", bar.app)
        app.run()
    """
    def __init__(self):
        self.apps = []

    def add_app(self, title, func):
        """Adds a new application.
        Parameters
        ----------
        func:
            the python function to render this app.
        title:
            title of the app. Appears in the dropdown in the sidebar.
        """
        self.apps.append({
            "title": title,
            "function": func
        })

    def run(self):
        #st.set_page_config(layout="wide")
        
        image = 'data/logo01.png'
        st.sidebar.image(image) #, use_column_width=True) 
        st.sidebar.title("Navigation")
        app = st.sidebar.radio(
            'Go to',
            self.apps,
            format_func=lambda app: app['title'])

        app['function']()
        #if app['title'] == "Home":
        #	st.sidebar.title("About")
        #	st.sidebar.info("This app is made by so-and-so")
        	
