'https://www.w3resource.com/python-exercises/list/'


'''
# 1. Sum Items in List
'''

lis1 = [0, 2,-8]

def sum_list(lis):
    sum = 0
    for i in lis:
        sum = sum+i
    print(sum)
    return

# sum_list(lis1)

'''
2. Multiply Items in List
'''


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



'''
58. Replace Last Element with Another List

Write a Python program to replace the last element in a list with another list.
Sample data : [1, 3, 5, 7, 9, 10], [2, 4, 6, 8]
Expected Output: [1, 3, 5, 7, 9, 2, 4, 6, 8]
Click me to see the sample solution

'''


lis1 = [1, 3, 5, 7, 9, 10] 
lis2 = [2, 4, 6, 8]
# Expected Output: [1, 3, 5, 7, 9, 2, 4, 6, 8]

def replace_list(lis1,lis2):
    nw_list = []
    m = lis1.pop(-1)
    m.extend(lis2)
    print(m)


# replace_list(lis1,lis2)

'''
59. Check if N-th Element Exists in List

Write a Python program to check whether the n-th element exists in a given list.
Click me to see the sample solution
'''

x = [1, 2, 3, 4, 5, 6]


'''
60. Smallest Second Index Tuple

Write a Python program to find a tuple, the smallest second index value from a list of tuples.
Click me to see the sample solution
'''
pass

'''
61. Create List of Empty Dictionaries

Write a Python program to create a list of empty dictionaries.
Click me to see the sample solution

'''

n = 5

def List_of_Empty_Dictionaries(n):
    my_list = [{}]
    # my_list.append(n)
    for i in range(1,n+1):
        my_list.append(n)
    return my_list

# print(List_of_Empty_Dictionaries(n))



'''
62. Print Space-Separated List Elements

Write a Python program to print a list of space-separated elements.
Click me to see the sample solution


'''
lis = [1,3,5,7,9,10] 

def Space_Separated(lis):
    new_lis = []
    for i in lis:
        new_lis.append(i)
    print(new_lis,end='  ')
        # return 
pass
# Space_Separated(lis)


'''
63. Insert String Before List Items

Write a Python program to insert a given string at the beginning of all items in a list.
Sample list : [1,2,3,4], string : emp
Expected output : ['emp1', 'emp2', 'emp3', 'emp4']
Click me to see the sample solution

'''
lis1 = [1,2,3,4]
item = 'emp'
Expected_output = ['emp1', 'emp2', 'emp3', 'emp4']


def String_Before_List(lis1,item):
    new_lis = []
    for i in lis1:
        j = item+str(i)
        new_lis.append(j)
    print(new_lis)
    return

# String_Before_List(lis1,item)

'''
64. Iterate Over Two Lists Simultaneously

Write a Python program to iterate over two lists simultaneously.
Click me to see the sample solution
'''

lis1 = [1,2,3,4]

lis2 = ['emp1', 'emp2', 'emp3', 'emp4']


def Iterate_Two_Lists(lis1,lis2):
    for i,j in zip(lis1,lis2):
        print(i,j)
    return


# Iterate_Two_Lists(lis1,lis2)


'''
65. Move Zeros to End of List

Write a Python program to move all zero digits to the end of a given list of numbers.
Expected output:
Original list:
[3, 4, 0, 0, 0, 6, 2, 0, 6, 7, 6, 0, 0, 0, 9, 10, 7, 4, 4, 5, 3, 0, 0, 2, 9, 7, 1]
Move all zero digits to end of the said list of numbers:
[3, 4, 6, 2, 6, 7, 6, 9, 10, 7, 4, 4, 5, 3, 2, 9, 7, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0]
Click me to see the sample solutionPython programming course

'''


lis1 = [3, 4, 0, 0, 0, 6, 2, 0, 6, 7, 6, 0, 0, 0, 9, 10, 7, 4, 4, 5, 3, 0, 0, 2, 9, 7, 1]

Expected_Output = [3, 4, 6, 2, 6, 7, 6, 9, 10, 7, 4, 4, 5, 3, 2, 9, 7, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0]


def Zeros_to_End(lis1):
    nw_lis = []
    new_lis2 = []
    result = []
    for i in lis1:
        if '0' == str(i):
            nw_lis.append(i)
        else :
            new_lis2.append(i)
    new_lis2.extend(nw_lis)
    print(new_lis2)
    return
    
# Zeros_to_End(lis1)

'''
66. Find List with Highest Sum

Write a Python program to find the list in a list of lists whose sum of elements is the highest.
Sample lists: [1,2,3], [4,5,6], [10,11,12], [7,8,9]
Expected Output: [10, 11, 12]
Click me to see the sample solution

'''
lis1 = [1,2,3], [4,5,6], [10,11,12], [7,8,9]
nw_lis1 = []
nw_lis1.append(lis1)

# def HighestSum(nw_lis1):
#     sum = 0
#     for i in nw_lis1:
#         print(i)
#     #     sum = sum+i
#     # print(sum)
#     return

# HighestSum(lis1)

pass


'''
67. Find Values Greater Than Specified Number

Write a Python program to find all the values in a list that are greater than a specified number.
Click me to see the sample solution
'''

num = 25

lis1 = [10,26,12]


def greater_specifiednumber(num,lis1):
    for i in lis1:
        if i<num:
            print(True)
        else:
            print(False)
    return


# greater_specifiednumber(num,lis1)


'''
69. Remove Duplicates from List of Lists

Write a Python program to remove duplicates from a list of lists.
Sample list : [[10, 20], [40], [30, 56, 25], [10, 20], [33], [40]]
New List : [[10, 20], [30, 56, 25], [33], [40]]
Click me to see the sample solution

'''
sample_list = [[10, 20], [40], [30, 56, 25], [10, 20], [33], [40]]
list = [[10, 20], [30, 56, 25], [33], [40]]

def remove_Duplicates_Lists(sample_list):
    nw_list = set(sample_list)
    print(nw_list)
    # nw_list = []
    # for i in sample_list:
    #     print(i)
    # sample_list.sort()
    # print(sample_list)
    return 

# remove_Duplicates_Lists(sample_list)

'''
70. Find Items Starting with Specific Character

Write a Python program to find items starting with a specific character from a list.
Expected Output:
Original list:
['abcd', 'abc', 'bcd', 'bkie', 'cder', 'cdsw', 'sdfsd', 'dagfa', 'acjd']
Items start with a from the said list:
['abcd', 'abc', 'acjd']
Items start with d from the said list:
['dagfa']
Items start with w from the said list:
[]
Click me to see the sample solution

'''

Original_list = ['abcd', 'abc', 'bcd', 'bkie', 'cder', 'cdsw', 'sdfsd', 'dagfa', 'acjd']
elem = 'a'

'''
Items start with a from the said list:
['abcd', 'abc', 'acjd']
Items start with d from the said list:
['dagfa']
Items start with w from the said list:
[]
Click me to see the sample solution

'''

def Starting_Specific_Character(Original_list,elem):
    nw_list = []
    for i in Original_list:
        if elem == i.startswith(elem):
            nw_list.append(i)
    print(nw_list)
    return 

# Starting_Specific_Character(Original_list,elem)

    
'''
72. Remove all except specified character.

Write a Python program to remove all characters except a specified character from a given string.
Original string
Python Exercises
Remove all characters except P in the said string:
P
Original string
google
Remove all characters except g in the said string:
gg
Original string
exercises
Remove all characters except e in the said string:
eee
Click me to see the sample solution
'''
pass
'''
73. Count uppercase, lowercase, special, numeric.

Write a Python program to count Uppercase, Lowercase, special characters and numeric values in a given string.
Click me to see the sample solution
'''
str1 = '@W3Resource.Com'

# def count_string(str1):
#     new_lis = []

#     for i in str1:
#         new_lis.append(i)
#         if  i == 'A' :
#     return

# count_string(str1)
    

































'''
74. Minimum window with all chars of another string.

Write a Python program to find the minimum window in a given string that will contain all the characters of another given string.
Example 1
Input : str1 = " PRWSOERIUSFK "
str2 = " OSU "
Output: Minimum window is "OERIUS"

'''


pass



'''
76. Create Modified Run-Length Encoded List

Write a Python program to create a list reflecting the modified run-length encoding from a given list of 
integers or a given list of characters.
Original list:
[1, 1, 2, 3, 4, 4, 5, 1]
List reflecting the modified run-length encoding from the said list:
[[2, 1], 2, 3, [2, 4], 5, 1]
Original String:
aabcddddadnss
List reflecting the modified run-length encoding from the said string:
[[2, 'a'], 'b', 'c', [4, 'd'], 'a', 'd', 'n', [2, 's']]
Click me to see the sample solution
'''

pass

'''
78. Split List into Two Parts by Length

Write a Python program to split a given list into two parts where the length of the first part of the list is given.
Original list:
[1, 1, 2, 3, 4, 4, 5, 1]
Length of the first part of the list: 3
Splited the said list into two parts:
([1, 1, 2], [3, 4, 4, 5, 1])
Click me to see the sample solution


'''
pass

'''
79. Remove K-th Element from List

Write a Python program to remove the K'th element from a given list, and print the updated list.
Original list:
[1, 1, 2, 3, 4, 4, 5, 1]
After removing an element at the kth position of the said list:
[1, 1, 3, 4, 4, 5, 1]
Click me to see the sample solution

'''

# lis1 = [1, 1, 2, 3, 4, 4, 5, 1]

# def k_elem(lis1):
#     for i in lis1:

'''

80. Insert Element at Specified Position

Write a Python program to insert an element at a specified position into a given list.
Original list:
[1, 1, 2, 3, 4, 4, 5, 1]
After inserting an element at kth position in the said list:
[1, 1, 12, 2, 3, 4, 4, 5, 1]
Click me to see the sample solution      
'''


























'''
81. Extract Random Elements from List

Write a Python program to extract a given number of randomly selected elements from a given list.
Original list:
[1, 1, 2, 3, 4, 4, 5, 1]
Selected 3 random numbers of the above list:
[4, 4, 1]
Click me to see the sample solution
'''

lis1 = [1, 1, 2, 3, 4, 4, 5, 1]

def Random_Elements_from_List(lis1):
    import random
    for i in lis1:
        j = random.random()
        print(j)
    return
    

# Random_Elements_from_List(lis1)

















'''
82. Generate Combinations from List

Write a Python program to generate combinations of n distinct objects taken from the elements of a given list.
Original list: [1, 2, 3, 4, 5, 6, 7, 8, 9] Combinations of 2 distinct objects: [1, 2] [1, 3] [1, 4] [1, 5] .... [7, 8] [7, 9] [8, 9]
Click me to see the sample solution
'''

'''
83. Round Numbers and Calculate Total Sum

Write a Python program to round every number in a given list of numbers and print the total sum multiplied by the length of the list.
Original list: [22.4, 4.0, -16.22, -9.1, 11.0, -12.22, 14.2, -5.2, 17.5]
Result:
243
Click me to see the sample solution

'''
lis1 =  [22.4, 4.0, -16.22, -9.1, 11.0, -12.22, 14.2, -5.2, 17.5]

def Round_Numbers_Calculate_Sum (lis1):
    sum = 0
    for i in lis1:
        k = round(i*len(lis1))
        sum = k+sum
    print(sum)
    return

# Round_Numbers_Calculate_Sum(lis1)




















'''
84. Round Numbers, Find Min/Max, Multiply by 5

Write a Python program to round the numbers in a given list, print the minimum and maximum numbers and 
multiply the numbers by 5. Print the unique numbers in ascending order separated by space.
Original list: [22.4, 4.0, 16.22, 9.1, 11.0, 12.22, 14.2, 5.2, 17.5]
Minimum value: 4
Maximum value: 22
Result:
20 25 45 55 60 70 80 90 110
Click me to see the sample solution
'''

lis1 = [22.4, 4.0, 16.22, 9.1, 11.0, 12.22, 14.2, 5.2, 17.5]

def min_max(lis1):
    nw_lis1 = []
    for i in lis1:
        k = round(i)

        nw_lis1.append(k)
    nw_lis1.sort()
    print(f"minimum and maximum numbers",nw_lis1[0],nw_lis1[-1])
    print(nw_lis1)
    return

# min_max(lis1)























'''
85. Create Multidimensional List with Zeros

Write a Python program to create a multidimensional list (lists of lists) with zeros.
Multidimensional list: [[0, 0], [0, 0], [0, 0]]
Click me to see the sample solutionBackend development course


'''


pass




#86-90

'''

86. Create 3x3 Grid with Numbers

Write a Python program to create a 3X3 grid with numbers.
3X3 grid with numbers:
[[1, 2, 3], [1, 2, 3], [1, 2, 3]]
Click me to see the sample solution
'''


num1 = 11
num2 =12
num3 = 13

def grid_3X3(num1,num2,num3):
    new_lis =[]
    pass


'''
90. Count Lists in Nested List

Write a Python program to count the number of lists in a given list of lists.
Original list:
[[1, 3], [5, 7], [9, 11], [13, 15, 17]]
Number of lists in said list of lists:
4
Original list:
[[2, 4], [[6, 8], [4, 5, 8]], [10, 12, 14]]
Number of lists in said list of lists:
3
Click me to see the sample solution
'''



'''
89. Zip Two Lists of Lists

Write a Python program to Zip two given lists of lists.
Original lists:
[[1, 3], [5, 7], [9, 11]]
[[2, 4], [6, 8], [10, 12, 14]]
Zipped list:
[[1, 3, 2, 4], [5, 7, 6, 8], [9, 11, 10, 12, 14]]
Click me to see the sample solution

'''

lis1 = [[1, 3], [5, 7], [9, 11]]
lis2 = [[2, 4], [6, 8], [10, 12, 14]]

final_lis = [[1, 3, 2, 4], [5, 7, 6, 8], [9, 11, 10, 12, 14]]


def zip_list(lis1,lis2):
    lis1[0].extend(lis2[0])
    lis1[1].extend(lis2[1])
    lis1[2].extend(lis2[2])

    print(lis1)
    return


# zip_list(lis1,lis2)


#91-95

'''
91. Find List with Max and Min Lengths

Write a Python program to find a list with maximum and minimum lengths.
Original list:
[[0], [1, 3], [5, 7], [9, 11], [13, 15, 17]]
List with maximum length of lists:
(3, [13, 15, 17])
List with minimum length of lists:
(1, [0])
Original list:
[[0], [1, 3], [5, 7], [9, 11], [3, 5, 7]]
List with maximum length of lists:
(3, [3, 5, 7])
List with minimum length of lists:
(1, [0])
Original list:
[[12], [1, 3], [1, 34, 5, 7], [9, 11], [3, 5, 7]]
List with maximum length of lists:
(4, [1, 34, 5, 7])
List with minimum length of lists:
(1, [12])
Click me to see the sample solution
'''
# Original list:
# [[0], [1, 3], [5, 7], [9, 11], [13, 15, 17]]
# List with maximum length of lists:
# (3, [13, 15, 17])
# List with minimum length of lists:
# (1, [0])

lis1 = [[0], [1, 3], [5, 7], [9, 11], [13, 15, 17]]
def Max_Min_Lengths(lis1):
    nw_lis = []
    for i in lis1:
        nw_lis.append(len(i))
    print(nw_lis)
    # print(max(nw_lis))

    return

# Max_Min_Lengths(lis1)

'''
92. Check if Nested List Is Subset

Write a Python program to check if a nested list is a subset of another nested list.
Original list:
[[1, 3], [5, 7], [9, 11], [13, 15, 17]]
[[1, 3], [13, 15, 17]]
If the one of the said list is a subset of another.:
True
Original list:
[[[1, 2], [2, 3]], [[3, 4], [5, 6]]]
[[[3, 4], [5, 6]]]
If the one of the said list is a subset of another.:
True
Original list:
[[[1, 2], [2, 3]], [[3, 4], [5, 7]]]
[[[3, 4], [5, 6]]]
If the one of the said list is a subset of another.:
False

'''

pass

'''
93. Count Sublists Containing Element

Write a Python program to count the number of sublists that contain a particular element.
Original list:
[[1, 3], [5, 7], [1, 11], [1, 15, 7]]
Count 1 in the said list:
3
Count 7 in the said list:
2
Original list:
[['A', 'B'], ['A', 'C'], ['A', 'D', 'E'], ['B', 'C', 'D']]
Count 'A' in the said list:
3
Count 'E' in the said list:
1
Click me to see the sample solution


'''

pass

'''
94. Count Unique Sublists in List

Write a Python program to count the number of unique sublists within a given list.
Original list:
[[1, 3], [5, 7], [1, 3], [13, 15, 17], [5, 7], [9, 11]]
Number of unique lists of the said list:
{(1, 3): 2, (5, 7): 2, (13, 15, 17): 1, (9, 11): 1}
Original list:
[['green', 'orange'], ['black'], ['green', 'orange'], ['white']]
Number of unique lists of the said list:
{('green', 'orange'): 2, ('black',): 1, ('white',): 1}
Click me to see the sample solution

'''
pass


'''
95. Sort Strings in Sublists

Write a Python program to sort each sublist of strings in a given list of lists.
Original list:
[[2], [0], [1, 3], [0, 7], [9, 11], [13, 15, 17]]
Sort the list of lists by length and value:
[[0], [2], [0, 7], [1, 3], [9, 11], [13, 15, 17]]
Click me to see the sample solution
'''


lis1 = [[2], [0], [1, 3], [0, 7], [9, 11], [13, 15, 17]]
# [[0], [2], [0, 7], [1, 3], [9, 11], [13, 15, 17]]

def Sort_Strings(lis1):
    lis1.sort()
    print(lis1)
    return

# Sort_Strings(lis1)


'''96. Sort List of Lists by Length and Value

Write a Python program to sort a given list of lists by length and value.
Original list:
[[2], [0], [1, 3], [0, 7], [9, 11], [13, 15, 17]]
Sort the list of lists by length and value:
[[0], [2], [0, 7], [1, 3], [9, 11], [13, 15, 17]]
Click me to see the sample solution

'''

lis1 = [[2], [0], [1, 3], [0, 7], [9, 11], [13, 15, 17]]

ot = [[0], [2], [0, 7], [1, 3], [9, 11], [13, 15, 17]]

def Sort_List(lis1):
    nw_lis1 = []
    nw_lis2 = []

    for i in lis1:
        if len(i)==1:
            nw_lis1.append(i)
            nw_lis1.sort()
        else:
            nw_lis2.append(i)
            nw_lis2.sort()
        
    print(nw_lis1+nw_lis2)

# Sort_List(lis1)


'''
97. Remove Sublists Outside Range

Write a Python program to remove sublists from a given list of lists that contain an element outside a given range.
Original list:
[[2], [0], [1, 2, 3], [0, 1, 2, 3, 6, 7], [9, 11], [13, 14, 15, 17]]
After removing sublists from a given list of lists, which contains an element outside the given range:
[[13, 14, 15, 17]]
Click me to see the sample solution

'''

pass


'''
98. Scramble Letters in List Strings

Write a Python program to scramble the letters of a string in a given list.
Original list:
['Python', 'list', 'exercises', 'practice', 'solution']
After scrambling the letters of the strings of the said list:
['tnPhyo', 'tlis', 'ecrsseiex', 'ccpitear', 'noiltuos']
Click me to see the sample solution


'''
pass

'''
99. Find Max and Min in Heterogeneous List

Write a Python program to find the maximum and minimum values in a given heterogeneous list.
Original list:
['Python', 3, 2, 4, 5, 'version']
Maximum and Minimum values in the said list:
(5, 2)
Click me to see the sample solution

'''

lis1 = ['Python', 3, 2, 4, 5, 'version']

def max_min(lis1):
    nw_lis1 = []
    nw_lis2 = []
    for i in lis1:
        if isinstance(i,int):
            nw_lis1.append(i)
    print(max(nw_lis1),min(nw_lis1))
    return

# max_min(lis1)


'''
100. Extract Common Index Elements from Lists

Write a Python program to extract common index elements from more than one given list.
Original lists:
Common index elements of the said lists:
[1, 7]
Click me to see the sample solution

'''
lis1 = [1, 1, 3, 4, 5, 6, 7]
lis2 = [0, 1, 2, 3, 4, 5, 7]
lis3 = [0, 1, 2, 3, 4, 5, 7]


def Common_Index_Elements(lis1,lis2,lis3):
    nw_lis = []
    for i in zip(lis1,lis2,lis3):
        print(i)
        # print(i.index(i))


# Common_Index_Elements(lis1,lis2,lis3)



'''
102. Extract Strings by Length

Write a Python program to extract specified size of strings from a give list of string values.
Original list:
['Python', 'list', 'exercises', 'practice', 'solution']
length of the string to extract:
8
After extracting strings of specified length from the said list:
['practice', 'solution']
Click me to see the sample solution

'''
lis1 = ['Python', 'list', 'exercises', 'practice', 'solution']
le = 8
# print(len(lis1[2]))


def Strings_by_Length(lis1,le):
    nw_lis = []
    for i in lis1:
        if le == len(i):
            nw_lis.append(i)
    print(nw_lis)
    return

# Strings_by_Length(lis1,le)

'''
103. Extract Continuous Elements from List

Write a Python program to extract specified number of elements from a given list, which follows each other continuously.
Original list:
[1, 1, 3, 4, 4, 5, 6, 7]
Extract 2 number of elements from the said list which follows each other continuously:
[1, 4]
Original lists:
[0, 1, 2, 3, 4, 4, 4, 4, 5, 7]
Extract 4 number of elements from the said list which follows each other continuously:
[4]
Click me to see the sample solution

'''

lis1 = [1, 1, 3, 4, 4, 5, 6, 7]

# [1, 4]

def Continuous_Elements(lis1):
    nw_elem = []
    for i in lis1:
        if i == i-1:    
            pass

# Continuous_Elements(lis1)



'''
105. Average of Two Lists

Write a Python program to compute average of two given lists.
Original list:
[1, 1, 3, 4, 4, 5, 6, 7]
[0, 1, 2, 3, 4, 4, 5, 7, 8]
Average of two lists:
3.823529411764706
Click me to see the sample solution Python programming course

'''
lis1 = [1, 1, 3, 4, 4, 5, 6, 7]
lis2 = [0, 1, 2, 3, 4, 4, 5, 7, 8]


def Average_Two_Lists(lis1,lis2):
    sum1 = 0
    sum2 = 0
    for i,j in zip(lis1,lis2):
        sum1=sum1+i
        sum2 = sum2+j
    avg = sum1+sum2
    print(avg/2)
    return

# Average_Two_Lists(lis1,lis2)

'''

106. Count Integers in Mixed List

Write a Python program to count integers in a given mixed list.
Original list:
[1, 'abcd', 3, 1.2, 4, 'xyz', 5, 'pqr', 7, -5, -12.22]
Number of integers in the said mixed list:
6
Click me to see the sample solution

'''

lis1 = [1, 'abcd', 3, 1.2, 4, 'xyz', 5, 'pqr', 7, -5, -12.22]

def Count_Integers(lis1):
    nw_lis = []
    j = int()
    for i in lis1:
        if i == j :
            nw_lis.append(i)
    print(nw_lis)
    return

# Count_Integers(lis1)


'''

107. Remove Column from Nested List

Write a Python program to remove a specified column from a given nested list.
Original Nested list:
[[1, 2, 3], [2, 4, 5], [1, 1, 1]]
After removing 1st column:
[[2, 3], [4, 5], [1, 1]]
Original Nested list:
[[1, 2, 3], [-2, 4, -5], [1, -1, 1]]
After removing 3rd column:
[[1, 2], [-2, 4], [1, -1]]
Click me to see the sample solution

'''


'''

110. Find Most Frequent Item in List

Write a Python program to find the item with the most occurrences in a given list.
Original list:
[2, 3, 8, 4, 7, 9, 8, 2, 6, 5, 1, 6, 1, 2, 3, 4, 6, 9, 1, 2]
Item with maximum occurrences of the said list:
2
Click me to see the sample solution

'''

lis1 = [2, 3, 8, 4, 7, 9, 8, 2, 6, 5, 1, 6, 1, 2, 3, 4, 6, 9, 1, 2]

def most_occurrences(lis1):
    nw_lis = []
    for i in lis1:
        k = lis1.count(i)
        nw_lis.append(k)
    print(nw_lis)
    return 

# most_occurrences(lis1)


'''
111. Access Multiple Elements by Index

Write a Python program to access multiple elements at a specified index from a given list.
Original list:
[2, 3, 8, 4, 7, 9, 8, 2, 6, 5, 1, 6, 1, 2, 3, 4, 6, 9, 1, 2]
Index list:
[0, 3, 5, 7, 10]
Items with specified index of the said list:
[2, 4, 9, 2, 1]
Click me to see the sample solution
'''

lis1 = [2, 3, 8, 4, 7, 9, 8, 2, 6, 5, 1, 6, 1, 2, 3, 4, 6, 9, 1, 2]
index = [0, 3, 5, 7, 10]

def Multiple_Elements_Index(lis1):
    nw_lis = []
    for i in enumerate(lis1,1):
        print(i)
    return


# Multiple_Elements_Index(lis1)

'''

112. Check If List Is Sorted

Write a Python program to check whether a specified list is sorted or not.
Original list:
[1, 2, 4, 6, 8, 10, 12, 14, 16, 17]
Is the said list is sorted!
True
Original list:
[1, 2, 4, 6, 8, 10, 12, 14, 16, 17]
Is the said list is sorted!
False
Click me to see the sample solution


'''
lis1 = [1, 2, 4, 6, 8, 10, 12, 14, 16, 17]
lis2 = [1, 2, 4, 6, 18, 10, 12, 55, 16, 17]


def List_Sorted(lis1):
    nw_lis = []
    lis1.sort()
    print(lis1)
    # nw_lis.append(k)
    # if nw_lis == lis1:
    #     print('TRUE')
    # else:
    #     print('False')
    
    return


# List_Sorted(lis1)
























'''
113. Remove Duplicate Dictionaries from List

Write a Python program to remove duplicate dictionary entries from a given list.
Original list with duplicate dictionary:
[{'Green': '#008000'}, {'Black': '#000000'}, {'Blue': '#0000FF'}, {'Green': '#008000'}]
After removing duplicate dictionary of the said list:
[{'Black': '#000000'}, {'Blue': '#0000FF'}, {'Green': '#008000'}]
Click me to see the sample solution

'''
lis1 = [{'Green': '#008000'}, {'Black': '#000000'}, {'Blue': '#0000FF'}, {'Green': '#008000'}]


def Duplicate_Dictionaries_from_List(lis1):

    for i in lis1:
        print(i)
    return

# Duplicate_Dictionaries_from_List(lis1)



'''115. Check for Unique Elements in List

Write a Python program to check if the elements of a given list are unique or not.
Original list:
[1, 2, 4, 6, 8, 2, 1, 4, 10, 12, 14, 12, 16, 17]
Is the said list contains all unique elements!
False
Original list:
[2, 4, 6, 8, 10, 12, 14]
Is the said list contains all unique elements!
True
Click me to see the sample solution'''


# lis1 = [2, 4, 6, 8, 10, 12, 14]
# lis2 = [1, 2, 4, 6, 8, 2, 1, 4, 10, 12, 14, 12, 16, 17]


# def Unique_Elements(lis1):
#     my_lis = []
#     for i in lis1:
#         x = lis1.count(i)
#         print(f'no of element{i}:{x}')


# Unique_Elements(lis2)