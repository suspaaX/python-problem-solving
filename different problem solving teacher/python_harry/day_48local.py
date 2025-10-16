"local and global variable"

x = 5 #global variable

def testing():
    x = 5 #local variable
    y=10
    print(y)

testing()
print(x)
# print(y)#didnot excute because globally y declare ni hua hai
