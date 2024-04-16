# # use python (name of the file) hello.py to run code on the terminal


# # print function
# print("Hello, world!")

# # input function, variables, value assignment,
name = input("What is your name? ")
print(f"Hello {name}!")
# birth_year = float(input("Enter your year of birth: "))
# age = 2024 - birth_year
# concatination

# Pass 3 arguments to the print function
# print("your are", age, "years old")

#  Use the + operator to concatenate
#  Convert the age into a string
# print("your are " + str(age) + " years old")

#  Python 2 
#  Difference between raw_input(python2) and input(python3) functions

# input function, variables, value assignment,
# name = raw_input("What is your name? ")
# print("Hello, ", name, "!")
# print(name)

# embed expressions inside strings by prefixing the string with an f 
support = input("How can we assist you? ")
stack = input("Enter your tech stack: ")
print (f"Hi, your issue on {support} has been reviewed. Your knowledge in {stack} is really required here {name}!!")
