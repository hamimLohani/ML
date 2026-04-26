
def add(num1=0, num2=0): # default argument
    return num1 + num2


def add(*num): # variable length argument (tuple)
    sum = 0
    for n in num:
        sum += n
    
    return sum

def person(name, age):
    print('name: ', name, ', age: ', age, sep="")


def special_person(**info): # keyword variable length arguments (dictionary)
    for key, value in info.items():
        print(key, ' : ', value)


special_person(name='hamim', age=21, height=5.6)
person(age=21, name='hamim') # keyword argument
print(add(2, 4,4))