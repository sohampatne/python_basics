# Logic 1
from asyncio.windows_events import NULL
from random import randint
from xml.dom import minicompat

minNumber = NULL
maxNumber = NULL

randomNumber = randint(minNumber, maxNumber)
chances = 3

# print(randomNumber)
username = str(input("PLease enter your name: "))
level = int(
    input(
        "Please chose a level [Easy(1), Medium(2), Difficult(3), Insane\{Almost impossible\}(4)]: "
    )
)

# Chances processor {based on level}
if level == 1:
    chances = 10
    minNumber = 0
    maxNumber = 10
    additionRedux = 2

elif level == 2:
    chances = 10
    minNumber = 0
    maxNumber = 20
    additionRedux = 2

elif level == 3:
    chances = 10
    minNumber = 0
    maxNumber = 50
    additionRedux = 3

elif level == 4:
    chances = 10
    minNumber = 0
    maxNumber = 100
    additionRedux = 5

while chances > 0:
    # print('Please enter your guessed number (HINT: %d to %d): ', % minNumber, % maxNumber)
    ans = input(
        "Please enter your guessed number (HINT: Your number ranges from "
        + str(minNumber)
        + " to "
        + str(maxNumber)
        + "): "
    )
    # ans = input('Please enter your guessed number (HINT: %d to %d): ', % minNumber, % maxNumber)

    if ans == str(randomNumber):
        print("You guessed the number " + username + ", well done!")
        print("Hooray!")
        break
    elif randomNumber > int(ans):
        print("The number is greater than your guess")
        minNumber = int(ans) + additionRedux
    elif randomNumber < int(ans):
        print("The number is smaller than your guess ")
        maxNumber = int(ans) - additionRedux

    chances -= 1
    print("Chances left: " + str(chances))

    if chances == 0:
        print(
            "\nBetter luck next time "
            + username
            + " ! The number was: "
            + str(randomNumber)
        )
