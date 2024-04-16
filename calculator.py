# Working with Intergers 
# Aritmetic symbols include +, -, *, /, % and **

#  Addition 
# x = input("Enter value of x: ")
# y = input("Enter value of y: ")
# #  N/B User input values are always of type string
# #  Hence we need to convert them to integers
# z= int(x) + int(y)
# print(z)

# refactor 
# x = int(input("Enter value of x: "))
# y = int(input("Enter value of y: "))
# print(x + y)

# # subtractions
# a = x - y

# # multiplications
# b = x * y

# # divisions
# c = x / y

# # modulus
# d = x % y
# print(a, b, c, d)

# #  Working with floating point numbers
# k = float(input("Enter value of x: "))
# l = float(input("Enter value of y: "))
# print(k + l)

# # round to nearest integer
# z = round(k + l)
# print(z)

# # add a , to separate 000
# e = 999
# f = 1
# g = e + f
# print(f"{g:,}")  

# round to nearest a specific number of decimal places

h = 2.93456
i = h * 2345

#  1 way to round to a specific number of decimal places 3
j = round(h + i, 3)

print(j)
print(f"{j:.4f}")