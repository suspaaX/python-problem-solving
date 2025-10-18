print("Welcome to my computer quiz!")

playing = input("Do you want to play? ")

if playing.lower() != "yes":
    quit()

print("Okay! Let's play :)")
score = 0

answer = input("what does CPU stand for? ")
if answer.lower() == "central processing unit":
    print('correct!')
    score += 1
else:
    print("Incorrect!") 

answer = input(" what does GPU stand for?")
if answer.lower() == "graphics processing unit":
    print('correct!')
    score += 1
else:
    print("Incorrect!")

answer = input("what does RAM stand for?")
if answer.lower() == "random acess memory":
    print('correct!')
    score += 1
else:
    print("Incorrect!")

answer = input("what does PSU stand for?")
if answer.lower() == "power supply":
    print('correct!')
    score += 1
else:
    print("Incorrect!")

print("you got " + str(score) + "question correct!")
print("you got " + str(score) + "question correct!")
    