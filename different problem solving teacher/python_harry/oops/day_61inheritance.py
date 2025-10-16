class Employee:
    def __init__(self,name,id):
        self.name=name
        self.id=id

    def show_details(self):
        print(f"name of employee is {self.name} and code is {self.id}")


class Programmer(Employee):
    def show_language(self):
        print("the default lang is python")




e1 = Employee("abhi",420)
e1.show_details()

e2 =Employee("raja-ram",254)
e2.show_details()
# e2.show_language()

e3 = Programmer("abhishek",659)
e3.show_details()
e3.show_language()






