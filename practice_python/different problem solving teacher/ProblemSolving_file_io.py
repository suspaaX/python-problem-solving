'''
1. Read Entire File

Write a Python program to read an entire text file.

Click me to see the sample solution
'''
file = 'test.txt'

def readline(file):
    with open(file,'r+') as f:
        txt = f.read()
        print(txt)
        f.close()
        return

# readline(file)


'''
2. Read First N Lines

Write a Python program to read first n lines of a file.

Click me to see the sample solution


'''


pass


'''
5. File to List

Write a Python program to read a file line by line and store it into a list.

Click me to see the sample solution
'''

def file_list(file):
    f = open(file,'r+')
    content = []
    content.append(f.readlines())
    print(content)
    return

# file_list(file)


'''
9. Line Count

Write a Python program to count the number of lines in a text file.

Click me to see the sample solution

'''
file_name = 'test.txt'
def LineCount(file_name):
    file = open('test.txt','r+')
    content = file.readlines()
    print(len(content))
    return

# LineCount(file_name)


'''

10. Word Frequency Counter

Write a Python program to count the frequency of words in a file.

Click me to see the sample solution 

'''
file_name = 'test.txt'
word = 'page'

def word_frequency(file_name,word):
    file = open(file_name,'r+')
    all_read_line = file.readlines()
    lis1 = [all_read_line]

    for i in lis1:
        if word == lis1:
            print(lis1.count(word))
        return


# word_frequency(file_name,word)

'''
11. Get File Size

Write a Python program to get the file size of a plain file.

Click me to see the sample solution
'''
file = 'test.txt'

def file_size(file):
    import os
    t = os.stat(file)
    print(t.st_size)
    return
    
# file_size(file)

'''
13. Copy File Contents

Write a Python program to copy the contents of a file to another file .

Click me to see the sample solution
'''

file1 = 'test.txt'
file2 = 'test2.txt'

def copy_file(file,file2):
    import shutil
    shutil.copy(file,file2)
    return

# copy_file(file1,file2)

'''
14. Combine Lines from Two Files

Write a Python program to combine each line from first file with the corresponding line in second file.

Click me to see the sample solution
'''

def combine_file():
    
    pass

'''
15. Random Line Reader

Write a Python program to read a random line from a file.

Click me to see the sample solution

'''
    
file1 = 'test.txt'

def random_line_reader(file1):
    import random
    file = open(file1,'r+')
    content = file.readlines()
    print(random.choice(content))
    return
    
# random_line_reader(file1)