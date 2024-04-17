#  Working with return key word to return value from a function
def main():
    x = int(input("Enter the value of x: "))
    print("x squared is:", square(x))

def square(n):
    # one way to calculate the square of a number
    return n * n
    # 2nd way 
    return n ** 2
    # 3rd way
    return pow(n, 2)
main()