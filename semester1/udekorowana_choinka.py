n = int(input("Podaj wysokosc choinki: "))

for i in range (1,n+1):
  for k in range(n-i,0,-1):
    print(" ", end="")
  for j in range(1,2*i):
    if i%2!=0: #nieparzyste
      if j ==1 or j == 2*i-1:
        print("!", end="")
      else:
        print("*", end="")
    else: #parzyste
        if (j-2>0 and (j-2)%4==0) or (j-2==0):
          print("o",end="")
        else:
          print("*",end="")
  print("")
