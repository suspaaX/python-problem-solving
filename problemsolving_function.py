'https://www.w3resource.com/python-exercises/python-functions-exercises.php#google_vignette'

'''1. Maximum of Three Numbers

Write a Python function to find the maximum of three numbers.
'''

# def max_num(num1,num2,num3):

#     num = [num1,num2,num3]

#     if num1>num2 and num1>num3:
#         print(num1)
#     elif num2>num3 and num2>num1:
#         print(num2)
#     else:
#         print(num3)

#     return num


# max_num(10,65,-789)

'DONE'

'''2. Sum All Numbers in a List

Write a Python function to sum all the numbers in a list.

Sample List : (8, 2, 3, 0, 7)
Expected Output : 20'''

# num = (8, 2, 3, 0, 7)

# def all_sum(*num):

#     sum = 0
#     for i in num:
#         sum = i+sum

#     return sum


# c = all_sum(8, 2, 3, 0, 7)

# print(c)

'DONE'

'''3. Multiply All Numbers in a List

Write a Python function to multiply all the numbers in a list.

Sample List : (8, 2, 3, -1, 7)
Expected Output : -336'''


# num = (8, 2, 3, -1, 7)

# def mul_num(*num):
#     j = 1
#     for i in num:
#         j = i*j

#     return j


# c = mul_num(8, 2, 3, -1, 7,789)
# print(c)

'DONE'

'''4. Reverse a String

Write a Python program to reverse a string.

Sample String : "1234abcd"
Expected Output : "dcba4321"
Click me to see the sample solution'''

# str = '1234abcd'

# def rev_str(str):
#     new_str=str[::-1]
#     print(new_str)


# str = "ram"
# rev_str(str)

'DONE'


'''5. Factorial of a Number

Write a Python function to calculate the factorial of a number (a non-negative integer). The function accepts the number as an argument.

'''

# num = 5

# def fact(num):

#     fact = 1

#     for i in range(1,num+1):

#         fact = i*fact

#     print(fact)

# num = 3

# fact(num)


'DONE'


'''
6. Check if a Number Falls Within a Given Range

Write a Python function to check whether a number falls within a given range.'''


# srt_num =10

# end_num =20

# tgt_num = 15


# def num_range(srt_num,end_num,tgt_num):

#     try:

#         if tgt_num >srt_num and tgt_num<end_num:
#             print(f"Number is in the range of start no:{srt_num} and last number:{end_num} and your no is {tgt_num}")

#         else:
#             print(f"you enter wrong no:{tgt_num}")
    
#     except Exception as e:
#         print(e)

# s = 5
# e = 10
# t = 47
# num_range(s,e,t)


'DONE'


'''# 7. Count Uppercase and Lowercase Letters in a String

# Write a Python function that accepts a string and counts the number of upper and lower case letters.


# Sample String : 'The quick Brow Fox'
# Expected Output :
# No. of Upper case characters : 3
# No. of Lower case Characters : 12
'''


# l = 'The quick Brow Fox'

# def string_test(l)



# num = (1,57,98,987,789)

# def avg_num(*num):

#     # avg = 0

#     for i in num:

#         # avg = (i + avg)/len(num)
#         print(i)

#     # return avg



# # c = avg_num(num)

# # print(c)

# print(avg_num(num))




'''8. Return a New List with Distinct Elements from a List

Write a Python function that takes a list and returns a new list with distinct elements from the first list.

Sample List : [1,2,3,3,3,3,4,5]
Unique List : [1, 2, 3, 4, 5]'''


# mylis = [1,2,3,3,3,3,4,5]

# def dist_num(mylis):
#     new_lis = [set(mylis)]
#     print(new_lis)


# c = dist_num(mylis)
# print(c)

'DONE'  

'''
9. Check Whether a Number is Prime

Write a Python function that takes a number as a parameter and checks whether the number is prime or not.

Note : A prime number (or a prime) is a natural number greater than 1 and that has no positive divisors other than 1 and itself.'''







# skip














'''10. Print Even Numbers from a Given List

Write a Python program to print the even numbers from a given list.

Sample List : [1, 2, 3, 4, 5, 6, 7, 8, 9]
Expected Result : [2, 4, 6, 8]'''

# mylis =  [1, 2, 3, 4, 5, 6, 7, 8, 9]


# def test_even(mylis):
#     nw_lis =[]
#     for i in mylis:
#         if i%2 ==0:
#             nw_lis.append(i)

#     return nw_lis


# c = test_even(mylis)
# print(c)

'DONE'  


'''11. Check if a Number is Perfect

Write a Python function to check whether a number is "Perfect" or not.

According to Wikipedia : In number theory, a perfect number is a positive integer that is equal to the sum of its proper positive divisors, that is, 
the sum of its positive divisors excluding the number itself (also known as its aliquot sum). Equivalently, a perfect number is a number that is half the sum 
of all of its positive divisors (including itself).
Example : The first perfect number is 6, because 1, 2, and 3 are its proper positive divisors, and 1 + 2 + 3 = 6. Equivalently, 
the number 6 is equal to half the sum of all its positive divisors: ( 1 + 2 + 3 + 6 ) / 2 = 6. The next perfect number is 28 = 1 + 2 + 4 + 7 + 14. 
This is followed by the perfect numbers 496 and 8128.

'''










# skip














'''12. Check if a String is a Palindrome

Write a Python function that checks whether a passed string is a palindrome or not.

Note: A palindrome is a word, phrase, or sequence that reads the same backward as forward, e.g., madam or nurses run.
'''






















'''16. Create and Print a List of Squares for Numbers 1 to 30

Write a Python function to create and print a list where the values are the squares of numbers between 1 and 30 (both included).'''


# num = 30

# def sqr_no(num):

#     for i in range(1,num+1):

#         print(i*i)

# print(sqr_no(30))

'''20. Detect the Number of Local Variables Declared in a Function

Write a Python program to detect the number of local variables declared in a function.

Sample Output:
3
'''


