
def squre(num):
    return num * num

def cube(num):
    return num * num * num

def operate(num, operation):
    return operation(num)

def sp_operate(nums, operation):
    for i in nums:
        print(operation(i))

print(operate(5, cube))

sp_operate([1,2,3,4], cube)