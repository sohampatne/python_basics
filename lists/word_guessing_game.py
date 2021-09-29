# import random
from random import randint

wordList = ['Giraffe', 'Lion', 'Tiger', 'Monkey', 'Dog']
hintList = ['Has long neck', 'King of the Jungle', 'National animal', 'Lives in trees', 'Domestic guard animal']

index = randint(0, len(wordList)-1)
animalName = wordList[index]
points = 0
chances = 3

while chances >= 1:
    userAns = input('Please enter animal name (HINT: ' + hintList[index] + ', ' + str(len(animalName)) + ' letter word): ')
    if animalName.lower() == userAns.lower() :
        print('Hooray! You guessed the animal name!')
        break
    else:
        print('Your guess was incorrect')
    chances -=1






