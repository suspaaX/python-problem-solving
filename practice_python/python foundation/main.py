# #conditional statement
# a = 45
# if(a>5):
#     print('a is greater than 5')
# elif(a>17):
#     print ('a is greater than 17')
# else:
#     print ('a is greater than 3 and 17' )

# print("hello world")
# print 1 to 50 through while loop

# i = 1
# while i<=50:
#     print(i)
#     i = i+1


# i = 20
# for i in range(0,21):
#     print(i)


# i = 10
# for i in range(-10,11):
#     print(i)


#print 1 to 10 through while loop

# i = 1
# while i <= 10 :
#     print('Number ' + str(i))
#     i = i+1

#print('Done')

#print 1-50 through while loop

# i = 0
# while i<50:
#     print(i)
#     i = i+1
# print('Done')

#print harry 5 time 

# i = 0
# while i<=5:
#     print('harry')
#     i = i +1


#print the content using while loops

# fruits = ['bananba','mango','papaya','apple','kiwi']
# i = 0
# while i<len(fruits):
#     print(fruits[i])
#     i = i+1

# print content through for loops

# numbers = ['bananba','mango','papaya','apple','kiwi']

# for number in numbers:
#     print(number)

#note#step size in loops
#print 1 to 8 through for loop

# for i in range(8):
#     print(i)

#note always start from 0


#print 1 to 8 through for loop

# for i in range(1,8):
#     print(i)
# note always start with initial no in my case 1


# note step size in for loop in range i.e (1,10,2) (1,4,7,10)


# else in for loop
# for i in range(1,8):
#     print(i)

# else:
#     print("this is inside else of for")

# print list through for loop
# l=[1,7,8]
# for item in l :
#     print(item)
# print('Done')

#break in for loop

#print 1 to 5 through for loop in give no 1 to 10 and don't print statement

# # for item in range(1,10):
# #     print(item)
# #     if item == 5 :
# #         break
# # else:
#     print('This is final result')

# note else will only work with sucessfully completed of for loop 


#pass statement simly do nothing in loop i.e
# print 1 to 10
# for item in range(0,10):
#     print(item)
#     if item >10:
#         pass
# print('Done')

# def sound(player):
#     pass

# if i>10:
#     pass

# while i<19:
#     pass



#contine  statement simply simply skip value i.e
#prin 1 to 10 skip 5 
# for i in range(1,10):
#     if i == 1:
#         continue
#     print(i)
    
# print('Done')

#print table of given no using for loop

# num = int(input('please enter your number:'))
# for item in range(1,11):
#     print(str(num) + 'x' + str(item) + '=' + str(num*item))

#f" string is best way to write code in table

# num = int(input("enter your number:"))
# for item in range(1,11):
#     print(f"{num} x  {item}  = {num*item}")
    

#write a program to greet all name in list which start with "s"


# l1 = ['Harry','Sohan','Sachin','Rahul']


# for item in l1:
#     if item.startswith('S'):
#         print('Goodmorning,' + item)

#print any table using while loop

#print given no is prime or not

# num = int(input('Enter your no:'))
# prime =True

# for i in range(2,num):
#     if (num % i == 0):

# print this pattern

#         *
#     *   *   *
# *   *   *   *   * for n =3?

# print this pattern

# *
# * *
# * * * for n =3 

# n = 4
# for i in range(4):
#     print('*' * (i+1))


#function
#print greetings after user enter his name use functions 

# n = 1 * 2 *  3 *  4 * 5

# n = 5
# product = 1
# for i in range(n):
    
#     product = product*(i+1)
# print(product)

# a = 22

# if (a>9):
#     print("greater")
# else:
#     print("lesser")


# a = 10

# if (a>3):
#     print("a is greater than 3")
# elif(a>7):
#     print("a is grater  than  7")
# elif(a>10):
#     print("a is grater than 10")
# elif(a>15):
#     print("a is greater than 15")

# else:
#     print("a is lesser than all")

# print("Done")
    


# age = int(input("Enter your age:"))

# if age>18:
#     print("Your age is greater than 18")
# elif age<18 :
#     print("age is not greater than 18")

# # else:
# #     print ('not greater than 18')


#print greatest of given four no.

# num1 = int(input('Enter your no:'))
# num2 = int(input('Enter your no:'))
# num3 = int(input('Enter your no:'))
# num4 = int(input('Enter your no:'))

# if (num1>num2):
#     f1 = num1

# else:
#     f1 = num2

# if (num2>num3):
#     f2 = num2

# else:
#     f2 = num3


# if (num3>num4):
#     f3 = num3

# else:
#     f3 = num4


# if (f1>f2):
#     i1 = f1

# else:
#     i1 = f2


# if (f2>f3):
#     i2 = f2

# else:
#     i2 = f3

# if(i1>i2):
#     j = i1
# else:
#     j = i2

# print(str(j) + "is greatest number")

# write a program to find out whether a student is pass or fail 
# it requires total 40% and atleat 33% in each subject 
# to pass assume 3 subjects and take 
# marks as an input from the user






