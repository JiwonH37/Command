import a2
from pathlib import Path
import os

current = None

while True: 
    user_input = input("Welcome! Do you want to create or load a DSU file (type 'c' to create or 'l' to load): \n")
    if user_input.lower() == 'admin':
        a2.main()
        break

    elif user_input.lower() == 'c':
        filename = input("Enter the name of the file that you want to create: ")
        user_path = input("Enter the path that you want to create the file in: ")

        if user_path[-1] != '/':
            user_path += '/'
        user_input = 'C '+ user_path + ' -n '+ filename
        path = user_path + filename +'.dsu'
        path_Path = Path(path)
        if not(os.path.exists(path_Path)):
            current = a2.c_command(user_path, user_input)
            print(f"File created successfully")
        
        elif os.path.exists(path_Path):
            current = a2.o_command(path)
            print("The file already existed, so we loaded it for you :)")
        
        
        while True:
            print()
            u_input = input("Enter 'E' to EDIT the file\nEnter 'P' to PRINT the data stored in the file\nEnter 'Q' to QUIT\n")
            if u_input.lower() == 'e':
                print()
                opt_input = input("Enter '-usr [username]' to edit the username\nEnter '-pwd [PASSWORD]' to edit password\nEnter '-bio [BIO]' to edit biography\nEnter '-addpost [NEW POST]' to make a post\nEnter '-delpost [ID]' to delete selected post\nYou can enter username and password in a single command\n")
                instruction = 'E' +' '+opt_input
                print()
                current = a2.e_command(current, instruction)

            elif u_input.lower() == 'p':
                print()
                opt_input = input("Enter '-usr' to print the username\nEnter '-pwd to print password\nEnter '-bio' to print biography\nEnter '-posts' to print all posts\nEnter '-post [ID]' to print selected post\nEnter '-all' to print all information\nYou can enter username and password in a single command\n")
                instruction = 'P' +' '+opt_input
                print()
                current = a2.p_command(current, instruction)

            elif u_input.lower() == 'q':
                exit()

    elif user_input.lower() == 'l':
        user_path = input("Great! Enter the directory path that you want to load: ")
        path = Path(user_path)

        while 'dsu' not in user_path:
            print("Oops, the file type is not supported. Please enter a DSU file")
            user_path = input()
        
        while not(os.path.exists(path)):
            user_path = input("The path entered is not found. Enter another directory: ")
            path = Path(user_path)
        
        if user_path[-3:] == 'dsu':
            current = a2.o_command(user_path)

        while True:
            u_input = input("Enter 'E' to EDIT the file\nEnter 'P' to PRINT the data stored in the file\nEnter 'Q' to QUIT\n")
            if u_input.lower() == 'e':
                print()
                opt_input = input("Enter '-usr [USERNAME]' to edit the username\nEnter '-pwd [PASSWORD]' to edit password\nEnter '-bio [BIO]' to edit biography\nEnter '-addpost [NEW POST]' to make a post\nEnter '-delpost [ID]' to delete selected post\nYou can enter username and password in a single command\n")
                instruction = 'E' +' '+opt_input
                current = a2.e_command(current, instruction)

            elif u_input.lower() == 'p':
                print()
                opt_input = input("Enter '-usr' to print the username\nEnter '-pwd to print password\nEnter '-bio' to print biography\nEnter '-posts' to print all posts\nEnter '-post [ID]' to print selected post\nEnter '-all' to print all information\nYou can enter username and password in a single command\n")
                instruction = 'P' +' '+opt_input
                current = a2.p_command(current, instruction)

            elif u_input.lower() == 'q':
                exit()
    else:
        print("Invalid command. Please enter another command: ")
        continue



