def decorators(func):
    def wrapper():
        print("Before function runs")
        func()
        print("After function runs")
    return wrapper

@decorators
def say_hello():
    print("Hello World")

say_hello()