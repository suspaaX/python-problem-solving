'https://www.w3resource.com/python-exercises/string/'


'''# 1. Calculate string length.

# Write a Python program to calculate the length of a string.'''


# '''str = "w3resource.com"

# print(len(str))'''

#DONE


'''2. Count character frequency in a string.

Write a Python program to count the number of characters (character frequency) in a string.
Sample String : 'google.com'
Expected Result : {'g': 2, 'o': 3, 'l': 1, 'e': 1, '.': 1, 'c': 1, 'm': 1}'''


def str_count(str):
    dict1 = dict()

    for key in str:
        ky = str.count(key)
        dict1.update({key:ky})

    return dict1

# print(str_count("raja"))

#DONE


'''3. Get string of first and last 2 chars.

Write a Python program to get a string made of the first 2 and last 2 characters of a given string. If the string length is less than 2, return the empty string instead.
Sample String : 'w3resource'
Expected Result : 'w3ce'
Sample String : 'w3'
Expected Result : 'w3w3'
Sample String : ' w'
Expected Result : Empty String'''

def str_trim_two(str1):

    if len(str1)>2:
        return (str1[0:2]+str1[len(str1)-2:len(str1)])
    else:
        return("empty string")

# print(str_trim_two("abhishek"))

#DONE

'''4. Replace first char occurrences with $.

Write a Python program to get a string from a given string where all occurrences of its first char have been changed to '$', except the first char itself.
Sample String : 'restart'
Expected Result : 'resta$t'

'''

str ='restart'
char = '$'
Expected_Result = 'resta$t'


def char_occurrences(str,char):
    fchar = str[0]
    schar = str[1:len(str)]
    if fchar in schar:
        x = schar.replace(fchar,char)
        print(x)
    return

# char_occurrences(str,char)

'''5. Swap first 2 chars of 2 strings.

Write a Python program to get a single string from two given strings, separated by a space and swap the first two characters of each string.
Sample String : 'abc', 'xyz'
Expected Result : 'xyc abz'

'''

pass





























'''6. Add ing or ly to a string.

Write a Python program to add 'ing' at the end of a given string (length should be at least 3). 
If the given string already ends with 'ing', add 'ly' instead. If the string length of the given string is less than 3,
 leave it unchanged.


Sample String : 'abc'
Expected Result : 'abcing'
Sample String : 'string'
Expected Result : 'stringly'
'''

str1 = 'abc'
str2 = 'string'

adstr1 = 'ing'
adstr2 = 'ly'


def change_str_ing_ly(str1,adstr1,adstr2):
    if adstr1 not in str1:
        print(str1+adstr2)
    elif adstr2 in str2:
        print(str2+adstr1)
    


# change_str_ing_ly(str2,adstr1,adstr2)
























'''7. Replace 'not'...'poor' with 'good'.

Write a Python program to find the first appearance of the substrings 'not' and 'poor' in a given string. If 'not' follows 'poor', replace the whole 'not'...'poor' substring with 'good'. Return the resulting string.
Sample String : 'The lyrics is not that poor!'
'The lyrics is poor!'
Expected Result : 'The lyrics is good!'
'The lyrics is poor!'''


'''8. Find longest word in a list.

Write a Python function that takes a list of words and return the longest word and the length of the longest one.
Sample Output:
Longest word: Exercises
Length of the longest word: 9
'''

str = "PHP", "Exercises", "Backend"


def longest_word(str):
    lst = []
    for i in str:
        x = (len(i))
        lst.append(x)
    print(max(lst),i)
        
# longest_word(str)

'''
9. Remove nth character from a string.

Write a Python program to remove the nth index character from a nonempty string.
Click me to see the sample solution

'''


# print(remove_char('Python', 0))  # Output: 'ython'
# print(remove_char('Python', 3))  # Output: 'Pyton'
# print(remove_char('Python', 5))  # Output: 'Pytho'

str = 'Python'
idx = 2

def remove_nth_indexchar(str,idx):
    x = str[idx]
    str.replace(str,x)
    print(x)



# remove_nth_indexchar(str,idx)





















'''
10. Swap first and last chars of a string.

Write a Python program to change a given string to a newly string where the first and last chars have been exchanged.
Click me to see the sample solution
'''


str1 = 'abcd' # Output: 'dbca'

str2 = '12345' # Output: '52341' 


def Swap_first_last(str1):
    fchar = str1[0]
    lchar = str1[-1]

    new_str = lchar+str1[1:-1]+fchar
    print(new_str)
    return

# Swap_first_last(str1)
# Swap_first_last(str2)




'''

11. Remove odd index chars from a string.

Write a Python program to remove characters that have odd index values in a given string.
Click me to see the sample solution
'''
# print(odd_values_string('abcdef'))  # Output: 'ace'
# print(odd_values_string('python'))  # Output: 'pto'

str = 'abcdef'

def Remove_odd_index_chars(str):
    print(str[0:len(str)]:1)







Remove_odd_index_chars(str)





































'''


12. Count word occurrences in a sentence.

Write a Python program to count the occurrences of each word in a given sentence.

'''

str1 = 'the quick brown fox jumps over the lazy dog.'

def word_count(str1):
    result = str()
    for i in str1:
        result.count(i)
    return result

# print(word_count(str1))




'''
18. Get first 3 chars of a string.

Write a Python function to get a string made of the first three characters of a specified string. If the length of the string is less than 3, return the original string.
Sample function and result :
first_three('ipy') -> ipy
first_three('python') -> pyt'''

str1 = 'python'

def first_three(str1):

    result = str1[0:3]

    return result

# print(first_three('9878978'))

#DONE


'''


27. Remove indentation from text.

Write a Python program to remove existing indentation from all of the lines in a given text.
'''

str1 = "this is my text"

def remove_indentation(str1):

    result = str1.strip()

    return result

sample_text = '''
    Python is a widely used high-level, general-purpose, interpreted,
    dynamic programming language. Its design philosophy emphasizes
    code readability, and its syntax allows programmers to express
    concepts in fewer lines of code than possible in languages such
    as C++ or Java.
    '''

# print(remove_indentation(sample_text))



def longest_word(myLis):

    for i in myLis:
        my_item = i
    
    return my_item

# print(longest_word(myLis))

'''

28. Add prefix to each line of text.

Write a Python program to add prefix text to all of the lines in a string.
Click me to see the sample solution


'''

sample_text = '''
    Python is a widely used high-level, general-purpose, interpreted,
    dynamic programming language. Its design philosophy emphasizes
    code readability, and its syntax allows programmers to express
    concepts in fewer lines of code than possible in languages such
    as C++ or Java.
    '''


import textwrap

text_without_indenitation = textwrap.dedent(sample_text)

# print()

# print(text_without_indenitation)


'''
30. Print numbers with 2 decimal places.

Write a Python program to print the following numbers up to 2 decimal places.
Click me to see the sample solution
'''

num = 12.65789

def two_decimal(num):

    new_num = "{:.2f}".format(num)

    print(new_num)

    return

# two_decimal(4589.78965)

'''
31. Print numbers with sign (2 decimals).

Write a Python program to print the following numbers up to 2 decimal places with a sign.
Click me to see the sample solution
'''
    
# two_decimal(-12.999999)


'''32. Print numbers without decimal places.

Write a Python program to print the following positive and negative numbers with no decimal places.
Click me to see the sample solution

'''

def no_decimal(num):
    new_num = '{:.0f}'.format(num)
    print (new_num)
    return

# no_decimal(num)



'''
33. Print integers with left-padded zeros.

Write a Python program to print the following integers with zeros to the left of the specified width.
Click me to see the sample solution
'''

num3 = 13
def left_padded_zeros(num):
    new_num = '{:0>3d}'.format(num)
    print(new_num)
    return 

# left_padded_zeros(num3)

'''
34. Print integers with * right-padded.

Write a Python program to print the following integers with '*' to the right of the specified width.
Click me to see the sample solution
'''

def right_padded_zero(num):
    new_num = '{:0<4d}'.format(num)
    print(new_num)
    return

# right_padded_zero(89)



'''
35. Display number with comma separator.

Write a Python program to display a number with a comma separator.
Click me to see the sample solution
'''


num = 1204

def num_seprator(num):
    new_num = '{:,}'.format(num)
    print (new_num)
    return

# num_seprator(num)

'''
36. Format number as percentage.

Write a Python program to format a number with a percentage.
Click me to see the sample solution
'''

def format_percentage(num):
    num = num/100
    new_num = '{:.2%}'.format(num)
    print(new_num)
    return

# format_percentage(172)

'''
37. Align number left, right, center (width=10).

Write a Python program to display a number in left, right, and center aligned with a width of 10.
Click me to see the sample solution   

'''

num = 22
def align_num(num): 
    left_align = '{:>10d}'.format(num)
    right_align = '{:<10d}'.format(num)
    centre_align = '{:^10d}'.format(num)
    return left_align,right_align,centre_align

# print(align_num(23))

'''
38. Count substring occurrences in string.

Write a Python program to count occurrences of a substring in a string.
Click me to see the sample solution
'''

pass

'''
39. Reverse a string.

Write a Python program to reverse a string.
Click me to see the sample solution
'''

pass

'''
40. Reverse words in a string.

Write a Python program to reverse words in a string.
Click me to see the sample solution
'''

pass

'''
41. Strip specific characters from string.

Write a Python program to strip a set of characters from a string.
Click me to see the sample solution
'''

pass

'''
42. Count repeated characters in string.

Write a Python program to count repeated characters in a string.
Sample string: 'thequickbrownfoxjumpsoverthelazydog'
Expected output :
o 4
e 3
u 2
h 2
r 2
t 2

'''


str1 = 'thequickbrownfoxjumpsoverthelazydog'

def string_count(str1):
    set_1 = set(str1)
    for el in set_1:
        x = str1.count(el)
        if x >=2: 
            print(el,x)

str1 = "tomatto"
# string_count(str1)

'''
43. Print area (rectangle) and volume (cylinder).

Write a Python program to print the square and cube symbols in the area of a rectangle and the volume of a cylinder.
Sample output:
The area of the rectangle is 1256.66cm2
The volume of the cylinder is 1254.725cm3
Click me to see the sample solution

#logger

'''

pass


'''
44. Find character indices in string.

Write a Python program to print the index of a character in a string.
Sample string: w3resource
Expected output:
Current character w position at 0
Current character 3 position at 1
Current character r position at 2
- - - - - - - - - - - - - - - - - - - - - - - - -
Current character c position at 8
Current character e position at 9
Click me to see the sample solution
'''

Sample_string =  'w3resource'


def find_index(Sample_string):
    for i in enumerate(Sample_String):
        print(i)
        return
    

# find_index(Sample_String)

pass


'''
46. Convert string to list of words.

Write a Python program to convert a given string into a list of words.
Sample Output:
['The', 'quick', 'brown', 'fox', 'jumps', 'over', 'the', 'lazy', 'dog.']
['The', 'quick', 'brown', 'fox', 'jumps', 'over', 'the', 'lazy', 'dog.']
Click me to see the sample solution
'''

str1 ="The quick brown fox jumps over the lazy dog."

def string_list(str1):
    t =str1.split()
    print(t)
    return

    # string_list(str1)

'''47. Lowercase first n characters of string.

Write a Python program to lowercase the first n characters in a string.
Click me to see the sample solution

'''
pass

'''
48. Swap commas and dots in a string.

Write a Python program to swap commas and dots in a string.
Sample string: "32.054,23"
Expected Output: "32,054.23"
Click me to see the sample solution
'''

pass

'''
49. Count and display vowels in text.

Write a Python program to count and display vowels in text.
Click me to see the sample solution
'''


str1 = 'w3resource'

def count_vowel(str1):
    vowel = 'a','e','i','o','u'
    for i in vowel :
        pass
    for j in str1:
        pass

        if j in i :
            print(j)

# count_vowel(str1)



# o4                                                                                                             
# ['e', 'o', 'u', 'e']   


'''
50. Split string on last delimiter occurrence.

Write a Python program to split a string on the last occurrence of the delimiter.
Click me to see the sample solution
'''

pass

'''51. Find first non-repeating character.

Write a Python program to find the first non-repeating character in a given string.
Click me to see the sample solution
'''
pass


'''
52. Permutations with repetition in string.

Write a Python program to print all permutations with a given repetition number of characters of a given string.
Click me to see the sample solution
'''
pass
'''
53. Find first repeated character.

Write a Python program to find the first repeated character in a given string.
Click me to see the sample solution
'''

pass

'''
54. Find repeated character with smallest index.

Write a Python program to find the first repeated character in a given string where the index of the first occurrence is smallest.
Click me to see the sample solutionPython certification
'''
pass
'''
55. Find first repeated word in string.

Write a Python program to find the first repeated word in a given string.
Click me to see the sample solution
'''

pass

'''
56. Find second most repeated word.

Write a Python program to find the second most repeated word in a given string.
Click me to see the sample solution
'''
pass

'''
57. Remove spaces from string.

Write a Python program to remove spaces from a given string.
Click me to see the sample solution
'''


str1 = "w 3 res ou r ce"

def remove_space(str1):
    new_str= str1.strip(' ')
    print(new_str)
    return

# remove_space(str1)

'''
59. Find maximum occurring character.

Write a Python program to find the maximum number of characters in a given string.
Click me to see the sample solution
'''

str1 = "abcdefghijkb"

def max_occurance(str1):
    new_str = str()
    for elem in str1:
        i = elem
        print(i)
    return
   
# print(max_occurance(str1))
pass

'''
60. Capitalize first and last letters of words.

Write a Python program to capitalize the first and last letters of each word in a given string.
Click me to see the sample solution
'''

str1 = "python exercises practice solution"
pass

'''
61. Remove duplicate characters in string.

Write a Python program to remove duplicate characters from a given string.
Click me to see the sample solution
'''

str1 = "python exercises practice solution"

# def remove_duplicate(str1):
#     for i in str1:
        
#     return
    
# remove_duplicate(str1)

'''
62. Sum digits in string.

Write a Python program to compute the sum of the digits in a given string.
Click me to see the sample solution
'''

# str1  = 'abcd1234'

# def sum_digit_string(str1):
#     sum = 0
#     for i in str1:
#         print(type(i))
#     return sum

# print(sum_digit_string(str1))


'''
63. Remove leading zeros in IP address.

Write a Python program to remove leading zeros from an IP address.
Click me to see the sample solution
'''
pass

'''
64. Find max length of consecutive zeros (binary).

Write a Python program to find the maximum length of consecutive 0's in a given binary string.
Click me to see the sample solution
'''
pass

'''
65. Common characters between two strings.

Write a Python program to find all the common characters in lexicographical order from two given lower case strings. If there are no similar letters print "No common characters".
Click me to see the sample solution
'''

pass

'''
66. Make strings anagrams (retain characters).

Write a Python program to make two given strings (lower case, may or may not be of the same length) anagrams without removing any characters from any of the strings.
Click me to see the sample solution
'''

pass

'''
67. Remove consecutive duplicates in string.

Write a Python program to remove all consecutive duplicates of a given string.
Click me to see the sample solution
'''

pass

'''
68. Separate single and multiple occurrence chars.

Write a Python program to generate two strings from a given string. For the first string, use the characters that occur only once, and for the second, use the characters that occur multiple times in the said string.
Click me to see the sample solution

'''
pass



'''
79. Find smallest and largest words.

Write a Python program to find the smallest and largest words in a given string.
Click me to see the sample solution
'''

str1 = 'Write a Java program to sort an array of given integers using Quick sort Algorithm.'
def smallest_largest(str1):
    smallest = 0
    largest = 0
    t = str1.split()
    print(t)
    
    # for i in t:
    #     print(len(i),i)

# print(smallest_largest(str1))

'''
80. Substrings with same first and last char.

Write a Python program to count the number of substrings with the same first and last characters in a given string.
Click me to see the sample solution
'''
# def count():


# pass


'''
81. Index of substring or "Not found".

Write a Python program to determine the index of a given string at which a certain substring starts.
If the substring is not found in the given string return 'Not found'.
Click me to see the sample solution
'''


'''
82. Wrap string into paragraph with width.

Write a Python program to wrap a given string into a paragraph with a given width.
Sample Output:
Input a string: The quick brown fox.
Input the width of the paragraph: 10
Result:
The quick
brown fox.
Click me to see the sample solution
'''
pass

'''
83. Print number in decimal, octal, hex, binary.

Write a Python program to print four integer values - decimal, octal, hexadecimal (capitalized), binary - in a single line.
Sample Output:
Input an integer: 25
Decimal Octal Hexadecimal (capitalized), Binary
25 31 19 11001
Click me to see the sample solution
'''


pass

'''
84. Swap cases in string.

Write a Python program to swap cases in a given string.
Sample Output:
pYTHON eXERCISES
jAVA
nUMpY
Click me to see the sample solution
'''

# sapmle = "Python Exercises"
# output = 'pYTHON eXERCISES'

# def swap_string(sample):
#     nw_str = sample.lower()
#     nw.
#     print(nw_str)
#     return nw_str


# swap_string(sapmle)


'''
85. Bytearray to hexadecimal string.

Write a Python program to convert a given Bytearray to a Hexadecimal string.
Sample Output:
Original Bytearray :
[111, 12, 45, 67, 109]
Hexadecimal string:
6f0c2d436d
Click me to see the sample solution

'''

pass


'''

86. Delete all occurrences of character.

Write a Python program to delete all occurrences of a specified character in a given string.
Sample Output:
Original string:
Delete all occurrences of a specified character in a given string
Modified string:
Delete ll occurrences of specified chrcter in given string
Click me to see the sample solution

'''

# str1 = "Delete all occurrences of a specified character in a given string"

# output = 'Delete ll occurrences of specified chrcter in given string'


# def test_pattern(str1):
#     if str1 == try
#     print(new_str)
#     return new_str

# test_pattern(str1)
        
'''
87. Find common values in two strings.

Write a Python program to find the common values that appear in two given strings.
Sample Output:
Original strings:
Python3
Python2.7
Intersection of two said String:
Python
Click me to see the sample solution
'''

pass

'''
88. Check string for capital, lower, number, length.

Write a Python program to check whether a given string contains a capital letter, 
a lower case letter, a number and a minimum length.
Sample Output:
Input the string: W3resource
['Valid string.']
Click me to see the sample solution
'''

# str1 = 'Input the string: W3resource'

# def check_valid(str1):

# pass

'''
89. Remove unwanted characters in string.

Write a Python program to remove unwanted characters from a given string.
Sample Output:
Original String : Pyth*^on Exercis^es
After removing unwanted characters:
Python Exercises
Original String : A%^!B#*CD
After removing unwanted characters:
ABCD
Click me to see the sample solution
'''

pass

'''
90. Remove duplicate words in string.

Write a Python program to remove duplicate words from a given string.
Sample Output:
Original String:
Python Exercises Practice Solution Exercises
After removing duplicate words from the said string:
Python Exercises Practice Solution
Click me to see the sample solution

'''
str1 = 'Python Exercises Practice Solution Exercises'
output ='Python Exercises Practice Solution'

def remove_duplicate(str1):
    emp_str = str()
    new_str = str1.split()
    set1 = set(new_str)
    emp_str(set1)
    return emp_str

# remove_duplicate(str1)

'''
91. Convert heterogeneous list to string.

Write a Python program to convert a given heterogeneous list of scalars into a string.
Sample Output:
Original list:
['Red', 100, -50, 'green', 'w,3,r', 12.12, False]
Convert the heterogeneous list of scalars into a string:
Red,100,-50,green,w,3,r,12.12,False
Click me to see the sample solution

'''
str1 = ['Red', 100, -50, 'green', 'w,3,r', 12.12, False]

"Red,100,-50,green,w,3,r,12.12,False"


def lis_to_str(str1):
    for i in str1:
        print(str(i))
    # return str1 

    # lis_to_str(type(str1))


'''92. Find similarity between two strings.

Write a Python program to find string similarity between two given strings.
Sample Output:
Original string:
Python Exercises
Python Exercises
Similarity between two said strings:
1.0
Original string:
Python Exercises
Python Exercise
Similarity between two said strings:
0.967741935483871
Original string:
Python Exercises
Python Ex.
Similarity between two said strings:
0.6923076923076923
Original string:
Python Exercises
Python
Similarity between two said strings:
0.5454545454545454
Original string:
Java Exercises
Python
Similarity between two said strings:
0.0
Click me to see the sample solution
'''
pass

'''
93. Extract numbers from string.

Write a Python program to extract numbers from a given string.
Sample Output:
Original string: red 12 black 45 green
Extract numbers from the said string: [12, 45]
Click me to see the sample solution



'''
pass


'''
94. Hex color code to RGB tuple.

Write a Python program to convert a hexadecimal color code to a tuple of integers corresponding to its RGB components.
Sample Output:
(255, 165, 1)
(255, 255, 255)
(0, 0, 0)
(255, 0, 0)
(0, 0, 128)
(192, 192, 192)
Click me to see the sample solution
'''
pass

'''
95. RGB to hex color code.

Write a Python program to convert the values of RGB components to a hexadecimal color code.
Sample Output:
FFA501
FFFFFF
000000
000080
C0C0C0
Click me to see the sample solution
'''
pass







