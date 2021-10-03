diamondLevel = int(input('Please enter diamond level (must be even number odd number): '))
counter = 1
starCounter = 1
dashCounter = diamondLevel - 1

if diamondLevel%2 == 0 :
    print('Please enter odd value!')

else :
    diamondLevel = diamondLevel//2 + 1
    while diamondLevel >= counter :
        print(' ' * dashCounter + '*' * starCounter)
        counter += 1
        starCounter += 2
        dashCounter -= 1

    starCounter -= 4
    dashCounter+= 2
    counter = 1
    while diamondLevel > counter :
        print(' ' * dashCounter + '*' * starCounter)
        counter += 1
        starCounter -= 2
        dashCounter += 1