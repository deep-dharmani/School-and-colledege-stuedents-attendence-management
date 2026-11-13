import os
school_password="2283"
stuedent_password="5436"
def add_stuedent():
    print("Enter school password")
    password=get_input(4)
    if password==school_password:
        times=" "
        while True:
            name=input(f"Enter{times}stuedent name: ")
            surname=input(f"Enter surname of {name}: ")
            Id=input(f"Enter {name}'s id no: ")
            class_=input(f"Enter class: ")
            joined=input(f"on which date {name} joined: ")
            times=" another "
            info=f">>{name} {surname}\n>id:\n{" "*len("id:"),Id}\n>class:{" "*len("class:"),class_}\n>date of\
joined:{" "*len(">date of joined:"),joined}\n>>attedence:"
            folder=r"C:\\Users\\hp\\Desktop\\school & colledge stuedents management\\stuedent_info"
            class_folder = os.path.join(folder, class_)
            os.makedirs(class_folder, exist_ok=True)
            file_path = os.path.join(class_folder, f"{Id}.md")
            with open(file_path,"x",encoding="utf-8") as file:
                write=file.write(info)
                print(write)            
    else:
        print(f"wrong password is entered:{password}")
def daily_attendence():
    print("Enter school password")
    password=get_input(4)
    if password==school_password:
        date=input("Enter todays date :  ")
        while True:
            class_=input("Enter class name: ")
            I_d=input("Enter stuedent id  :")
            print("Enter 1 for full attend")
            print("Enter 2 for half attend")
            attend=get_input(1)
            folder=r"C:\\Users\\hp\\Desktop\\school & colledge stuedents management\\stuedent_info"
            class_folder = os.path.join(folder, class_)
            file_path = os.path.join(class_folder, f"{I_d}.md")
            if os.path.exists(file_path):
                match attend:
                    case "1":
                        with open(file_path,"a") as file:
                            write=file.write(f"\n>{date}:Full Attend")
                            print(write)
                    case "2":
                        with open(file_path,"a") as file:
                            write=file.write(f"\n>{date}:Half Attend")
                            print(write)
                    case _:
                        print("Enter right attend method")
            else:
                print(f"class: {class_}")
                print(f"Id:     {I_d}")
                print("something went wrong")
    else:
        print(f"wrong password is entered:{password}")
def all_stuedents():
    password_=input("Enter stuedent password: ")
    if password_==stuedent_password:
        class_=input("Enter class: ")
        i_d_=input("Enter stuedent:")
        try:
            folder=r"C:\\Users\\hp\\Desktop\\school & colledge stuedents management\\stuedent_info"
            class_folder = os.path.join(folder, class_)
            file_path = os.path.join(class_folder, f"{i_d_}.md")
            with open(file_path,"r") as file:
                read_=file.read()
                print(read_) 
        except:
            print(f"class:{class_}")
            print(f"id:{i_d_}")
            print("something is given wrong")          
    else:
        print("wrong password")
import msvcrt
def get_input(length):
    text = ""
    while len(text) < length:
        char = msvcrt.getwch()
        if char == "\r":
            break
        print(char, end="", flush=True)
        text += char
    print()
    return text
print("Enter 1 for Add a new student")
print("Enter 2 for daily Attendence")
print("Enter 3 for checking stuendent details")
work=get_input(1)
match work:
    case"1":
        add_stuedent()
    case"2":
        daily_attendence()
    case"3":
        all_stuedents()
    case _:
        print(f"{work} is invalid key.")