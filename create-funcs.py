#  Creating greetings functions in python

def hello(arg):
    print("Hello", arg)

name = input("What is your name? ")
hello(name)

# setting arguments to default values
def greeting(sal="world"):
    print("Greetings", sal)

name = input("What is your name? ")
greeting(name)

