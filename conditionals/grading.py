score = int(input("Enter your score for grading: "))

if score >= 90:
    print("You have an A!")
elif score >= 70:
    print("You have a B!")
elif score >= 60:
    print("You have a C!")
elif score >= 40:
    print("You have a D!")
elif score >= 20:
    print("You have a E!")
else:
    print("You have failed!")