<<<<<<< HEAD
def square(x):
    return x*x

for i in range(11):
    print(f"Square of {i} is {square(i)}")
=======
def squares(x):
    return x*x

for i in range(11):
    print(f"Square of {i} is {squares(i)}")
>>>>>>> style

print("Executed")

#functions with many arguments
def addition(*num):
    return sum(num)

print(addition(1,2,3,4,5))

def show_info(**info):
    print(info)

show_info(name="Ali", age=22)
<<<<<<< HEAD
=======

def product (*num):
    result  = 1
    for i in num:
        result *= i
    return result

print(product(1,2,4))
>>>>>>> style
