myArray = [12, 5, 3, 6, 8, 9, 43]

userValue = int(input('Please Enter the Number: '))

while userValue not in myArray:
    print('False')
    userValue = int(input('Please Enter the Number: '))

print('True')