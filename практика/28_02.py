arr1 = [1, 2, 3, 4, 5, 9, 10]
arr2 = [4, 5, 6, 7, 8, 9]

'''arr1 = [1, 2, 2, 3, 4, 4, 4, 5]
arr2 = [2, 2, 4, 4, 6, 7, 8]'''

a = []
for i in arr1:
    if arr2.count(i)>=1:
        a.append(i)

print(set(a))