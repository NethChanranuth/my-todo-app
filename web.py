import streamlit as st
import functions

todos = functions.get_todos("todos.txt")


def add_todo():
    new_todo = st.session_state["new_todo"]
    new_todo = new_todo + "\n"
    todos.append(new_todo)
    functions.write_todos(todos)


st.title("My Todo App")
st.subheader("This is my todo app.")
st.write("This app is to increase your productivity.")


for todo in todos:
    checkbox = st.checkbox(todo, key=todo)
    if checkbox:
        todos.remove(todo)
        functions.write_todos(todos)
        del st.session_state[todo]
        st.experimental_rerun()

st.text_input(label="input", label_visibility="hidden",
              placeholder="Add new todo...",
              on_change=add_todo, key='new_todo')
