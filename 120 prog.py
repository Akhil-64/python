print("natural numbers")
n=0
def exception1(n1):
  try:
    while True:
      print(n1)
      n1=n1+1
      if(n1>20):
        raise StopIteration
  except StopIteration:
    print("number exceeds limit")

exception1(n)
