import functions
import FreeSimpleGUI as sg

# Creating items for GUI
label = sg.Text("Type in a to-do")
input_box = sg.InputText(tooltip="Enter todo")
add_button = sg.Button("Add")

#Create Layout List, Each list inside list is displayed as a row in the gui
layout = [[label], [input_box, add_button]]

window = sg.Window("My To-Do App", layout=layout) #layout expects a list of lists (rows)
window.read() # Displays window
window.close()
