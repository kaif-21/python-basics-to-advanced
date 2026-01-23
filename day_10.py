# reading file
with open("example.csv","r") as file:
    for line in file:
        print(line.strip())  #strip() remove the new line charcter

# writing file (overwriting)
with open("example.csv","w") as file:
    file.write("hello kaif \nhow are you")
    file.write("\nthis is a new line")

# write a file (without overwriting)

with open("example.csv","a") as file:
    file.write("\nappend operation taking place!!\n")


# writing a list of line to a file
lines=["First line\n","second line\n","third line\n"]
with open("example.csv","a") as file:
    file.writelines(lines)


# binary file

# writing to a binary file
data=b'\x00\x01\x02\x03\x04'
with open("example.txt",'wb') as file:
    file.write(data)

# reading a binary file
with open("example.txt","rb") as file:
    content = file.read()
    print(content)

# read the content from source text file and write to a destination text file
with open("example.csv","r") as source_file:
    content = source_file.read()

with open("destination.csv","w")as destination_file:
    destination_file.write(content)



# writing and then reading a file

with open("example.csv","w+") as file:
    file.write("hello world\n")
    file.write("this is a new line \n")

#     move the curser to the beginning
    file.seek(0)

    #read the content of the file
    content = file.read()
    print(content)

