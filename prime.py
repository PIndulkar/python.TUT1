numberList = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
primeList = []
for num in numberList :
    if num == 0 or num == 1 :
        continue  
    for i in range(2, num // 2 + 1) :
        if num % i == 0 :
            break
    else :
        primeList.append(num)
if len(primeList) : 
    print("Prime Number : ",end = "-> ")
    for ans in primeList :
        print(ans, end = ", ")
else :
    print("No any number from the given list is Prime")