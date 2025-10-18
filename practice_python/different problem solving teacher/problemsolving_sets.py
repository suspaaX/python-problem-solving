'''1. Create a Set

Write a Python program to create a set.'''

# Create a new set:
# set()
# <class 'set'>

# Create a non empty set:
# {0, 1, 2, 3, 4}
# <class 'set'>

# Using a literal:
# <class 'set'>
# {1, 2, 3, 'bar', 'foo'}

a = set()
# print(a)

num1 = {0, 1, 2, 3, 4}
# print(type(num1))

num2 =  {1, 2, 3, 'bar', 'foo'}
# print(type(num2))

'''2. Iterate Over Sets

Write a Python program to iterate over sets.

Click me to see the sample solution'''


num_set = set([0, 1, 2, 3, 4, 5])

char_set = set("w3resource")

# for i in num_set:
#     print(i)

# for set in char_set:
#     print(set)


'''
3. Add Member(s) to a Set

Write a Python program to add member(s) to a set.

Click me to see the sample solution
'''

# set()

# Add single element:
# {'Red'}

# Add multiple items:
# {'Green', 'Red', 'Blue'}

elem = set()

lis1 = [{'Green', 'Red', 'Blue'}]

for i in lis1:
    elem.update(i)

# print(elem)



'''
4. Remove Item(s) from a Given Set

Write a Python program to remove item(s) from a given set.

Click me to see the sample solution
'''


# Original set:
set1 = {0, 1, 3, 4, 5}

# After removing all elements from the said set:
# set() 


# Original set:
set2 = {0, 1, 3, 4, 5}

# After removing the first element from the said set:
# {1, 3, 4, 5}


def all_item_remove(set1):
    set1.clear()
    print(set1)
    return

# all_item_remove(set1)

def one_item_remove(set1):
    set1.pop()
    print(set1)
    return

# one_item_remove(set2)

'''5. Remove an Item from a Set if Present

Write a Python program to remove an item from a set if it is present in the set.

Click me to see the sample solution'''

# Original set elements:
set1 = {0, 1, 2, 3, 4, 5}

# Remove 0 from the said set:
set2 = {0, 1, 2, 3, 5}

# Remove 5 from the said set:
set3 = {0, 1, 2, 3}

# Remove 2 from the said set:
set4 = {0, 1, 2, 3}

# Remove 7 from the said set:
set5 = {0, 1, 2, 3}

def remove_partcular(set1,elem):
    set1.discard(elem)
    print(set1)
    return

# remove_partcular(set1,0)
# remove_partcular(set2,0)
# remove_partcular(set3,5)
# remove_partcular(set4,2)
# remove_partcular(set5,7)


'''6. Create an Intersection of Sets

Write a Python program to create an intersection of sets.

Click me to see the sample solution'''


# Original set elements:
set1 = {'green', 'blue'}
set2 =  {'yellow', 'blue'}

# Intersection of two said sets:
# ['blue']

def intersection(set1,set2):
    intscn = set1.intersection(set2)
    print(intscn)
    
# intersection(set1,set2)

'''
7. Create a Union of Sets

Write a Python program to create a union of sets.

Click me to see the sample solution'''


# Original sets:
set1 = {'green', 'blue'}
set2 = {'blue', 'yellow'}

# Union of above sets:
# {'green', 'yellow', 'blue'}

# Original sets:
set3 = {1, 2, 3, 4, 5}
set4 = {1, 5, 6, 7, 8, 9}

# Union of above sets:
# {1, 2, 3, 4, 5, 6, 7, 8, 9}


def set_union(set1,set2):
    new_set = set1.union(set2)
    print(new_set)
    return

# set_union(set3,set4)


# 8. Create Set Difference

# Write a Python program to create set difference.

# Click me to see the sample solution

# Original sets:
set1= {'green', 'blue'}
set2 = {'yellow', 'blue'}

# Difference of setc1 - setc2:
# {'green'}

# Difference of setc2 - setc1:
# {'yellow'}

# Original sets:
set3 = {1, 2, 3, 4, 5}
set4 = {1, 5, 6, 7, 8, 9}

# Difference of setn1 - setn2:
# {2, 3, 4}

# Difference of setn2 - setn1:
# {8, 9, 6, 7} 


'''9. Create a Symmetric Difference

Write a Python program to create a symmetric difference.

Click me to see the sample solution
'''    
