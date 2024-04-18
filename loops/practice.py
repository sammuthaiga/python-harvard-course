#  More examples on continous loops
#  Hiring system if score is above 50.in progress though.[-_-] *[._.]*
def main():
  results = get_results()
  congraturate(results)


def get_results():
  while True:
    n = int(input("Enter your score: "))
    if n >= 50:
        return n
    else:
        print("Please try again after 10 minutes")
  
def congraturate(results):
  name = input("Whats your name? ").capitalize().split()
  candidates = ["sam", "ben", "cara", "mike"]
#   list iteratio
  for i in range(len(candidates)):
    print(f"congrats!, {name[i]}")
  



main()

