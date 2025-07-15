import time

def timer(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        print("Execution time:", time.time() - start)
        return result
    return wrapper

@timer
def slow_function():
    time.sleep(1)
    print("Function complete.")

slow_function()