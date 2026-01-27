# # CLasses and Object
# from fontTools.misc.psLib import skipwhiteRE
#
#
# class car():
#     pass
# audi=car()
# bmw=car()
#
# print(audi,bmw)
#
# audi.window=4
# print(audi.window)
#
# tata=car()
# tata.doors=4
# print(tata.doors)
#
# print(dir(tata))
#
# # instance variable and method
# class dog():
#     ##contructor
#     def __init__(self,name,age,address):
#         self.name=name
#         self.age=age
#         self.address=address
# # create object
# dog1=dog("kaif",21,"sikar")
# print(dog1)
# print(dog1.name)
# print(dog1.age)
# print(dog1.address)
#
# dog2=dog1
# print(dog2.name)
# print(dog2.age)

# define a class with instance methods
class dog:
    def __init__(self,name,age):
        self.name=name
        self.age=age

    def bark(self):
        print(f"{self.name} says bhaoo bhaoo")

class cat:
    def __init__(self,name,age):
        self.name=name
        self.age=age

    def speak(self):
        print(f"{self.name} says meoww meowww")



dog1=dog("sheru",2)
dog1.bark()
dog2=dog("charlie",3)
dog2.bark()

cat1=cat("jinieee",1)
cat1.speak()
cat2=cat("miniee",1)
cat2.speak()


# modeling a bank account

# define a class for a bank account

class BankAccount:
    def __init__(self,accountholder,balance):
        self.accountholder=accountholder
        self.balance=balance

    def deposit(self,amount):
        self.balance+=amount
        print(f"{amount} is deposit.new balance is {self.balance}")

    def withdraw(self,amount):
        if amount>self.balance:
            print("insufficulent balance")
        else:
            self.balance-=amount
            print(f"{amount} is withdrawn. available balance is {self.balance}")

    def get_balance(self):
        return self.balance

# create an object

account=BankAccount("kaif chouhan",1000)
print(account.get_balance())
# call instance method
account.deposit(100)
print(account.get_balance())
account.withdraw(560)
print(account.get_balance())


