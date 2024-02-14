from pathlib import Path
import os
from Profile import Profile
from Profile import Post

def make_post(content, current):
    post = Post(content)
    current.add_post(post)

def delete_post(id, current):
    current.get_posts()
    current.del_post(int(id))

def c_command(directory, user_input):
    myPath = Path(directory)
    file_list = user_input.split()
    file = file_list[-1]+'.dsu'
    path = directory + file

    username = input("Enter a username: ").strip()
    while len(username) < 1:
        username = input("The username cannot be a space. Please enter a proper username: ")

    password = input("Enter a password: ").strip()
    while len(password) < 1:
        password = input("The password cannot be a space. Please enter a proper password: ")

    bio = input("Enter a bio(optional): ")

    if '-n' in  file_list[-2]:
        if os.path.exists(myPath):
            with open(path, "w") as file: 
                info = Profile(path, username, password)
                info.bio = bio
                info.save_profile(path)
    elif '-n' not in file:
        print("ERROR")

    return info

def o_command(directory):
    profile = Profile()
    if directory[-3:] == 'dsu':
        profile.load_profile(directory)

    return profile

def e_command(current, instruction):
    option = instruction.split()
    command = ['-usr', '-pwd', '-bio', '-addpost', '-delpost']

    while option[1] not in command:
        instruction = input("The command does not exist. Please enter a correct command: ")
        option = 'E ' +instruction
        option = option.split()

    if '-usr' in instruction:
        index = option.index('-usr')
        lst = instruction.split('-')

        if len(lst) < 3:
            name = instruction[7:].strip()
            while (len(name) <= 2) or (' ' in name):
                name = input("Please enter the username without a whitespace: ")
        else:
            name = lst[1][3:].strip()
            while (len(name) <= 2) or (' ' in name):
                name = input("Please enter the username without a whitespace: ")

        current.username = name
        current.save_profile(current.dsuserver)

    if '-pwd' in instruction:
        index = option.index('-pwd')
        lst = instruction.split('-')
        if len(lst) < 3:
            pw = instruction[7:].strip()
            while (len(pw) <= 2) or (' ' in pw):
                pw = input("Please enter the password without a whitespace: ")
        else:
            pw = lst[2][3:].strip()
            while (len(pw) <= 2) or (' ' in pw):
                pw = input("Please enter the password without a whitespace: ")
        current.password = pw
        current.save_profile(current.dsuserver)
    
    elif '-bio' in instruction:
        index = instruction.find('-bio')
        bio_join = ' '.join(option[index:])
        current.bio = bio_join
        current.save_profile(current.dsuserver)
    
    elif '-addpost' in instruction:
        index = instruction.find('-addpost')
        addpost_join = ' '.join(option[index:])
        while len(addpost_join) <= 2:
            addpost_join = input("The post should contain at least one letter. Enter again: ")
        make_post(addpost_join, current)
        current.save_profile(current.dsuserver)

    elif '-delpost' in instruction:
        num = option[-1]
        delete_post(num, current)
        current.save_profile(current.dsuserver)
    return current
        
    
def p_command(current, instruction):
    option = instruction.split()
    command = ['-usr', '-pwd', '-bio', '-posts', '-post', '-all']


    while option[1] not in command:
        instruction = input("The command does not exist. Please enter a correct command: ")
        option = 'P ' +instruction
        option = option.split()
    

    if '-usr' in instruction:
        print(f"username: {current.username}")

    if '-pwd' in instruction:
        print(f"password: {current.password}")
    
    if '-bio' in instruction:
        print(f"bio: {current.bio}")
    
    if '-posts' in instruction:
        num = 0
        posts = current.get_posts()
        if len(posts) == 0:
            print("EMPTY")
        else:
            for i in posts:
                print(f"{num}: {i}")
                num += 1
    
    elif '-post' in instruction:
        posts = current.get_posts()
        index_num = option[-1]
        print(f"{index_num}: {posts[int(index_num)]}")

    if '-all' in instruction:
        posts = current.get_posts()
        num = 0
        print(f"username: {current.username}")
        print(f"password: {current.password}")
        print(f"biography: {current.bio}")
        for i in posts:
            print(f"{num}: {i}")
            num += 1
    
    return current
     
def main():
    current = None
    while True:
        user_path = input()
        lst = user_path.split()

        if lst[0].upper() == 'C':
            current = c_command(lst[1], user_path)
        elif lst[0].upper() == 'O':
            current = o_command(lst[1])
        elif lst[0].upper() == 'E':
            e_command(current, user_path)
        elif lst[0].upper() == "P":
            p_command(current, user_path)
        elif lst[0].upper() == 'Q':
            exit()

if __name__ == '__main__':
    main()
