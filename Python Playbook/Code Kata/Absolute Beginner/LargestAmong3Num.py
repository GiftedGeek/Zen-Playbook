A=int(input())
B=int(input())
C=int(input())

if(A>B) and (B>C):
  print(A)
elif(B>C) and (B>A):
    print(B)
else:
    print(C)
