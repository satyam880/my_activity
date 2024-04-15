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
    def wrapper(*args,**kwargs):
        args_value= (",").join(str(arg) for arg in args)
        kw_args=  (',').join(f" {k}->{v}" for k,v in kwargs.items())
        print(f"calling {func.__name__} with args {args_value} and kwargs{kw_args}")
        result= func(*args,**kwargs)
        return result
    return wrapper



@debug
def database(name,description,use="development", db="database"):
    print("database is called")


database("mongodb", "sql", use="development", db="database")

