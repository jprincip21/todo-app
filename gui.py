import functions
import FreeSimpleGUI as sg
import time
import os

if not os.path.exists("todos.txt"):
    with open("todos.txt", "w") as f:
        pass


sg.theme("darkgrey8")

# Creating items for GUI
label = sg.Text("Type in a to-do")
clock_label = sg.Text('', key="clock")

input_box = sg.InputText(tooltip="Enter todo",
                         key="todo")
todos_box = sg.Listbox(values=functions.get_todos(),
                       key="todos",
                       enable_events=True,
                       size=(45,10))

add_button = sg.Button(image_source="assets/add.png", key="Add", tooltip="Add")
edit_button = sg.Button("Edit")
complete_button = sg.Button(image_source="assets/complete.png", key="Complete", tooltip="Complete")
exit_button = sg.Button("Exit")

add_complete_layout = [[edit_button],
                       [complete_button]]

add_complete_column = sg.Column(add_complete_layout)

#Create Layout List, Each list inside list is displayed as a row in the gui
layout = [[clock_label],
        [label],
        [input_box, add_button],
        [todos_box, add_complete_column],
        [exit_button]]

window = sg.Window("My To-Do App",
                   layout=layout, #layout expects a list of lists (rows)
                   font=("Helvetica", 16))

while True:
    event, values = window.read(timeout=200) # Displays window

    if event == sg.WIN_CLOSED:
        break

    window["clock"].update(value=time.strftime("%d-%m-%Y %H:%M:%S"))
    match event:
        # When the user clicks something the event variable is updated to be a string of the key.
        # We use this to decide what to do.
        case "Add":
            # The user clicked the add button so we grab the input box
            # text from the values dictionary using the input box key
            # We also get the list of todos, append the new todo and update the file
            todos = functions.get_todos()
            new_todo = values['todo'] + "\n"
            todos.append(new_todo)
            functions.write_todos(todos)
            window["todos"].update(values=todos)

        case "Edit":
            # When the edit button is pressed we grab the todo the user clicked
            # by using the Listbox key in the values dictionary
            # We then get the todos list, find the index of the todo and update that index
            try:
                todo_to_edit = values['todos'][0]
                new_todo = values['todo'] + "\n"

                todos = functions.get_todos()
                index = todos.index(todo_to_edit)
                todos[index] = new_todo
                functions.write_todos(todos)

                window["todos"].update(values=todos)
            except IndexError:
                print("No Item selected")
                sg.popup("Please select an item first", font=("Helvetica", 16))

        case "Complete":
            try:
                selected_todo = values['todos'][0]
                todos = functions.get_todos()
                index = todos.index(selected_todo)
                todos.remove(selected_todo)
                functions.write_todos(todos)
                window["todos"].update(values=todos)
                window["todo"].update(value="")
            except IndexError:
                print("No Item selected")
                sg.popup("Please select an item first", font=("Helvetica", 16))

        case "todos":
            # When the user clicks on a todo we grab the value from the values dictionary using the
            # Listbox key from the values dictionary
            # This value is then displayed using the input box key on the window
            todo_to_edit = values['todos'][0].strip()
            window["todo"].update(value=todo_to_edit)

        case "Exit":
            break



window.close()


