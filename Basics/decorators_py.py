# first class objects

def say_hello(name):
    return f"Hello {name}"

def be_awesome(name):
    return f"Yo {name}, together we're the awesomest!"

def greet_bob(greeter_func):
    return greeter_func("Bob")

# inner function

def parent():
    print("Printing from parent()")

    def first_child():
        print("Printing from first_child()")

    def second_child():
        print("Printing from second_child()")

    second_child()
    first_child()

# functions as return values

def parent(num):
    def first_child():
        return "Hi! I'm Elias"
    def second_child():
        return "Hi! I'm Ester"

    if num == 1:
        return first_child
    else:
        return second_child
