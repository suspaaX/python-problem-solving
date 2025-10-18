class Math:

    def __init__(self,num):
        self.num = num
        


    def addonNum(self,n):

        self.num = self.num+n
        

    @staticmethod
    def add(a,b):
        return a+b


a = Math(10)

# print(a.add(10,54))
# print(Math.add(10,89))

print(a.addonNum(6))
print(a.num)


