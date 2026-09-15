# age=int(input("Enter your age: "))
#
# if age <=13:
#     print("You are a child")
# elif age > 13 and age <=18:
#     print("You are a teenager")
# elif age > 18:
#     print("You are adult")
# else:
#     print("print the valid number")


# password = "9660"
#
# user_pass = input("Enter password: ")
#
# if user_pass == password:
#     print("Welcome")
# else:
#     print("Wrong password")
#     print("Please enter again")
# number=int(input("Enter a number: "))
#
# if number % 5 ==0:
#     print('the number is divided by 5')
# else:
#     print('the number is NOT divided by 5')
#
#
# number=int(input("Enter a number: "))
#
# if number % 2 == 0:
#     print("Even")
# elif number % 2 == 1:
#     print("Odd")
# else:
#     print('error')

# a = int(input("enter first number: "))
# b = int(input("enter second number: "))
# c = int(input("enter third number: "))
#
# if a > b:
#     if a > c:
#         print(a)
#     else:
#         print(c)
#
# elif b > c:
#     if b > a:
#         print(b)
#     else:
#         print(a)
#
# else:
#     print(c)

# a = int(input("Enter a: "))
# b = int(input("Enter b: "))
# c = int(input("Enter c: "))
#
# if a<b:
#     if b>c:
#         print(b)
#     else:
#         print(c)
# else:
#     print(a)

# i=1
# while i<=5:
#     print(i)
#     i+=1
#
# i=5
# while i>=1:
#     print(i)
#     i-=1

#
# num=int(input("Enter a number: "))
#
# i=1
# while i<11:
#     print(num*i)
#     i=i+1

i=1
while i<21:
    if i%2==1:
        i+=1
        continue
    print(i)
    i+=1