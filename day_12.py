# # exception handling
#
# try:
#     a=b
# except:
#     print("the variable has not been assigned")
#
# try:
#     a = b
# except NameError as ex:
#     print(ex)
#
# try:
#     result=1/0
# except ZeroDivisionError as ex:
#     print(ex)
#
# try:
#     number=int(input("Enter a number:"))
#     result=10/number
# except ValueError as ex:
#     print("this is not a valid number")
# except ZeroDivisionError:
#     print("enter denominator grater than zero ")
# except Exception as ex:
#     print(ex)
#
# # try,except,else block
# try:
#     num=int(input("Enter a number:"))
#     result=10/num
# except ValueError:
#     print("this is not a valid number")
# except ZeroDivisionError:
#     print("you can't divided by zero! ")
# else:
#     print(f"the resut is: {result}")
#
#
# # try,except,else block and finally
# try:
#     num=int(input("Enter a number:"))
#     result=10/num
# except ValueError:
#     print("this is not a valid number")
# except ZeroDivisionError:
#     print("you can't divided by zero! ")
# else:
#     print(f"the resut is: {result}")
# finally:
#     print("this is a final statement")

# file handling and exception handling

try:
    file=open("example.txt","r")
    content=file.read()
    print(content)
except FileNotFoundError:
    print("file not found")
finally:
    print("this is a final statement")
