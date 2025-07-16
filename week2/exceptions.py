import sys

try:
    x = int(input("x:"))
    y = int(input("y:"))
except ValueError:
    print("You are a dick!")
    sys.exit(1)

try:
    result = x/y
except ZeroDivisionError:
    print("Dickhead!")
    sys.exit(1)



print(f"{x}/{y} = {result}")