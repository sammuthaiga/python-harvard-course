# def main():
#     x = get_int()
#     print(f"X is {x}")


# def get_int():
#     while True:
#         try:
#             x = int(input("Enter the value of x? "))
#         except ValueError:
#             print("X must be a integer")
#         else:
#             break
#     return x


# main()

# shorter version

def main():
    x = get_int()
    print(f"x is {x}")

def get_int():
    while True:
        try:
            return int(input(" What is x?  "))
        except ValueError:
            print("x must be an integer")

main()


