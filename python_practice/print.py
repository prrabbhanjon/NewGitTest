#! /usr/bin/python3

a=int(input("RangeFinal "))
print("Prime Numbers in the range")
for n in range(2, a):
   p=0
   for x in range(2, n):
        if n % x == 0:
                break
        else:
           if(p==0):
              print(n,end=' ')
              p=1
