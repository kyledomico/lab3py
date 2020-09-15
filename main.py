# Author: Kyle Domico kdd5262@psu.edu
# Collaborator: Travis Stauffer tcs5399@psu.edu
# Collaborator: Teya Davis tmd5681@psu.edu
# Collaborator: Shengyou Jiang sjj5492@psu.edu
# Section: 1
# Breakout: 2

def sum_n(n):
  total = 0
  if n < 0:
    return total
  else:
    total = n + sum_n(n-1)
  return total

def print_n(s,n):
  if n == 1:
    return print(s)
  elif n < 1:
    return
  else:
    print(s)
    print_n(s,n-1)
  return

def run():
  n = int(input("Enter an int: "))
  print(f"sum is {sum_n(n)}.")
  s = input("Enter a string: ")
  print_n(s,n)

if __name__ == "__main__":
  run()

    

