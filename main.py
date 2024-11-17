import sys
sys.stdin = open("./io/in.txt", "r")
sys.stdout = open("./io/out.txt", "wt")
def sqr(x):
  return(x**2)

def main():
  t=int(input())
  for _ in range(t):
    x=int(input())
    print(sqr(x))
main()
