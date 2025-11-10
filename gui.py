import functions
import FreeSimpleGUI as sg

# Creating items for GUI
label = sg.Text("Type in a to-do")
input_box = sg.InputText(tooltip="Enter todo", key="todo")
add_button = sg.Button("Add")
exit_button = sg.Button("Exit")

#Create Layout List, Each list inside list is displayed as a row in the gui
layout = [[label], [input_box, add_button], [exit_button]]

window = sg.Window("My To-Do App",
                   layout=layout, #layout expects a list of lists (rows)
                   font=("Helvetica", 16))

while True:
    event, values = window.read() # Displays window
    print(event)
    print(values)
    match event:
        case "Add":
            todos = functions.get_todos()
            new_todo = values['todo'] + "\n"
            todos.append(new_todo)
            functions.write_todos(todos)

        case "Exit":
            window.close()
            break

        case sg.WIN_CLOSED:
            break


