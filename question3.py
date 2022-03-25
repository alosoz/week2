#  3. Write a Python program that returns a dictionary which consists the unique elements 
#  in the following tuple as keys and the number of occurrences of elements as values.

from itertools import count
from re import X


tuple1 = (20, 10, 60, 70, 50, 20, 80, 20, 10, 20, 60, 60, 50)
list2 = list(tuple1)
#  print(list2)

list3 = []
list1 = []

for i in tuple1:
    if i not in list1:
        list1.append(i)
    else:
        pass


for x in list1:
    y = list2.count(x)
    list3.append(y)

print(list1)
print(list3)

dict = {}
dict2 = {}

for a in range(len(list3)):
    dict[list1[a]] = list3[a]

print(dict2)

# for key in list1:
#     for value in list3:
#         dict[key] = value
#         list3.remove(value)
#         break

#dict = {list1[z]: list3[z] for z in range(len(list1))}

print(dict)


