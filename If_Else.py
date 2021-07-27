#!/bin/python3
# my original implementation:
N = int(input())

if N % 2 != 0:
    print('Weird')
elif N % 2 == 0 and (N >= 2 and N <= 5):
    print('Not Weird')
elif N % 2 == 0 and (N >= 6 and N <= 20):
    print('Weird')
elif N % 2 == 0 and N > 20:
    print('Not Weird')

# alternative implementation:
n = int(input().strip())
check = {True: "Not Weird", False: "Weird"}

print(check[
          n % 2 == 0 and (
                  n in range(2, 6) or
                  n > 20)
          ])
