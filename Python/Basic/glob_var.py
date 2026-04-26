a = 10

def something():
    globals()['a'] = 20
    a = 15
    print('inside :', a)


something()
print('outside :', a)