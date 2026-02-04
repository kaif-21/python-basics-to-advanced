#Custom exception (Rise and Throw an exception)
class Error(Exception):
    pass

class dobException(Error):
    pass

year=int(input("Enter the dob"))
age=2024-year
try:
    if age<=30 and age>=18:
        print("the age is valid so you can apply for the exam")
    else:
        raise dobException
except dobException:
    print("the age is invalid so you cannot apply for the exam")


