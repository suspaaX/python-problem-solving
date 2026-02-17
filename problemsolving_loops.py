'https://www.w3resource.com/python-exercises/python-conditional-statements-and-loop-exercises.php'


'''https://pynative.com/python-if-else-and-for-loop-exercise-with-solutions/'''

'''Exercise 1: Print first 10 natural numbers using while loop'''

def natural_num(num):
    i = 0
    while (i<num):
        i = i+1
        print(i)
    
# natural_num(10)


'''Exercise 2: Print the following pattern'''

# 1 
# 1 2 
# 1 2 3 
# 1 2 3 4 
# 1 2 3 4 5

row = 5 
'''
for i in range(1,row+1):
    for j in range(1,row-(row-i)+1):
        print(j,end=' ')
    print()
'''

'''Exercise 3: Calculate sum of all numbers from 1 to a given number'''

def sum_all(num):
    j = 0
    for i in range(1,num+1):
        j = j+i
    return j

# print(sum_all(10))

'''Exercise 4: Print multiplication table of a given number'''

def multi_table(num):
    for i in range(1,11):
        c = (num * i)
        print (c)
    
# print(multi_table(10))

'''Exercise 5: Display numbers from a list using a loop'''

num = [12,12,45,58,67,65]

def list_num(num):
    for i in num:
        print(i)

# print(list_num(num))

'''Exercise 6: Count the total number of digits in a number'''

def total_digit(num1):
    num1 = str(num1)
    return len(num1)

# print(total_digit(45677894))


'''Exercise 7: Print the following pattern'''


# 5 4 3 2 1 
# 4 3 2 1 
# 3 2 1 
# 2 1 
# 1


row = 5
'''
for i in range(1,row+1):
    for j in range(1,(row-i)+2):
        print((row+1)-j,end='')
    print()
'''

'''Exercise 8: Print list in reverse order using a loop'''
num = [10, 20, 30, 40, 50]

def rev_num(num):
    num = list(num)
    num.reverse()
    for elem in num:
        print(elem)
    return

num = [2,56,78,69,54]

# rev_num(num)

'''Exercise 9: Display numbers from -10 to -1 using for loop'''

# for i in range(-10,0):
#     print(i)

'''Exercise 10: Display a message “Done” after the successful execution of the for loop'''

# num = 10 

# for i in range(1,num+1):
#     print(i)
# print('DONE')


'''Exercise 11: Print all prime numbers within a range'''

'''Exercise 12: Display Fibonacci series up to 10 terms'''


'''Exercise 13: Find the factorial of a given number'''

num = 15

def fact(num):
    facti = 1
    for i in range(1,num+1):
        facti = facti*i
    return facti

# print(fact(5))


'''Exercise 14: Reverse a integer number'''

num = 145658

def reverse_num(num):
    num = str(num)
    lis=list(num)
    lis.reverse()

    for j in lis:
        print(j,end='')
    print()

    return

# reverse_num(556)

'''Exercise 15: Print elements from a given list present at odd index positions'''

my_list = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]


def odd_element(my_list):
    for i in my_list[1:-1:2]:
        print(i)
    return

# odd_element(my_list)
        

'''Exercise 16: Calculate the cube of all numbers from 1 to a given number'''

num = 100
def cube(num):
    for i in range(1,num+1):
        c= i*i*i
        print (c)
    return 

# cube(10)

'''Exercise 17: Find the sum of a series of a number up to n terms'''


# # number of terms
# num = 2
# terms = 5
# # 2+22+222+2222+22222=2469

# # Expected output:
# 24690

# def sum_series(num,terms):



'''Exercise 18: Print the following pattern'''


# * 
# * * 
# * * * 
# * * * * 
# * * * * * 
# * * * * 
# * * * 
# * * 
# *


'''Exercise 19: Print Full Multiplication Table'''

'''Exercise 20: Print the alternate numbers pattern'''

# 1  
# 2 3  
# 4 5 6  
# 7 8 9 10  
# 11 12 13 14 15

row = 5

# for i in range(1,row+1):
#     for j in range(1,row-(row-i)+1):
#         print(j,end='  ')
#     print()



'''Exercise 21: Flatten a nested list using loops'''

nested_list = [1, [2, 3], [4, 5, 6], 7, [8, 9]]

def flatten_list(nested_list):
    flat_list = []
    for element in nested_list:
        if isinstance(element,list):
            for ele in element:
                flat_list.append(ele)
        else:
            flat_list.append(element)

    return flat_list

# print(flatten_list(nested_list))


'''Exercise 22: Find largest and smallest digit in a number'''

num1 = 9876543210

num2 = -5082

num3 =897


def largest_number(num1):
    large_num = []
    num1 = str(num1)
    for i in num1:
        j = int(i)
        if  1<j>9:
            large_num.append(j)
        else:
            j==9
            large_num.append(j)
    return 



'''==========================='THE END'================================================='''


'''
1. Divisible by 7 and Multiples of 5

Write a Python program to find those numbers which are divisible by 7 and multiples of 5, between 1500 and 2700 (both included).

Click me to see the sample solution
'''

pass

'''
2. Temperature Converter

Write a Python program to convert temperatures to and from Celsius and Fahrenheit.

[ Formula : c/5 = f-32/9 [ where c = temperature in celsius and f = temperature in fahrenheit ]

Expected Output :

60°C is 140 in Fahrenheit
45°F is 7 in Celsius

Click me to see the sample solution
'''



def tem_conv():

    pass


'''

3. Number Guessing Game

Write a Python program to guess a number between 1 and 9.

Note : User is prompted to enter a guess. If the user guesses wrong then the prompt appears again until the guess is correct, on successful guess, user will get a "Well guessed!" message, and the program will exit.

Click me to see the sample solution
'''
pass

'''4. Construct Pattern (Diamond Pattern)

Write a Python program to construct the following pattern, using a nested for loop.

* 
* * 
* * * 
* * * * 
* * * * * 
* * * * 
* * * 
* * 
*

'''

row = 9


# for i in range(1,row+1):
#     for j in range(1,i):
#         print('*',end='')
#         pass


'''
5. Reverse a Word

Write a Python program that accepts a word from the user and reverses it.

Click me to see the sample solution
'''
# str1 ='father'

# def reverse_word(str1):
#     new_str = 
#     return new_str

# print(reverse_word(str1))

'''
6. Count Even and Odd Numbers

Write a Python program to count the number of even and odd numbers in a series of numbers

Sample numbers : numbers = (1, 2, 3, 4, 5, 6, 7, 8, 9) 

Expected Output :

Number of even numbers : 5
Number of odd numbers : 4

Click me to see the sample solution
'''


num1 = (1, 2, 3, 4, 5, 6, 7, 8, 9) 


def check_odd_even(num1):
    num_odd =[]
    num_even = []
    for i in num1:
        if i%2 ==0:
            num_even.append(i)
            
        else:
            num_odd.append(i)
        
    print(f'no of even:',len(num_odd))
    print(f'no of even:',len(num_even))



# print(check_odd_even(num1))

pass
            

'''
7. Print Items with Types

Write a Python program that prints each item and its corresponding type from the following list.

Sample List : datalist = [1452, 11.23, 1+2j, True, 'w3resource', (0, -1), [5, 12], {"class":'V', "section":'A'}]
'''

lis1 = [1452, 11.23, 1+2j, True, 'w3resource', (0, -1), [5, 12], {"class":'V', "section":'A'}]

def data_types (lis1):
    for i in lis1:
        print(i,type(i))
    
# data_types(lis1)

'''
8. Print Numbers 0 to 6 Except 3 and 6

Write a Python program that prints all the numbers from 0 to 6 except 3 and 6.

Note : Use 'continue' statement.

Expected Output : 0 1 2 4 5

Click me to see the sample solution

'''

# num = 6

# for i in range(0,7):
    
'''
9. Fibonacci Series Between 0 and 50

Write a Python program to get the Fibonacci series between 0 and 50.

Note : The Fibonacci Sequence is the series of numbers :


0, 1, 1, 2, 3, 5, 8, 13, 21, ....
Every next number is found by adding up the two numbers before it.

Expected Output : 1 1 2 3 5 8 13 21 34

Click me to see the sample solution
'''
pass

'''
10. FizzBuzz Variation

Write a Python program that iterates the integers from 1 to 50. For multiples of three print "Fizz" instead of the number and for multiples of five print "Buzz". For numbers that are multiples of three and five, print "FizzBuzz".

Sample Output :

fizzbuzz
1
2
fizz
4
buzz

Click me to see the sample solution

'''
pass

'''
11. Two-Dimensional Array (Multiplication Table)

Write a Python program that takes two digits m (row) and n (column) as input and generates a two-dimensional array. 
The element value in the i-th row and j-th column of the array should be i*j.

Note :
i = 0,1.., m-1
j = 0,1, n-1.

Test Data : Rows = 3, Columns = 4
Expected Result : [[0, 0, 0, 0], [0, 1, 2, 3], [0, 2, 4, 6]]

Click me to see the sample solution

'''
pass

'''

Python Conditional Statements and loops
Last update on March 26 2025 08:12:01 (UTC/GMT +8 hours)

Discover more
Python Programming
python
Java programming resources
This resource offers a total of 220 Python conditional statements and loops problems for practice. It includes 44 main exercises, each accompanied by solutions, detailed explanations, and four related problems.

[An Editor is available at the bottom of the page to write and execute the scripts.]


1. Divisible by 7 and Multiples of 5

Write a Python program to find those numbers which are divisible by 7 and multiples of 5, between 1500 and 2700 (both included).

Click me to see the sample solution


2. Temperature Converter

Write a Python program to convert temperatures to and from Celsius and Fahrenheit.

[ Formula : c/5 = f-32/9 [ where c = temperature in celsius and f = temperature in fahrenheit ]

Expected Output :

60°C is 140 in Fahrenheit
45°F is 7 in Celsius

Click me to see the sample solution


3. Number Guessing Game

Write a Python program to guess a number between 1 and 9.

Note : User is prompted to enter a guess. If the user guesses wrong then the prompt appears again until the guess is correct, on successful guess, user will get a "Well guessed!" message, and the program will exit.

Click me to see the sample solution


4. Construct Pattern (Diamond Pattern)

Write a Python program to construct the following pattern, using a nested for loop.

* 
* * 
* * * 
* * * * 
* * * * * 
* * * * 
* * * 
* * 
*
Click me to see the sample solution


5. Reverse a Word

Write a Python program that accepts a word from the user and reverses it.

Click me to see the sample solution


6. Count Even and Odd Numbers

Write a Python program to count the number of even and odd numbers in a series of numbers

Sample numbers : numbers = (1, 2, 3, 4, 5, 6, 7, 8, 9) 

Expected Output :

Number of even numbers : 5
Number of odd numbers : 4

Click me to see the sample solution


7. Print Items with Types

Write a Python program that prints each item and its corresponding type from the following list.

Sample List : datalist = [1452, 11.23, 1+2j, True, 'w3resource', (0, -1), [5, 12], {"class":'V', "section":'A'}]

Click me to see the sample solution


8. Print Numbers 0 to 6 Except 3 and 6

Write a Python program that prints all the numbers from 0 to 6 except 3 and 6.

Note : Use 'continue' statement.

Expected Output : 0 1 2 4 5

Click me to see the sample solution


9. Fibonacci Series Between 0 and 50

Write a Python program to get the Fibonacci series between 0 and 50.


Note : The Fibonacci Sequence is the series of numbers :


0, 1, 1, 2, 3, 5, 8, 13, 21, ....
Every next number is found by adding up the two numbers before it.

Expected Output : 1 1 2 3 5 8 13 21 34

Click me to see the sample solution


10. FizzBuzz Variation

Write a Python program that iterates the integers from 1 to 50. For multiples of three print "Fizz" instead of the number and for multiples of five print "Buzz". For numbers that are multiples of three and five, print "FizzBuzz".

Sample Output :

fizzbuzz
1
2
fizz
4
buzz

Click me to see the sample solution


11. Two-Dimensional Array (Multiplication Table)

Write a Python program that takes two digits m (row) and n (column) as input and generates a two-dimensional array. The element value in the i-th row and j-th column of the array should be i*j.

Note :
i = 0,1.., m-1
j = 0,1, n-1.

Test Data : Rows = 3, Columns = 4
Expected Result : [[0, 0, 0, 0], [0, 1, 2, 3], [0, 2, 4, 6]]

Click me to see the sample solution


'''

pass
'''
12. Sequence of Lines to Lowercase

Write a Python program that accepts a sequence of lines (blank line to terminate) as input and prints the 

lines as output (all characters in lower case).

Click me to see the sample solution


'''
pass

'''
14. Count Digits and Letters in a String

Write a Python program that accepts a string and calculates the number of digits and letters.

Sample Data : Python 3.2

Expected Output :

Letters 6
Digits 2

Click me to see the sample solution

'''

str1 = 'W3resource'   

def count_letter_digit (str1):
    letter = []
    digit = []
    for i in str1:
        if i == str(i):
            d = letter.append(i)
            len(letter)
        elif i == int(i):
            digit.append(i)
            lt = len(digit)

        print(d)
    return


# count_letter_digit(str1)

'''
15. Password Validity Checker

Write a Python program to check the validity of passwords input by users.

Validation :

At least 1 letter between [a-z] and 1 letter between [A-Z].
At least 1 number between [0-9].
At least 1 character from [$#@].
Minimum length 6 characters.
Maximum length 16 characters.
Click me to see the sample solution
'''

pass

'''
16. Numbers with All Even Digits

Write a Python program to find numbers between 100 and 400 (both included) where each digit of a number is an even number. 


The numbers obtained should be printed in a comma-separated sequence.

Click me to see the sample solution


'''

num1 =100
num2 = 400

def even_interval(num1,num2):
    for i in range(num1,num2+1):
        if i%2 ==0:
            print(i)


# even_interval(num1,num2)



'''

17. Alphabet Pattern 'A'

Write a Python program to print the alphabet pattern 'A'.

Expected Output:

  ***                                                                   
 *   *                                                                  
 *   *                                                                  
 *****                                                                  
 *   *                                                                  
 *   *                                                                  
 *   *


'''

pass
'''18-31 skip'''


'''
32. Vowel or Consonant Checker

Write a Python program to check whether an alphabet is a vowel or consonant.

Expected Output:

Input a letter of the alphabet: k                                       
k is a consonant.
Click me to see the sample solution
'''

lttr = 'i'

def cons_vowl_checker(lttr):
    if  lttr=='a':
        print('This is vowel')
    elif  lttr=='e':
        print('This is vowel')

    elif  lttr=='i':
        print('This is vowel')

    elif  lttr=='o':
        print('This is vowel')

    elif  lttr=='u':
        print('This is vowel')

    else:
        print('This is constant')
    
    return

# cons_vowl_checker('c')

'''

33. Month Name to Number of Days

Write a Python program to convert a month name to a number of days.

Expected Output:

List of months: January, February, March, April, May, June, July, August
, September, October, November, December                                
Input the name of Month: February                                       
No . of days: 28/29 days 
Click me to see the sample solution

'''


month = 'January'

def no_of_days(month):

    if month == ['March','January','May','July',' August','October','December ']:
        print('No. of days: 31 days ')

    elif month == ['April','June','September',' November']:
        print('No. of days: 31 days ')

    elif month == ['February']:
        print('No. of days: 28/29 days ')

    else:
        print('error in code...')
    return


# no_of_days(month)



'''
35. String Represents Integer Checker

Write a Python program that checks whether a string represents an integer or not.

Expected Output:

Input a string: Python                                                  
The string is not an integer.  
Click me to see the sample solution


'''
str = 'The string is not an integer'


def int_str(str):
    chck_int = int()
    for i in str:
        if i == chck_int:
            print('The string is not an integer')
        else:
            print('The string is string')
            break
    return
    
int_str()






























'''
40. Median of Three Values

Write a Python program to find the median of three values.

Expected Output:

Input first number: 15                                                  
Input second number: 26                                                 
Input third number: 29                                                  
The median is 26.0   
Click me to see the sample solution

'''
























'''
41. Next Day Calculator

Write a Python program to get the next day of a given date.

Expected Output:

Input a year: 2016                                                      
Input a month [1-12]: 08                                                
Input a day [1-31]: 23                                                  
The next date is [yyyy-mm-dd] 2016-8-24   
Click me to see the sample solution
'''

# year = input('Input a year:')
# month =input('Input a month:')
# day = input('Input a day:')

# next_date = 





'''
42. Sum and Average of n Integers

Write a Python program to calculate the sum and average of n integer numbers (input from the user). Input 0 to finish.

Click me to see the sample solution

'''



# def sum_n_avg(*args):
#     sum = 0
#     avg = 0
#     for i in args:
#         sum = sum+i
#         avg = sum/len(args)
#     print(sum)
#     print(avg)


#     return


# sum_n_avg(26,26,26)
























'''
43. Multiplication Table

Write a Python program to create the multiplication table (from 1 to 10) of a number.

Expected Output:

Input a number: 6                                                       
6 x 1 = 6                                                               
6 x 2 = 12                                                              
6 x 3 = 18                                                              
6 x 4 = 24                                                              
6 x 5 = 30                                                              
6 x 6 = 36                                                              
6 x 7 = 42                                                              
6 x 8 = 48                                                              
6 x 9 = 54                                                              
6 x 10 = 60 
Click me to see the sample solution
'''



# num = 7

# for i in range(1,11):
#     print(num,'x' ,i ,'=', num*i)


'''


44. Nested Loop Number Pattern

Write a Python program to construct the following pattern, using a nested loop number.

Expected Output:

1
22
333
4444
55555
666666
7777777
88888888
999999999
Click me to see the sample solution
'''
# row = 9 

# for i in range(1,row+1):
#     for j in range(1,i+1):
#         print(j,end='')
#     print()






















