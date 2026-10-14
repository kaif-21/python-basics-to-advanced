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
from Demos.win32ts_logoff_disconnected import username

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
# #     i=i+1
#
# i=1
# while i<21:
#     if i%2==1:
#         i+=1
#         continue
#     print(i)
#     i+=1

# word="artificial intelligence"
#
# for ch in word:
#     if ch in 'aeiou':
#         print(ch,'yes')
#
# n = int(input("Enter a number: "))
#
# sum = 0
#
# for i in range(1, n + 1):
#     sum = sum + i
#
# print("Sum =", sum)

# here are the 10 q for condition statements


# num=int(input("Enter a number"))
#
# if num<0:
#     print("negative number")
# elif num>=0:
#     print("positive number")
# else:
#     print('error')


# num=int(input("Enter a number"))

# if num%2==0:
#     print("Even")
# else:
#     print("Odd")

# age=int(input("Enter a age"))
#
# if age<=12:
#     print("child")
# elif age<=19:
#     print("teenager")
# elif age<=59:
#     print('adult')
# else:
#     print('senior citizen')


# a=int(input("enter a"))
# b=int(input("enter b"))
#
# if a>b :
#     print("a is greater than b")
# else:
#     print("b is greater than a")

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
#
# age=int(input("Enter a age"))
#
# if age>=18:
#     print('voting eligible')
# else:
#     print('voting not eligible')
#

# marks=int(input("enter no marks:"))
#
# if marks >= 90:
#     print("A")
# elif marks >= 80:
#     print("B")
# elif marks >= 70:
#     print("C")
# elif marks >= 60:
#     print("D")
# else:
#     print("F")

# num=int(input("Enter a number"))
#
# if num%5==0 and num%11==0:
#     print('5 aur 11 dono se divisible hai')
# elif num%5==0 and num%11!=0:
#     print('Sirf 5 se divisible hai')
# elif num%5!=0 and num%11==0:
#     print("Sirf 11 se divisible hai")
# else:
#     print("dono divisible nahi hai")

# num1=int(input("Enter a number"))
# num2=int(input("Enter a number"))
# operator=input(('choose any one operator(+,-,/,%)'))
#
# if operator=='+':
#     print(num1+num2)
#
# elif operator=='-':
#     print(num1,num2)
#
# elif operator=='/':
#     print(num1/num2)
# elif operator=='%':
#     print(num1%num2)
# else:
#     print("Operator not found")



# username='kaif'
# password='1234'
#
# username=input('Enter username: ')
# password=input('Enter password: ')
#
# if username=='kaif' and password=='1234':
#     print("login successful")
# elif username=='kaif' and password!='1234':
#     print("password doesn't match")
# elif username!='kaif' and password=='1234':
#     print('username doesn\'t match')
# else:
#     print("login failed")


# if-else and elif condition
age=int(input("enter your age"))

# if age>=18 and age<=40:
#     print("adult")
# elif age<=17 and age>=10:
#     print("teenager")
# elif age>=41:
#     print("old")
# else:
#     print("baby")

# nested condition
if age<=18 and age>=10:
    if age<=40:
        print("you are young")
    print("you are boy")
else:
    print("error")

