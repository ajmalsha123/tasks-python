array= [1,2,3,4,5,6,7,8,9];
print("Original array: ")
for i in range(0, len(array)):
    print(array[i])
print("Array in reverse order: ")
for i in range(len(array)-1, -1, -1):
    print(array[i])