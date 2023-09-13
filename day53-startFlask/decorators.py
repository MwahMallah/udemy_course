import time

def timer(callback):
    def timer_inner(*args, **kwagrs):
        start = time.time()
        callback()
        elapsed = round((time.time() - start) * 1000)
        print(f"Function {callback.__name__} runned in {elapsed} ms")
    return timer_inner

@timer
def fast_function():
    for i in range(10000000):
        i * i
        
@timer
def slow_function():
    for i in range(100000000):
        i * i


fast_function()
slow_function()