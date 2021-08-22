import random
from random import randint

wordList = ['Giraffe', 'Lion', 'Tiger', 'Monkey', 'Dog']
hintList = ['Has long neck', 'King of the Jungle', 'National animal', 'Lives in trees', 'Domestic guard animal']

index = randint(0, 4)
animalName = wordList[index]
points = 0
chances = 3

print(wordList.count("Lion"))


while chances >= 1:
    # For Cheaters ---> #print('The animals name is'  + animalName)
    userAns = input('Please enter animal name (HINT: ' + hintList[index] + '): ')
    if animalName == userAns:
        print('Hooray! You guessed the animal name!')
        break
    else:
        print('Your guess was incorrect')
    chances -=1






