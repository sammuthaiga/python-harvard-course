# create a function to immitate the column-block in super mario

def main():
    print_block(3)
    print_row(4)

# def print_block(height):
#     for _ in range(height):
#         print("##")
 
def print_block(height):
    print("##\n" * height, end="")

def print_row(width):
    print("?" * 4)
main()