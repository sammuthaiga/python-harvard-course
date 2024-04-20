# # Error handling using exceptions and else 
# try:
#     x = int(input("What is the value of x? "))
# except ValueError:
#     print("X is not an interger")
# else:
#     print(f"x ix {x}")

# include a loop to keep asking for value of x if user doesn't input an interger
while True:
     try:
            x = int(input("What is the values of X? "))
     except ValueError:
            print("Error! X is not an integer")
     else:
            break
      
print(f"X is {x}")
       
