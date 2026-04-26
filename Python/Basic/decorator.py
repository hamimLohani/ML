# this is a decorator, it will take function, has an inner function
def greater(func):
    def wrap(a,b):
        if a<b:
            a,b = b,a
        return func(a,b)
    return wrap

def log(func): 
    def wrap(*a):
        print('values:', a)
        print('Result:', func(*a))
        return func(*a)
    return wrap

@log
def add(a,b):
    return a+b

@log
@greater # sub = greater(sub)
def sub(a,b):
    return a-b

@log
@greater # div = greater(div)
def div(a,b):
    return a/b

print(sub(2,4))
print(div(2,4))
add(2,3)