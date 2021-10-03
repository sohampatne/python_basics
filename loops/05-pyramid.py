counter = 1
userName = str(input('Hello there user! \nWhat is You Name?: '))
print('Hi ' + userName + '! Welcome to my pyramid builder program. ')
pyramidLevel = int(input('Please enter the Number of levels you want in the pyramid : '))
starCounter = 1
dashCounter = pyramidLevel - 1

while counter <= pyramidLevel :
    print( ' ' * dashCounter + '*' * starCounter)
    counter += 1
    starCounter += 2
    dashCounter -= 1