letter = '''Dear <|name|>,
you are selected!
<|DATE|>'''

name = input("Enter your name\n")
Date = input("Enter your Date\n")


letter = letter.replace("<|name|>",name )
letter = letter.replace("<|DATE|>",Date )
print(letter)