from array import array

arr1 = array('i', [2,4,3,5])

arr2 = arr1 # reference

arr3 = array(arr1.typecode, arr1.tolist()) # copy
arr4 = array(arr1.typecode, (n for n in arr1)) # copy, more effecient

arr1[3] = 1 # also change arr2[3]

print(arr1)
print(arr2)
print(arr3)
print(arr4)