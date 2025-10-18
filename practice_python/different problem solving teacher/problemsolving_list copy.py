lis1 = [1, 2, 3, 4, 4]

lis2 = [1, 1, 1, 0, 0, 0, 2, -2, -2]

lis3 = [2, 2]

lis4 = [1]

Original_List  = [10, 20, 30, 40, 20, 50, 60, 40]    



# 1. Sum Items in List

lis1 = [0, 2,-8]


def sum_list(lis):
    sum = 0
    for i in lis:
        sum = sum+i
    print(sum)
    return

# sum_list(lis1)

# 2. Multiply Items in List

def mul_list(lis):
    mul = 1
    for i in lis:
        mul = mul*i
    print(mul)
    return

# mul_list(lis1)

# 3. Get Largest Number in List

def largest_num(lis):
    lis.sort()
    print(lis[-1])
    return

# largest_num(lis1)
    
# 4. Get Smallest Number in List

def smallest_num(lis):
    lis.sort()
    print(lis[0])
    return

# smallest_num(lis1)

# 5. Count Strings with Same Start and End

# Write a Python program to count the number of strings from a given list of strings. 
# The string length is 2 or more and the first and last characters are the same.

sample_list = ['12221','abc', 'xyz', 'aba', '1221']

# Expected Result : 2

def test_string(sample_list):
    test = []
    for elem in sample_list:
        if len(elem)>=3 and elem[0]==elem[-1]:
            test.append(elem)
        print(test)
        break
    return
    
# test_string(sample_list)

'''wrong answer'''


# 6. Sort Tuples by Last Element

# Write a Python program to get a list, 
# sorted in increasing order by the last element 
# in each tuple from a given list of non-empty tuples.

sample_list = [(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]

Expected_Result =[(2, 1), (1, 2), (2, 3), (4, 4), (2, 5)]


def sorted_tuple(sample_list):
    sample_list.sort()
    print(sample_list)
    return


# sorted_tuple(sample_list)

'''wrong answer'''

# 7. Remove Duplicates from List

# Write a Python program to remove duplicates from a list.


a = [10, 20, 30, 20, 10, 50, 60, 40, 80, 50, 40]


def remove_duplicate(a):
    a = set(a)
    b = [a]
    c = []
    for i in b:
        c.append(i)
    print(c)
    return

# remove_duplicate(a)



# 8. Check if List is Empty

# Write a Python program to check if a list is empty or not.

'''skip'''

# 9. Clone or Copy a List

# Write a Python program to clone or copy a list.
# Click me to see the sample solution

'''skip'''

# 12. Remove Specific Elements from List

# Write a Python program to print a specified list after removing the 0th, 4th and 5th elements.
sample_list = ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']
Expected_Output = ['Green', 'White', 'Black']


def remove_element(sample_list):
    new_list = []
    sample_list.pop(0)
    sample_list.pop(4)
    sample_list.pop(5)
    print(sample_list)
    return

# remove_element(sample_list)

# 13. Generate 3D Array

# Write a Python program to generate a 3*4*6 3D array whose each element is *.

'''skip'''

# 14. Remove Even Numbers from List

# Write a Python program to print the numbers of a specified list after removing even numbers from it.

num = [1, 2, 3, 2, 1, 5, 6, 4, 8, 5, 4]

def remove_even(num):

    new_list = []
    for i in num:
        i %2 == 0
        new_list.append(i)
    print(new_list)
    return
    
# remove_even(num)


# 15. Shuffle List

# Write a Python program to shuffle and print a specified list.

# def suffle_list(num):
#     suffle_list.random

'''skip'''

# 16. Generate Square Numbers in Range

# Write a Python program to generate and print a list of the first and 
# last 5 elements where the values are square numbers between 1 and 30 (both included).



# 27. Find Second Smallest Number in List

# Write a Python program to find the second smallest number in a list.

([2])
([1, 2, -8, -2, 0, -2])
([1, 1, 0, 0, 2, -2, -2])
([1, 1, 1, 0, 0, 0, 2, -2, -2])
([2, 2])

 # Edge case with two identical elements, returns None


# 28. Find Second Largest Number in List

''''Write a Python program to find the second largest number in a list.
Click me to see the sample solution'''

lis1 = [1, 2, 3, 4, 4]

lis2 = [1, 1, 1, 0, 0, 0, 2, -2, -2]

lis3 = [2, 2]

lis4 = [1]

def second_largest(lis1):
    lis1.sort()
    print(lis1[-2])
    return

# second_largest(lis4)


# 29. Get Unique Values from List

'''
Write a Python program to get unique values from a list.

'''
Original_List  = [10, 20, 30, 40, 20, 50, 60, 40]                                                             
List_of_unique_numbers =[40, 10, 50, 20, 60, 30]  


def unique_list(Original_List):
    new_list = set(Original_List)
    print("unique no from list:",new_list)
    return

# unique_list(Original_List)


# 30. Count Frequency of List Elements

'''Write a Python program to get the frequency of elements in a list.'''

Original_List = [10, 10, 10, 10, 20, 20, 20, 20, 40, 40, 50, 50, 30]                                         
# Frequency of the elements in the List :  Counter({10: 4, 20: 4, 40: 2, 50: 2, 30: 1})

def frequency_of_elements(Original_List):
    count_elem = {}
    for i in Original_List:
        ele = Original_List.count(i)
        count_elem.update({i:ele})
    print(count_elem)
    return

# frequency_of_elements(Original_List)

# 31. Count Elements in List Within Range

'''Write a Python program to count the number of elements in a list within a specified range.'''

list1 = [10, 20, 30, 40, 40, 40, 70, 80, 99]

list2 = ['a', 'b', 'c', 'd', 'e', 'f']

def count_element_range(list,a,b):
    min = int(a)
    max = int(b) 
    count = {}
    for i in range(min,max):
        count.update(i)
        


'''
32. Check if List Contains Sublist

Write a Python program to check whether a list contains a sublist.
Click me to see the sample solution
'''

pass

'''
33. Generate All Sublists

Write a Python program to generate all sublists of a list.
Click me to see the sample solution
'''

pass

'''
34. Compute Primes Using Sieve of Eratosthenes

Write a Python program that uses the Sieve of Eratosthenes method to compute prime numbers up to a specified number.
Note: In mathematics, the sieve of Eratosthenes, (Ancient Greek: κόσκινον Ἐρατοσθένους, kóskinon Eratosthénous) one of a number of prime number sieves, is a simple, ancient algorithm for finding all prime numbers up to any given limit.
Click me to see the sample solution
'''

pass

'''
35. Create List with Range Concatenation

Write a Python program to create a list by concatenating a given list with a range from 1 to n.
Sample list : ['p', 'q']
n =5
Sample Output : ['p1', 'q1', 'p2', 'q2', 'p3', 'q3', 'p4', 'q4', 'p5', 'q5']
'''
pass


'''
36. Get Variable ID or String

Write a Python program to get a variable with an identification number or string.
Click me to see the sample solution
'''

pass

'''
37. Find Common Items in Lists

Write a Python program to find common items in two lists.
Click me to see the sample solution
'''

pass

'''
38. Swap Every n-th and (n+1)th Values

Write a Python program to change the position of every n-th value to the (n+1)th in a list.
Sample list: [0,1,2,3,4,5]
Expected Output: [1, 0, 3, 2, 5, 4]
Click me to see the sample solutionPython Game Development


'''
pass

'''
39. Convert Integers List to Single Integer

Write a Python program to convert a list of multiple integers into a single integer.
Sample list: [11, 33, 50]
Expected Output: 113350
Click me to see the sample solution
'''

Sample_list = [1, 33, 50,5697,987]
# Expected_Output: 113350


def IntList_SinInt(Sample_list):
    for i in Sample_list:
        print(i,end='')
    return 


# (IntList_SinInt(Sample_list))



'''
40. Split List by First Character

Write a Python program to split a list based on the first character of a word.
Click me to see the sample solution
'''
pass

'''
41. Create Multiple Lists

Write a Python program to create multiple lists.
Click me to see the sample solution
'''


pass

'''
44. Generate Groups of Consecutive Numbers

Write a Python program to generate groups of five consecutive numbers in a list.
Click me to see the sample solution
'''

lis1 = [4, 5, 6, 7, 8, 1, 2, 3,1, 2, 4, 8, 16, 32, 64]

# def list_of_five(list1):
#     new_list = [[i]*5 for i in list1]
#     return new_list

# print(list_of_five(lis1))

'''
46. Select Odd Items from List

Write a Python program to select the odd items from a list.
Click me to see the sample solution
'''

lis1 = [4, 5, 6, 7, 8, 1, 2, 3,1, 2, 4, 8, 16, 32, 64]

def odd_list(lis1):
    new_list = []
    for i in range(1,len(lis1)+1):
        ny = i
        print(ny)
    return

# (odd_list(lis1))


#print 1 -100 all odd

'''47. Insert Element Before Each List Item

Write a Python program to insert an element before each element of a list.
Click me to see the sample solution

'''
lis1 =   ['Red', 'Green', 'Black']
elem = 'c'


def insert_element(lis1,elem):
    new_list = []
    for i in lis1:
        new_list.append([elem]+[i])
    return new_list
    
# print(insert_element(lis1,elem))

'''
52. Difference Between Two Lists

Write a Python program to compute the difference between two lists.
Sample data: ["red", "orange", "green", "blue", "white"], ["black", "yellow", "green", "blue"]
Expected Output:
Color1-Color2: ['white', 'orange', 'red']
Color2-Color1: ['black', 'yellow']
Click me to see the sample solution
'''

lis1 =  ["red", "orange", "green", "blue", "white"]
lis2 = ["black", "yellow", "green", "blue"]

set3 =set()
for i in lis1:
    set3.add(i)

set4 = set()
for i in lis2:
    set4.add(i)

# print(set3.difference(set4))
# print(set4.difference(set3))

'''
53. Create List with Infinite Elements

Write a Python program to create a list with infinite elements.
Click me to see the sample solution
'''


def infinite_elements(*num):
    new_lis1 = []
    new_lis1.append(num)
    return new_lis1


# print(infinite_elements(1,4,5,57,9845,4))


'''

54. Concatenate List Elements

Write a Python program to concatenate elements of a list.
Click me to see the sample solution

'''

color = ['red', 'green', 'orange']

def Concatenate_List(color):
    new_elem = str()
    for elem in color:
        new_elem.join(elem)
        return new_elem
    

print(Concatenate_List(color))


'''
55. Remove Key-Value Pairs from Dictionaries in List


Write a Python program to remove key-value pairs from a list of dictionaries.
Click me to see the sample solution
'''

original_list = [{'key1': 'value1', 'key2': 'value2'}, {'key1': 'value3', 'key2': 'value4'}]

def remove_keyvalue(original_list):
    pass

'''
56. Convert String to List

Write a Python program to convert a string to a list.
Click me to see the sample solution
'''

color = "['Red', 'Green', 'White']"

def Str_to_Lis(color):
    pass

'''57. Check All Strings Match Given String

Write a Python program to check if all items in a given list of strings are equal to a given string.
Click me to see the sample solution
'''

color1 = ["green", "orange", "black", "white"]

color2 = ["green", "green", "green", "green"]

