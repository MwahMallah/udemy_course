def logging_decorator(callback):
    def wrapper(*args, **kwargs):
        print(f"You called {callback.__name__}{args}")
        print(f"It returned: {callback(*args)}")
    return wrapper

@logging_decorator
def a_function(*args):
    result = 1
    for arg in args:
        result *= arg
    return result


a_function(1, 2, 3)