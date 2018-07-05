#Exercise 14
# List Remove Duplicates
# Write a program (function!) that takes a list and returns a new list that contains all the elements of the first list minus all the duplicates.
# Extras:
# Write two different functions to do this - one using a loop and constructing a list, and another using sets.
# Go back and do Exercise 5 using sets, and write the solution for that in a different function.
#My wrong answer
import random
list = random.sample(range(1, 100), 15)
new_list =[]
d_list = []
for i in list:
    if i.count() >= 2:
        d_list.append(i)

    elif i.count() == 1:
        new_list.append(i)
print("The duplicate list: ", d_list, "\n", "New_list is: ", new_list)
#AttributeError: 'int' object has no attribute 'count'

#The answer
def dedupe_v1(x):
  y = []
  for i in x:
    if i not in y:
      y.append(i)
  return y

#this one uses sets
def dedupe_v2(x):
    return list(set(x))

a = [1,2,3,4,3,2,1]
print(a)
print(dedupe_v1(a))
print(dedupe_v2(a))

#My new answer with set()
# The sets module provides classes for constructing and manipulating unordered collections of unique elements.
# Common uses include membership testing, removing duplicates from a sequence,
# and computing standard math operations on sets such as intersection, union, difference, and symmetric difference.
list = [1,2,4,6,9,7,7,7,5,3,3,2,1,1]
new_list =[]
d_list = []
for i in list:
    if i not in d_list:
        d_list.append(i)
    else:
        new_list.append(i)
print("The duplicate list: ", sorted(d_list), "\n", "New_list is: ", set(new_list))

#Extra Exercise
a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
print(sorted(b))
print(sorted(set(a) & set(b)))
print(sorted(set(a) | set(b)))

print((set(a)).sort())
AttributeError: 'set' object has no attribute 'sort'
