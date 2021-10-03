
userAns = 'Y'

while userAns == 'Y' or userAns == 'y':
    userInput = input('Please enter your name: ')
    userOpinion = input('Describe yourself in one word: ')
    print('Hi ' + str(userInput) + ', you are ' + userOpinion + '!')
    userAns = str(input('Do you want to continue? (Y/N): '))
