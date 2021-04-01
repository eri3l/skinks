import streamlit as st
from multiapp import MultiApp
from apps import home, toes, search # import your app modules here

app = MultiApp()


# Add all your application here
app.add_app("Home", home.app)
app.add_app("Toes", toes.app)
app.add_app("Search", search.app)


# The main app
app.run()
