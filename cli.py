# from functions import get_todos, write_todos
import functions
import time

date = time.strftime("%b %d, %Y %H:%M:%S")
print(f"It is {date}")


while True:
    user_action = input("Type add, show, edit, complete or exit: ").lower()
    user_action = user_action.strip()

    if user_action.startswith("add"):
        todo = user_action[4:]

        todos = functions.get_todos()

        todos.append(todo + '\n')

        functions.write_todos(todos)

    elif user_action.startswith("show"):

        todos = functions.get_todos()

        for index, item in enumerate(todos):
            item = item.strip("\n")
            row = f"{index + 1}. {item}"
            print(row)

    elif user_action.startswith("edit"):
        try:
            number = int(user_action[5:])
            number -= 1

            todos = functions.get_todos()

            new_todo = input("Enter new todo: ")

            todos[number] = new_todo + '\n'

            functions.write_todos(todos)

        except ValueError:
            print("Invalid Input Try Again")
            continue
        except IndexError:
            print("No Number with that index")
            continue

    elif user_action.startswith("complete"):
        try:
            number = int(user_action[9:])

            index = number - 1

            todos = functions.get_todos()

            todo_to_remove = todos[index].strip("\n")
            todos.pop(index)
            # todos.remove(todos[index])

            functions.write_todos(todos)

            message = f"Todo {todo_to_remove} was removed from the list."
            print(message)

        except IndexError:
            print("There is no item with that Number")
            continue

    elif user_action.startswith("exit"):
        break
    else:
        print("Command not valid.")

