#my original implementation:
a = int(input())
b = int(input())

print(a+b)
print(a-b)
print(a*b)

#alternative implementation:
a = int(input())
b = int(input())

print('{0} \n{1} \n{2}'.format((a + b), (a - b), (a * b)))