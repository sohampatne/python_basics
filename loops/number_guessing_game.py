# Logic 1
from random import randint

minNumber = 0
maxNumber = 15

randomNumber = randint(minNumber, maxNumber)
chances = 3

# print(randomNumber)
username = str(input('PLease enter your name: '))

while chances > 0:
    #print('Please enter your guessed number (HINT: %d to %d): ', % minNumber, % maxNumber)
    ans = input('Please enter your guessed number (HINT: ' + str(minNumber) + ' to ' + str(maxNumber) + '): ')
    #ans = input('Please enter your guessed number (HINT: %d to %d): ', % minNumber, % maxNumber)

    if ans == str(randomNumber):
        print('You guessed the number ' + username + ', well done!')
        print('Hooray!')
        break
    elif randomNumber > int(ans):
        print('The number is greater than your guess')
        minNumber = int(ans) + 1
    elif randomNumber < int(ans):
        print('The number is smaller than your guess ')
        maxNumber = int(ans) - 1

    chances -= 1
    print('Chances left: ' + str(chances))

    if chances == 0:
        print('\nBetter luck next time ' + username + ' ! The number was: ' + str(randomNumber))







