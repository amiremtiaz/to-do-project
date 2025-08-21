import todocode

while True:
    print("***  Wellcome to your program  *** " , end = "\n\n")
    print("1. Show your list: ")
    print("2. add todo: ")
    print("3. delete todo: ")
    print("4. edit todo: ")
    print("5. show date: ")
    print("6. exit: ")
    bottom = int(input("Enter your choice: "))
    menu = todocode.ToDo()
    match bottom:
        case 1:
            menu.show_do_list()
        case 2:
            menu.add_todo()
        case 3:
            menu.delete_todo()
        case 4:
            menu.edit_todo()
        case 5:
            menu.show_date()
        case 6:
            print("DO YOU WORK! ")
            break
        case _:
            print("sorry , i didnt understand that! ")
