import random

def numGenerator():
    numArray = []

    for i in range(0, 100):
        x = random.randint(1,100)
        numArray.append(x)
    print (numArray)

    smallestNum = min(numArray)
    largestNum = max(numArray)

    print('The smallest number is: ', smallestNum)
    print('The largest number is: ', largestNum)

numGenerator()