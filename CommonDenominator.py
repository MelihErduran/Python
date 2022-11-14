#Find the Common Denominators of 2 Given Numbers
num1 = int(input('Please Enter the First Number: '))
num2 = int(input('Please Enter the Second Number: '))

def comDenom(num1, num2):
    small = None
    commonDenominatorArray=[]
    if (num1 < num2):
        small = num1
    else:
        small =num2
    
    for i in range (1, small):
        if (num1 % i == 0 and num2 % i == 0):
            print('Common Denominator: ', i)
            commonDenominatorArray.append(i)

    return (commonDenominatorArray)

print(comDenom(num1, num2))