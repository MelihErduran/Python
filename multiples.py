def multiples(num, length):
    finalArray = []
    for i in range (1, length):
        finalArray.append(num*i)
    return finalArray

multiples(7, 5)
multiples(12, 10)
multiples(17, 6)

multiples(int(input('Number: ')), int(input('Length: ')))