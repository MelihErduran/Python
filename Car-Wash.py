def carWash(paid):
    if paid == '6':
        print('White Foam\nOne Rinse\nDrip dry')
    
    if paid == '12':
        print('Tricolor Foam\nTwo Rinses\nBlow')


carWash(input('Please Enter Amount of Cash Payed. \n$6 For Basic Car Wash \n$12 For Platinum\n'))