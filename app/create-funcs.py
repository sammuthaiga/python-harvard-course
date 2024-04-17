#  Creating greetings functions in python
def main():
    name = input("What is your name? ")
    hello(name)
    greeting()

def hello(arg):
    print("Hello", arg)


# setting arguments to default values
def greeting(sal="world"):
    print("Greetings", sal)
   

main()

