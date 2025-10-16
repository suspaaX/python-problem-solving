# num = int(input('enter your no:'))

# if num>5 and num<9:
#     print(num)
# else:
#     raise ValueError('no shoul be in 5 and 9')

#after writing quit value errot nahi aana chye other luch bhi string pr error

num = input('enter your no:')

if num == 'quit':
    pass
    raise ValueError('no should be in 5 and 9')
else:
    int(num)>5 and int(num)<9
    print(num)
    raise ValueError('no should be in 5 and 9')