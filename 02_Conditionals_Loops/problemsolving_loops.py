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

for i in range(1,row+1):
    for j in range(1,row-(row-i)+1):
        print(j,end='  ')
    print()

























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