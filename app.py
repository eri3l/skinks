import streamlit as st
from multiapp import MultiApp
from apps import home, toes, search 

app = MultiApp()

app.add_app("Home", home.app)
app.add_app("Toes", toes.app)
app.add_app("Search", search.app)

app.run()
