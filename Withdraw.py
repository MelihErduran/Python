def withdrawMoney(currentBalance, amount):
    if (currentBalance >= amount):
        currentBalance = currentBalance - amount
        return currentBalance
    if currentBalance < amount:
        return 'You don\'t have enough money'
withdrawMoney(100, int(input('How much do you want to withdraw')))