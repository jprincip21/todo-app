import streamlit as st
import functions

functions.file_exists("todos.txt")
todos = functions.get_todos()

st.title("My Todo App") # Title
# st.subheader("This is my Todo App") # Sub Heading
# st.write("This app is to track todos") # Paragraph Text

for todo in todos:
    st.checkbox(todo)

st.text_input(label="", placeholder="Enter a todo")