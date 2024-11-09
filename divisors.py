import sys

numbers = int(sys.argv[1])

for i in range(1, numbers+1):
  if numbers % i:
    print(i, end=" ")

print()
