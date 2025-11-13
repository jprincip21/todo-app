import streamlit as st
import functions

def add_todo():
    todo = st.session_state["new_todo"]
    todos.append(todo + "\n")
    functions.write_todos(todos)
    st.session_state["new_todo"] = ""

def complete_todo():
    todo

functions.file_exists("todos.txt")
todos = functions.get_todos()

st.title("My Todo App") # Title
# st.subheader("This is my Todo App") # Sub Heading
# st.write("This app is to track todos") # Paragraph Text

for todo in todos:
    st.checkbox(todo)

text_input = st.text_input(label=" ", placeholder="Enter a todo", on_change=add_todo, key="new_todo")

st.session_state