# create a function to immitate the column-block in super mario

def main():
    # print_block(3)
    # print_row(4)
    print_square(3)

#  Loop inside a loop.
# def print_square(size):
# print a row of size (3)
#     for i in range(size):
#  print a brick of size 3 in each row 3 times.
#         for j in range(size):
#             print("#", end="")
#  Print a new blank line which moves the cursor down the next line
#         print ()
#  Shorter way
def print_square(size):
    for i in range(size):
        print("#"  * size)












# def print_block(height):
#     for _ in range(height):
#         print("##")
 
# def print_block(height):
#     print("##\n" * height, end="")

# def print_row(width):
#     print("?" * 4)
main()