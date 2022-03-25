#  1. Write a Python program which executes following rules on this given 
# list => numbers = [2, 3, 5, 7, 11, 13, 17, 19]

numbers = [2, 3, 5, 7, 11, 13, 17, 19]

num = int(input("Write a number: "))

for x in range(num):
    y = numbers[0]
    numbers.remove(y)
    numbers.append(y)
print(numbers)
