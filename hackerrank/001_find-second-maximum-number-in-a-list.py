if __name__ == '__main__':
    n = int(input())
    # print(str(n))
    arr = input().split()
    arr.sort()
    count = len(arr)
    maxNumber = max(arr)
    # runnerUpScore = arr[count - 3]
    # print('runnerUpScore = ' + str(runnerUpScore))
    arr.remove(maxNumber)
    # print('max number = '+ str(maxNumber))
    # print(str(maxNumber))
    index = count - 2
    # print('count = '+ str(count))
    if n != count:
        print('Error! Please reload program')
    else:
        while index >= 0:
            temp = arr[index]
            #print(str(index) + '-->' + temp)
            if (temp < maxNumber):
                runnerUpNumber = temp
                print(runnerUpNumber)
                break
            index -= 1

