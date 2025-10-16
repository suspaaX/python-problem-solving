def num():
    for i in range(5):
        return i


def my_generator():
    for i in range(5):
        yield i

    # return i

print(num())
print(my_generator())
