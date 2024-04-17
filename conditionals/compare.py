#  Common comparison symbols include:
# >, >=, <, <=, ==, !=.
# x = int(input("Enter the value of x: "))
# y = int(input("Enter the value of y: "))

# if x < y:
#     print("X is les than Y")
# elif x > y:
#     print("X is greater than Y")
# else:
#     print(" X is equal to Y")

names = ["Sam", "Mary", "Brain", "Loise"]

passcode = input("Please enter your name: ").strip().capitalize()
for name in names:
    if passcode == names[0]:
        print(f"Hi,",{passcode}, "you are a developer.")
        break
    elif passcode == names[1]:
        print(f"Hi,",{passcode}, "you are an administrator.")
        break
    elif passcode == names[2]:
        print(f"Hi,",{passcode}, "you are a dentist.")
        break
    elif passcode == names[3]:
        print(f"Hi,",{passcode}, "you are the team leader.")
        break
    else:
        print("Kindly Sing up")
        break