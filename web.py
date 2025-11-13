import streamlit as st
import functions

def add_todo():
    todo = st.session_state["new_todo"]
    todos.append(todo + "\n")
    functions.write_todos(todos)
    st.session_state["new_todo"] = ""

functions.file_exists("todos.txt")
todos = functions.get_todos()

st.title("My Todo App") # Title
# st.subheader("This is my Todo App") # Sub Heading
# st.write("This app is to track todos") # Paragraph Text

for i, todo in enumerate(todos):
    checkbox = st.checkbox(todo, key=todo)
    if checkbox: # Checks if a checkbox is pressed
        todos.pop(i) # Removes that specific todo from the todos list by using the index
        functions.write_todos(todos)
        del st.session_state[todo]
        st.rerun()

text_input = st.text_input(label=" ", placeholder="Enter a todo", on_change=add_todo, key="new_todo")