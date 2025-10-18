
# # class Person:
# #     name = "abhi"
# #     occ = "developer"

# #     def info(self):
# #         print(f"{self.name} is a {self.occ}")


# # p1  = Person()
# # # print(p1.name)
# # # print(p1.occ)

# # p1.info()


# ####constructor

# class Person:
#     def __init__(self,n,o):
#         print("hey i am a doctor")
#         self.name = n
#         self.occ = o
    

#     def info(self):
#         print(f"{self.n} is a {self.o}")



# p1 = Person("sonu","govt")
# p2 = Person("amar","govt2")
# p3 = Person(1,2,3)#self indicates as p3 so 2 arugments needed
# p4 = Person()#takes argments

# p1.info()
# p2.info()



# # class Person:

# #     def __init__(self,name,occ):#__init__dunder method
# #         print("hey i am a doctor")
# #     #     self.name=name
#     #     self.occ=occ

#     # def info(self):
#     #     print(f"{self.name} is a {self.occ}")





# # p1  = Person("abhi","developer")
# # # print(p1.name)
# # # print(p1.occ)

# # p1.info()


"the end"

###constructer
class Person:
    def __init__(self,name,occ):
        self.name = name
        self.occ=occ

    def info(self):
        print(f"{self.name} is {self.occ}")


a1 = Person("binad","job")
a1.info()

a2 = Person("sinod","service")
a2.info()


"the end"





