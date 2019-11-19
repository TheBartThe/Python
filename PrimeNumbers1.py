prime = 1
primeList = [2]
for i in range(3, 3000001):
    for j in primeList:
        if((i % j == 0)):
            continue
        elif(primeList.index(j) == (len(primeList) - 1)):
            prime += 1
            print(i)
            primeList.append(i)
print(prime)
