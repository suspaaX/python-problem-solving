# def hello():
#     print("hello world")


# def greet(fx):
#     def mfx():
#         print("Good morning")
#         fx()
#         print("thanks for using this fumction")
#     return mfx
    

# @greet
# def add(a,b):
#     print(a+b)


# # hello()

# add(4,5)

"the end"



    # def greet(fx):
    #     def mfx():
    #         print("good morning")
    #         fx()
    #         print("thanks for using this function")
    #     return mfx

    # # @greet
    # def hello():
    #     print("hello world!")


    # def add(a,b):
    #     print(a+b)

# greet(hello)()
# hello()






def greet(fx):
    def mfx():
        print("good morning")
        fx()
        print("thanks for using this function")
    return mfx

# @greet
def hello():
    print("hello world!")

@greet
def add(a,b):
    print(a+b)

# greet(hello)()
# hello()

greet(add)(5,6)