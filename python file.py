f = open("sample.txt", "r")

line_num = 1

for line in f:
    if "Python" in line:
        print(line)
        print(line_num)
    else:
        line_num+=1

f.close()



