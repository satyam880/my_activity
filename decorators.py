#decoartors
import time
# 1. timing function


def toll(func):
    def wrapper():
        start=time.time()
        print("Before called")
        result=func()
        print("After called")
        end=time.time()
        print(f"{func.__name__} ran in {end-start}")
        return result
    return wrapper

@toll
def running_function():
    print("I am called")
    time.sleep(3)

running_function()

# running_function= toll(running_Function)

# 2. debug function



def debug(func):
    def wrapper(*args):
        args_value= (",").join(str(arg) for arg in args)
        print(f"calling {func.__name__} with {args_value}")

    return wrapper



@debug
def database(arg1,arg2):
    print("database is called")


database("mongodb","sql")