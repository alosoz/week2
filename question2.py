#  2. Write a Python program that returns the following dictionary with sorted values. 
# NOTE: Dictonaries have keys and values. Here the values are lists. So, the returned dictonary 
# should have sorted values(list)

data = { 'a': [5, 3, 9, 0, 2, 3, 1], 'b': [4, 7, 5, 1, 2], 'c': [8, 1, 3, 2, 4] }

for key in data:
    value = data[key]
    value.sort()
    print(value)
    data[key]=value

print(data)
    
