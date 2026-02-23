import os

file="passwords.txt"
#============================
#add passwords
#============================
def add_password():
    website=input("Enter your website name")
    username=input("Enter your username")
    password=input("Enter your password")
    with open(file,"a") as f:
        f.write(f"{website},{username},{password}\n")
    print("Password added successfully")

#=============================
#view password
#=============================
def view_password():
    if not os.path.exists(file):
        print("no password stored yet\n")
        return
    with open(file,"r") as f:
        lines=f.readlines()

        if len(lines) == 0:
            print("file is empty")
            return

    print("Password stored successfully")
    with open(file,'r')as f:
        for line in f:
            website,username,password =line.strip().split(",")
            print(f"website: {website},username: {username},password:{password}")
    print()
#===========================
#search password
#===========================
def search_password():
    if not os.path.exists(file):
        print("no password stored yet\n")
        return

    search_site=input("Enter your website name")

    with open(file,'r')as f:
        for line in f:
            website,username,password=line.strip().split(",")
            if website.lower()==search_site.lower():
                print(f"found-> username: {username}, password: {password}")
                return
    print("no record found")
#=============================
# delete password
#=============================
def delete_password():
    if not os.path.exists(file):
        print("no password stored yet\n")
        return

    delete_site=input("Enter your website name")
    found=False

    with open(file,'r')as f:
        lines=f.readlines()

    with (open(file,'w') as f):
        for line in lines:
            website,username,password=line.strip().split(",")
            if website.lower() != delete_site.lower():
                f.write(line)
            else:
                found=True
    if found:
        print("password deleted successfully")
    else:
        print("password not found")

#==================================
#main menu
#==================================
while True:
    print("Welcome to password manager")
    print("1. Add a new password")
    print("2. View a password")
    print("3. Search a password")
    print("4. Delete a password")
    print("5. Exit")


    choose=input("Enter your choice")

    if choose=="1":
        add_password()
    elif choose=="2":
        view_password()
    elif choose=="3":
        search_password()
    elif choose=="4":
        delete_password()
    elif choose=="5":
        print("Thank you for using password manager")
        break
    else:
        print("invalid choice")


