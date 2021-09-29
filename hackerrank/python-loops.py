if __name__ == '__main__':
    n = int(input('Please enter number: '))
    minusCount = int(0)

    while n > 0:
        minusCount += 1
        finalResult = n - minusCount
        print(finalResult)
