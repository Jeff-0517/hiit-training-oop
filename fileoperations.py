# note = open("note.txt", "r")
# content = note.read()
# note.close()
# print (content)


import os
def create_file():
    """create a new file"""
    if os.path.exists(FILE_NAME): 
        print("filealready exists.")
    else:
        with open(FILE_NAME, "w") as file:
            print("file created successfully")




FILE_NAME = "student.text"

note = open("note.txt", "a")
note.write("Hi you are welcome")
note.close()


note = open("note.txt", "r")
content = note.read()
note. close()
# print(content)


def write_file():
    """write data to file (overwrite existing content)"""
    with open(FILE_Name, "W") as file:
        name = input("enter student name: ")
        age = input("enter student age: ")





