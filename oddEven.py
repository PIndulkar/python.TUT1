t1 = (2,3,4,5,6,7,8,9,12,21,23,32)
even = []
odd = []
for i in t1:
    if i%2 == 0:
        even.append(i)
    else:
        odd.append(i)
print("The prime number is-->",even)
print("The Odd number is-->",odd)