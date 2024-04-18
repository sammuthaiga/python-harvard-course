# while True:
#     n = int(input("Enter the value of n: "))
#     if n > 0:
#         break

# for i in range(n):
#     print("Hello")

def main():
    number = get_number()
    meow(number)

def get_number():
    while True:
         n= int(input("Enter value of n: "))
         if n > 0:
            return n
       

def meow(n):
    for _ in range(n):
        print("Hello")

main()