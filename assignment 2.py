# -*- coding: utf-8 -*-
"""Empedded project.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1ywLstkWuwp-YhftP1gIg8hJ2cFgQNrL_

Assignment 2
"""

# 1. Write a Python program to add an item to a tuple.
# the code works in collab but not jupyter

x = ("Ahmed", "Adham", "Omar", "Sara")
print(x)

while True:
    item = input("Please enter your name: ").lower()
    y = list(x)
    y.append(item)
    x = tuple(y)
    print(x)

    choice = input("Want to add more? (y/n) ")

    if choice == "n":
        break
    elif choice == "y":
        pass
    else:
        print("Wrong input")
        break

#2. Write a Python program to sum all the items in a list.
sum = 0
list = [1 , 5 , 40 , 13]
for i in list:
 sum+=i
print(sum)

# 3. Write a Python program to multiply all the items in a list.
sum = 1
list = [1 , 5 , 40 , 13]
for i in list:
 sum *= i
print(sum)

# 4. Write a Python program to get the smallest number from a list.
list = [1 , 5 , 40 , 13]
minimum = min(list)
print("the samllest number is", minimum)

# 5. Write a Python program to get the largest number from a list.
list = [1 , 5 , 40 , 13]
maximum = max(list)
print("the bigger number is", maximum)

# 6. Write a Python program to count the number of strings from a given list of strings

#ctr = 0
x = [1, "apple", "banana", 5, "orange", "grape", "cherry"]
#for i in x:
result = len(x)
print("Number of strings in the list:", result)

# 7. Write a Python program to clone or copy a list
x = [1, "apple", "banana", 5, "orange", "grape", "cherry"]
y = []
for i in x:
    y.append(i)
print(y)

# 7. Write a Python program to clone or copy a list
x = [1, "apple", "banana", 5, "orange", "grape", "cherry"]
y = []
for i in x:
    y.append(i)
print(y)

# 8. Write a Python program to remove item(s) from a given set.

x = ["fruits" , "apple", "banana", "orange", "grape", "cherry"]
print(x)

while True:
    item = input("Please enter what you want to remove: ").lower()
    if item not in x:
        print("Error: The item is not in the list. Try again.")
    else:
        x.remove(item)
        print("Updated list:", x)

    choice = input("Want to remove more? (y/n) ")

    if choice.lower() == "n":
        break
    elif choice.lower() == "y":
        pass
    else:
        print("Wrong input")
        continue

# 9. Write a Python program to check if a set is a subset of another set.

x = {"a", "b", "c"}
y = {"f", "e", "d", "c", "b", "a"}

z = x.issubset(y)

print(z)

# 10. Write a Python program to remove all elements from a given set.

y = {"f", "e", "d", "c", "b", "a"}
print(y)
y.clear()
print("\nthe set after clearing: ", y)

# 11. Write a Python program to find the maximum and minimum values in a set.

set1 = {1 , 30 , 2.5 , 100 , 0.5 , 66}
max = max(set1)
min = min(set1)
print("the maximum number is" , max)
print("the minimum number is" , min)

# 12. Write a Python program to find the index of an item in a tuple.

x = ("apple", "banana", "orange", "grape", "cherry", "pear", "watermelon")

item = input("Enter the item you want to know its index: ")
if item not in x:
    print("Try again, wrong input")
else:
    I = x.index(item)
    print("The item's index is:", I)

# 13. Write a Python program to convert a tuple to a dictionary.

tuple1 = ((1 ,"apple" ), (2 , "banana"),( 3 , "orange") , (4 , "grape"), (5 , "cherry") , (6 , "pear"), (7 , "watermelon"))

D = dict((x,y) for x,y in tuple1)
print(D)

#14. Write a Python program to unzip a list of tuples into individual lists.

thelist = [(1 ,"apple", "cat"), (2 , "banana" ,"dog"),( 3 , "orange" , "elephant") , (4 , "grape", "lion"), (5 , "cherry" , "tiger") , (6 , "pear" , "penguin"), (7 , "watermelon" , "zebra")]
numbers , fruits , animals = zip(*thelist)
print(numbers)
print(fruits)
print(animals)

# 15. Write a Python program to reverse a tuple.


 tuple1 = ('z','a','d','f','g','e','e','k')
 tuple2 = tuple1[::-1]
print(tuple2)

# 16. Write a Python program to convert a list of tuples into a dictionary.


thelist = [(1 ,"apple"), (2 , "banana"),( 3 , "orange") , (4 , "grape"), (5 , "cherry") , (6 , "pear"), (7 , "watermelon")]
dict1 = {key: value for key, value in thelist}

print(dict1)

# 17. Write a Python program to replace the last value of tuples in a list.


lista = [(10, 20, 40), (40, 50, 60), (70, 80, 90)]
for i in lista:
  print(i[:-1] + (100,))

# 18. Write a Python program to sort a tuple by its float element.

float_tuple = (1.23, 3.14, 2.71, 0.987, 4.56)
tuple(sorted(float_tuple))