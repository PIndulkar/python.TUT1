def removeDuplicate(l1):#Define Function for Remove Duplicates from list
    ans_list = []
    for i in l1:
        if i not in ans_list:
            ans_list.append(i)
    return ans_list
#
l1 = [7,17,18,17,18,20,26,10]
print(removeDuplicate(l1))#Function Call