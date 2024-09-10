
# Python Function Decoration
# @functools.wrap
# for name, items in function

#func return
# *args, **kwargs

#func print func



#function Example
#foo
#bar

def decorator(func):
    def wrapper():
        print("before")
        func()
        print("after")
    return wrapper()

def example():
    print ("lead by example")

def demonstrate_decorator_pattern() -> None:
    example2 = decorator(example)
    example2()
