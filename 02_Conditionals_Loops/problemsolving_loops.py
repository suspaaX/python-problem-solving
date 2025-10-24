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
    
data_types(lis1)

