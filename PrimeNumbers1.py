from math import sqrt

prime = 1
primeList = [2]
for i in range(3, 3000001):
    for j in primeList:
        if((i % j == 0)):
            break
        elif(j >= sqrt(i)):
            prime += 1
            primeList.append(i)
            break
print(prime)
