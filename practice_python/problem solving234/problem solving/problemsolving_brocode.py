#############################################################introduction###########################################################################


# #i like izza
# print("I like pizza") 
# print("i like chips")


#############################################################Data types#################################################################################

#string
# first_name = "abhishek"
# food = "chips"
# email = "abhishekkumar269@gmail.com"


# print(f"your name is {first_name}")
# print(f"your fav. food is {food}")
# print(f"your email is {email}")


#intenger

# age  = 31
# quantity = 41
# num_of_student = 78

# print(f"no of student in class {num_of_student }")
# print(f"i bougt no of quntity {quantity}")
# print(f"my age is {age}")

#float
 
# price  = 12.99
# distance = 78.8
# temp = 45.8

# print(f"today temp is {temp}")
# print(f"your city distance is {distance}")
# print(f"mango price is {price}")


#Boolean

# is_student = True
# train_on_time =False
# is_raining = False


# if is_student:
#     print("class is full")

# else:
#     print("class is empty")


# if train_on_time:
#     print("train is coming")
# else:
#     print("train is late")


# if is_raining:
#     print("dont go outside")

# else:
#     print("go outside")


# data_type = "intenger" ,"string","float","boolean"

#############################################################typecasting#################################################################################


# int(),float(),bool(),str()

# age = 32
# price = 45.65
# name = "abhishek kumar"
# name1 = "265"
# is_studying = True

# print(type(age))

# age = float(age)
# print(type(age))

# age +=1
# print(age)

# print(type(price))

# price  = int(price)
# print(type(price))

# name = bool(name)
# print(type(name))

# name1 = int(name1)
# name1 += 1

# print(name1)


#############################################################input in python#################################################################################

#rectangle problem
# rect_length = int(input("lenth of rectangle:"))

# rect_width = int(input("width of rectangle:"))

# area = rect_length * rect_width 

# print(f"area of rectangle is {area}cm^2")

#shopping cart problems

# item = input("what whould youlike to buy:")
# price = float(input("what is price:"))
# quan = int(input("how much wouldyou like:"))

# total = price * quan


# print(f"you bought {item } which quantity is {quan} and your total price is {total} happy shopping!")





#############################################################arthmetic opertor#################################################################################

# friend = 5

# friend = friend + 1

# friend +=1

# print(friend)

# friend = friend -1

# friend -=1

# print(friend)

# # friend = friend*3

# friend *=3

# print(friend)

# friend = friend/3

# friend /=3

# print(round(friend,1))

# friend = friend%2

# friend %=2

# print(friend)


#############################################################if-else-elif#################################################################################

# age = 105

# if age > 100:
#     print("you are not allowed for signup")   


# elif age > 18:
#     print("you can signup")

# else:
#     print("you can't signup")






#############################################################logical operator#################################################################################
# and
# or
# not 

# temp = 26
# is_sunny = True



# if temp>25 and is_sunny:
#     print("it is sunny amd not raining")
# else:
#     print("go  out side")


#############################################################condtion statement if else in one line#######################################

# x if condition else y


# num = -78

# print( "Postive"if num>0 else "Negative")

# num = 2

# print("EVEN" if num%2 == 0 else "ODD")


# a = 0.5

# b = 78

# # max_num = "A is bigger" if a>b else "B is bigger"

# min_num = "A is lesser" if a<b else "B is lesser"


# # print(max_num)

# print(min_num)


# age  = 89

# status = "Adult" if age >= 18 else "Minor"

# print(status)


# temp  = 30

# weather =  "Hot " if temp>15 else "cold"

# print(weather)


# user_role = "user78"

# access_level = "Full access" if user_role == "admin" else "Limited access"

# print(access_level)

#############################################################string method##############################################################

# name  = "Abhishek kumar"

# name = "abhsiSHEK KUMAR"


# name  = "123"

# name  = len(name)


# name = name.upper()

# name = name.isalpha()

# name = name.isdigit()

# name = name.find(" ")

# nane = name.capitalize()

# name = name.lower()

# name = name.rfind("m")

# print(name)

# phone_no = input("Enter your phone no:")

# result =  phone_no.replace("0","1")

# print(result)

# print(help(str))


# print("hello world")


#validate user input excercise

#USER NAME IS NOT MORE THAN 12 CHARCTER
#USER MUST NOT CONTAIN SPACES
#USER MUST NOT CONTAIN DIGITS

# username  = input("Enter your name:")

# if len(username)>100:
#     print("User name is more than 12 character")

# elif not username.isalpha():
#     print("Username cant be number")

# else:

#     print(f"welcome to SUSPAA{username}")


#############################################################indexing###################################################################


# credit_card = "3244-6259-6789"

# credit_card = credit_card[0]

# credit_card = credit_card[0:4]

# credit_card = credit_card[4]

# credit_card = credit_card[0:-1]

# credit_card = credit_card[-4:]

# print(f"last four digit of credit is xxxx-xxxx-{credit_card}")

# credit_card = credit_card[::-1]

# credit_card = credit_card[0::2]

# credit_card = credit_card[0::3]

# credit_card = credit_card[0::]

# credit_card = credit_card[::-1]
# # print(f"your credit number in reverser order is:{credit_card}")

# print(credit_card)

#############################################################format specfiers##############################################################


# price1 = 3.14569
# price2 = 45
# price3 = 78.897

# price1 = 3000.14569
# price2 = -4500
# price3 = 7800.897


# print(f"price 1 is ${price1:1f}")
# print(f"price 2 is ${price2:1f}")
# print(f"price 3 is ${price3:1f}")

# print(f"price 1 is ${price1:2f}")
# print(f"price 2 is ${price2:2f}")
# print(f"price 3 is ${price3:2f}")

# print(f"price 1 is ${price1:.2f}")
# print(f"price 2 is ${price2:.2f}")
# print(f"price 3 is ${price3:.2f}")

# print(f"price 1 is ${price1:<10}")
# print(f"price 2 is ${price2:<10}")
# print(f"price 3 is ${price3:<10}")


# print(f"price 1 is ${price1:,.1f}")
# print(f"price 2 is ${price2:,.1f}")
# print(f"price 3 is ${price3:,.1f}")


# print(f"price 1 is ${price1:010}")
# print(f"price 2 is ${price2:010}")
# print(f"price 3 is ${price3:010}")


#############################################################while loop###################################################################

#while condition is only for code exction statement is true excute code


# name = input("Enter your name:")

# if name =="":
#     print("you dinot enter your name")

# else:
#     print(f"hello{name}")

# while name =="":
#     print("You didnot enter your name:")
#     name = input("Enter your name:")
# print(f"hello{name}")



# age = int(input("Enter your age:"))

# while age < 0: 

#     print("age can't be negative")

#     age = int(input("Enter your age:"))

# print(f"your actual is { age }")


# num = int(input("Enter your in between 1 - 10:"))

# while num < 0 or num > 10:

#     print("this is not valid no.")
#     num = int(input("Enter your in between 1 - 10:"))

# print(f"your no is {num}")


# food = input("Enter your fav. food(q to quit):")

# while not food == "q":
#     print(f"your fav food is {food}")
#     food = input("Enter your fav. food(q to quit)")

# print("bye")


#python compound interest calculator

# principal = 0
# rate  = 0 
# time = 0

# while principal <= 0:
#     print("Enter your principle")
#     if principal <= 0:
#         print("Principal cant be zero or negative")

# print(f"your principal amount is {principal}")


######################################################################for loop#################################################
#for loops =    excute a block if code a fixted no of times
# you can itrate of range,string,sequence ,etc.

# for x in reversed(range(1,11)):
#     print(x)

# print("happy new year")


# for x in range(1,11,2):
#         print(x)

# print("happy new year")


# credit_card = "3244-8259-6789"

# for x in credit_card:
#     print(x)

#wap a program to skip 13 form 1-20.


# for x in range(1,21):

#     if x == 13:
#         continue #continue is used for skip certain char from programe
#     print(x)
      
# for x in range(1,21):

#     if x == 13:
#         break #break is used for urgent stop in programe.
#     print(x)
      










































































########################################################collection#################################################################

#collection- single variable store multiple value

#List


#sets


#tuple



##List  
#dublicate are ok
##orederd and changeble


# fruits = ["apple","banana","grapes","carrot"]

# print(fruits[0])

# print(fruits[0:])

# print(fruits[:-1])

# print(fruits[0:5])

# fruits[0] = "potato"

# fruits.append("orange")

# fruits.sort()

# fruits.clear()

# print(fruits.count("apple"))

# fruits.reverse()

# fruits = len(fruits )

# fruits.insert(15,"gum")

# for fruit in fruits:
#     print(fruit)

# print("pineapple" in fruits)

# print("potato" in fruits)

# print(help(fruits))

# print(dir(fruits))

# print(fruits.index("apple"))

# print(len(fruits))

# print(fruits)


##sets##
#always underd unordered 
#duplicate not allowed
#adding allowed
#indexing not allowed

# fruits = {"apple","banana","grapes","carrot" }
# fruits = {"apple","banana","grapes","carrot" ,"apple"}
# fruits.add("potato")
# print(fruits[0])
# fruits.clear()
# fruits.pop()
# print(len(fruits))
# print(help(fruits))

# print(fruits)


##tuple##
#duplicate is allowed

# fruits = ("apple","banana","grapes","carrot" )

# fruits = ("apple","banana","grapes","carrot" ,"apple")

# print(len(fruits))

# print(fruits.count("apple"))

# print(fruits.index("apple"))

# print(fruits)

# print("apple" in fruits)

# print(fruits.count("carrot"))

######################################shopping cart problem#############################################

# food  = []
# price  = []
# total = 0


# while True:
#     food = input("Enter to food you want buy(q to quit):")
#     if food ==  "q":
#         break

# print(food)

####################################2d list ####################################################################

# fruits = ["apple","pineapple","banana"]
# veggie = ["potato","brinjal","beans"]
# meats = ["chicken","eggs","fish"]

# groceries = [fruits,veggie,meats]

# # print(fruits)
# print(veggie)
# print(meats)

# fruits[0] = "gauva"
# print(fruits)




# print(groceries[0][2])

# print(groceries[1][2])


# print(groceries[3])
# print(groceries[1])
# print(groceries[2])

# print(groceries[2][1])


# print(groceries[2][3])


# groceries = [("apple","pineapple","banana"),
#             ("potato","brinjal","beans"),
#             ("chicken","eggs","fish")]

# # print(groceries)


# # for el in groceries:

# #     for x in el:
# #         print(x, end = " ")

# #     print()

# print(groceries)


##########################mobile keyword##################################

 
# num_pad = ((1,2,3),
#         (4,5,6),
#         (7,8,9),
#         ("*",0,"#"))


# for el in num_pad:
#     for num in el:
#         print(num,end= " ")
#     print()


# print(num_pad)

################################################quiz project#########################################################


            
























################################################Dictonary #########################################################

# capital = {"bihar":"patna",
# "gujrat":"ahemdabd",
# "up":"lucknow",
# "mp":"bhopal"
# }


# print(type(capital))

# print(len(capital))

# print(capital.keys())

# print(capital.clear())

# print(capital.keys())

# print(capital)

# print(type(capital))

# print(capital.get("patna"))

# print(help(capital))

# print(capital)

# print(capital.get("bihar"))

# print(capital.pop("bihar"))

# print(capital)

# print(capital.get("delhi"))

# if capital.get("tamilnadu"):
#     print("capital is exist")

# else:
#     print("capital is not exist in dictionary")


# capital.update({"assam":"dispur"})


# capital.update({"bihar":"purnia"})

# capital.pop("bihar")

# capital.popitem()

# print(capital)

# value = capital.values()

# print(value)


# for cap in capital.keys():
#     print(cap)


# for val in capital.values():
#     print(val)

# item = capital.items()
# print(item)


# for k,v in capital.items():
#     print(f"{k}:{v}")



























































