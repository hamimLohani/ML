
def outer():
    print("outer func")

    def inner(num):
        print("inner func", num)
        return 5
    
    return inner

something = outer()
something(3)