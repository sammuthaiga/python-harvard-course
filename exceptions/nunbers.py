# Error handling using exceptions and else 
try:
    x = int(input("What is the value of x? "))
except ValueError:
    print("X is not an interger")
else:
    print(f"x ix {x}")
