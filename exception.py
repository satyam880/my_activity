try:
    print('Resource opened')
    x=int(input("Enter 1st number b/w 1 to 100->"))
    if(x<1 or x>100):
        raise ValueError("number must be b/w 1 to 100->")
    y=int(input("Enter 2nd number"))
    z=x/y
    print(f"division{z}")
except Exception as e:
    print(e)
finally:
    print("Resource closed")